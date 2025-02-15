# Brain Tumor Classification (MRI Scans) 🧠

## Project Overview

This project is a deep learning model for classifying brain tumors using MRI scans. It utilizes Convolutional Neural Networks (CNN) to distinguish between different tumor types and healthy brain scans.

## Dataset 📊

### Dataset Overview

The dataset used in this project is provided by Rajarshi Mandal on Kaggle. It contains 7,023 MRI brain scans categorized into four classes:

### Tumor Classes

Glioma Tumor: Tumors originating in the glial cells of the brain or spine. These are among the most common and aggressive types of brain tumors.

Meningioma Tumor: Develops in the meninges, the protective membranes covering the brain and spinal cord. Most are non-cancerous but can cause complications due to their size and location.

Pituitary Tumor: Forms in the pituitary gland, which regulates vital body functions. Although often benign, they can disrupt hormonal balance and cause significant health issues.

Healthy: MRI scans without evidence of tumors, serving as control samples for comparison and training AI models.

### Dataset Sources 📂

[Training Dataset: Brain Tumor MRI Scans - Kaggle](https://www.kaggle.com/datasets/rm1000/brain-tumor-mri-scans)

[Testing Dataset: Brain Tumor Classification MRI - Kaggle](https://www.kaggle.com/datasets/sartajbhuvaji/brain-tumor-classification-mri)


## Model Architecture 🏗️

### Model Overview

This project implements a Convolutional Neural Network (CNN) using TensorFlow and Keras. The model consists of:

### Layers

Convolutional Layers: Extract spatial features from MRI scans.

Pooling Layers: Reduce dimensionality while retaining important features.

Fully Connected Layers: Perform classification based on extracted features.

Softmax Activation: Outputs probabilities for each tumor class.

## Results 📈

### Model Performance

After training the CNN model on the dataset, the following results were observed:

Training Accuracy: Achieved high accuracy on the training set, indicating the model effectively learns patterns in MRI scans.

Validation Accuracy: The model generalizes well to unseen data, with consistent accuracy across validation sets.

Confusion Matrix Analysis: Most misclassifications occur between similar tumor types (e.g., Glioma vs. Meningioma), suggesting further tuning may be required.

### Future Improvements

Implementing data augmentation techniques to enhance model robustness.

Fine-tuning hyperparameters to further improve classification performance.

Exploring different CNN architectures for better feature extraction.

## Disclaimer ⚠️

This is a dummy project for learning purposes and is not intended for real medical diagnosis.

## Contact 📬

If you have any questions or want to collaborate, feel free to reach out!
**LinkedIn**: https://www.linkedin.com/in/ahmad-zaenal-hayat/
**Email**: a.zaenalhayat@gmail.com

Feel free to explore the scripts and insights, and let's harness the power of data together! 🌟

