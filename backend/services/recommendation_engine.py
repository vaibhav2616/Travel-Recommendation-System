"""
Core Recommendation and Itinerary Generation Engine.
Synthesizes multi-level filters, 3-tier Indian pricing packages in ₹ INR,
day-by-day itineraries, highway pitstops, and stays.
"""

from typing import List, Dict, Any, Optional
from ..data.destinations import DESTINATIONS
from ..data.dhabas_and_cafes import DHABAS_AND_CAFES
from ..data.stays import STAYS_DATA
from ..models.schemas import (
    FilterRequest, RecommendationResponse, PackageTier, CostBreakdown,
    DayPlan, DayActivity, StayRecommendation, Pitstop
)
from .route_service import RouteService
from .weather_service import WeatherService
from .ai_service import AIService

class RecommendationEngine:
    @staticmethod
    def get_all_destinations() -> List[Dict[str, Any]]:
        return DESTINATIONS

    @staticmethod
    def match_destination(req: FilterRequest) -> Dict[str, Any]:
        """
        Matches best destination based on region, style, or explicit ID.
        """
        # 1. Exact destination_id match
        if req.destination_id:
            for d in DESTINATIONS:
                if d["id"] == req.destination_id:
                    return d

        # 2. Filter by region
        matched = DESTINATIONS
        if req.region and req.region.lower() != "all":
            filtered = [d for d in DESTINATIONS if d["region"].lower() == req.region.lower()]
            if filtered:
                matched = filtered

        # 3. Filter by vibe / style
        if req.travel_style and req.travel_style.lower() != "all":
            style_map = {
                "adventure": ["High Altitude", "Snow Adventures", "Tungnath Trek", "Living Root Bridges"],
                "heritage": ["Living Forts", "Havelis", "Ancient Temples", "Subah-e-Banaras"],
                "laid_back": ["Coastal Road Trip", "Houseboat Cruise", "Tea Plantations", "Coffee Plantations"],
                "spiritual": ["Ganga Aarti", "Ancient Temples", "Subah-e-Banaras", "Ram Mandir"],
                "nature": ["Pine Mist", "Waterfalls", "Coffee Plantations", "Living Root Bridges"]
            }
            target_tags = style_map.get(req.travel_style.lower(), [])
            if target_tags:
                tag_matched = [d for d in matched if any(tag in d.get("vibe_tags", []) for tag in target_tags)]
                if tag_matched:
                    matched = tag_matched

        # Return first matching destination, or default
        return matched[0] if matched else DESTINATIONS[0]

    @staticmethod
    def compute_packages(
        dest: Dict[str, Any],
        duration_days: int,
        group_type: str,
        transport_mode: str
    ) -> List[PackageTier]:
        """
        Calculates 3 tiered packages (Backpacker, Comfort, Royal Luxury) in INR (₹).
        """
        # Multipliers based on group size
        group_size_map = {
            "solo": 1,
            "couple": 2,
            "family_elders": 4,
            "friends": 4
        }
        people_count = group_size_map.get(group_type, 2)
        dist_km = dest.get("distance_km", 400)

        # 1. BACKPACKER TIER
        # Hostels (~₹750/night), State Bus / Sleeper Train / Shared Cab, Dhaba street food (~₹400/day)
        bp_stay_per_person = 800 * (duration_days - 1)
        bp_trans_per_person = max(800, int(dist_km * 2.2))
        bp_food_per_person = 450 * duration_days
        bp_act_per_person = 250 * duration_days
        bp_buf_per_person = 500
        bp_total_person = bp_stay_per_person + bp_trans_per_person + bp_food_per_person + bp_act_per_person + bp_buf_per_person

        bp_breakdown = CostBreakdown(
            transport_cost=bp_trans_per_person,
            stay_cost=bp_stay_per_person,
            food_cost=bp_food_per_person,
            activities_permits_cost=bp_act_per_person,
            buffer_cost=bp_buf_per_person,
            total_cost_per_person=bp_total_person,
            total_cost_group=bp_total_person * people_count
        )

        backpacker = PackageTier(
            id="backpacker",
            name="Nomad Backpacker",
            tagline="Zostels, Scenic State Buses & Legendary Dhabas",
            cost_per_person=bp_total_person,
            total_group_cost=bp_total_person * people_count,
            breakdown=bp_breakdown,
            stay_style="Cozy boutique hostels (Zostel/Hosteller) & Village homestays",
            dining_style="Iconic highway dhabas, local street stalls & kulhad chai",
            transport_type="Sleeper / Superfast Express & Shared Mountain Jeeps",
            features=[
                "Dorm / Private room in community-vibe hostel",
                "Self-guided trails and free walking tours",
                "Authentic local street food and famous dhabas",
                "24/7 Backpacker community support & map guide"
            ],
            is_recommended=False
        )

        # 2. COMFORT / EXPLORER TIER (RECOMMENDED)
        # 3-4 star boutique homestays (~₹3,800/night for 2 = ₹1,900/person), Vande Bharat / Outstation Cab
        cf_stay_per_person = 2100 * (duration_days - 1)
        cf_trans_per_person = max(1800, int(dist_km * 4.5))
        cf_food_per_person = 950 * duration_days
        cf_act_per_person = 600 * duration_days
        cf_buf_per_person = 1200
        cf_total_person = cf_stay_per_person + cf_trans_per_person + cf_food_per_person + cf_act_per_person + cf_buf_per_person

        cf_breakdown = CostBreakdown(
            transport_cost=cf_trans_per_person,
            stay_cost=cf_stay_per_person,
            food_cost=cf_food_per_person,
            activities_permits_cost=cf_act_per_person,
            buffer_cost=cf_buf_per_person,
            total_cost_per_person=cf_total_person,
            total_cost_group=cf_total_person * people_count
        )

        comfort = PackageTier(
            id="comfort",
            name="Heritage Explorer",
            tagline="Boutique Havelis, AC Comfort & Authentic Regional Thalis",
            cost_per_person=cf_total_person,
            total_group_cost=cf_total_person * people_count,
            breakdown=cf_breakdown,
            stay_style="Charming 3-4★ boutique mountain chalets / heritage homestays with breakfast",
            dining_style="Famous regional dining joints, garden cafes & scenic restaurants",
            transport_type="Vande Bharat Executive / Private AC Sedan or SUV",
            features=[
                "Handpicked scenic boutique stays with mountain/lake views",
                "Comfortable AC transport with verified drivers",
                "Priority monument entries & guided nature/temple walks",
                "Curated culinary tasting experiences"
            ],
            is_recommended=True
        )

        # 3. ROYAL LUXURY TIER
        # 5-Star Heritage Palaces/Luxury Resorts (~₹18,000/night for 2 = ₹9,000/person), Private SUV / Flights
        lx_stay_per_person = 9500 * (duration_days - 1)
        lx_trans_per_person = max(5500, int(dist_km * 9.0))
        lx_food_per_person = 2500 * duration_days
        lx_act_per_person = 1800 * duration_days
        lx_buf_per_person = 3500
        lx_total_person = lx_stay_per_person + lx_trans_per_person + lx_food_per_person + lx_act_per_person + lx_buf_per_person

        lx_breakdown = CostBreakdown(
            transport_cost=lx_trans_per_person,
            stay_cost=lx_stay_per_person,
            food_cost=lx_food_per_person,
            activities_permits_cost=lx_act_per_person,
            buffer_cost=lx_buf_per_person,
            total_cost_per_person=lx_total_person,
            total_cost_group=lx_total_person * people_count
        )

        luxury = PackageTier(
            id="luxury",
            name="Maharaja Royal Luxury",
            tagline="Grand Heritage Palaces, Private Chauffeured SUVs & Fine Dining",
            cost_per_person=lx_total_person,
            total_group_cost=lx_total_person * people_count,
            breakdown=lx_breakdown,
            stay_style="5★ Heritage Palaces, Private Pool Villas & Luxury Himalayan Castles",
            dining_style="Royal Thali banquets, champagne breakfasts & curated chef tables",
            transport_type="Private Luxury Innova Crysta / BMW / Airport Transfers",
            features=[
                "Suite accommodation in iconic palaces (Taj/Oberoi/Heritage Castles)",
                "Chauffeured luxury SUV throughout the trip",
                "Private historian & temple priest access",
                "Complimentary Ayurvedic wellness spa treatments"
            ],
            is_recommended=False
        )

        return [backpacker, comfort, luxury]

    @staticmethod
    def generate_itinerary(
        dest: Dict[str, Any],
        duration_days: int,
        group_type: str,
        diet: str,
        season: str
    ) -> List[DayPlan]:
        """
        Builds a customized day-by-day itinerary with Morning, Afternoon, Evening, Night slots.
        """
        dest_id = dest["id"]
        dest_name = dest["name"]
        itinerary: List[DayPlan] = []

        # Archetype templates tailored for Indian destinations
        day_blueprints = {
            "delhi-manali": [
                {
                    "theme": "The Ascent & Murthal Breakfast Run",
                    "activities": [
                        ("Morning", "Pre-dawn departure from Delhi; sunrise stop at Murthal for hot stuffed tandoori parathas with white makhan and ginger tea.", "Murthal Highway", "Iconic Breakfast", "Tandoori Gobhi-Aloo Paratha at Amrik Sukhdev"),
                        ("Afternoon", "Drive through the Bilaspur-Sundernagar tunnels; stop by Pandoh dam reservoir for panoramic photographs.", "Pandoh Dam", "Scenic Overlook", "Pahadi Rajma Madra at Shiva Dhaba"),
                        ("Evening", "Arrive in Manali; check in to your cedar-wood stay and take an evening stroll across Old Manali's cobblestone bridge.", "Old Manali", "Golden Hour", "Hot apple cider & thin-crust pizza at Cafe 1947"),
                        ("Night", "Bonfire under deodar pines with acoustic music and star-studded mountain skies.", "Old Manali Village", "Cozy Fireside", "Warm Pahadi Siddu with desi ghee")
                    ],
                    "tip": "Start from Delhi before 5:30 AM to bypass the Singhu border truck traffic.",
                    "stay": "Boutique Apple Orchard Cottage in Old Manali"
                },
                {
                    "theme": "Atal Tunnel Crossing & Sissu Waterfalls",
                    "activities": [
                        ("Morning", "Early drive through the engineering marvel of Atal Tunnel (9.02 km) crossing into the dramatic dry Lahaul valley.", "Atal Tunnel & Sissu", "Engineering Wonder", "Steaming Thukpa and butter tea in Sissu"),
                        ("Afternoon", "Walk to the base of the majestic Sissu waterfall; relax in the poplars along the turquoise Chandra river.", "Chandra Riverbed", "River Walk", "Pahadi Maggie and Tingmo"),
                        ("Evening", "Return through Solang valley; try thrilling paragliding or cable car ride with panoramic valley views.", "Solang Valley", "Adrenaline", "Roasted mountain bhutta with spicy lemon"),
                        ("Night", "Dinner at Mall road with authentic Tibetan delicacies.", "Manali Mall Road", "Bazaar Walk", "Steamed Tibetan Momos at Chopsticks")
                    ],
                    "tip": "Carry a windproof jacket to Sissu; wind speeds in Lahaul valley pick up dramatically by afternoon.",
                    "stay": "Old Manali Valley View Resort"
                },
                {
                    "theme": "Sacred Cedar Woods & Hot Springs",
                    "activities": [
                        ("Morning", "Peaceful walk through the 500-year-old towering Dhungri forest to the sacred wooden Hadimba Temple.", "Hadimba Forest", "Spiritual Nature", "Fresh apple juice and walnut cake"),
                        ("Afternoon", "Visit Vashisht village natural sulfur hot springs for a rejuvenating therapeutic bath.", "Vashisht Hot Springs", "Wellness", "Organic Pahadi Thali at a local dhaba"),
                        ("Evening", "Cafe hopping in Old Manali, browsing woolen shawls and handmade jewelry in local village stalls.", "Old Manali Alleys", "Cultural Immersion", "Wood-fired trout or mushroom risotto"),
                        ("Night", "Relaxing terrace dinner with views of the snow-lit peaks under the moon.", "Hotel Terrace", "Quiet Night", "Warm Badam Milk with saffron")
                    ],
                    "tip": "Temple bells ring early for the 6:30 AM Hadimba aarti—a deeply serene experience without tourists.",
                    "stay": "Old Manali Valley View Resort"
                },
                {
                    "theme": "Naggar Castle Heritage & Riverside Farewell",
                    "activities": [
                        ("Morning", "Drive along the left bank to historic Naggar Castle (1460 AD) with exquisite Himalayan wooden architecture.", "Naggar Castle", "Heritage Wonder", "German bakery strudel and French press coffee"),
                        ("Afternoon", "Visit the Nicholas Roerich Art Gallery surrounded by peaceful deodar gardens.", "Naggar Estate", "Art & Serenity", "Traditional Himachali Dham feast"),
                        ("Evening", "Riverside sunset picnic along the Beas river near Raison; buy authentic Kullu shawls from weavers' cooperatives.", "Beas Riverbed", "Scenic Farewell", "Kulhad chai with fresh ginger"),
                        ("Night", "Begin relaxing return journey or overnight Volvo journey with fond mountain memories.", "Highway Outskirts", "Homeward Bound", "Dinner at Ambala Highway Dhaba")
                    ],
                    "tip": "Visit the Himachal Handloom weavers outlet near Kullu to get genuine Kullu shawls with GI tags.",
                    "stay": "Homeward transit / Extension stay"
                }
            ],
            "default": [
                {
                    "theme": "Departure & Highway Discoveries",
                    "activities": [
                        ("Morning", f"Early departure from {dest.get('default_origin', 'your city')}; morning breakfast at an iconic highway dhaba.", "Highway Express", "Road Trip Vibe", "Piping hot stuffed parathas or crisp dosas"),
                        ("Afternoon", f"Scenic arrival in {dest_name}; scenic hotel check-in and unhurried freshening up.", "Arrival Check-in", "Settling In", "Freshly prepared local welcome meal"),
                        ("Evening", "Stroll through the heritage promenade or local marketplace taking in the sights and scents.", "Town Center", "Orientation Walk", "Signature street snacks & local tea"),
                        ("Night", "Welcome dinner at a handpicked regional restaurant with cultural ambiance.", "Heritage Diner", "Evening Feast", "Authentic regional thali specialty")
                    ],
                    "tip": "Pack small cash notes for local temple offerings, highway toll gates and street vendor chai.",
                    "stay": "Boutique Heritage Homestay"
                },
                {
                    "theme": "Iconic Landmarks & Cultural Secrets",
                    "activities": [
                        ("Morning", "Sunrise visit to the premier natural or spiritual landmark before crowds arrive.", "Primary Landmark", "Golden Light", "Traditional local breakfast specialty"),
                        ("Afternoon", "Curated tour of historic palaces, temples, or nature reserves with a local guide.", "Historic Quarter", "Heritage Dive", "Traditional home-style lunch feast"),
                        ("Evening", "Sunset viewpoint visit with panoramic photography and hot kulhad chai.", "Scenic Viewpoint", "Sunset Magic", "Roasted snacks & spiced chai"),
                        ("Night", "Leisurely dinner at a bohemian courtyard cafe with folk melodies.", "Boutique Cafe", "Atmospheric Night", "Signature regional delicacies")
                    ],
                    "tip": "Ask local shopkeepers for the oldest traditional sweet shop—it's always better than tourist traps.",
                    "stay": "Boutique Heritage Homestay"
                },
                {
                    "theme": "Offbeat Trails & Nature Immersion",
                    "activities": [
                        ("Morning", "Morning nature walk through pine woods, tea hills, backwaters, or hidden village alleys.", "Nature Trail", "Fresh Air", "Fresh fruits & herbal mountain tea"),
                        ("Afternoon", "Visit nearby waterfalls, secluded riverbeds, or ancient stepwells for tranquility.", "Hidden Spot", "Untouched Beauty", "Picnic lunch or village meal"),
                        ("Evening", "Souvenir shopping for local handicrafts, spices, silks, and artisanal teas.", "Artisans Market", "Shopping", "Hot savory chaat & fresh sugarcane juice"),
                        ("Night", "Farewell campfire or candle-lit dinner with music and starry skies.", "Resort Lawn", "Celebration", "Special chef tasting menu")
                    ],
                    "tip": "Always bargain respectfully at street markets, or visit state-run emporiums for fixed fair pricing.",
                    "stay": "Boutique Heritage Homestay"
                },
                {
                    "theme": "Sacred Memories & Homeward Journey",
                    "activities": [
                        ("Morning", "Gentle morning reflection; final temple darshan or peaceful sunrise river walk.", "Sanctuary / River", "Peaceful Dawn", "Light breakfast and filter coffee"),
                        ("Afternoon", "Check-out and embark on the return route with pleasant pitstops.", "Scenic Highway", "Smooth Transit", "Highway dhaba lunch feast"),
                        ("Evening", "Arrive back refreshed, carrying bags full of authentic memories and stories.", "Home Destination", "Trip Completion", "Comfort tea at home"),
                        ("Night", "Rest and cherish the unforgettable frames of your Indian voyage.", "Home", "Soulful Memories", "Homecooked comfort meal")
                    ],
                    "tip": "Keep your trip photos backed up and review your favorite local restaurant on Google Maps to support local families.",
                    "stay": "Home destination"
                }
            ]
        }

        # Select blueprint based on dest_id or use default
        blueprint = day_blueprints.get(dest_id, day_blueprints["default"])

        # Adjust for requested duration
        for day_idx in range(duration_days):
            bp_idx = day_idx if day_idx < len(blueprint) else (day_idx % len(blueprint))
            data = blueprint[bp_idx]

            activities: List[DayActivity] = []
            for time_slot, desc, loc, tag, food in data["activities"]:
                title_text = f"{time_slot} Experience: {tag}" if tag else f"{time_slot} Exploration"
                activities.append(DayActivity(
                    time_of_day=time_slot,
                    title=title_text,
                    description=desc,
                    location=loc,
                    highlight_tag=tag,
                    food_recommendation=food
                ))

            itinerary.append(DayPlan(
                day=day_idx + 1,
                title=f"Day {day_idx + 1}: {data['theme']}",
                theme=data["theme"],
                activities=activities,
                local_tip=data["tip"],
                stay_recommendation=data["stay"]
            ))

        return itinerary

    @staticmethod
    def get_recommendation(req: FilterRequest, api_key: Optional[str] = None) -> RecommendationResponse:
        """
        Main generator that synthesizes the entire trip recommendation.
        """
        destination = RecommendationEngine.match_destination(req)
        dest_id = destination["id"]
        origin = req.origin if req.origin and req.origin.strip() else destination.get("default_origin", "Delhi")

        # 1. Weather
        weather = WeatherService.get_weather_for_destination(dest_id, req.season)

        # 2. Route & Pitstops
        route = RouteService.calculate_route(dest_id, origin)

        # 3. Packages
        packages = RecommendationEngine.compute_packages(
            destination, req.duration_days, req.group_type, req.transport_mode
        )
        # Mark user's budget tier as active
        active_tier_id = req.budget_tier.lower() if req.budget_tier.lower() in ["backpacker", "comfort", "luxury"] else "comfort"
        for pkg in packages:
            pkg.is_recommended = (pkg.id == active_tier_id)

        # 4. Day-by-Day Itinerary
        itinerary = RecommendationEngine.generate_itinerary(
            destination, req.duration_days, req.group_type, req.diet_preference, req.season
        )

        # 5. Stays
        raw_stays = STAYS_DATA.get(dest_id, STAYS_DATA.get("delhi-manali", []))
        stays: List[StayRecommendation] = []
        for s in raw_stays:
            stays.append(StayRecommendation(
                name=s["name"],
                type=s["type"],
                location=s["location"],
                approx_price_per_night_inr=s["approx_price_per_night_inr"],
                vibe=s["vibe"],
                amenities=s["amenities"],
                rating=s["rating"]
            ))

        # 6. Food Spots (Dhabas & Cafes)
        raw_food = DHABAS_AND_CAFES.get(dest_id, [])
        curated_food: List[Pitstop] = []
        for f in raw_food:
            curated_food.append(Pitstop(
                name=f["name"],
                category=f["category"],
                highway=f["highway"],
                km_from_origin=f["km_from_origin"],
                location=f["location"],
                famous_for=f["famous_for"],
                pure_veg=f["pure_veg"],
                jain_available=f["jain_available"],
                avg_cost_inr=f["avg_cost_inr"],
                rating=f.get("rating", 4.5),
                highlight_dish=f.get("highlight_dish"),
                image_url=f.get("image_url")
            ))

        # 7. AI Story & Personalized Tips
        ai_meta = AIService.generate_story_and_tips(
            destination["name"],
            origin,
            req.season,
            req.group_type,
            active_tier_id,
            req.diet_preference,
            api_key=api_key
        )

        return RecommendationResponse(
            destination_id=dest_id,
            destination_name=destination["name"],
            state=destination["state"],
            tagline=destination["tagline"],
            cover_image=destination["cover_image"],
            vibe_tags=destination.get("vibe_tags", []),
            season=req.season,
            weather=weather,
            route=route,
            packages=packages,
            active_package_id=active_tier_id,
            itinerary=itinerary,
            hotels_and_stays=stays,
            curated_food_spots=curated_food,
            ai_story=ai_meta.get("story"),
            ai_personalized_tips=ai_meta.get("tips", [])
        )
