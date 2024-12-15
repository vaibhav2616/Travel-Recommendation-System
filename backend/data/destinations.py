"""
Curated Indian Destinations and Travel Corridors Database
Includes authentic Indian routes, highway identifiers, altitude, seasonal characteristics, and vibe tags.
"""

DESTINATIONS = [
    {
        "id": "delhi-manali",
        "name": "Manali & Solang Valley",
        "state": "Himachal Pradesh",
        "region": "Himalayas",
        "tagline": "Roaring Beas River, Pine Forests & Snowbound Passes",
        "altitude_m": 2050,
        "primary_highway": "NH44 & NH3 (Kiratpur-Manali Expressway)",
        "ideal_duration_days": 4,
        "cover_image": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?auto=format&fit=crop&w=1200&q=80",
        "vibe_tags": ["High Altitude", "Pine Mist", "River Cafes", "Old Wooden Villages", "Snow Adventures"],
        "default_origin": "Delhi",
        "distance_km": 530,
        "driving_time_hours": 10.5,
        "toll_estimate_inr": 820,
        "road_condition": "Smooth 4-lane expressway till Bilaspur, scenic ghat curves with tunnels through Mandi and Kullu.",
        "scenic_highlights": [
            "Kiratpur-Nerchowk tunnels cutting travel time",
            "Pandoh Dam & Beas River gorge",
            "Kullu apple orchards and shawl weaving clusters",
            "Atal Tunnel crossing to Lahaul valley"
        ],
        "seasons": {
            "monsoon": {
                "temp_range": "15°C to 24°C",
                "rainfall": "High",
                "vibe_summary": "Lush emerald valleys, mist tumbling over cedar tops, roaring Beas river, fresh mountain corn.",
                "advisories": ["Occasional cloudburst / landslide warnings near Mandi ghats", "River rafting usually paused", "Verify Rohtang pass access"],
                "what_to_pack": ["Quick-dry trek pants", "Waterproof trekking shoes with grip", "Light breathable raincoat", "Mosquito repellent"]
            },
            "winter": {
                "temp_range": "-3°C to 12°C",
                "rainfall": "Snowfall frequent",
                "vibe_summary": "Fairytale snowy landscapes, steaming bowls of Thukpa, bonfire evenings in Old Manali, skiing at Solang.",
                "advisories": ["Black ice near Marhi and Atal Tunnel early morning", "Carry tire snow chains if driving own car", "Keep buffer day for snow blockage"],
                "what_to_pack": ["Heavy down jacket", "Thermal inners (merino wool)", "Waterproof snow boots", "Gloves & beanie", "Moisturizer & lip balm"]
            },
            "autumn": {
                "temp_range": "8°C to 20°C",
                "rainfall": "Dry & Crisp",
                "vibe_summary": "Golden deodar foliage, apple picking harvest season, crisp clear Himalayan skies, perfect photography.",
                "advisories": ["Rapid temperature drop after sunset", "Pre-book boutique stays in Old Manali"],
                "what_to_pack": ["Layered fleece", "Windcheater", "Sturdy sneakers", "Camera with polarising filter"]
            },
            "summer": {
                "temp_range": "12°C to 28°C",
                "rainfall": "Mild",
                "vibe_summary": "Ultimate escape from plains heat, blooming paragliding fields, riverside cafe chilling, trout fishing.",
                "advisories": ["High tourist traffic on weekends; start drives before 6 AM", "Green tax checkposts"],
                "what_to_pack": ["Light cottons + evening jacket", "Sunscreen SPF 50+", "UV sunglasses", "Hydration flask"]
            }
        },
        "alternate_transits": [
            {
                "mode": "train",
                "title": "Vande Bharat / Shatabdi to Chandigarh + Mountain Cab",
                "duration_str": "3h 15m Train + 6h Mountain Cab",
                "approx_cost_inr": 2400,
                "scenic_rating": 4,
                "description": "Board early morning Vande Bharat (Train 22447) from New Delhi to Chandigarh, followed by a scenic private cab via the new Kiratpur Expressway.",
                "carbon_rating": "Medium"
            },
            {
                "mode": "flight",
                "title": "Flight to Bhuntar (Kullu) Airport + 1h Cab",
                "duration_str": "1h 20m Flight + 1h Cab to Manali",
                "approx_cost_inr": 6500,
                "scenic_rating": 5,
                "description": "Dramatic aerial flight through Himalayan valleys directly landing at Bhuntar runway, then a picturesque riverside drive to Manali.",
                "carbon_rating": "High"
            }
        ]
    },
    {
        "id": "delhi-rishikesh-chopta",
        "name": "Rishikesh, Devprayag & Chopta",
        "state": "Uttarakhand",
        "region": "Himalayas",
        "tagline": "Spiritual Ghats, Sacred Sangams & The Mini Switzerland of Garhwal",
        "altitude_m": 2680,
        "primary_highway": "NH334 & NH7 (Badrinath Highway)",
        "ideal_duration_days": 4,
        "cover_image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "vibe_tags": ["Ganga Aarti", "Highland Meadows", "Ancient Temples", "Boho Bakeries", "Tungnath Trek"],
        "default_origin": "Delhi",
        "distance_km": 420,
        "driving_time_hours": 9.0,
        "toll_estimate_inr": 540,
        "road_condition": "Smooth Delhi-Meerut expressway, 4-lane till Rishikesh, well-tarred all-weather mountain road till Chopta.",
        "scenic_highlights": [
            "Delhi-Meerut Expressway rapid transit",
            "Ganga Aarti along Parmarth Niketan & Triveni Ghat",
            "Devprayag confluence of Bhagirathi and Alaknanda rivers",
            "Misty rhododendron forests of Chopta & Tungnath (world's highest Shiva temple)"
        ],
        "seasons": {
            "monsoon": {
                "temp_range": "18°C to 27°C",
                "rainfall": "Very High",
                "vibe_summary": "Verdant green Garhwal hills, thunderous Ganga flow, misty forest meadows, hot ginger tea by waterfalls.",
                "advisories": ["Char Dham route experiences temporary landslip hold-ups", "Rafting in Rishikesh is closed during monsoons"],
                "what_to_pack": ["Tough poncho", "Waterproof backpack cover", "Salt for mountain leeches on grass treks", "Powerbank"]
            },
            "winter": {
                "temp_range": "-4°C to 10°C",
                "rainfall": "Snowy in Chopta",
                "vibe_summary": "Snow-capped meadows (Bugyals), crystal clear views of Chaukhamba and Nanda Devi peaks, cozy bonfire homestays.",
                "advisories": ["Road past Sari village can be slippery with ice", "Tungnath temple closed for winter, trek to Snowline open"],
                "what_to_pack": ["Heavy fleece layers", "Crampons / snow spikes for boots", "Insulated water thermos", "Sun protection"]
            },
            "autumn": {
                "temp_range": "10°C to 22°C",
                "rainfall": "Clear skies",
                "vibe_summary": "Sublime mountain visibility, post-monsoon green meadows turning golden, ideal stargazing conditions in Chopta.",
                "advisories": ["Chilly winds on mountain ridges; windproof outer shell essential"],
                "what_to_pack": ["Windproof jacket", "Trekking poles", "Headlamp for sunrise summit treks"]
            },
            "summer": {
                "temp_range": "16°C to 32°C",
                "rainfall": "Low",
                "vibe_summary": "Rhododendrons in vibrant pink and red bloom, pleasant cool weather in Chopta, evening dip at secret Ganga beaches.",
                "advisories": ["Pre-book camps in Chopta as eco-regulations limit tent counts"],
                "what_to_pack": ["Cotton daywear", "Light jacket for nights", "UV hat", "Trail walking shoes"]
            }
        },
        "alternate_transits": [
            {
                "mode": "train",
                "title": "Vande Bharat Express (Delhi to Yog Nagari Rishikesh)",
                "duration_str": "4h 45m Train + Mountain Cab to Chopta",
                "approx_cost_inr": 1650,
                "scenic_rating": 4,
                "description": "Take the smooth New Delhi - Rishikesh Vande Bharat, then hire a registered mountain taxi through Byasi and Devprayag.",
                "carbon_rating": "Low"
            },
            {
                "mode": "flight",
                "title": "Flight to Dehradun (Jolly Grant) + 40m Cab to Rishikesh",
                "duration_str": "55m Flight + 40m Cab",
                "approx_cost_inr": 3800,
                "scenic_rating": 3,
                "description": "Short hop to Dehradun airport located right near the foothills, 30 minutes from Rishikesh.",
                "carbon_rating": "High"
            }
        ]
    },
    {
        "id": "mumbai-goa-nh66",
        "name": "Goa Coastal & Konkan Hinterlands",
        "state": "Goa / Maharashtra",
        "region": "Coastal",
        "tagline": "Konkan Ghats, Cashew Groves, Portuguese Quarters & Golden Shores",
        "altitude_m": 15,
        "primary_highway": "NH66 (Mumbai-Goa Coastal Highway)",
        "ideal_duration_days": 5,
        "cover_image": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?auto=format&fit=crop&w=1200&q=80",
        "vibe_tags": ["Coastal Road Trip", "Konkan Seafood & Solkadhi", "Feni Distilleries", "Fontainhas Heritage", "Secret Lagoons"],
        "default_origin": "Mumbai",
        "distance_km": 580,
        "driving_time_hours": 10.0,
        "toll_estimate_inr": 480,
        "road_condition": "Four-lane coastal highway widening in progress, magnificent winding river bridges and green mango-orchard stretches.",
        "scenic_highlights": [
            "Kashedi Ghat and coastal mountain curves",
            "Chiplun river valley viewpoint",
            "Authentic Malvani roadside fish thali pitstops",
            "Pastel-hued Portuguese Latin Quarter in Panaji"
        ],
        "seasons": {
            "monsoon": {
                "temp_range": "24°C to 30°C",
                "rainfall": "High & Dramatic",
                "vibe_summary": "Goa at its most soulful: lush paddy fields glistening, Dudhsagar falls in full fury, empty beaches, romantic cafe rain watching.",
                "advisories": ["Sea is rough; swimming strictly prohibited on all beaches", "Motorcycle rentals require extra caution in rain"],
                "what_to_pack": ["Waterproof flip flops", "Breathable linen shirts", "Waterproof dry bags for phones", "Light umbrella"]
            },
            "winter": {
                "temp_range": "20°C to 32°C",
                "rainfall": "Zero",
                "vibe_summary": "Vibrant beach shacks, flea markets, world-class DJ sunsets, balmy ocean swims, candle-lit beach dinners.",
                "advisories": ["Peak festive pricing around Christmas/New Year; advance bookings mandatory"],
                "what_to_pack": ["Swimwear", "Sunscreen", "Beach cover-ups", "Evening resort wear"]
            },
            "autumn": {
                "temp_range": "23°C to 32°C",
                "rainfall": "Light showers tapering off",
                "vibe_summary": "Post-monsoon freshness, beach shacks newly opening, moderate crowd, gorgeous sunsets over Chapora Fort.",
                "advisories": ["Pleasant sunny days with occasional sudden drizzle"],
                "what_to_pack": ["Cotton shorts", "Sunglasses", "Mosquito repellent", "Camera"]
            },
            "summer": {
                "temp_range": "27°C to 35°C",
                "rainfall": "Low",
                "vibe_summary": "Quiet unhurried Goa, discounted heritage homestays, fresh Alphonso mangoes, sunset beer by the water.",
                "advisories": ["Afternoons are humid; plan beach time before 10 AM and after 4:30 PM"],
                "what_to_pack": ["Loose linens", "Wide-brim hat", "Electrolytes", "Cooling aloe vera gel"]
            }
        },
        "alternate_transits": [
            {
                "mode": "train",
                "title": "Madgaon Vande Bharat Express (CSMT to Goa)",
                "duration_str": "7h 45m Scenic Konkan Train",
                "approx_cost_inr": 2100,
                "scenic_rating": 5,
                "description": "Travel on the legendary Konkan Railway over viaducts, through tunnels, and across sparkling coastal backwaters with large panoramic windows.",
                "carbon_rating": "Low"
            },
            {
                "mode": "flight",
                "title": "Flight to MOPA (North Goa) or Dabolim",
                "duration_str": "1h 15m Flight",
                "approx_cost_inr": 3400,
                "scenic_rating": 2,
                "description": "Direct quick flight connecting Mumbai to the new MOPA North Goa airport, 35 minutes to Vagator and Morjim.",
                "carbon_rating": "High"
            }
        ]
    },
    {
        "id": "jaipur-jodhpur-jaisalmer",
        "name": "The Royal Rajasthan Desert Circuit",
        "state": "Rajasthan",
        "region": "Rajasthan",
        "tagline": "Golden Sand Dunes, Majestic Fortresses & Royal Thali Feasts",
        "altitude_m": 225,
        "primary_highway": "NH11 & NH125 (Desert Expressway)",
        "ideal_duration_days": 6,
        "cover_image": "https://images.unsplash.com/photo-1599661046289-e31897846e41?auto=format&fit=crop&w=1200&q=80",
        "vibe_tags": ["Living Forts", "Camel Desert Safaris", "Dal Baati Churma", "Folk Stargazing", "Havelis"],
        "default_origin": "Delhi",
        "distance_km": 780,
        "driving_time_hours": 12.0,
        "toll_estimate_inr": 920,
        "road_condition": "World-class smooth expressways, expansive desert straightaways with minimal traffic between Jodhpur and Jaisalmer.",
        "scenic_highlights": [
            "Amber Fort & Nahargarh sunset in Jaipur",
            "Mehrangarh Fort towering over the Blue City of Jodhpur",
            "Jaisalmer Golden Fort: only living fort in India",
            "Sam Sand Dunes desert camping under the Milky Way"
        ],
        "seasons": {
            "monsoon": {
                "temp_range": "26°C to 36°C",
                "rainfall": "Low to Moderate",
                "vibe_summary": "The desert blooms with gentle shrubs, peacocks dancing on palace lawns, soothing evening breezes.",
                "advisories": ["Occasional flash water on low highway passes", "Mild humidity during daytime"],
                "what_to_pack": ["Breathable cottons", "Hat", "Walking sandals", "Stole for temple visits"]
            },
            "winter": {
                "temp_range": "7°C to 25°C",
                "rainfall": "Zero",
                "vibe_summary": "Absolute best time to visit: crisp desert air, folk music by bonfire under star-studded skies, warm Ghewar & Ker Sangri.",
                "advisories": ["Nights in desert tents can drop below 5°C; warm jackets needed"],
                "what_to_pack": ["Warm woolens for nights", "Shawl/poncho", "Sun protection for afternoon fort tours"]
            },
            "autumn": {
                "temp_range": "20°C to 33°C",
                "rainfall": "Dry",
                "vibe_summary": "Festive season, Pushkar camel fair preparations, vibrant bazaars full of bandhani fabrics and silver jewelry.",
                "advisories": ["High footfall in heritage monuments"],
                "what_to_pack": ["Sunglasses", "Light jacket", "Comfortable walking shoes with socks for hot stone courtyards"]
            },
            "summer": {
                "temp_range": "32°C to 45°C",
                "rainfall": "Dry Heat",
                "vibe_summary": "Budget traveler's paradise: luxury palace hotels available at 70% off, serene empty temples.",
                "advisories": ["Extreme heatwaves in desert; outdoor activities restricted to before 9 AM and after 5:30 PM"],
                "what_to_pack": ["Ultra-light full-sleeve cottons", "Electrolyte powders", "Heavy sunscreen", "Scarf for face covering"]
            }
        },
        "alternate_transits": [
            {
                "mode": "train",
                "title": "Vande Bharat Express (Delhi to Jaipur/Jodhpur)",
                "duration_str": "3h 45m to Jaipur, 7h 50m to Jodhpur",
                "approx_cost_inr": 1850,
                "scenic_rating": 3,
                "description": "Smooth semi-high speed transit with complimentary regional breakfast and comfortable executive chairs.",
                "carbon_rating": "Low"
            },
            {
                "mode": "flight",
                "title": "Flight Delhi to Jodhpur / Jaisalmer Airport",
                "duration_str": "1h 15m Flight",
                "approx_cost_inr": 4500,
                "scenic_rating": 2,
                "description": "Direct flight saving 14 hours of drive time, landing right next to the desert dunes.",
                "carbon_rating": "High"
            }
        ]
    },
    {
        "id": "bangalore-coorg-wayanad",
        "name": "Coorg, Kabini & Wayanad",
        "state": "Karnataka / Kerala",
        "region": "South",
        "tagline": "Misty Coffee Estates, Wild Elephant Corridors & Kodava Feasts",
        "altitude_m": 1150,
        "primary_highway": "NH275 & Mysore-Madikeri Road",
        "ideal_duration_days": 4,
        "cover_image": "https://images.unsplash.com/photo-1596401057633-54a8fe8ef647?auto=format&fit=crop&w=1200&q=80",
        "vibe_tags": ["Coffee Plantations", "Wildlife Safari", "Kodava Pork / Veg Stew", "Waterfalls", "Bamboo Rafting"],
        "default_origin": "Bengaluru",
        "distance_km": 260,
        "driving_time_hours": 5.5,
        "toll_estimate_inr": 340,
        "road_condition": "Bangalore-Mysore 10-lane expressway allows cruising at 100 km/h, followed by shaded ghat roads bordered by teak forests.",
        "scenic_highlights": [
            "Bengaluru-Mysuru Access-Controlled Expressway",
            "Maddur Vada & Bidadi Thatte Idli stops",
            "Sprawling Robusta and Arabica coffee estates with silver oak shade",
            "Nagarhole & Bandipur national park borders"
        ],
        "seasons": {
            "monsoon": {
                "temp_range": "18°C to 24°C",
                "rainfall": "Very High",
                "vibe_summary": "Coorg at its rawest beauty: Abbey Falls roaring, mist hanging like silk over coffee plants, piping hot filter coffee.",
                "advisories": ["High leech activity on estate walks; wear leech socks", "Ghat curves require cautious driving in heavy rain"],
                "what_to_pack": ["Leech socks", "Gore-Tex rain jacket", "Waterproof boots", "Mosquito lotion"]
            },
            "winter": {
                "temp_range": "13°C to 28°C",
                "rainfall": "Negligible",
                "vibe_summary": "Pleasant morning chill, clear blue skies, estate walks, birdwatching, campfire nights with pandi curry and akki rotti.",
                "advisories": ["Early morning fog across Mysore expressway"],
                "what_to_pack": ["Cardigan / light sweater", "Walking shoes", "Camera with zoom lens for birding"]
            },
            "autumn": {
                "temp_range": "16°C to 27°C",
                "rainfall": "Gentle showers",
                "vibe_summary": "Coffee berries ripening to ruby red, blooming wild orchids, sparkling mountain streams.",
                "advisories": ["Moderate crowd on long weekends"],
                "what_to_pack": ["Casual cottons", "Umbrella", "Sneakers"]
            },
            "summer": {
                "temp_range": "20°C to 33°C",
                "rainfall": "Afternoon thundershowers",
                "vibe_summary": "Fragrant coffee blossom season turning estates snow-white, cool refuge from Bengaluru heat.",
                "advisories": ["River water levels lower; waterfalls have moderate flow"],
                "what_to_pack": ["Sun hat", "Sunglasses", "Cotton apparel"]
            }
        },
        "alternate_transits": [
            {
                "mode": "train",
                "title": "Vande Bharat Express (Bangalore to Mysore) + 2h Cab",
                "duration_str": "1h 45m Train + 2h Cab to Coorg",
                "approx_cost_inr": 1200,
                "scenic_rating": 4,
                "description": "Ultra-fast sprint on Chennai-Bangalore-Mysore Vande Bharat, then a scenic estate cab climb to Madikeri.",
                "carbon_rating": "Low"
            },
            {
                "mode": "road",
                "title": "Self-Drive SUV via Nagarhole Forest Corridor",
                "duration_str": "5h 30m Scenic Drive",
                "approx_cost_inr": 2800,
                "scenic_rating": 5,
                "description": "Drive through the elephant corridor in Nagarhole with chances of spotting deer, peacocks, and wild tuskers.",
                "carbon_rating": "Medium"
            }
        ]
    },
    {
        "id": "kochi-munnar-alleppey",
        "name": "Munnar Tea Hills & Alleppey Backwaters",
        "state": "Kerala",
        "region": "South",
        "tagline": "Emerald Tea Carpets, Floating Houseboats & Malabar Spice Feasts",
        "altitude_m": 1600,
        "primary_highway": "NH85 (Gap Road Kochi-Dhanushkodi)",
        "ideal_duration_days": 5,
        "cover_image": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?auto=format&fit=crop&w=1200&q=80",
        "vibe_tags": ["Tea Plantations", "Houseboat Cruise", "Appam & Stew", "Ayurvedic Spa", "Kathakali & Kalaripayattu"],
        "default_origin": "Kochi",
        "distance_km": 190,
        "driving_time_hours": 4.5,
        "toll_estimate_inr": 120,
        "road_condition": "Newly restored Munnar Gap Road is widely hailed as one of the most scenic cliff-side drives in Asia.",
        "scenic_highlights": [
            "Cheeyappara and Valara roaring waterfalls",
            "Munnar Gap Road cliff hugging bends with sea of clouds",
            "Eravikulam National Park (home to Nilgiri Tahr)",
            "Vembanad Lake sunset houseboat cruise in Alleppey"
        ],
        "seasons": {
            "monsoon": {
                "temp_range": "19°C to 26°C",
                "rainfall": "Very High",
                "vibe_summary": "Kerala's magical Ayurveda monsoon (Karkidaka Chikitsa), waterfalls in glorious spate, romantic houseboat rain cruises.",
                "advisories": ["High-altitude hiking may have slippery moss; stick to paved trails"],
                "what_to_pack": ["Trench raincoat", "Quick dry apparel", "Waterproof phone pouch"]
            },
            "winter": {
                "temp_range": "10°C to 24°C",
                "rainfall": "Dry & Crisp",
                "vibe_summary": "Sub-zero frost nights in top station Munnar, pleasant sunny backwater days, fresh Karimeen fry on banana leaves.",
                "advisories": ["Evenings in Munnar get quite chilly"],
                "what_to_pack": ["Light sweater / shawl", "Cotton clothes for Alleppey", "Sunglasses"]
            },
            "autumn": {
                "temp_range": "18°C to 28°C",
                "rainfall": "Moderate",
                "vibe_summary": "Post-monsoon tea gardens vivid green, Nehru Trophy boat race season nearby, tranquil canals.",
                "advisories": ["Book houseboats with verified pollution & safety clearance"],
                "what_to_pack": ["Insect repellent", "Cotton shirts", "Camera"]
            },
            "summer": {
                "temp_range": "22°C to 32°C",
                "rainfall": "Occasional",
                "vibe_summary": "Munnar stays refreshingly cool while plains are warm; great time to spot Nilgiri Tahr calves.",
                "advisories": ["Backwaters in Alleppey can be humid during midday; ensure AC houseboat"],
                "what_to_pack": ["Sun protection", "Linen shirts", "Sandals"]
            }
        },
        "alternate_transits": [
            {
                "mode": "train",
                "title": "Vande Bharat Express (Trivandrum/Ernakulam to Alleppey)",
                "duration_str": "1h 10m Express Train",
                "approx_cost_inr": 650,
                "scenic_rating": 4,
                "description": "Glides parallel to the coastal palm groves and lagoon bridges directly into Alleppey station.",
                "carbon_rating": "Low"
            },
            {
                "mode": "flight",
                "title": "Fly into Cochin International (COK) + 3.5h Hill Cab",
                "duration_str": "Direct Flight + Hill Climb",
                "approx_cost_inr": 3600,
                "scenic_rating": 4,
                "description": "World's first 100% solar-powered airport, leading directly into the hill highway.",
                "carbon_rating": "Medium"
            }
        ]
    },
    {
        "id": "varanasi-ayodhya-prayagraj",
        "name": "Kashi, Ayodhya & Sangam Spiritual Circuit",
        "state": "Uttar Pradesh",
        "region": "Sacred",
        "tagline": "Timeless Ghats, Vedic Chants, Banarasi Silk & Sacred Rivers",
        "altitude_m": 80,
        "primary_highway": "NH19 & Purvanchal Expressway",
        "ideal_duration_days": 4,
        "cover_image": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?auto=format&fit=crop&w=1200&q=80",
        "vibe_tags": ["Subah-e-Banaras", "Ganga Aarti", "Kachori Jalebi", "Boat Ride at Dawn", "Ram Mandir"],
        "default_origin": "Delhi",
        "distance_km": 820,
        "driving_time_hours": 11.5,
        "toll_estimate_inr": 1150,
        "road_condition": "World-class 6-lane Yamuna & Agra-Lucknow Expressway linked to Purvanchal Expressway for smooth driving.",
        "scenic_highlights": [
            "Sunrise wooden row-boat cruise across 84 Ghats of Kashi",
            "Evening Grand Ganga Aarti at Dashashwamedh Ghat",
            "Newly consecrated Ram Mandir complex in Ayodhya",
            "Triveni Sangam boat ride at Prayagraj"
        ],
        "seasons": {
            "monsoon": {
                "temp_range": "26°C to 34°C",
                "rainfall": "High",
                "vibe_summary": "Ganga in majestic full spate touching the top steps of the ghats, dramatic monsoon clouds over minarets and temples.",
                "advisories": ["Boats may be suspended if Ganga water level crosses danger mark", "Ghat walkways can be submerged"],
                "what_to_pack": ["Non-slip footwear for wet stone steps", "Umbrella", "Quick dry pants"]
            },
            "winter": {
                "temp_range": "8°C to 23°C",
                "rainfall": "Dry",
                "vibe_summary": "Peak season: magical morning fog lifting over the river, migratory Siberian gulls flocking the ghats, piping hot Malaiyo & rabdi.",
                "advisories": ["Dense morning fog on Yamuna/Purvanchal expressway; drive with fog lights after 8 AM"],
                "what_to_pack": ["Warm jacket", "Shawl for evening Ganga aarti", "Comfortable walking shoes for maze-like gallis"]
            },
            "autumn": {
                "temp_range": "19°C to 30°C",
                "rainfall": "Minimal",
                "vibe_summary": "Dev Deepawali spectacle: 1 million clay lamps lit across the crescent ghats, fireworks and classical concerts.",
                "advisories": ["Book ghat boats months in advance for Dev Deepawali"],
                "what_to_pack": ["Camera", "Traditional Indian attire for temple darshan", "Sunglasses"]
            },
            "summer": {
                "temp_range": "30°C to 44°C",
                "rainfall": "Hot & Dry",
                "vibe_summary": "Soulful unhurried temple darshans with no queues, refreshing thandai and Banarasi paan at midnight.",
                "advisories": ["Afternoons are scorching; do temple visits between 5-9 AM and after 6 PM"],
                "what_to_pack": ["White cotton clothes", "Scarf for sun protection", "Electrolytes", "Sandalwood paste"]
            }
        },
        "alternate_transits": [
            {
                "mode": "train",
                "title": "Vande Bharat Express (Delhi to Varanasi - Train 22436)",
                "duration_str": "8h 00m Semi High-Speed Train",
                "approx_cost_inr": 1750,
                "scenic_rating": 4,
                "description": "India's flagship Vande Bharat route: reaches Varanasi from Delhi in just 8 hours with comfortable executive seating and meals.",
                "carbon_rating": "Low"
            },
            {
                "mode": "flight",
                "title": "Flight Delhi to Lal Bahadur Shastri Airport (VNS)",
                "duration_str": "1h 20m Flight",
                "approx_cost_inr": 3900,
                "scenic_rating": 2,
                "description": "Quick flight directly into Varanasi, 45 minutes to the heritage Ghats via Ring Road.",
                "carbon_rating": "High"
            }
        ]
    },
    {
        "id": "guwahati-shillong-cherrapunji",
        "name": "Meghalaya: Shillong, Cherrapunji & Dawki",
        "state": "Meghalaya",
        "region": "NorthEast",
        "tagline": "Living Root Bridges, Crystal Umngot River & Cloud-Shrouded Canyons",
        "altitude_m": 1520,
        "primary_highway": "NH6 (Guwahati-Shillong Expressway)",
        "ideal_duration_days": 5,
        "cover_image": "https://images.unsplash.com/photo-1589182373726-e4f658ab50f0?auto=format&fit=crop&w=1200&q=80",
        "vibe_tags": ["Living Root Bridges", "Crystal Clear Water", "Rock Music Cafes", "Nohkalikai Falls", "Caving"],
        "default_origin": "Guwahati",
        "distance_km": 165,
        "driving_time_hours": 4.5,
        "toll_estimate_inr": 140,
        "road_condition": "Smooth 4-lane expressway winding around Umiam Lake till Shillong; scenic 2-lane pine road till Sohra.",
        "scenic_highlights": [
            "Umiam Lake viewpoint water sports & boating",
            "Nohkalikai Falls (tallest plunge waterfall in India)",
            "Single & Double Decker Living Root Bridges of Nongriat",
            "Dawki Umngot River where boats look like they are floating in mid-air"
        ],
        "seasons": {
            "monsoon": {
                "temp_range": "18°C to 24°C",
                "rainfall": "Wettest Place on Earth",
                "vibe_summary": "Nature at its most dramatic: hundreds of thunderous waterfalls tumbling down limestone gorges, mystical swirling clouds.",
                "advisories": ["Dawki river loses its crystal transparency during heavy rain", "Steep stone steps down to root bridges become wet"],
                "what_to_pack": ["Heavy-duty waterproof raincoat", "Anti-skid trail shoes", "Waterproof dry bags"]
            },
            "winter": {
                "temp_range": "6°C to 18°C",
                "rainfall": "Low",
                "vibe_summary": "Dawki Umngot river is like 100% transparent liquid glass, cherry blossoms blooming across Shillong, vibrant music festivals.",
                "advisories": ["Evenings in Shillong are quite chilly"],
                "what_to_pack": ["Warm fleece/jacket", "Sneakers", "GoPro / action camera for river boating"]
            },
            "autumn": {
                "temp_range": "12°C to 22°C",
                "rainfall": "Low",
                "vibe_summary": "Shillong Autumn Festival, clear waterfall pools, pleasant hiking weather through sacred Khasi groves.",
                "advisories": ["Book boutique stays in Police Bazar or Laitumkhrah early"],
                "what_to_pack": ["Layered clothing", "Walking boots", "Powerbank"]
            },
            "summer": {
                "temp_range": "16°C to 26°C",
                "rainfall": "Moderate showers",
                "vibe_summary": "Escaping mainland heat, exploring ancient Mawsmai caves, zip-lining over Cherrapunji canyons.",
                "advisories": ["Sudden afternoon cloud covers are common"],
                "what_to_pack": ["Light jacket", "Sturdy sneakers", "Quick-dry clothes"]
            }
        },
        "alternate_transits": [
            {
                "mode": "flight",
                "title": "Flight to Guwahati (GAU) + 3h Mountain Cab to Shillong",
                "duration_str": "Flight + 3h Expressway Cab",
                "approx_cost_inr": 4800,
                "scenic_rating": 5,
                "description": "Fly to Guwahati, then drive on the spectacular highway skirting Umiam Lake with momo stops on the route.",
                "carbon_rating": "Medium"
            },
            {
                "mode": "train",
                "title": "Vande Bharat Express (New Jalpaiguri to Guwahati) + Cab",
                "duration_str": "5h 30m Train + 3h Cab",
                "approx_cost_inr": 1850,
                "scenic_rating": 4,
                "description": "Crosses the Brahmaputra river plains with views of the tea estates and foothill forests.",
                "carbon_rating": "Low"
            }
        ]
    },
    {
        "id": "leh-ladakh-circuit",
        "name": "Leh, Nubra Valley & Pangong Tso",
        "state": "Ladakh (UT)",
        "region": "Himalayas",
        "tagline": "Trans-Himalayan Moonscapes, Glacial Passes & Turquoise High-Altitude Lakes",
        "altitude_m": 3500,
        "primary_highway": "NH3 (Manali-Leh Highway) & Khardung La Pass",
        "ideal_duration_days": 6,
        "cover_image": "https://images.unsplash.com/photo-1581793745862-99fde7fa73d2?auto=format&fit=crop&w=1200&q=80",
        "vibe_tags": ["High Altitude Desert", "Buddhist Monasteries", "Khardung La (17,982 ft)", "Pangong Tso Blue", "Bactrian Camels"],
        "default_origin": "Delhi",
        "distance_km": 980,
        "driving_time_hours": 22.0,
        "toll_estimate_inr": 850,
        "road_condition": "Rugged high-altitude military highway open Jun-Oct. World-class BRO engineering over Baralacha La, Nakee La, and Tanglang La passes.",
        "scenic_highlights": [
            "Gata Loops (21 hairpin mountain bends climbing 1,500 ft)",
            "Morey Plains: 40 km flat high-altitude plateau at 15,000 ft",
            "Khardung La: One of the world's highest motorable passes",
            "Diskit Monastery & white sand dunes of Hunder with double-humped camels",
            "Pangong Tso lake shifting colors from turquoise to deep cobalt"
        ],
        "seasons": {
            "monsoon": {
                "temp_range": "10°C to 25°C",
                "rainfall": "Rain-Shadow Area (Dry & Clear)",
                "vibe_summary": "Peak travel season: while mainland India faces rains, Ladakh enjoys crystal-clear blue skies and roaring mountain streams.",
                "advisories": ["High-altitude sickness (AMS) risk; 48 hours mandatory acclimatization in Leh before crossing passes", "Carry Diamox and stay hydrated"],
                "what_to_pack": ["Heavy windcheater", "UV sunglasses with wrap-around protection", "SPF 50+ sunscreen", "Thermals & gloves", "Electrolytes"]
            },
            "winter": {
                "temp_range": "-15°C to 5°C",
                "rainfall": "Heavy Snow & Sub-Zero Freeze",
                "vibe_summary": "Chadar Frozen River Trek season, snow leopards roaming Hemis National Park, peaceful empty monasteries with prayer chants.",
                "advisories": ["High passes closed; accessible only by air into Leh airport", "Extreme sub-zero frostbite conditions"],
                "what_to_pack": ["Down expedition jacket (-20°C rated)", "Thermal inners x3", "Fleece-lined trekking boots", "Balaclava"]
            },
            "autumn": {
                "temp_range": "2°C to 18°C",
                "rainfall": "Dry & Crisp",
                "vibe_summary": "Golden poplars lining Indus and Zanskar rivers, Ladakhi Festival masked dances, crystal night skies for Milky Way photography.",
                "advisories": ["Pangong and Nubra camps start dismantling by mid-October"],
                "what_to_pack": ["Layered fleece", "Sturdy boots", "DSLR with wide-angle lens & tripod"]
            },
            "summer": {
                "temp_range": "8°C to 22°C",
                "rainfall": "Clear",
                "vibe_summary": "Passes opening ceremony, melting glacial streams, pleasant daytime temperatures, prayer flag fluttering on every ridge.",
                "advisories": ["High UV index; sunburn occurs within 30 minutes without sun protection"],
                "what_to_pack": ["Sun hat", "Lip balm with SPF", "Water bottle with filter", "Windproof jacket"]
            }
        },
        "alternate_transits": [
            {
                "mode": "flight",
                "title": "Flight Delhi to Kushok Bakula Rimpochee Airport (IXL)",
                "duration_str": "1h 25m Spectacular Flight",
                "approx_cost_inr": 5800,
                "scenic_rating": 5,
                "description": "One of the most dramatic mountain flight approaches on Earth over the snow-covered Greater Himalayas into Leh valley.",
                "carbon_rating": "Medium"
            },
            {
                "mode": "road",
                "title": "Manali-Leh Highway 2-Day 4x4 Expedition",
                "duration_str": "2 Days Expedition with Jispa Night Halt",
                "approx_cost_inr": 8500,
                "scenic_rating": 5,
                "description": "Epic bucket-list road trip across 5 Himalayan high passes with overnight camping by Bhaga river in Jispa.",
                "carbon_rating": "High"
            }
        ]
    },
    {
        "id": "kolkata-darjeeling-gangtok",
        "name": "Darjeeling & Gangtok: The Queen of Hills",
        "state": "West Bengal / Sikkim",
        "region": "Himalayas",
        "tagline": "Toy Train Chugs, Kanchenjunga Sunrises & Steaming Momos",
        "altitude_m": 2134,
        "primary_highway": "NH10 (Siliguri-Gangtok) & Hill Cart Road",
        "ideal_duration_days": 5,
        "cover_image": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "vibe_tags": ["DHR Toy Train", "Kanchenjunga Golden Peaks", "Glenary's Bakery", "First Flush Teas", "Tsomgo Glacial Lake"],
        "default_origin": "Kolkata",
        "distance_km": 610,
        "driving_time_hours": 12.5,
        "toll_estimate_inr": 620,
        "road_condition": "Smooth NH12 from Kolkata through Malda till Siliguri; winding Hill Cart Road climbing through tea terraces to Darjeeling.",
        "scenic_highlights": [
            "Batasia Loop & UNESCO World Heritage Darjeeling Himalayan Railway",
            "Tiger Hill 4:30 AM sunrise view illuminating Mount Kanchenjunga in gold",
            "Happy Valley Tea Estate tea plucking and artisanal tastings",
            "Tsomgo (Changu) Lake & Baba Mandir near Indo-China border at 12,400 ft"
        ],
        "seasons": {
            "monsoon": {
                "temp_range": "14°C to 20°C",
                "rainfall": "Heavy & Misty",
                "vibe_summary": "Tea gardens glistening in emerald green, clouds rolling into hotel rooms, hot darjeeling tea & steaming tingmo.",
                "advisories": ["NH10 along Teesta river can experience landslide delays; keep buffer time"],
                "what_to_pack": ["Sturdy umbrella", "Waterproof shoes", "Quick-dry socks"]
            },
            "winter": {
                "temp_range": "2°C to 12°C",
                "rainfall": "Dry & Crisp",
                "vibe_summary": "Unrivaled crystal visibility of Mount Kanchenjunga, Christmas carols and warm pastries at Glenary's, snow at Nathu La.",
                "advisories": ["Early mornings at Tiger Hill are below freezing; dress in heavy woolens"],
                "what_to_pack": ["Heavy wool coat", "Gloves & scarf", "Lip care", "Thermal inners"]
            },
            "autumn": {
                "temp_range": "10°C to 18°C",
                "rainfall": "Clear",
                "vibe_summary": "Post-monsoon golden skies, vibrant Durga Puja festive spirit in foothills, tea harvest concluding.",
                "advisories": ["Peak tourist rush during October festive holidays; book Toy Train joyrides in advance"],
                "what_to_pack": ["Cardigans", "Camera with zoom lens", "Comfortable walking shoes"]
            },
            "summer": {
                "temp_range": "12°C to 22°C",
                "rainfall": "Mild showers",
                "vibe_summary": "Classic British colonial hill station escape, pleasant walking promenade along The Mall and Chowrasta.",
                "advisories": ["Pre-book Sikkim Inner Line Permits (ILP) for Nathu La"],
                "what_to_pack": ["Light sweaters", "Sun hat", "Sneakers"]
            }
        },
        "alternate_transits": [
            {
                "mode": "train",
                "title": "Vande Bharat Express (Howrah to New Jalpaiguri - Train 22301)",
                "duration_str": "7h 30m Train + 2.5h Mountain Cab",
                "approx_cost_inr": 1950,
                "scenic_rating": 4,
                "description": "Board early morning Vande Bharat from Howrah to NJP in under 8 hours, then take a shared or private hill taxi climbing into Darjeeling.",
                "carbon_rating": "Low"
            },
            {
                "mode": "flight",
                "title": "Flight to Bagdogra (IXB) + 2.5h Hill Taxi",
                "duration_str": "1h 10m Flight + 2.5h Cab",
                "approx_cost_inr": 3400,
                "scenic_rating": 3,
                "description": "Quick flight directly to Bagdogra airport in North Bengal, leading straight onto the Hill Cart Road.",
                "carbon_rating": "High"
            }
        ]
    },
    {
        "id": "hampi-badami-gokarna",
        "name": "Hampi, Badami & Gokarna Om Beach",
        "state": "Karnataka",
        "region": "South",
        "tagline": "Vijayanagara Boulder Ruins, 6th-Century Rock Caves & Sacred Beach Coast",
        "altitude_m": 467,
        "primary_highway": "NH48 & NH67 (Deccan Corridor)",
        "ideal_duration_days": 5,
        "cover_image": "https://images.unsplash.com/photo-1600100397608-f010f421b5d1?auto=format&fit=crop&w=1200&q=80",
        "vibe_tags": ["UNESCO Boulder Ruins", "Stone Chariot", "Coracle River Rides", "Badami Red Sandstone Caves", "Om Beach Sunset"],
        "default_origin": "Bengaluru",
        "distance_km": 360,
        "driving_time_hours": 6.5,
        "toll_estimate_inr": 420,
        "road_condition": "Smooth 6-lane NH48 till Chitradurga, then 4-lane highway passing sunflower fields and wind turbine farms to Hospet.",
        "scenic_highlights": [
            "Vijaya Vittala Temple & iconic monolithic Stone Chariot with musical pillars",
            "Sunset hike up Matanga Hill overlooking sprawling ruins & Tungabhadra river",
            "Round woven coracle boat ride across the rushing boulders of Tungabhadra",
            "Badami 6th-century Chalukyan rock-cut cave temples carved into red cliffs",
            "Om Beach & Kudle Beach in Gokarna with laid-back beach shacks"
        ],
        "seasons": {
            "monsoon": {
                "temp_range": "22°C to 30°C",
                "rainfall": "Moderate",
                "vibe_summary": "Emerald green moss coating 500-year-old stone boulders, Tungabhadra river roaring, pleasant cool breezes across the ruins.",
                "advisories": ["Stone ruins and boulder steps can become slick when wet; wear gripping footwear"],
                "what_to_pack": ["Trekking sandals with rubber grip", "Light poncho", "Cotton clothes"]
            },
            "winter": {
                "temp_range": "16°C to 31°C",
                "rainfall": "Zero",
                "vibe_summary": "Absolute best time for Hampi: Hampi Utsav celebrations, cool morning cycling between ancient bazaars, peaceful beach sunsets.",
                "advisories": ["Sun can still feel warm in afternoon rocky terrain; carry water bottle"],
                "what_to_pack": ["Cotton daywear", "Light evening cardigan", "Sun hat & UV sunglasses", "Cycling shoes"]
            },
            "autumn": {
                "temp_range": "20°C to 32°C",
                "rainfall": "Low",
                "vibe_summary": "Pleasant unhurried travel, sunflower fields in full bloom along the highway, clear starlit skies over the boulder landscape.",
                "advisories": ["Book licensed ASI heritage guides at Vittala temple"],
                "what_to_pack": ["Camera with wide angle", "Comfortable sneakers", "Sunscreen"]
            },
            "summer": {
                "temp_range": "28°C to 41°C",
                "rainfall": "Dry Heat",
                "vibe_summary": "Offbeat traveler's dream: completely empty ruins for photography, cool refuge at Gokarna beaches in the evening.",
                "advisories": ["Granite boulders radiate intense heat; do site visits 6-10 AM and 4:30-7 PM"],
                "what_to_pack": ["Breathable cotton linens", "Electrolyte sachets", "Wide brim sun hat", "Cooling face mist"]
            }
        },
        "alternate_transits": [
            {
                "mode": "train",
                "title": "Hampi Express / Vande Bharat (Bengaluru to Hosapete / Dharwad)",
                "duration_str": "8h Overnight Train (Hospet) / 5h Vande Bharat (Hubli)",
                "approx_cost_inr": 1150,
                "scenic_rating": 4,
                "description": "Comfortable overnight train directly arriving at Hosapete Junction (12 km from Hampi ruins) at 7:00 AM.",
                "carbon_rating": "Low"
            },
            {
                "mode": "road",
                "title": "Self-Drive SUV via Chitradurga Fort & Windmills",
                "duration_str": "6h 30m Smooth Expressway Drive",
                "approx_cost_inr": 3600,
                "scenic_rating": 4,
                "description": "Cruising along the 6-lane Asian Highway past the historic Chitradurga stone fortress with famous Davanagere Benne Dosa stops.",
                "carbon_rating": "Medium"
            }
        ]
    }
]

