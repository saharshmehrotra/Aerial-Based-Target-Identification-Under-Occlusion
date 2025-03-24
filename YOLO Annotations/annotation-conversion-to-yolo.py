import os
import glob
import cv2

def convert_annotations_for_dataset(image_dir, ann_dir, output_dir):
    """
    Converts VisDrone annotations to YOLO format for a given dataset.
    
    Parameters:
      image_dir (str): Directory containing the images.
      ann_dir (str): Directory containing the original annotations.
      output_dir (str): Directory to save the converted YOLO-format annotations.
      
    For each annotation file, the script:
        - Finds the corresponding image (tries .jpg then .png)
        - Reads the image dimensions from the image file.
        - Converts each annotation from:
              x1, y1, w, h, score, category, truncation, occlusion
          to YOLO format:
              <class_id> <x_center> <y_center> <width> <height> <occlusion>
          with all values normalized by the image's actual width and height.
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Process every annotation file (*.txt) in the annotation directory.
    for ann_file in glob.glob(os.path.join(ann_dir, "*.txt")):
        base_name = os.path.splitext(os.path.basename(ann_file))[0]
        
        # Look for the corresponding image. Adjust the extensions if needed.
        image_path = os.path.join(image_dir, base_name + ".jpg")
        if not os.path.exists(image_path):
            image_path = os.path.join(image_dir, base_name + ".png")
        if not os.path.exists(image_path):
            print(f"Warning: Image for {ann_file} not found. Skipping.")
            continue

        # Read the image to get its dimensions.
        img = cv2.imread(image_path)
        if img is None:
            print(f"Warning: Could not load image {image_path}. Skipping.")
            continue
        height, width = img.shape[:2]

        # Read the annotation file.
        with open(ann_file, "r") as f:
            lines = f.readlines()

        yolo_annotations = []
        for line in lines:
            # Split by comma, strip extra spaces, and filter out empty strings.
            parts = [p.strip() for p in line.strip().split(',') if p.strip()]
            if len(parts) != 8:
                print(f"Skipping malformed line in {ann_file}: {line.strip()}")
                continue

            try:
                x1, y1, w, h, score, category, truncation, occlusion = map(float, parts)
            except ValueError:
                print(f"Skipping non-numeric line in {ann_file}: {line.strip()}")
                continue

            # Calculate YOLO bounding box parameters using the actual image dimensions.
            x_center = (x1 + w / 2) / width
            y_center = (y1 + h / 2) / height
            w_norm = w / width
            h_norm = h / height

            # Write annotation as: <class_id> <x_center> <y_center> <width> <height> <occlusion>
            yolo_annotations.append(f"{int(category)} {x_center:.6f} {y_center:.6f} {w_norm:.6f} {h_norm:.6f} {int(occlusion)}")

        # Save the converted annotations into the output folder.
        output_file = os.path.join(output_dir, os.path.basename(ann_file))
        with open(output_file, "w") as f:
            f.write("\n".join(yolo_annotations))

    print(f"✅ Conversion complete for dataset with images in '{image_dir}'.")
    print(f"YOLO annotations saved in '{output_dir}'.\n")


# Define your dataset directories:

# Train set
train_image_dir = r"C:\Users\jmdgo\Downloads\VisDrone2019-DET-train\VisDrone2019-DET-train\images"
train_ann_dir   = r"C:\Users\jmdgo\Downloads\VisDrone2019-DET-train\VisDrone2019-DET-train\annotations"
train_output_dir = r"C:\Users\jmdgo\Downloads\VisDrone2019-DET-train\yolo_labels"

# Validation set
val_image_dir = r"C:\Users\jmdgo\Downloads\VisDrone2019-DET-val\VisDrone2019-DET-val\images"
val_ann_dir   = r"C:\Users\jmdgo\Downloads\VisDrone2019-DET-val\VisDrone2019-DET-val\annotations"
val_output_dir = r"C:\Users\jmdgo\Downloads\VisDrone2019-DET-val\yolo_labels"

# Test set (Test-dev)
test_image_dir = r"C:\Users\jmdgo\Downloads\VisDrone2019-DET-test-dev\images"
test_ann_dir   = r"C:\Users\jmdgo\Downloads\VisDrone2019-DET-test-dev\annotations"
test_output_dir = r"C:\Users\jmdgo\Downloads\VisDrone2019-DET-test-dev\yolo_labels"

# Convert each dataset
convert_annotations_for_dataset(train_image_dir, train_ann_dir, train_output_dir)
convert_annotations_for_dataset(val_image_dir, val_ann_dir, val_output_dir)
convert_annotations_for_dataset(test_image_dir, test_ann_dir, test_output_dir)
