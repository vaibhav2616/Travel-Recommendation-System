"""
Indian seasonal climate and weather dynamics service.
Provides accurate seasonal models for Monsoon, Himalayan Winter, Autumn, and Summer escapes.
"""

from typing import Dict, Any, Optional
from ..data.destinations import DESTINATIONS
from ..models.schemas import WeatherInfo

SEASON_DISPLAY_NAMES = {
    "monsoon": "Monsoon Rains & Misty Ghats (Jul - Sep)",
    "winter": "Crisp Winter & Snow Bound (Nov - Feb)",
    "autumn": "Golden Autumn & Festivals (Oct - Nov)",
    "summer": "Pleasant Summer Escapes (Mar - Jun)"
}

class WeatherService:
    @staticmethod
    def get_weather_for_destination(dest_id: str, season: str = "monsoon") -> WeatherInfo:
        season_clean = season.lower().strip()
        if season_clean not in ["monsoon", "winter", "autumn", "summer"]:
            season_clean = "monsoon"

        target_dest = None
        for d in DESTINATIONS:
            if d["id"] == dest_id:
                target_dest = d
                break

        if not target_dest:
            target_dest = DESTINATIONS[0]

        seasons_data = target_dest.get("seasons", {})
        s_data = seasons_data.get(season_clean, seasons_data.get("monsoon", {}))

        return WeatherInfo(
            season=season_clean,
            season_display=SEASON_DISPLAY_NAMES.get(season_clean, season_clean.capitalize()),
            temp_range=s_data.get("temp_range", "18°C to 28°C"),
            rainfall_level=s_data.get("rainfall", "Moderate"),
            vibe_summary=s_data.get("vibe_summary", "Pleasant weather with refreshing mountain breezes."),
            advisories=s_data.get("advisories", ["Check local road conditions prior to departure"]),
            what_to_pack=s_data.get("what_to_pack", ["Comfortable clothes", "Walking shoes", "Personal meds"])
        )

