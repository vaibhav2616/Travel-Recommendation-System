"""
FastAPI Routes for Indian Travel Recommendations, Routes, Weather, and AI customizations.
"""

from typing import List, Dict, Any, Optional
from fastapi import APIRouter, Query, Header, HTTPException
from ..models.schemas import (
    FilterRequest, RecommendationResponse, RouteDetail,
    WeatherInfo, AICustomizeRequest, AICustomizeResponse
)
from ..services.recommendation_engine import RecommendationEngine
from ..services.route_service import RouteService
from ..services.weather_service import WeatherService
from ..services.ai_service import AIService
from ..data.destinations import DESTINATIONS

router = APIRouter(prefix="/api", tags=["Travel Recommendations"])

@router.get("/destinations", response_model=List[Dict[str, Any]])
def list_destinations(region: Optional[str] = Query(None, description="Optional region filter")):
    if region and region.lower() != "all":
        return [d for d in DESTINATIONS if d["region"].lower() == region.lower()]
    return DESTINATIONS

@router.get("/destinations/{dest_id}", response_model=Dict[str, Any])
def get_destination(dest_id: str):
    for d in DESTINATIONS:
        if d["id"] == dest_id:
            return d
    raise HTTPException(status_code=404, detail="Destination not found")

@router.post("/recommendations", response_model=RecommendationResponse)
def get_recommendations(
    req: FilterRequest,
    x_gemini_key: Optional[str] = Header(None, alias="X-Gemini-Key")
):
    try:
        response = RecommendationEngine.get_recommendation(req, api_key=x_gemini_key)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendation: {str(e)}")

@router.get("/weather/{dest_id}", response_model=WeatherInfo)
def get_weather(dest_id: str, season: str = Query("monsoon")):
    return WeatherService.get_weather_for_destination(dest_id, season)

@router.post("/routes/calculate", response_model=RouteDetail)
def calculate_route(dest_id: str = Query(...), origin: Optional[str] = Query(None)):
    return RouteService.calculate_route(dest_id, origin)

@router.post("/ai/customize", response_model=AICustomizeResponse)
def customize_itinerary(
    req: AICustomizeRequest,
    x_gemini_key: Optional[str] = Header(None, alias="X-Gemini-Key")
):
    effective_key = req.api_key or x_gemini_key
    return AIService.customize_itinerary_prompt(
        itinerary_context=req.itinerary_context,
        user_prompt=req.user_prompt,
        api_key=effective_key
    )

# ==============================================================================
# Machine Learning Microclimate & Route Weather Endpoints
# ==============================================================================
from ..services.ml_weather_service import MLWeatherService
from pydantic import BaseModel, Field

class MLPointWeatherRequest(BaseModel):
    latitude: float = Field(..., description="Latitude coordinate")
    longitude: float = Field(..., description="Longitude coordinate")
    altitude_m: float = Field(default=200.0, description="Altitude/Elevation in meters")
    month: int = Field(default=7, ge=1, le=12, description="Month of year (1-12)")
    hour: int = Field(default=12, ge=0, le=23, description="Hour of day (0-23)")
    terrain_code: int = Field(default=0, ge=0, le=6, description="0:Plains, 1:Foothills, 2:Ghats, 3:Alpine, 4:Desert, 5:Coastal, 6:Plateau")
    dist_ratio: float = Field(default=0.5, ge=0.0, le=1.0)
    user_temp_offset: float = Field(default=0.0)

class MLRouteWeatherRequest(BaseModel):
    destination_id: str
    origin: str = "Delhi"
    user_temperature_c: Optional[float] = None
    month: int = 7
    departure_hour: int = 6

@router.post("/ml/predict-weather")
def predict_ml_weather(req: MLPointWeatherRequest):
    """
    Evaluates the trained Deep Neural Network for single point weather condition,
    temperature, precipitation probability, humidity, and road hazard index.
    """
    return MLWeatherService.predict_weather(
        lat=req.latitude,
        lon=req.longitude,
        alt_m=req.altitude_m,
        month=req.month,
        hour=req.hour,
        terrain=req.terrain_code,
        dist_ratio=req.dist_ratio,
        user_temp_offset=req.user_temp_offset
    )

@router.post("/ml/route-weather-profile")
def get_ml_route_weather_profile(req: MLRouteWeatherRequest):
    """
    Simulates weather transitions along the entire highway corridor using the trained Deep Neural Network.
    Returns mile-by-mile checkpoints, elevation curves, and road hazard alerts.
    """
    return MLWeatherService.predict_route_weather_profile(
        dest_id=req.destination_id,
        origin=req.origin,
        user_temp=req.user_temperature_c,
        month=req.month,
        hour=req.departure_hour
    )

@router.get("/ml/model-info")
def get_ml_model_info():
    """
    Returns architecture, training loss, parameter count, and validation metrics
    for the locally trained Deep Neural Network.
    """
    model = MLWeatherService.get_model()
    total_params = (
        model.W1.size + model.b1.size +
        model.W2.size + model.b2.size +
        model.W3.size + model.b3.size +
        model.W_reg.size + model.b_reg.size +
        model.W_cls.size + model.b_cls.size
    )
    return {
        "model_type": "Multi-Task Deep Multi-Layer Perceptron (DNN)",
        "parameter_count": int(total_params),
        "layers": [
            {"layer": 1, "type": "Dense + ReLU", "in": 8, "out": 64},
            {"layer": 2, "type": "Dense + ReLU", "in": 64, "out": 32},
            {"layer": 3, "type": "Dense + ReLU", "in": 32, "out": 16},
            {"head_1": "Linear Regression Head", "in": 16, "out": 4, "targets": ["Temperature (°C)", "Precipitation Probability", "Humidity (%)", "Road Hazard Index"]},
            {"head_2": "Softmax Classification Head", "in": 16, "out": 6, "classes": ["clear", "cloudy", "rain", "heavy_rain", "fog", "snow"]}
        ],
        "training_history": model.training_history,
        "offline_ready": True,
        "external_api_keys_required": False
    }

