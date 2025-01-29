# Object Width Measurement using OpenCV

This Python script uses OpenCV to capture video from a webcam, detect objects based on color, and estimate the width of the detected objects in centimeters. It is designed to work with a specific color range and uses contour detection to identify objects.

## Requirements

- Python 3.x
- OpenCV (`cv2`)
- NumPy (`numpy`)

You can install the required libraries using pip:


pip install opencv-python numpy
How It Works
Video Capture: The script captures video from the default webcam (or a specified camera index).

Color Detection: It converts the video frames to the HSV color space and applies a mask to detect objects within a specified color range.

Contour Detection: Contours are detected from the masked image, and bounding boxes are drawn around the detected objects.

Width Calculation: The width of the detected object is calculated and displayed on the video frame in centimeters.

Display: The processed video frames are displayed in real-time.

Code Overview
Color Range: The script detects objects within the HSV color range [160, 100, 20] to [179, 255, 255] (reddish colors). You can adjust these values to detect different colors.

Contour Filtering: Only contours with an area greater than 100 pixels are considered to avoid noise.

Width Calculation: The width of the object is estimated using a scaling factor (l1), which is set to 15 in the script. Adjust this value based on your camera setup and object distance.

Usage
Connect a webcam to your system.

Run the script:

bash
Copy
python object_width_measurement.py
Point the webcam at an object within the specified color range.

The script will display the video feed with bounding boxes and the estimated width of the object in centimeters.

Customization
Color Range: Modify the lower and upper HSV values in the script to detect different colors.

Scaling Factor: Adjust the l1 variable to calibrate the width calculation for your specific setup.

Contour Area Threshold: Change the area > 100 condition to filter contours based on your requirements.

Example Output
The script will display a live video feed with:

Bounding boxes around detected objects.

Lines drawn diagonally across the bounding box.

The estimated width of the object displayed in centimeters.

Notes
Ensure proper lighting conditions for accurate color detection.

The accuracy of the width measurement depends on the camera calibration and the distance between the camera and the object.
