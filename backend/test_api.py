"""
Automated unit and integration test suite for the Indian Travel Recommendation System.
Directly tests all route handlers, schemas, and engines.
"""

import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from backend.routes.travel import (
    list_destinations, get_destination, get_recommendations,
    get_weather, calculate_route, customize_itinerary
)
from backend.models.schemas import FilterRequest, AICustomizeRequest
from backend.data.destinations import DESTINATIONS

def test_destinations_listing():
    print("Testing list_destinations()...")
    dests = list_destinations(region=None)
    assert len(dests) >= 6, "Expected at least 6 destinations"
    assert any(d["id"] == "delhi-manali" for d in dests)
    assert any(d["id"] == "mumbai-goa-nh66" for d in dests)
    print(f"  -> Found {len(dests)} curated Indian destinations OK!")

    print("Testing region filter (Himalayas)...")
    him_dests = list_destinations(region="Himalayas")
    assert len(him_dests) >= 2
    for d in him_dests:
        assert d["region"] == "Himalayas"
    print(f"  -> Regional filtering OK ({len(him_dests)} Himalayan destinations found)!")

def test_single_destination():
    print("Testing get_destination('delhi-manali')...")
    dest = get_destination("delhi-manali")
    assert dest["name"] == "Manali & Solang Valley"
    assert dest["altitude_m"] == 2050
    print("  -> Single destination retrieval OK!")

def test_recommendation_generation():
    print("Testing get_recommendations() with multi-level filters...")
    req = FilterRequest(
        origin="Delhi",
        destination_id="delhi-manali",
        region="Himalayas",
        travel_style="adventure",
        group_type="couple",
        budget_tier="comfort",
        season="winter",
        diet_preference="pure_veg",
        transport_mode="road",
        pace="balanced",
        duration_days=4
    )
    res = get_recommendations(req)

    assert res.destination_id == "delhi-manali"
    assert res.destination_name == "Manali & Solang Valley"
    assert len(res.packages) == 3, "Expected 3 tiered packages (Backpacker, Comfort, Luxury)"

    # Verify packages
    pkg_map = {p.id: p for p in res.packages}
    assert "backpacker" in pkg_map
    assert "comfort" in pkg_map
    assert "luxury" in pkg_map

    comfort_pkg = pkg_map["comfort"]
    assert comfort_pkg.cost_per_person > 0
    assert comfort_pkg.breakdown.stay_cost > 0
    assert comfort_pkg.breakdown.food_cost > 0
    assert comfort_pkg.breakdown.transport_cost > 0
    assert comfort_pkg.is_recommended is True

    # Verify weather
    assert res.weather.season == "winter"
    assert len(res.weather.what_to_pack) > 0

    # Verify highway pitstops
    assert len(res.route.pitstops) >= 3, "Expected at least 3 highway pitstops on Delhi-Manali"
    first_pitstop = res.route.pitstops[0]
    assert "Murthal" in first_pitstop.location or "Amrik Sukhdev" in first_pitstop.name
    assert first_pitstop.pure_veg is True

    # Verify itinerary
    assert len(res.itinerary) == 4, f"Expected 4-day itinerary, got {len(res.itinerary)}"
    for day in res.itinerary:
        assert len(day.activities) == 4, "Expected Morning, Afternoon, Evening, Night activities"

    # Verify stays & food
    assert len(res.hotels_and_stays) >= 2
    assert len(res.curated_food_spots) >= 2
    assert res.ai_story is not None
    print("  -> get_recommendations() produced comprehensive Indian travel model OK!")

def test_weather_endpoint():
    print("Testing get_weather('mumbai-goa-nh66', season='monsoon')...")
    w = get_weather("mumbai-goa-nh66", season="monsoon")
    assert w.season == "monsoon"
    assert len(w.advisories) > 0
    assert "Monsoon" in w.season_display
    print(f"  -> Weather OK: {w.temp_range}, {w.rainfall_level} rainfall!")

def test_route_calculation():
    print("Testing calculate_route('bangalore-coorg-wayanad', origin='Bengaluru')...")
    route = calculate_route(dest_id="bangalore-coorg-wayanad", origin="Bengaluru")
    assert route.origin == "Bengaluru"
    assert route.distance_km == 260
    assert len(route.pitstops) >= 2
    print(f"  -> Route OK: {route.distance_km} km on {route.primary_highway} with {len(route.pitstops)} pitstops!")

def test_ai_customization():
    print("Testing customize_itinerary()...")
    req = AICustomizeRequest(
        itinerary_context={
            "origin": "Delhi",
            "destination_name": "Manali",
            "season": "winter",
            "budget_tier": "comfort"
        },
        user_prompt="Make this 100% elder-friendly with minimal stairs and pure Jain food options"
    )
    res = customize_itinerary(req)
    assert len(res.modified_story) > 20
    assert len(res.custom_recommendations) >= 2
    print("  -> AI Customization OK!")

def test_ml_weather_endpoints():
    print("Testing ML Weather Deep Neural Network endpoints...")
    from backend.routes.travel import predict_ml_weather, get_ml_route_weather_profile, get_ml_model_info, MLPointWeatherRequest, MLRouteWeatherRequest

    # 1. Point prediction
    pt_req = MLPointWeatherRequest(latitude=32.2, longitude=77.2, altitude_m=2050.0, month=1, hour=14, terrain_code=3)
    pt_res = predict_ml_weather(pt_req)
    assert "temperature_c" in pt_res
    assert "condition" in pt_res
    assert "road_hazard_index" in pt_res
    print(f"  -> ML Point Prediction OK: {pt_res['temperature_c']}°C, Condition: {pt_res['condition']}, Hazard: {pt_res['road_hazard_index']}")

    # 2. Highway route weather profile
    rt_req = MLRouteWeatherRequest(destination_id="delhi-manali", origin="Delhi", user_temperature_c=29.0, month=7, departure_hour=6)
    rt_res = get_ml_route_weather_profile(rt_req)
    assert len(rt_res["checkpoints"]) == 8
    assert rt_res["min_temperature_c"] <= rt_res["max_temperature_c"]
    assert "highest_hazard_segment" in rt_res
    print(f"  -> ML Route Profile OK: 8 Checkpoints across {rt_res['total_distance_km']} KM on {rt_res['highway_code']}!")

    # 3. Model metadata
    info = get_ml_model_info()
    assert info["offline_ready"] is True
    assert info["external_api_keys_required"] is False
    assert info["parameter_count"] > 1000
    print(f"  -> ML Model Info OK: {info['model_type']} with {info['parameter_count']} parameters!")

if __name__ == "__main__":
    test_destinations_listing()
    test_single_destination()
    test_recommendation_generation()
    test_weather_endpoint()
    test_route_calculation()
    test_ai_customization()
    test_ml_weather_endpoints()
    print("\n=======================================================")
    print("ALL AUTOMATED TESTS PASSED CLEANLY AND COMPLETELY! ")
    print("=======================================================\n")
