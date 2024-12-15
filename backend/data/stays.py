"""
Handpicked authentic accommodations across 3 Indian travel tiers:
Backpacker (Zostels/Homestays), Comfort (Boutique/Havelis), and Royal Luxury (Palaces/5-Star).
"""

STAYS_DATA = {
    "delhi-manali": [
        {
            "name": "The Hosteller / Zostel Old Manali",
            "type": "hostel",
            "location": "Old Manali Village",
            "approx_price_per_night_inr": 850,
            "vibe": "Backpacker haven surrounded by apple trees, acoustic bonfires, high-speed WiFi and mountain views.",
            "amenities": ["Common Rooftop Cafe", "Lockers", "Bonfire Area", "High-speed WiFi", "Board Games"],
            "rating": 4.6
        },
        {
            "name": "Apple Country Boutique Resort & Spa",
            "type": "boutique_homestay",
            "location": "Log Huts Area, Manali",
            "approx_price_per_night_inr": 4200,
            "vibe": "Cedar wood mountain chalets overlooking the snow peaks with cedar bath tubs and orchard balconies.",
            "amenities": ["Mountain View Balconies", "Heating", "Buffet Breakfast", "Spa", "Fireplace Lounge"],
            "rating": 4.7
        },
        {
            "name": "The Himalayan Castle & Luxury Cottages",
            "type": "luxury_resort",
            "location": "Hadimba Road, Manali",
            "approx_price_per_night_inr": 16500,
            "vibe": "Victorian gothic stone castle with antique four-poster beds, heated outdoor swimming pool and fine dining.",
            "amenities": ["Heated Pool", "Antique Fireplaces", "Butler Service", "Orchard Dining", "Himalayan View Suites"],
            "rating": 4.9
        }
    ],
    "delhi-rishikesh-chopta": [
        {
            "name": "Shalom Backpackers / Zostel Rishikesh",
            "type": "hostel",
            "location": "Tapovan, Rishikesh",
            "approx_price_per_night_inr": 750,
            "vibe": "Rooftop yoga deck with views of the Ganga river, vibrant international backpacker community.",
            "amenities": ["Yoga Deck", "Co-working Space", "Ganga View Rooftop", "Community Kitchen"],
            "rating": 4.7
        },
        {
            "name": "Monal Himalayan Eco Camps & Homestay",
            "type": "boutique_homestay",
            "location": "Dugalbitta, Chopta",
            "approx_price_per_night_inr": 3200,
            "vibe": "Cozy Swiss alpine tents amidst deodar woods with unobstructed sunrise vistas of Chaukhamba peak.",
            "amenities": ["Attached Heated Bathrooms", "Stargazing Meadow", "Pahadi Home Cooking", "Bonfire Nights"],
            "rating": 4.8
        },
        {
            "name": "Ananda in the Himalayas / Taj Rishikesh",
            "type": "luxury_resort",
            "location": "Narendra Nagar / Byasi Foothills",
            "approx_price_per_night_inr": 28000,
            "vibe": "Palace of the Maharaja of Tehri Garhwal: world-renowned destination spa, private Ganga pebble beach.",
            "amenities": ["World-Class Ayurvedic Spa", "Private Infinity Pool", "Private Aarti", "Helipad Access", "Gourmet Organic Dining"],
            "rating": 5.0
        }
    ],
    "mumbai-goa-nh66": [
        {
            "name": "Whoopers Hostel / Woke Hostel Arpora",
            "type": "hostel",
            "location": "Anjuna / Arpora, North Goa",
            "approx_price_per_night_inr": 800,
            "vibe": "Old Portuguese villa turned social hostel with courtyard pool, palm trees, and scooter rentals.",
            "amenities": ["Swimming Pool", "Bicycle & Scooter Rentals", "Bar & Social Lounge", "Coworking Desks"],
            "rating": 4.6
        },
        {
            "name": "Casa da Graça / Heritage Fontainhas Villa",
            "type": "boutique_homestay",
            "location": "Fontainhas Latin Quarter, Panaji",
            "approx_price_per_night_inr": 4800,
            "vibe": "Restored 19th-century Portuguese townhouse with terracotta tiled roofs, wrought-iron balconies and azulejo tiles.",
            "amenities": ["Artisanal Breakfast", "Oyster Shell Windows", "Walking Tours", "Vintage Library"],
            "rating": 4.8
        },
        {
            "name": "Taj Exotica Resort & Spa / Alila Diwa",
            "type": "luxury_resort",
            "location": "Benaulim, South Goa",
            "approx_price_per_night_inr": 22000,
            "vibe": "Mediterranean-inspired 56-acre sprawling beachfront estate overlooking the Arabian Sea.",
            "amenities": ["Private Beach Access", "Golf Course", "Jiva Spa", "Private Plunge Pool Villas", "Sunset Seafood Grills"],
            "rating": 4.9
        }
    ],
    "jaipur-jodhpur-jaisalmer": [
        {
            "name": "Moustache Hostel Jaipur / Jodhpur",
            "type": "hostel",
            "location": "Near Forts",
            "approx_price_per_night_inr": 650,
            "vibe": "Colorful Rajasthani jharokhas, rooftop chai lounge with sunset fort views and puppet shows.",
            "amenities": ["Rooftop Cafe", "Luggage Storage", "Desert Safari Bookings", "AC Dorms"],
            "rating": 4.6
        },
        {
            "name": "Mandir Palace Heritage Homestay",
            "type": "boutique_homestay",
            "location": "Jaisalmer Fort Outskirts",
            "approx_price_per_night_inr": 5200,
            "vibe": "Intricately carved golden sandstone palace dating back two centuries with peacocks in the courtyards.",
            "amenities": ["Courtyard Dining", "Heritage Architecture", "Folk Dance Evenings", "Rooftop Fort Vistas"],
            "rating": 4.8
        },
        {
            "name": "Suryagarh Jaisalmer / Umaid Bhawan Palace",
            "type": "luxury_resort",
            "location": "Thar Desert / Jodhpur",
            "approx_price_per_night_inr": 32000,
            "vibe": "Fortress luxury in the middle of the Thar desert with royal champagne breakfasts and Halwai breakfasts.",
            "amenities": ["Desert Stargazing with Astronomer", "Chauffeured Thar Safaris", "Rait Spa", "Private Courtyard Suites"],
            "rating": 5.0
        }
    ],
    "bangalore-coorg-wayanad": [
        {
            "name": "Zostel Homes Coorg",
            "type": "hostel",
            "location": "Siddapur Coffee Belt",
            "approx_price_per_night_inr": 900,
            "vibe": "Perched inside a 50-acre working coffee estate with stream walks and homemade estate dinners.",
            "amenities": ["Coffee Plantation Tours", "Campfire", "Homecooked South Indian Meals", "Board Games"],
            "rating": 4.7
        },
        {
            "name": "Old Kent Estates & Heritage Cottages",
            "type": "boutique_homestay",
            "location": "Suntikoppa, Coorg",
            "approx_price_per_night_inr": 6800,
            "vibe": "British colonial planters bungalow built in the 1800s surrounded by Arabica coffee shrubs and hornbills.",
            "amenities": ["Plantation Spa", "Billiards Room", "Private Verandahs", "Curated Estate Dinners"],
            "rating": 4.9
        },
        {
            "name": "Evolve Back, Chikkana Halli Estate",
            "type": "luxury_resort",
            "location": "Ammathi, Coorg",
            "approx_price_per_night_inr": 29000,
            "vibe": "Kodava luxury villas with private private temperature-controlled plunge pools and fragrant spice groves.",
            "amenities": ["Private Pool Villas", "Ayurvedic Village", "Machan Tree Dining", "Birdwatching Expeditions"],
            "rating": 5.0
        }
    ],
    "kochi-munnar-alleppey": [
        {
            "name": "Artpackers.life / Lost Hostels",
            "type": "hostel",
            "location": "Fort Kochi / Alleppey Beach",
            "approx_price_per_night_inr": 700,
            "vibe": "Heritage Dutch school building turned art-filled hostel steps from spice markets and Chinese fishing nets.",
            "amenities": ["Art Gallery Lounge", "Bicycle Rentals", "Kitchen Access", "Hammocks"],
            "rating": 4.6
        },
        {
            "name": "Spice Tree Luxury Homestay & Cottages",
            "type": "boutique_homestay",
            "location": "Munnar Tea Slopes",
            "approx_price_per_night_inr": 5500,
            "vibe": "Stone-walled eco-chalets embedded in mountain tea contours with panoramic forest infinity views.",
            "amenities": ["Mountain Infinity Pool", "Tea Tasting Sessions", "Herbal Baths", "Yoga Room"],
            "rating": 4.8
        },
        {
            "name": "Kumarakom Lake Resort / Oberoi Vrinda",
            "type": "luxury_resort",
            "location": "Vembanad Lake Backwaters",
            "approx_price_per_night_inr": 26000,
            "vibe": "Traditional 16th-century ancestral Tharavadu wooden homes reconstructed on the backwaters with meandering pool villas.",
            "amenities": ["Meandering Pool Access", "Private Backwater Cruises", "Ayurmana Spa", "Traditional Sunset Performances"],
            "rating": 5.0
        }
    ],
    "varanasi-ayodhya-prayagraj": [
        {
            "name": "Moustache Hostel / Bunkedup Kashi",
            "type": "hostel",
            "location": "Assi Ghat, Varanasi",
            "approx_price_per_night_inr": 650,
            "vibe": "Minutes walk from Assi Ghat morning aarti, lively common room filled with sitar players and storytellers.",
            "amenities": ["Rooftop Ganga View", "Walking Tours", "Chai Lounge", "Book Exchange"],
            "rating": 4.7
        },
        {
            "name": "Surabhi Heritage Homestay Kashi",
            "type": "boutique_homestay",
            "location": "Near Dashashwamedh Ghat",
            "approx_price_per_night_inr": 3800,
            "vibe": "Traditional courtyard Haveli with carved wooden doors, brass lamps and rooftop view of temple spires.",
            "amenities": ["Courtyard Breakfast", "Private Ghat Guide", "Classical Music Soirées", "AC Rooms"],
            "rating": 4.8
        },
        {
            "name": "BrijRama Palace Heritage Grand Hotel",
            "type": "luxury_resort",
            "location": "Darbhanga Ghat, Varanasi",
            "approx_price_per_night_inr": 24000,
            "vibe": "One of the oldest landmark palaces on the Ganga Ghats, reached exclusively by private wooden royal boat.",
            "amenities": ["Private Royal Boat Arrival", "Rooftop Ganga View Dining", "Live Morning Shehnai", "Pure Satvik Fine Dining"],
            "rating": 5.0
        }
    ],
    "guwahati-shillong-cherrapunji": [
        {
            "name": "Is庇 (Is-Pia) Backpackers Homestay",
            "type": "hostel",
            "location": "Laitumkhrah, Shillong",
            "approx_price_per_night_inr": 750,
            "vibe": "Charming pine cottage with indie acoustic guitars, fireplace evenings, and local Khasi hosts.",
            "amenities": ["Fireplace", "Guitar & Records", "Shared Kitchen", "Trek Guidance"],
            "rating": 4.7
        },
        {
            "name": "Polo Orchid Resort Cherrapunji",
            "type": "boutique_homestay",
            "location": "Sohra Canyon Edge",
            "approx_price_per_night_inr": 5800,
            "vibe": "Villas overlooking the Seven Sisters waterfalls and deep mystical limestone gorges.",
            "amenities": ["Canyon View Infinity Pool", "Private Balconies", "Orchid Restaurant", "Campfire"],
            "rating": 4.7
        },
        {
            "name": "Ri Kynjai - Serenity by the Lake",
            "type": "luxury_resort",
            "location": "Umiam Lake, Meghalaya",
            "approx_price_per_night_inr": 18500,
            "vibe": "Khasi thatch architecture inspired cottages on stilts overlooking the tranquil waters of Umiam Lake.",
            "amenities": ["Traditional Khasi Herbal Spa", "Lakefront Balconies", "Boating Access", "Fine Dining Pine Room"],
            "rating": 4.9
        }
    ]
}

