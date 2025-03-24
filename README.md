# Aerial-Based Target Identification Under Occlusion

## Overview

This project focuses on enhancing real-time aerial target identification under occlusion using advanced deep learning techniques and multi-stage computer vision processing. The system aims to improve robustness and accuracy in detecting and classifying diverse targets, including vehicles and pedestrians, across multiple aerial datasets.

## Problem Statement

Accurate target identification in aerial imagery is challenging due to factors such as occlusions, varying viewpoints and complex backgrounds. Traditional object detection models struggle with these conditions in real-world scenarios. This project seeks to address these challenges by leveraging occlusion-aware detection models.

## Datasets

The project utilizes three key aerial datasets:

1. **VisDrone (38GB)**
   - Large-scale dataset for UAV-based object detection, tracking, and segmentation.
   - Captured in urban and suburban environments.
   - Targets include pedestrians, vehicles (cars, buses, trucks, vans), bicycles, and tricycles.
   - 10,209 images with annotated bounding boxes and object categories.

2. **NOMAD (277GB)**
   - Designed for human detection under occluded aerial views.
   - 42,825 high-resolution frames capturing actors at varying distances.
   - Bounding boxes include visibility levels for occlusion estimation.

3. **UAVDT (15GB)**
   - Focused on vehicle detection and tracking in UAV-based urban environments.
   - 80 video sequences with 23,258 frames, annotated for vehicle detection.
   - Contains varying occlusion, weather conditions, and complex backgrounds.

## Methodology

The project implements an **Occlusion Estimation Module (OEM)** to generate occlusion masks for better detection performance. The methodology involves:

### Data Preprocessing
- Loading dataset images and parsing bounding box annotations.
- Mapping images with corresponding occlusion information.

### Occlusion Mask Generation
- Extracting bounding boxes and visibility scores.
- Converting relative coordinates to absolute pixel values.
- Creating occlusion masks using intensity scaling (1-255) based on visibility levels.

### Model Integration
- Enhancing YOLO-based object detection models (YOLO v8x, YOLO v11x) with occlusion-aware input processing.
- Using transformer-based post-processing to refine detections under occlusions.

### Evaluation and Optimization
- Comparing detection performance with and without occlusion-aware enhancements.
- Refining the system based on quantitative performance metrics.

![CV Project - visual selection](https://github.com/user-attachments/assets/129b7623-09e6-4dc4-911b-1cac5a4e1f48)


## Implementation

The system processes images and annotations to create occlusion-aware data inputs:
- The UAVDT dataset is loaded, and annotations are parsed from text files.
- Bounding boxes are extracted, converted into pixel coordinates, and clamped within image dimensions.
- A binary occlusion mask is generated for each image, where occluded regions are highlighted based on visibility metrics.
- The generated masks are stored and visualized for qualitative assessment.
- The final processed dataset is used for training enhanced YOLO-based object detection models.

## Progress

- ✅ **Occlusion Estimation Module** implemented for UAVDT and NOMAD datasets.
- ✅ **YOLO v8x and YOLO v11x** trained on VisDrone dataset.
- 🚀 **Ongoing work** on transformer-based detection refinement.

## Outputs
- **VisDrone - YOLO v8x**:
![Screenshot 2025-03-24 141225](https://github.com/user-attachments/assets/e4fa971e-be47-4f8d-a23f-02479ee02b70)

- **VisDrone - YOLO v11x**:
![Screenshot 2025-03-24 141550](https://github.com/user-attachments/assets/ff5b83d6-c59e-41de-9ae5-b07ad49714c8)

![Screenshot 2025-03-24 205040](https://github.com/user-attachments/assets/1f64952e-3934-487e-a18d-b333773c5d0f)

