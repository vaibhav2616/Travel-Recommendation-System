"""
Indian Meteorological and Highway Route Dataset Generator for Weather ML/DL Model.
Generates synthetic yet physically grounded Indian weather profiles based on
altitude lapse rates, latitude/longitude zones, monsoons, western disturbances,
diurnal cycles, and terrain characteristics.
"""

import math
import numpy as np
from typing import Tuple, Dict, Any, List

# Terrain Categories
TERRAINS = {
    "plains": 0,       # Indo-Gangetic plains (Delhi, Punjab, UP)
    "foothills": 1,    # Shivaliks / Himalayan foothills (Chandigarh, Dehradun, Siliguri)
    "ghats": 2,        # Western Ghats / Mountain gorges (Mandi, Lonavala, Munnar slopes)
    "alpine": 3,       # High Himalayan mountain passes (Manali, Atal Tunnel, Leh, Chopta)
    "desert": 4,       # Thar desert (Jaipur, Jodhpur, Jaisalmer)
    "coastal": 5,      # Coastal Konkan, Goa, Kerala backwaters
    "plateau": 6       # Deccan plateau (Bengaluru, Mysore, Hampi)
}

CONDITION_CLASSES = [
    "clear",            # 0: Sunny or clear starlit skies
    "cloudy",           # 1: Overcast, misty, high clouds
    "rain",             # 2: Light to moderate rain showers
    "heavy_rain",       # 3: Monsoon downpour, thunderstorm
    "fog",              # 4: Dense radiation fog (winter plains)
    "snow"              # 5: Alpine Himalayan snowfall / sleet
]

def generate_indian_weather_sample(
    lat: float,
    lon: float,
    alt_m: float,
    month: int,
    hour: int,
    terrain: int,
    dist_ratio: float = 0.5,
    user_temp_offset: float = 0.0,
    noise: bool = True
) -> Dict[str, Any]:
    """
    Simulates authentic Indian meteorological physics.
    """
    # 1. Base Sea-Level Temperature by Latitude and Month
    # Northern India has extreme seasonal amplitude; Southern India has maritime stability
    is_northern = lat > 20.0
    seasonal_phase = (month - 5.5) / 12.0 * 2 * math.pi
    
    if is_northern:
        # Hot summers (May/Jun ~40C), cold winters (Jan ~10C)
        sea_level_temp = 27.0 - 13.0 * math.cos(seasonal_phase)
    else:
        # Southern coastal/peninsular: warm year-round (26C to 34C)
        sea_level_temp = 29.0 - 3.5 * math.cos(seasonal_phase)

    # 2. Altitude Environmental Lapse Rate (~6.5°C per 1,000 meters)
    lapse_rate = 0.0065
    altitude_cooling = alt_m * lapse_rate
    base_temp = sea_level_temp - altitude_cooling

    # 3. Diurnal Cycle (Hour of day: peak at 14:00, minimum at 05:00)
    diurnal_amp = 7.0 if terrain == 4 else (4.5 if terrain == 5 else 6.0) # Desert has high day-night swings
    diurnal_phase = (hour - 14) / 24.0 * 2 * math.pi
    diurnal_factor = diurnal_amp * math.cos(diurnal_phase)
    temp = base_temp + diurnal_factor

    # 4. User Location Temperature Coupling (Regional baseline nudge)
    if user_temp_offset != 0.0:
        temp += user_temp_offset * 0.15

    # 5. Monsoon & Precipitation Physics
    # Southwest Monsoon active in Months 6, 7, 8, 9 (Jun - Sep)
    is_monsoon_month = 6 <= month <= 9
    is_winter_month = month in [12, 1, 2]
    
    precip_prob = 0.08
    humidity = 40.0
    cloud_cover = 25.0

    if is_monsoon_month:
        if terrain in [2, 5]: # Western Ghats & Coastal
            precip_prob = 0.75 + 0.15 * math.sin(lon)
            humidity = 82.0 + 10.0 * math.sin(lat)
            cloud_cover = 85.0
            temp -= 3.0 # Monsoon cooling
        elif terrain == 1: # Foothills
            precip_prob = 0.65
            humidity = 78.0
            cloud_cover = 75.0
        elif terrain == 4: # Desert has low monsoon
            precip_prob = 0.22
            humidity = 50.0
            cloud_cover = 40.0
        else:
            precip_prob = 0.45
            humidity = 70.0
            cloud_cover = 60.0
    elif is_winter_month:
        if alt_m > 2200: # Western Disturbance high altitude snow
            precip_prob = 0.55
            humidity = 75.0
            cloud_cover = 65.0
        elif terrain == 0 and hour in [22, 23, 0, 1, 2, 3, 4, 5, 6, 7]: # Dense fog in northern plains
            humidity = 90.0
            cloud_cover = 50.0
            precip_prob = 0.10

    # 6. Add realistic Gaussian noise if requested
    if noise:
        temp += np.random.normal(0, 1.2)
        precip_prob = np.clip(precip_prob + np.random.normal(0, 0.08), 0.0, 1.0)
        humidity = np.clip(humidity + np.random.normal(0, 5.0), 10.0, 100.0)
        cloud_cover = np.clip(cloud_cover + np.random.normal(0, 8.0), 0.0, 100.0)

    # 7. Discrete Condition Classification
    if alt_m > 2000 and temp <= 1.5 and precip_prob > 0.35:
        condition_code = 5 # Snow
    elif precip_prob > 0.65 and cloud_cover > 70.0:
        condition_code = 3 # Heavy rain / thunderstorm
    elif precip_prob > 0.35:
        condition_code = 2 # Rain
    elif is_winter_month and terrain == 0 and humidity > 85.0 and hour in [22, 23, 0, 1, 2, 3, 4, 5, 6, 7]:
        condition_code = 4 # Dense Fog
    elif cloud_cover > 50.0:
        condition_code = 1 # Cloudy
    else:
        condition_code = 0 # Clear

    # 8. Road Hazard Index (0.0 to 1.0)
    # High hazards: snow, dense fog, torrential monsoon in ghats
    hazard_index = 0.05
    if condition_code == 5: # Snow
        hazard_index = 0.85
    elif condition_code == 4: # Dense fog
        hazard_index = 0.70
    elif condition_code == 3 and terrain in [1, 2]: # Landslide risk in ghats during heavy rain
        hazard_index = 0.80
    elif condition_code in [2, 3]:
        hazard_index = 0.45

    return {
        "features": [lat, lon, alt_m, float(month), float(hour), float(terrain), dist_ratio, user_temp_offset],
        "temperature": round(float(temp), 1),
        "precipitation_prob": round(float(precip_prob), 2),
        "humidity": round(float(humidity), 1),
        "cloud_cover": round(float(cloud_cover), 1),
        "road_hazard_index": round(float(hazard_index), 2),
        "condition_code": condition_code,
        "condition_label": CONDITION_CLASSES[condition_code]
    }

def build_training_dataset(num_samples: int = 10000) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Builds structured NumPy arrays for training the deep learning model.
    Returns:
    - X: Features (N, 8)
    - Y_reg: Continuous targets (N, 4) -> [temperature, precip_prob, humidity, road_hazard]
    - Y_cls: Discrete condition class labels (N,) -> 0 to 5
    """
    X_list = []
    Y_reg_list = []
    Y_cls_list = []

    # Indian geographical reference bounding zones
    zones = [
        # Manali / Atal Tunnel / Himachal (Alpine / Ghats)
        {"lat_range": (31.5, 32.8), "lon_range": (76.8, 77.5), "alt_range": (1200, 3600), "terrains": [2, 3]},
        # Leh / Ladakh (High Altitude Desert)
        {"lat_range": (33.8, 34.5), "lon_range": (77.2, 78.5), "alt_range": (3100, 5400), "terrains": [3]},
        # Delhi / Punjab / Haryana (Northern Plains)
        {"lat_range": (28.2, 30.8), "lon_range": (76.5, 77.8), "alt_range": (180, 280), "terrains": [0]},
        # Rishikesh / Chopta / Uttarakhand (Foothills & Alpine)
        {"lat_range": (29.8, 30.6), "lon_range": (78.2, 79.2), "alt_range": (350, 3200), "terrains": [1, 2, 3]},
        # Mumbai / Goa / Konkan (Coastal)
        {"lat_range": (15.2, 19.1), "lon_range": (72.8, 74.2), "alt_range": (0, 120), "terrains": [5]},
        # Coorg / Wayanad / Western Ghats (Ghats & Highlands)
        {"lat_range": (11.5, 12.8), "lon_range": (75.5, 76.5), "alt_range": (700, 1800), "terrains": [2]},
        # Rajasthan / Thar (Desert)
        {"lat_range": (26.0, 27.5), "lon_range": (70.5, 75.8), "alt_range": (180, 350), "terrains": [4]},
        # Varanasi / Purvanchal (Plains)
        {"lat_range": (25.1, 26.8), "lon_range": (81.5, 83.2), "alt_range": (70, 120), "terrains": [0]},
        # Meghalaya / Shillong (Hills & Canyons)
        {"lat_range": (25.2, 26.2), "lon_range": (91.5, 92.5), "alt_range": (150, 1600), "terrains": [2]}
    ]

    samples_per_zone = num_samples // len(zones)
    for z in zones:
        for _ in range(samples_per_zone):
            lat = np.random.uniform(z["lat_range"][0], z["lat_range"][1])
            lon = np.random.uniform(z["lon_range"][0], z["lon_range"][1])
            alt = np.random.uniform(z["alt_range"][0], z["alt_range"][1])
            month = np.random.randint(1, 13)
            hour = np.random.randint(0, 24)
            terrain = np.random.choice(z["terrains"])
            dist_ratio = np.random.uniform(0.0, 1.0)
            user_offset = np.random.uniform(-5.0, 5.0)

            sample = generate_indian_weather_sample(lat, lon, alt, month, hour, terrain, dist_ratio, user_offset)
            X_list.append(sample["features"])
            Y_reg_list.append([
                sample["temperature"],
                sample["precipitation_prob"],
                sample["humidity"],
                sample["road_hazard_index"]
            ])
            Y_cls_list.append(sample["condition_code"])

    return np.array(X_list, dtype=np.float32), np.array(Y_reg_list, dtype=np.float32), np.array(Y_cls_list, dtype=np.int64)

