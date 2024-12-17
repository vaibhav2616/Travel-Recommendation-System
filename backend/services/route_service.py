"""
Route and transit calculation service for Indian corridors.
Calculates distance, driving time, highway identifiers, tolls, and maps pitstops.
"""

from typing import List, Dict, Any, Optional
from ..data.destinations import DESTINATIONS
from ..data.dhabas_and_cafes import DHABAS_AND_CAFES
from ..models.schemas import RouteDetail, Pitstop, AlternateTransit

class RouteService:
    @staticmethod
    def get_destination_by_id(dest_id: str) -> Optional[Dict[str, Any]]:
        for d in DESTINATIONS:
            if d["id"] == dest_id:
                return d
        return None

    @staticmethod
    def calculate_route(dest_id: str, origin: Optional[str] = None) -> RouteDetail:
        destination = RouteService.get_destination_by_id(dest_id)
        if not destination:
            destination = DESTINATIONS[0]  # default to first

        actual_origin = origin if origin and origin.strip() else destination.get("default_origin", "Delhi")
        distance_km = destination["distance_km"]
        driving_hours = destination["driving_time_hours"]
        toll_inr = destination["toll_estimate_inr"]

        # Fetch pitstops
        raw_pitstops = DHABAS_AND_CAFES.get(destination["id"], [])
        pitstops: List[Pitstop] = []
        for p in raw_pitstops:
            pitstops.append(Pitstop(
                name=p["name"],
                category=p["category"],
                highway=p["highway"],
                km_from_origin=p["km_from_origin"],
                location=p["location"],
                famous_for=p["famous_for"],
                pure_veg=p["pure_veg"],
                jain_available=p["jain_available"],
                avg_cost_inr=p["avg_cost_inr"],
                rating=p.get("rating", 4.5),
                highlight_dish=p.get("highlight_dish"),
                image_url=p.get("image_url")
            ))

        # Sort pitstops along route km
        pitstops.sort(key=lambda x: x.km_from_origin)

        # Alternate transits
        alt_transits: List[AlternateTransit] = []
        for alt in destination.get("alternate_transits", []):
            alt_transits.append(AlternateTransit(
                mode=alt["mode"],
                title=alt["title"],
                duration_str=alt["duration_str"],
                approx_cost_inr=alt["approx_cost_inr"],
                scenic_rating=alt["scenic_rating"],
                description=alt["description"],
                carbon_rating=alt["carbon_rating"]
            ))

        return RouteDetail(
            origin=actual_origin,
            destination=destination["name"],
            primary_highway=destination["primary_highway"],
            distance_km=distance_km,
            driving_time_hours=driving_hours,
            toll_estimate_inr=toll_inr,
            road_condition=destination["road_condition"],
            scenic_highlights=destination["scenic_highlights"],
            pitstops=pitstops,
            alternate_transits=alt_transits
        )

