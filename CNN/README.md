# Steel Surface Defect Classification – Convolutional Neural Network

## 📌 Project Overview

This project implements a Deep Learning pipeline using **Convolutional Neural Networks (CNNs)** to classify steel surface defects from images.

The objective is to automatically detect and categorize different types of steel surface defects for **industrial quality inspection**.

Two CNN architectures were implemented and compared:

- Baseline CNN
- Regularized CNN

The model classifies images into **6 defect categories**.

---

## 🎯 Problem Statement

Given a steel surface image, predict the **type of defect present** in the image.

This is a **multi-class image classification problem**.

---

## 📂 Dataset

The project uses the **NEU Surface Defect Dataset**.

### Defect Classes

- Crazing  
- Inclusion  
- Patches  
- Pitted Surface  
- Rolled-in Scale  
- Scratches  

Image size used for training:

```
128 × 128
```

---

## 🧠 CNN Model Architecture

The CNN extracts spatial features using convolution layers followed by pooling layers and dense classification layers.

### Architecture Diagram

![Model Architecture](CNN/Images/model_architecture.png)

---

## ⚙️ Training Configuration

Optimizer: Adam  
Learning Rate: 0.0003  
Loss Function: Sparse Categorical Crossentropy  
Evaluation Metric: Accuracy  

---

## 📊 Model Evaluation

### Confusion Matrix – Baseline CNN

![Baseline CNN Confusion Matrix](CNN/Images/Confusion Matrix of baseline CNN.png)

### Confusion Matrix – Custom CNN

![Custom CNN Confusion Matrix](CNN/Images/Confusion Matrix of Custom CNN.png)

---

## 📈 Training Performance

### Accuracy Curve

![Accuracy Plot](CNN/Images/Accuracy Plot.png)

### Loss Curve

![Loss Graph](CNN/Images/Loss Graphs.png)

---

## 🔍 Model Explainability

Grad-CAM was used to visualize which regions of the image influenced the model’s predictions.

### Grad-CAM Visualization

![GradCAM](CNN/Images/Grad-CAM visualisation.png)

---

## 📂 Repository Structure

```
ACM-TASKS
│
├── CNN
│   ├── notebook.ipynb
│   │
│   └── Images
│        ├── Accuracy Plot.png
│        ├── Confusion Matrix of Custom CNN.png
│        ├── Confusion Matrix of baseline CNN.png
│        ├── Grad-CAM visualisation.png
│        ├── Loss Graphs.png
│        └── model_architecture.png
```

---

## 🚀 Future Improvements

- Apply transfer learning models such as ResNet or EfficientNet
- Increase dataset size
- Hyperparameter tuning
- Deploy the model as an inspection tool

---

## 👤 Author

Pavan Sai  
Artificial Intelligence & Data Science Student
