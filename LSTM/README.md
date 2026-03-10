# Stock Price Prediction using LSTM and GRU

## 📌 Project Overview

This project implements a **sequence intelligence system using Recurrent Neural Networks (RNNs)** to predict stock prices from historical time-series data.

The objective is to model temporal patterns in financial data using **Long Short-Term Memory (LSTM)** and **Gated Recurrent Unit (GRU)** architectures and evaluate their ability to forecast future price movements.

The system learns from past stock prices and predicts future values while analyzing model performance through multiple evaluation metrics.

---

## 🎯 Problem Statement

Financial markets produce sequential data where current prices depend on historical trends.  
The goal of this project is to **predict the next closing price of a stock using historical price sequences**.

This task is formulated as a **time-series regression problem**, where the model uses a sequence of past prices to estimate the next price value.

---

## 📂 Dataset

The dataset contains historical stock price information with the following features:

- Date
- Open price
- High price
- Low price
- Close price
- Volume

For this project, the **closing price** is used as the target variable since it represents the final trading value of the stock for each day.

---

## 🔧 Data Preprocessing

Several preprocessing steps were applied before training the models:

- Sorting the dataset chronologically
- Selecting the **Close price** as the prediction target
- Handling missing values
- Scaling the data using **MinMaxScaler**
- Creating sequential input windows for time-series modeling

---

## 🔄 Sequence Windowing

Time-series models require sequential input data.

A **sliding window approach** is used to create sequences:

```
Previous N days → Predict next day price
```

Example:

```
[Price₁, Price₂, Price₃ ... Price₁₀₀] → Predict Price₁₀₁
```

This allows the model to capture temporal dependencies in the data.

---

## 🧠 Models Implemented

Two recurrent neural network architectures were implemented.

### 1️⃣ Long Short-Term Memory (LSTM)

LSTM networks are designed to capture **long-term dependencies** in sequential data.

Key components:

- LSTM layers
- Dropout layers for regularization
- Dense output layer

---

### 2️⃣ Gated Recurrent Unit (GRU)

GRU is a simplified version of LSTM that often trains faster while maintaining similar predictive performance.

Key components:

- GRU layers
- Dropout regularization
- Dense output layer

---

## ⚙️ Training Strategy

The models were trained using the following configuration:

Optimizer:  
```
Adam
```

Loss Function:  
```
Mean Squared Error (MSE)
```

Training Techniques:

- Early stopping to prevent overfitting
- Validation monitoring during training

---

## 📊 Model Evaluation Metrics

Model performance was evaluated using regression metrics:

**Mean Absolute Error (MAE)**  
Measures the average absolute difference between predicted and actual values.

**Mean Squared Error (MSE)**  
Penalizes larger prediction errors more heavily.

**R-squared (R²)**  
Measures how well the model explains the variance in the data.

**Directional Accuracy**  
Evaluates whether the model correctly predicts the **direction of price movement** (up or down).

---

## 🔬 Architecture Comparison: LSTM vs GRU

Both models were evaluated on the same dataset to compare their performance.

| Model | MAE | R² Score |
|------|------|------|
| LSTM | *computed in notebook* | *computed in notebook* |
| GRU | *computed in notebook* | *computed in notebook* |

The comparison helps determine which architecture better captures temporal patterns in financial data.

---

## 🧪 Ablation Study: Window Size Experiment

To analyze how historical context affects prediction accuracy, two sequence lengths were tested.

| Window Size | MAE | R² |
|-------------|------|------|
| 100 Days | *computed in notebook* | *computed in notebook* |
| 30 Days | *computed in notebook* | *computed in notebook* |

Longer windows allow the model to capture deeper temporal patterns but increase training complexity.

---

## 📈 Prediction Visualization

The model predictions are compared against actual stock prices.

Example visualization:

```
Actual Price vs Predicted Price
```

This helps evaluate how closely the model follows real market trends.

---

## ⚠️ Error Analysis

Prediction errors were analyzed using residual distributions.

Key observations:

- The model performs well during stable price periods.
- Larger prediction errors occur during sudden price spikes or drops.
- Financial markets contain noise that is difficult for purely historical models to capture.

---

## 📂 Repository Structure

```
ACM-TASKS
│
├── LSTM
│   ├── LSTM_FINAL.ipynb
│   ├── README.md
│   ├── requirements.txt
│   │
│   └── Images
│        ├── loss_curve.png
│        ├── prediction_plot.png
│        └── error_distribution.png
```

---

## 🛠 Requirements

Install dependencies using:

```
pip install -r requirements.txt
```

Main libraries used:

- TensorFlow / Keras
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

---

## 🚀 Future Improvements

Possible improvements include:

- Incorporating additional financial indicators
- Using attention-based sequence models
- Multi-step time-series forecasting
- Integrating external economic signals

---


