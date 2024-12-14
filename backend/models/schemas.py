from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class FilterRequest(BaseModel):
    origin: str = Field(default="Delhi", description="Starting city")
    destination_id: Optional[str] = Field(default=None, description="Specific destination ID if selected")
    region: Optional[str] = Field(default="All", description="Indian region/category: Himalayas, Rajasthan, Coastal, South, Sacred, NorthEast")
    travel_style: Optional[str] = Field(default="all", description="Style: adventure, heritage, laid_back, spiritual, nature")
    group_type: str = Field(default="couple", description="solo, couple, family_elders, friends")
    budget_tier: str = Field(default="comfort", description="backpacker, comfort, luxury")
    min_budget: Optional[int] = Field(default=None, description="Min budget in INR")
    max_budget: Optional[int] = Field(default=None, description="Max budget in INR")
    season: str = Field(default="monsoon", description="monsoon, winter, autumn, summer")
    diet_preference: str = Field(default="all", description="pure_veg, jain, non_veg_local, street_food")
    transport_mode: str = Field(default="road", description="road, train_vande_bharat, flight")
    pace: str = Field(default="balanced", description="relaxed, balanced, packed")
    duration_days: int = Field(default=4, ge=2, le=14, description="Trip duration in days")
    custom_notes: Optional[str] = Field(default="", description="Special requirements or interests")

class CostBreakdown(BaseModel):
    transport_cost: int
    stay_cost: int
    food_cost: int
    activities_permits_cost: int
    buffer_cost: int
    total_cost_per_person: int
    total_cost_group: int

class PackageTier(BaseModel):
    id: str
    name: str
    tagline: str
    cost_per_person: int
    total_group_cost: int
    breakdown: CostBreakdown
    stay_style: str
    dining_style: str
    transport_type: str
    features: List[str]
    is_recommended: bool = False

class Pitstop(BaseModel):
    name: str
    category: str  # dhaba, cafe, viewpoint, stay, temple, landmark
    highway: str
    km_from_origin: int
    location: str
    famous_for: str
    pure_veg: bool = False
    jain_available: bool = False
    avg_cost_inr: int
    image_url: Optional[str] = None
    rating: float = 4.5
    highlight_dish: Optional[str] = None

class AlternateTransit(BaseModel):
    mode: str  # road, train, flight
    title: str
    duration_str: str
    approx_cost_inr: int
    scenic_rating: int  # 1 to 5
    description: str
    carbon_rating: str  # Low, Medium, High

class RouteDetail(BaseModel):
    origin: str
    destination: str
    primary_highway: str
    distance_km: int
    driving_time_hours: float
    toll_estimate_inr: int
    road_condition: str
    scenic_highlights: List[str]
    pitstops: List[Pitstop]
    alternate_transits: List[AlternateTransit]

class DayActivity(BaseModel):
    time_of_day: str  # Morning, Afternoon, Evening, Night
    title: str
    description: str = ""
    location: str
    highlight_tag: Optional[str] = None
    food_recommendation: Optional[str] = None

class DayPlan(BaseModel):
    day: int
    title: str
    theme: str
    activities: List[DayActivity]
    local_tip: str
    stay_recommendation: str

class WeatherInfo(BaseModel):
    season: str
    season_display: str
    temp_range: str
    rainfall_level: str
    vibe_summary: str
    advisories: List[str]
    what_to_pack: List[str]

class StayRecommendation(BaseModel):
    name: str
    type: str  # hostel, boutique_homestay, heritage_haveli, luxury_resort
    location: str
    approx_price_per_night_inr: int
    vibe: str
    amenities: List[str]
    rating: float

class RecommendationResponse(BaseModel):
    destination_id: str
    destination_name: str
    state: str
    tagline: str
    cover_image: str
    vibe_tags: List[str]
    season: str
    weather: WeatherInfo
    route: RouteDetail
    packages: List[PackageTier]
    active_package_id: str
    itinerary: List[DayPlan]
    hotels_and_stays: List[StayRecommendation]
    curated_food_spots: List[Pitstop]
    ai_story: Optional[str] = None
    ai_personalized_tips: List[str] = []

class AICustomizeRequest(BaseModel):
    itinerary_context: Dict[str, Any]
    user_prompt: str
    api_key: Optional[str] = None

class AICustomizeResponse(BaseModel):
    modified_story: str
    custom_recommendations: List[str]
    suggested_adjustments: List[Dict[str, Any]]
