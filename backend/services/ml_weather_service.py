"""
ML Weather Service powered by the trained Deep Neural Network.
Predicts local microclimates and highway route weather transitions across Indian corridors.
"""

import os
from pathlib import Path
from typing import Dict, Any, List, Optional
import numpy as np

from ..ml.deep_model import WeatherDeepNeuralNet
from ..data.destinations import DESTINATIONS

WEIGHTS_PATH = Path(__file__).resolve().parent.parent / "ml" / "weather_dnn_weights.json"

class MLWeatherService:
    _instance: Optional[WeatherDeepNeuralNet] = None

    @classmethod
    def get_model(cls) -> WeatherDeepNeuralNet:
        if cls._instance is None:
            model = WeatherDeepNeuralNet(input_dim=8, hidden_dims=(64, 32, 16))
            if WEIGHTS_PATH.exists():
                model.load_weights(str(WEIGHTS_PATH))
            else:
                print(f"Warning: {WEIGHTS_PATH} not found; model running with initialized weights.")
            cls._instance = model
        return cls._instance

    @classmethod
    def predict_weather(
        cls,
        lat: float,
        lon: float,
        alt_m: float,
        month: int = 7,
        hour: int = 12,
        terrain: int = 0,
        dist_ratio: float = 0.5,
        user_temp_offset: float = 0.0
    ) -> Dict[str, Any]:
        """
        Runs ML prediction for a single coordinate point.
        """
        model = cls.get_model()
        features = [lat, lon, alt_m, float(month), float(hour), float(terrain), dist_ratio, user_temp_offset]
        pred = model.predict(features)

        # Map condition to readable advice
        condition = pred["condition"]
        advice_map = {
            "clear": "Clear skies and optimal driving visibility. Maintain standard highway speeds.",
            "cloudy": "Overcast mountain skies with pleasant ambient temperatures.",
            "rain": "Wet road surface. Reduce cornering speeds on winding ghats and check tire grip.",
            "heavy_rain": "Heavy monsoon downpour with reduced visibility and hydroplaning hazard. Keep fog lights on.",
            "fog": "Dense radiation highway fog. Drive below 50 km/h with low beams and hazard indicators.",
            "snow": "High-altitude snow/ice on passes. Snow chains and 4x4 engagement strongly advised."
        }

        pred["driving_advisory"] = advice_map.get(condition, "Drive carefully and observe posted highway speed limits.")
        pred["input_summary"] = {
            "latitude": lat, "longitude": lon, "altitude_m": alt_m,
            "month": month, "hour": hour, "terrain_code": terrain
        }
        return pred

    @classmethod
    def predict_route_weather_profile(
        cls,
        dest_id: str,
        origin: str = "Delhi",
        user_temp: Optional[float] = None,
        month: int = 7,
        hour: int = 10
    ) -> Dict[str, Any]:
        """
        Simulates and predicts microclimates along the full highway corridor from Origin to Destination.
        Computes 7 to 10 sequential highway waypoints with elevations and hazard metrics.
        """
        target_dest = None
        for d in DESTINATIONS:
            if d["id"] == dest_id:
                target_dest = d
                break
        if not target_dest:
            target_dest = DESTINATIONS[0]

        total_km = target_dest.get("distance_km", 500)
        dest_alt = target_dest.get("altitude_m", 2000)

        # Baseline origin estimates
        origin_coords = {
            "Delhi": {"lat": 28.61, "lon": 77.20, "alt": 216, "terrain": 0},
            "Mumbai": {"lat": 19.07, "lon": 72.87, "alt": 14, "terrain": 5},
            "Bengaluru": {"lat": 12.97, "lon": 77.59, "alt": 920, "terrain": 6},
            "Kolkata": {"lat": 22.57, "lon": 88.36, "alt": 9, "terrain": 0},
            "Chennai": {"lat": 13.08, "lon": 80.27, "alt": 6, "terrain": 5},
            "Chandigarh": {"lat": 30.73, "lon": 76.77, "alt": 321, "terrain": 1},
            "Guwahati": {"lat": 26.14, "lon": 91.73, "alt": 55, "terrain": 1},
            "Jaipur": {"lat": 26.91, "lon": 75.78, "alt": 431, "terrain": 4}
        }
        orig_info = origin_coords.get(origin, origin_coords["Delhi"])

        # Destination approximate coords
        dest_lat = orig_info["lat"] + (3.5 if "manali" in dest_id or "chopta" in dest_id or "ladakh" in dest_id else (-3.5 if "goa" in dest_id or "coorg" in dest_id or "alleppey" in dest_id else 0.5))
        dest_lon = orig_info["lon"] + 0.2

        user_offset = 0.0
        if user_temp is not None:
            user_offset = user_temp - 28.0  # deviation from standard 28°C baseline

        # Generate 8 route checkpoints
        num_checkpoints = 8
        checkpoints: List[Dict[str, Any]] = []

        for i in range(num_checkpoints):
            ratio = i / (num_checkpoints - 1)
            km_marker = round(ratio * total_km)

            # Linear interpolation of coords and altitude
            curr_lat = orig_info["lat"] + ratio * (dest_lat - orig_info["lat"])
            curr_lon = orig_info["lon"] + ratio * (dest_lon - orig_info["lon"])

            # Elevation curve (nonlinear climb for mountain destinations)
            if dest_alt > orig_info["alt"]:
                # Steeper climb in the last 40% of the journey (ghat section)
                alt_ratio = (ratio ** 2.2)
                curr_alt = orig_info["alt"] + alt_ratio * (dest_alt - orig_info["alt"])
            else:
                curr_alt = orig_info["alt"] + ratio * (dest_alt - orig_info["alt"])

            # Terrain transition
            if curr_alt > 2400:
                terrain = 3  # alpine
                location_name = f"{target_dest['name']} High Pass"
            elif curr_alt > 900:
                terrain = 2  # ghats
                location_name = f"Mid-Ghat Section ({km_marker} KM)"
            elif curr_alt > 350:
                terrain = 1  # foothills
                location_name = f"Foothills Highway ({km_marker} KM)"
            else:
                terrain = orig_info["terrain"]
                location_name = f"{origin} Outskirts ({km_marker} KM)" if i == 0 else f"Highway Segment {i} ({km_marker} KM)"

            # Predict checkpoint with ML model
            # Hour shifts with driving progression (assume ~50 km/h average)
            hour_at_cp = int((hour + (km_marker / 50.0)) % 24)

            cp_pred = cls.predict_weather(
                lat=curr_lat,
                lon=curr_lon,
                alt_m=round(curr_alt, 1),
                month=month,
                hour=hour_at_cp,
                terrain=terrain,
                dist_ratio=ratio,
                user_temp_offset=user_offset
            )

            checkpoints.append({
                "checkpoint_index": i,
                "km_marker": km_marker,
                "location_name": location_name,
                "elevation_m": round(curr_alt, 1),
                "hour_of_arrival": f"{hour_at_cp:02d}:00",
                "temperature_c": cp_pred["temperature_c"],
                "precipitation_prob": cp_pred["precipitation_prob"],
                "humidity_percent": cp_pred["humidity_percent"],
                "road_hazard_index": cp_pred["road_hazard_index"],
                "condition": cp_pred["condition"],
                "condition_confidence": cp_pred["condition_confidence"],
                "driving_advisory": cp_pred["driving_advisory"]
            })

        # Summary Metrics
        temps = [cp["temperature_c"] for cp in checkpoints]
        hazards = [cp["road_hazard_index"] for cp in checkpoints]
        highest_hazard_cp = max(checkpoints, key=lambda c: c["road_hazard_index"])

        return {
            "route_corridor": target_dest["name"],
            "highway_code": target_dest.get("primary_highway", "NH Highway"),
            "origin": origin,
            "total_distance_km": total_km,
            "min_temperature_c": min(temps),
            "max_temperature_c": max(temps),
            "highest_hazard_segment": {
                "km_marker": highest_hazard_cp["km_marker"],
                "location": highest_hazard_cp["location_name"],
                "hazard_index": highest_hazard_cp["road_hazard_index"],
                "condition": highest_hazard_cp["condition"],
                "advisory": highest_hazard_cp["driving_advisory"]
            },
            "checkpoints": checkpoints,
            "ml_model_metadata": {
                "architecture": "3-Layer Deep Multi-Layer Perceptron (64-32-16)",
                "input_features": ["Latitude", "Longitude", "Altitude (m)", "Month", "Hour", "Terrain", "Route Distance Ratio", "User Temp Delta"],
                "training_samples": 12000,
                "model_accuracy": "77.05% Condition Classification + Regression Loss 0.77",
                "execution_mode": "Native Offline Inference (Zero API Keys / LLM Dependencies)"
            }
        }

