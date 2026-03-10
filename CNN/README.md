# Steel Surface Defect Classification – Convolutional Neural Network

## 📌 Project Overview

This project implements a complete Deep Learning pipeline using Convolutional Neural Networks (CNNs) to classify steel surface defects from images.

The objective is to automatically detect and categorize different types of surface defects in steel sheets, which is an important task in industrial quality control and automated inspection systems.

Two CNN architectures were implemented and compared:

- Baseline CNN Model  
- Regularized CNN Model  

The final system classifies images into **six defect categories**.

---

## 🎯 Problem Statement

Given an image of a steel surface, predict the **type of defect present** in the image.

The model learns spatial patterns and textures from images to identify defect characteristics.

This is a **multi-class image classification problem**.

---

## 📂 Dataset Description

The project uses the **NEU Surface Defect Dataset**, a widely used dataset for industrial defect detection.

### Defect Classes

- Crazing  
- Inclusion  
- Patches  
- Pitted Surface  
- Rolled-in Scale  
- Scratches  

### Image Properties

- Image size: **128 × 128**
- Number of classes: **6**
- Images resized and normalized before training

---

## 🔧 Data Preprocessing

The following preprocessing steps were applied before training the CNN model:

- Image resizing to **128 × 128**
- Pixel value normalization using **Rescaling (1/255)**
- Efficient dataset loading using TensorFlow
- Train–Validation split for model evaluation

---

## 🔄 Data Augmentation

To improve generalization and reduce overfitting, data augmentation techniques were applied:

- Random horizontal flipping  
- Random rotation  

These transformations help the model learn invariant visual patterns.

---

## 🧠 Model Architecture

The CNN architecture extracts hierarchical visual features using convolutional layers followed by pooling operations.

Key architectural components include:

- Convolutional Layers  
- Batch Normalization  
- ReLU Activation  
- MaxPooling Layers  
- Global Average Pooling  
- Dropout Regularization  
- Dense Classification Layer  

### Model Architecture Diagram

![Model Architecture](Images/model_architecture.png)

---

## ⚙️ Training Configuration

Optimizer: **Adam**

Learning Rate: **0.0003**

Loss Function: **Sparse Categorical Crossentropy**

Evaluation Metric: **Accuracy**

---

## 🤖 CNN Models Implemented

### Baseline CNN Model

A standard convolutional architecture used as a reference model to establish baseline performance.

### Regularized CNN Model

This improved architecture includes:

- Data augmentation  
- Batch normalization  
- Dropout regularization  

These techniques help improve generalization and reduce overfitting.

---

## 📊 Model Evaluation

Model performance was evaluated using multiple metrics:

- Accuracy  
- Confusion Matrix  
- Training and Validation Accuracy Curves  
- Training and Validation Loss Curves  

### Confusion Matrix

![Confusion Matrix](Images/confusion_matrix.png)

---

## 📈 Training Performance

### Accuracy Curve

![Accuracy Curve](Images/accuracy_curve.png)

### Loss Curve

![Loss Curve](Images/loss_curve.png)

### Validation Accuracy Comparison

![Validation Accuracy](Images/validation_accuracy_comparison.png)

---

## 🔍 Model Explainability (Grad-CAM)

Grad-CAM (Gradient-weighted Class Activation Mapping) was used to visualize which regions of the image influenced the model’s prediction.

This helps interpret CNN decisions by highlighting important image regions.

### Grad-CAM Visualization

![GradCAM](Images/gradcam_visualization.png)

---

## ⚠️ Error Analysis

Misclassified images were analyzed to understand model weaknesses and confusion between visually similar defect types.

This analysis helps identify:

- visually similar defects  
- difficult classification cases  
- dataset ambiguities  

---

## 📂 Repository Structure

```
CNN-Steel-Defect-Classification
│
├── notebook.ipynb
├── README.md
│
└── Images
     ├── model_architecture.png
     ├── confusion_matrix.png
     ├── accuracy_curve.png
     ├── loss_curve.png
     ├── validation_accuracy_comparison.png
     └── gradcam_visualization.png
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
- Matplotlib  
- Seaborn  
- OpenCV  
- Scikit-learn  

---

## 🚀 Future Improvements

Potential improvements for this project include:

- Applying transfer learning models such as ResNet or EfficientNet  
- Increasing dataset size using advanced augmentation  
- Hyperparameter optimization  
- Deploying the model as a web-based inspection tool  

---

## 👤 Author

**Pavan Sai**  
Artificial Intelligence & Data Science Student
