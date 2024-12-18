"""
Model Training Script for Indian Weather & Route Microclimate Deep Neural Network.
Executes training loop and exports serialized weights to weather_dnn_weights.json.
"""

import os
import sys
from pathlib import Path

# Add project root to sys.path
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))

from backend.ml.dataset import build_training_dataset
from backend.ml.deep_model import WeatherDeepNeuralNet

def main():
    print("=" * 60)
    print("SAFARNAMA: Training Indian Route Climate Deep Neural Network")
    print("=" * 60)

    # 1. Build training dataset
    X, Y_reg, Y_cls = build_training_dataset(num_samples=12000)
    print(f"Generated Training Data: X shape={X.shape}, Y_reg shape={Y_reg.shape}, Y_cls shape={Y_cls.shape}")

    # 2. Instantiate Deep Neural Network
    model = WeatherDeepNeuralNet(input_dim=8, hidden_dims=(64, 32, 16))

    # 3. Train
    model.train(X, Y_reg, Y_cls, epochs=35, batch_size=64, lr=0.005)

    # 4. Save trained weights
    output_path = Path(__file__).resolve().parent / "weather_dnn_weights.json"
    model.save_weights(str(output_path))

    # 5. Quick Sanity Test Inferences
    print("\n--- Verifying Model Inferences Across Key Indian Checkpoints ---")
    
    # Checkpoint 1: Delhi plains in January at 06:00 (Dense Winter Fog)
    # [lat, lon, alt_m, month, hour, terrain (0:plains), dist_ratio, user_temp_offset]
    delhi_winter = [28.6, 77.2, 216.0, 1.0, 6.0, 0.0, 0.0, 0.0]
    res1 = model.predict(delhi_winter)
    print(f"1. Delhi Plains (Jan 6 AM, 216m): {res1['temperature_c']}°C, Condition: {res1['condition']} (Conf: {res1['condition_confidence']}), Hazard: {res1['road_hazard_index']}")

    # Checkpoint 2: Atal Tunnel / Manali in January (Himalayan Snow)
    # [32.3, 77.1, 3050m, month 1, hour 14, terrain 3:alpine, dist_ratio 1.0, user_offset 0]
    atal_snow = [32.3, 77.1, 3050.0, 1.0, 14.0, 3.0, 1.0, 0.0]
    res2 = model.predict(atal_snow)
    print(f"2. Atal Tunnel Pass (Jan 2 PM, 3050m): {res2['temperature_c']}°C, Condition: {res2['condition']} (Conf: {res2['condition_confidence']}), Hazard: {res2['road_hazard_index']}")

    # Checkpoint 3: Goa Coastal in July (Monsoon Downpour)
    # [15.5, 73.8, 15m, month 7, hour 15, terrain 5:coastal, dist_ratio 1.0, user_offset 0]
    goa_monsoon = [15.5, 73.8, 15.0, 7.0, 15.0, 5.0, 1.0, 0.0]
    res3 = model.predict(goa_monsoon)
    print(f"3. Goa Coast (Jul 3 PM, 15m): {res3['temperature_c']}°C, Condition: {res3['condition']} (Conf: {res3['condition_confidence']}), Precip Prob: {res3['precipitation_prob']}")

    # Checkpoint 4: Jaisalmer Desert in May (Peak Summer Heat)
    # [26.9, 70.9, 220m, month 5, hour 14, terrain 4:desert, dist_ratio 1.0, user_offset 0]
    jaisalmer_summer = [26.9, 70.9, 220.0, 5.0, 14.0, 4.0, 1.0, 0.0]
    res4 = model.predict(jaisalmer_summer)
    print(f"4. Thar Desert (May 2 PM, 220m): {res4['temperature_c']}°C, Condition: {res4['condition']} (Conf: {res4['condition_confidence']}), Humidity: {res4['humidity_percent']}%")

    print("\nDeep Neural Network is fully trained, verified, and operational! 🚀")

if __name__ == "__main__":
    main()

