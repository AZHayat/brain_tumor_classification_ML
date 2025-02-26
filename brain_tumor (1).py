# -*- coding: utf-8 -*-
"""Brain Tumor.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1To7BSV3a0bNo2ed0XBR0oV0YzpXSjaTy

#ABOUT

## About the Dataset 🧠

This dataset, originally provided by **Rajarshi Mandal**, is sourced from **[Kaggle](https://www.kaggle.com/datasets/rm1000/brain-tumor-mri-scans)**. It consists of **7,023 MRI brain scan images** categorized into **four classes** based on the presence and type of brain tumor. These MRI scans are used to train and test AI models for **medical image classification**.

### 🔹 Dataset Structure  
The dataset is divided into **two main parts**:  

1. **Training Dataset** – [Brain Tumor MRI Scans - Kaggle](https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri)  
   - This set contains labeled MRI images used to train AI models in recognizing and classifying brain tumors.  
   - It includes **multiple images per class**, ensuring the model learns different variations and patterns.  

2. **Testing Dataset** – [Brain Tumor Classification MRI - Kaggle](https://www.kaggle.com/datasets/rm1000/brain-tumor-mri-scans)  
   - This dataset is used to evaluate the model's performance after training.  
   - It provides unseen MRI scans to check the model’s ability to generalize its predictions.  

---

### 🏷️ Tumor Categories

The MRI images in this dataset are categorized into **four classes**:

1. **Glioma Tumor**  
   - Originates from **glial cells** in the brain or spinal cord.  
   - One of the most **common and aggressive** types of brain tumors.  
   - Can grow quickly and impact neurological functions.  

2. **Meningioma Tumor**  
   - Develops in the **meninges**, the protective membranes surrounding the brain and spinal cord.  
   - Mostly **benign**, but their size and location can cause **pressure on the brain**.  

3. **Pituitary Tumor**  
   - Forms in the **pituitary gland**, which regulates **hormones** and essential bodily functions.  
   - Generally **non-cancerous**, but can **disrupt hormonal balance**, causing various health issues.  

4. **Healthy (No Tumor)**  
   - Contains **MRI scans of normal brains** with no visible tumors.  
   - Serves as a **control group** to help AI models differentiate between normal and abnormal brain structures.  

---

### 🔍 Purpose of the Dataset  
This dataset is widely used for:  
✔️ **Training AI models** for medical image analysis.  
✔️ **Benchmarking deep learning algorithms**, especially **Convolutional Neural Networks (CNNs)**.  
✔️ Assisting in **early tumor detection and diagnosis**.  
✔️ Developing **computer-aided diagnosis (CAD) systems** to support radiologists and neurologists.  

By leveraging this dataset, we aim to enhance **AI-driven medical imaging** and contribute to faster, more accurate diagnoses in healthcare. 🚀
"""

#install Library
!pip install tensorflow

#Import library
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Specify the file location in Google Drive
from google.colab import drive
drive.mount('/content/drive')

file_location = '/content/drive/MyDrive/PORTOFOLIO/BRAIN TUMOR 2'
print(os.listdir(file_location))

# Define the file paths for each tumor type and healthy scans
src_path = os.path.join(file_location, 'src')  # Main source folder
glioma_tumor_path = os.path.join(src_path, 'glioma')  # Path for Glioma Tumor scans
meningioma_tumor_path = os.path.join(src_path, 'meningioma')  # Path for Meningioma Tumor scans
pituitary_tumor_path = os.path.join(src_path, 'pituitary')  # Path for Pituitary Tumor scans
healthy_path = os.path.join(src_path, 'healthy')  # Path for scans with no tumor

# Print the number of files in each category
print(f"Number of Glioma Tumor scans: {len(os.listdir(glioma_tumor_path))}")
print(f"Number of Meningioma Tumor scans: {len(os.listdir(meningioma_tumor_path))}")
print(f"Number of Pituitary Tumor scans: {len(os.listdir(pituitary_tumor_path))}")
print(f"Number of Healthy scans: {len(os.listdir(healthy_path))}")

# Convert the data into a pandas DataFrame
tumor_data = {
    "Tumor Type": [
        "Glioma Tumor",
        "Meningioma Tumor",
        "Pituitary Tumor",
        "Healthy"
    ],
    "Number of Scans": [
        len(os.listdir(glioma_tumor_path)),
        len(os.listdir(meningioma_tumor_path)),
        len(os.listdir(pituitary_tumor_path)),
        len(os.listdir(healthy_path)),
    ]
}


tumor_table = pd.DataFrame(tumor_data)
tumor_table

#plot the tumor table
tumor_table.plot(x="Tumor Type", y="Number of Scans", kind="bar", color="blue")
plt.title("Number of Scans per Tumor Type")
plt.xlabel("Tumor Type")
plt.ylabel("Number of Scans")
plt.xticks(rotation=45)
plt.show()

from typing_extensions import Literal
from PIL import Image

# Define the paths
sample_image_healthy = os.path.join(healthy_path, os.listdir(healthy_path)[0])
sample_image_glioma = os.path.join(glioma_tumor_path, os.listdir(glioma_tumor_path)[0])
sample_image_meningioma = os.path.join(meningioma_tumor_path, os.listdir(meningioma_tumor_path)[0])
sample_image_pituitary = os.path.join(pituitary_tumor_path, os.listdir(pituitary_tumor_path)[0])

# Open the images using PIL
image_healthy = Image.open(sample_image_healthy)
image_glioma = Image.open(sample_image_glioma)
image_meningioma = Image.open(sample_image_meningioma)
image_pituitary = Image.open(sample_image_pituitary)

fig, axes = plt.subplots(2, 3, figsize=(12, 6))
axes[0, 0].axis('off')
axes[0, 2].axis('off')

axes[0, 1].imshow(image_healthy, cmap='gray')
axes[1, 0].imshow(image_glioma, cmap='gray')
axes[1, 1].imshow(image_meningioma, cmap='gray')
axes[1, 2].imshow(image_pituitary, cmap='gray')

axes[0, 1].set_title("Healthy Brain")
axes[1, 0].set_title("Glioma Tumor")
axes[1, 1].set_title("Meningioma Tumor")
axes[1, 2].set_title("Pituitary Tumor")


plt.tight_layout()
plt.suptitle("Sample Images from Each Tumor Type", fontsize=16, y=1.02, fontweight='bold')
plt.show()

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Preprocessing data
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=30,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

test_datagen = ImageDataGenerator(rescale=1./255)

# Set batch size and image size
batch_size = 32
img_size = (150, 150)

# Set up generators
train_generator = train_datagen.flow_from_directory(
    src_path,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical'  # Multi-class classification
)

validation_generator = test_datagen.flow_from_directory(
    src_path,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical'
)

# Display the classes and the number of images in each category
print(train_generator.class_indices)
print(f'Training data: {train_generator.samples} images')
print(f'Validation data: {validation_generator.samples} images')

# Build the CNN model
model = tf.keras.Sequential([
    # First Convolutional Layer
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

    # Second Convolutional Layer
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

    # Third Convolutional Layer
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

    # Flatten the 2D outputs into 1D to feed into the fully connected layer
    tf.keras.layers.Flatten(),

    # Fully connected layer
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dropout(0.5),

    # Output layer with 4 neurons for 4 classes: Glioma, Meningioma, Pituitary, Healthy
    tf.keras.layers.Dense(4, activation='softmax')
])

# Compile the model with Adam optimizer and categorical cross-entropy loss
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Display the model summary
model.summary()

# Early stopping to prevent overfitting by stopping training when the validation loss doesn't improve
early_stopping = tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5)

# Train the model
history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // batch_size,
    epochs=20,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // batch_size,
    callbacks=[early_stopping]
)

# Evaluate the model on validation data
val_loss, val_accuracy = model.evaluate(validation_generator)
print(f"Validation Loss: {val_loss}, Validation Accuracy: {val_accuracy}")

# Save the trained model
model.save('brain_tumor_model.keras')

from tensorflow.keras.models import load_model

# Memuat model yang sudah disimpan
model = load_model('brain_tumor_model1.H5')

# To make predictions for new images
def predict_image(img_path):
    img = image.load_img(img_path, target_size=img_size)
    img_array = image.img_to_array(img) / 255.0  # Normalize the image
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction)  # Get the class with the highest probability
    return class_idx, prediction

# Example of prediction
img_path = 'path_to_new_image.jpg'  # Replace with the path to the image you want to predict
class_idx, prediction = predict_image(img_path)
print(f"Predicted class index: {class_idx}, Prediction: {prediction}")

from tensorflow.keras.preprocessing import image

img_size = (150, 150)

# Function to predict an image
def predict_image(img_path):
    img = image.load_img(img_path, target_size=img_size)
    img_array = image.img_to_array(img) / 255.0  # Normalize the image
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction)
    return class_idx, prediction

# Function to predict all images in a folder and return as a DataFrame
def predict_images_in_folder(folder_path):
    predictions = []
    for img_name in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img_name)
        if os.path.isfile(img_path) and img_path.lower().endswith(('.png', '.jpg', '.jpeg')):  # Ensure it's an image file
            class_idx, prediction = predict_image(img_path)
            predictions.append({
                'Image Name': img_name,
                'Predicted Class Index': class_idx,
                'Prediction': prediction.flatten()
            })
    df_predictions = pd.DataFrame(predictions)
    return df_predictions

# Test with another image
test_path_folder = os.path.join(file_location, 'TEST')
folder_path = os.path.join(test_path_folder, 'TEST2')
df_predictions = predict_images_in_folder(folder_path)

# Print the DataFrame as a table
df_predictions

from tensorflow.keras.preprocessing import image

img_size = (150, 150)

# Function to predict an image
def predict_image(img_path):
    img = image.load_img(img_path, target_size=img_size)
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction)

    healthy_percentage = round(prediction[0][1] * 100, 2)
    glioma_percentage = round(prediction[0][0] * 100, 2)
    meningioma_percentage = round(prediction[0][2] * 100, 2)
    pituitary_percentage = round(prediction[0][3] * 100, 2)

    tumor_class = ['GLIOMA', 'HEALTHY', 'MENINGIOMA', 'PITUITARY'][class_idx]
    return tumor_class, healthy_percentage, glioma_percentage, meningioma_percentage, pituitary_percentage, prediction.flatten()

# Function to predict all images in a folder and return as a DataFrame
def predict_images_in_folder(folder_path):
    predictions = []
    for img_name in os.listdir(folder_path):
        img_path = os.path.join(folder_path, img_name)
        if os.path.isfile(img_path) and img_path.lower().endswith(('.png', '.jpg', '.jpeg')):
            tumor_class, healthy_percentage, glioma_percentage, meningioma_percentage, pituitary_percentage, prediction = predict_image(img_path)
            predictions.append({
                'img_name': img_name,
                'predicted_tumor': tumor_class,
                'healthy%': healthy_percentage,
                'glioma%': glioma_percentage,
                'meningioma%': meningioma_percentage,
                'pituitary%': pituitary_percentage
            })
    df_predictions = pd.DataFrame(predictions)
    return df_predictions

# Test with another image
test_path_folder = os.path.join(file_location, 'TEST')
folder_path = os.path.join(test_path_folder, 'TEST2')
df_predictions = predict_images_in_folder(folder_path)

# Print the DataFrame as a table
df_predictions