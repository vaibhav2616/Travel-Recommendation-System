"""
Deep Neural Network (MLP) Architecture for Indian Weather & Route Microclimate Prediction.
Implemented with native NumPy matrix operations for zero external dependencies,
complete offline determinism, and sub-millisecond inference latency.
"""

import json
import math
import numpy as np
from typing import Dict, Any, Tuple, Optional

class WeatherDeepNeuralNet:
    """
    Multi-Task Deep Neural Network:
    - Shared Backbone: Input (8) -> Dense(64, ReLU) -> Dense(32, ReLU) -> Dense(16, ReLU)
    - Head 1 (Regression): Dense(16 -> 4) for [Temp (°C), Precip Prob, Humidity (%), Road Hazard]
    - Head 2 (Classification): Dense(16 -> 6, Softmax) for Weather Condition classes
    """
    def __init__(self, input_dim: int = 8, hidden_dims: Tuple[int, int, int] = (64, 32, 16)):
        self.input_dim = input_dim
        self.h1, self.h2, self.h3 = hidden_dims
        self.reg_dim = 4
        self.cls_dim = 6

        # Normalization constants (mean and standard deviation)
        self.x_mean = np.zeros(input_dim, dtype=np.float32)
        self.x_std = np.ones(input_dim, dtype=np.float32)
        self.y_reg_mean = np.zeros(self.reg_dim, dtype=np.float32)
        self.y_reg_std = np.ones(self.reg_dim, dtype=np.float32)

        # Initialize Weights & Biases using He/Xavier Normal Initialization
        np.random.seed(42)
        self.W1 = np.random.randn(input_dim, self.h1).astype(np.float32) * np.sqrt(2.0 / input_dim)
        self.b1 = np.zeros(self.h1, dtype=np.float32)

        self.W2 = np.random.randn(self.h1, self.h2).astype(np.float32) * np.sqrt(2.0 / self.h1)
        self.b2 = np.zeros(self.h2, dtype=np.float32)

        self.W3 = np.random.randn(self.h2, self.h3).astype(np.float32) * np.sqrt(2.0 / self.h2)
        self.b3 = np.zeros(self.h3, dtype=np.float32)

        # Head 1: Regression Weights
        self.W_reg = np.random.randn(self.h3, self.reg_dim).astype(np.float32) * np.sqrt(1.0 / self.h3)
        self.b_reg = np.zeros(self.reg_dim, dtype=np.float32)

        # Head 2: Classification Weights
        self.W_cls = np.random.randn(self.h3, self.cls_dim).astype(np.float32) * np.sqrt(1.0 / self.h3)
        self.b_cls = np.zeros(self.cls_dim, dtype=np.float32)

        self.training_history: Dict[str, Any] = {}

    @staticmethod
    def relu(x: np.ndarray) -> np.ndarray:
        return np.maximum(0.0, x)

    @staticmethod
    def softmax(x: np.ndarray) -> np.ndarray:
        exps = np.exp(x - np.max(x, axis=-1, keepdims=True))
        return exps / np.sum(exps, axis=-1, keepdims=True)

    def normalize_x(self, X: np.ndarray) -> np.ndarray:
        return (X - self.x_mean) / (self.x_std + 1e-7)

    def forward(self, X_norm: np.ndarray) -> Tuple[np.ndarray, np.ndarray, Dict[str, np.ndarray]]:
        """
        Forward pass returning regression outputs, classification probabilities, and activations.
        """
        z1 = np.dot(X_norm, self.W1) + self.b1
        a1 = self.relu(z1)

        z2 = np.dot(a1, self.W2) + self.b2
        a2 = self.relu(z2)

        z3 = np.dot(a2, self.W3) + self.b3
        a3 = self.relu(z3)

        # Head 1: Linear regression
        out_reg_norm = np.dot(a3, self.W_reg) + self.b_reg

        # Head 2: Softmax classification
        logits_cls = np.dot(a3, self.W_cls) + self.b_cls
        out_cls_prob = self.softmax(logits_cls)

        cache = {
            "X_norm": X_norm,
            "z1": z1, "a1": a1,
            "z2": z2, "a2": a2,
            "z3": z3, "a3": a3,
            "out_reg_norm": out_reg_norm,
            "out_cls_prob": out_cls_prob
        }
        return out_reg_norm, out_cls_prob, cache

    def train(
        self,
        X: np.ndarray,
        Y_reg: np.ndarray,
        Y_cls: np.ndarray,
        epochs: int = 40,
        batch_size: int = 64,
        lr: float = 0.003
    ):
        """
        Trains the network using mini-batch gradient descent with multi-task loss.
        """
        N = X.shape[0]

        # 1. Compute and store normalization parameters
        self.x_mean = np.mean(X, axis=0)
        self.x_std = np.std(X, axis=0)
        self.x_std[self.x_std == 0] = 1.0

        self.y_reg_mean = np.mean(Y_reg, axis=0)
        self.y_reg_std = np.std(Y_reg, axis=0)
        self.y_reg_std[self.y_reg_std == 0] = 1.0

        X_norm = self.normalize_x(X)
        Y_reg_norm = (Y_reg - self.y_reg_mean) / (self.y_reg_std + 1e-7)

        # One-hot encode Y_cls
        Y_cls_onehot = np.zeros((N, self.cls_dim), dtype=np.float32)
        Y_cls_onehot[np.arange(N), Y_cls] = 1.0

        loss_history = []
        acc_history = []

        print(f"Training Weather Deep Neural Network on {N} Indian climate samples...")

        for epoch in range(epochs):
            # Shuffle dataset
            indices = np.random.permutation(N)
            X_shuffled = X_norm[indices]
            Y_reg_shuffled = Y_reg_norm[indices]
            Y_cls_shuffled = Y_cls_onehot[indices]
            Y_cls_raw_shuffled = Y_cls[indices]

            epoch_loss = 0.0
            correct = 0

            # Learning rate decay
            current_lr = lr * (0.95 ** (epoch // 5))

            for i in range(0, N, batch_size):
                xb = X_shuffled[i:i + batch_size]
                y_reg_b = Y_reg_shuffled[i:i + batch_size]
                y_cls_b = Y_cls_shuffled[i:i + batch_size]
                y_cls_raw = Y_cls_raw_shuffled[i:i + batch_size]
                B = xb.shape[0]

                # Forward
                pred_reg_b, pred_cls_b, cache = self.forward(xb)

                # Losses
                # 1. MSE Loss for Regression
                loss_reg = np.mean((pred_reg_b - y_reg_b) ** 2)
                # 2. Cross-Entropy Loss for Classification
                loss_cls = -np.mean(np.sum(y_cls_b * np.log(pred_cls_b + 1e-9), axis=1))
                total_loss = loss_reg + 0.5 * loss_cls
                epoch_loss += total_loss * B

                # Accuracy
                preds = np.argmax(pred_cls_b, axis=1)
                correct += np.sum(preds == y_cls_raw)

                # Backpropagation
                # dL / d(pred_reg)
                d_reg = (2.0 / (B * self.reg_dim)) * (pred_reg_b - y_reg_b)
                # dL / d(logits_cls) = (pred - target) / B
                d_cls = 0.5 * (pred_cls_b - y_cls_b) / B

                # Head gradients
                dW_reg = np.dot(cache["a3"].T, d_reg)
                db_reg = np.sum(d_reg, axis=0)

                dW_cls = np.dot(cache["a3"].T, d_cls)
                db_cls = np.sum(d_cls, axis=0)

                # Backbone gradient at a3
                da3 = np.dot(d_reg, self.W_reg.T) + np.dot(d_cls, self.W_cls.T)
                dz3 = da3 * (cache["z3"] > 0)
                dW3 = np.dot(cache["a2"].T, dz3)
                db3 = np.sum(dz3, axis=0)

                da2 = np.dot(dz3, self.W3.T)
                dz2 = da2 * (cache["z2"] > 0)
                dW2 = np.dot(cache["a1"].T, dz2)
                db2 = np.sum(dz2, axis=0)

                da1 = np.dot(dz2, self.W2.T)
                dz1 = da1 * (cache["z1"] > 0)
                dW1 = np.dot(cache["X_norm"].T, dz1)
                db1 = np.sum(dz1, axis=0)

                # Parameter Update (SGD with momentum/decay)
                self.W_reg -= current_lr * dW_reg
                self.b_reg -= current_lr * db_reg
                self.W_cls -= current_lr * dW_cls
                self.b_cls -= current_lr * db_cls
                self.W3 -= current_lr * dW3
                self.b3 -= current_lr * db3
                self.W2 -= current_lr * dW2
                self.b2 -= current_lr * db2
                self.W1 -= current_lr * dW1
                self.b1 -= current_lr * db1

            epoch_loss /= N
            epoch_acc = (correct / N) * 100.0
            loss_history.append(float(epoch_loss))
            acc_history.append(float(epoch_acc))

            if (epoch + 1) % 10 == 0 or epoch == 0:
                print(f"  Epoch [{epoch+1}/{epochs}] - Loss: {epoch_loss:.4f} | Condition Acc: {epoch_acc:.1f}%")

        self.training_history = {
            "final_loss": round(float(loss_history[-1]), 4),
            "final_accuracy": round(float(acc_history[-1]), 2),
            "epochs": epochs,
            "samples_trained": N
        }
        print(f"Model Training Complete! Final Accuracy: {self.training_history['final_accuracy']}%")

    def predict(self, X: Any) -> Dict[str, Any]:
        """
        Runs inference on given input features array (N, 8) or (8,) or list.
        """
        if isinstance(X, (list, tuple)):
            X = np.array(X, dtype=np.float32)
        elif not isinstance(X, np.ndarray):
            X = np.array(X, dtype=np.float32)

        if X.ndim == 1:
            X = np.expand_dims(X, axis=0)

        X_norm = self.normalize_x(X)
        pred_reg_norm, pred_cls_prob, _ = self.forward(X_norm)

        # Denormalize regression output
        pred_reg = (pred_reg_norm * (self.y_reg_std + 1e-7)) + self.y_reg_mean

        condition_classes = ["clear", "cloudy", "rain", "heavy_rain", "fog", "snow"]

        results = []
        for i in range(X.shape[0]):
            temp_c = round(float(pred_reg[i, 0]), 1)
            precip_p = round(float(np.clip(pred_reg[i, 1], 0.0, 1.0)), 2)
            humidity = round(float(np.clip(pred_reg[i, 2], 5.0, 100.0)), 1)
            hazard = round(float(np.clip(pred_reg[i, 3], 0.0, 1.0)), 2)

            class_idx = int(np.argmax(pred_cls_prob[i]))
            class_label = condition_classes[class_idx]
            confidence = round(float(pred_cls_prob[i, class_idx]), 3)

            results.append({
                "temperature_c": temp_c,
                "precipitation_prob": precip_p,
                "humidity_percent": humidity,
                "road_hazard_index": hazard,
                "condition": class_label,
                "condition_confidence": confidence,
                "all_class_probabilities": {
                    condition_classes[j]: round(float(pred_cls_prob[i, j]), 3) for j in range(6)
                }
            })

        return results[0] if len(results) == 1 else results

    def save_weights(self, filepath: str):
        """
        Serializes all trained weights, biases, and normalization constants into JSON.
        """
        data = {
            "x_mean": self.x_mean.tolist(),
            "x_std": self.x_std.tolist(),
            "y_reg_mean": self.y_reg_mean.tolist(),
            "y_reg_std": self.y_reg_std.tolist(),
            "W1": self.W1.tolist(),
            "b1": self.b1.tolist(),
            "W2": self.W2.tolist(),
            "b2": self.b2.tolist(),
            "W3": self.W3.tolist(),
            "b3": self.b3.tolist(),
            "W_reg": self.W_reg.tolist(),
            "b_reg": self.b_reg.tolist(),
            "W_cls": self.W_cls.tolist(),
            "b_cls": self.b_cls.tolist(),
            "training_history": self.training_history
        }
        with open(filepath, "w") as f:
            json.dump(data, f, indent=2)
        print(f"Saved Weather Deep Neural Network weights to: {filepath}")

    def load_weights(self, filepath: str):
        """
        Loads weights from JSON.
        """
        with open(filepath, "r") as f:
            data = json.load(f)

        self.x_mean = np.array(data["x_mean"], dtype=np.float32)
        self.x_std = np.array(data["x_std"], dtype=np.float32)
        self.y_reg_mean = np.array(data["y_reg_mean"], dtype=np.float32)
        self.y_reg_std = np.array(data["y_reg_std"], dtype=np.float32)

        self.W1 = np.array(data["W1"], dtype=np.float32)
        self.b1 = np.array(data["b1"], dtype=np.float32)
        self.W2 = np.array(data["W2"], dtype=np.float32)
        self.b2 = np.array(data["b2"], dtype=np.float32)
        self.W3 = np.array(data["W3"], dtype=np.float32)
        self.b3 = np.array(data["b3"], dtype=np.float32)
        self.W_reg = np.array(data["W_reg"], dtype=np.float32)
        self.b_reg = np.array(data["b_reg"], dtype=np.float32)
        self.W_cls = np.array(data["W_cls"], dtype=np.float32)
        self.b_cls = np.array(data["b_cls"], dtype=np.float32)
        self.training_history = data.get("training_history", {})
        print(f"Loaded Weather Deep Neural Network weights from: {filepath}")
