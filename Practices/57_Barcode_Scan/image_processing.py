#!/usr/bin/env python
# -*- coding: utf-8 -*-

##
# @file image_processing.py
#
# @brief Process cv2 frames or images for various aspects.
# This is suppose to be used as a standalone library.
#
# @section image_processing.py Description
# Process cv2 frames or images for various aspects.
#
# @section author_doxygen Author(s)
# - Created by Tushar G Hedaoo on 07 March 2025.
# - Modified by Tushar G Hedaoo on 07 March 2025.
#
# Copyright (c) 2025 Kohler Ventures.  All rights reserved.

__author__ = "Tushar G Hedaoo"
__copyright__ = "Copyright 2025"

import traceback, zxingcpp
import cv2, numpy as np

class ImageProcessing():
    """! The image processing class.
    Defines the class that handles specific to KV image processing operations.
    """

    class ColorTolerance():
        """! Color tolerance ranges. """
        red_lower_color = np.array([0, 150, 120])  
        red_upper_color = np.array([10, 255, 255])  
        blue_lower_color = np.array([100, 100, 100])
        blue_upper_color = np.array([130, 255, 255])
        green_lower_color = np.array([35, 50, 50])
        green_upper_color = np.array([75, 255, 255])
        white_lower_color = np.array([0, 0, 220])
        white_upper_color = np.array([180, 30, 255])
        turquiose_lower_color = np.array([80, 50, 50])
        turquiose_upper_color = np.array([100, 255, 255])
        # TODO import magenta if needed.
    
    @staticmethod
    def detect_color(frame : np.ndarray, frame_size : dict):
        """! Analyze single color in the requested frame and roi.
        Image processing using contour and masking to analyze a spectrum of colors.
        Marks the frame with the color found. Saves any color transitions in a csv file.
        @param frame            cv2 MatLike frame from an image and video.
        @param frame_size       region of interest where the color needs to be analyzed.
                                    frame_size should be of format 
                                    {
                                        "start_coordinate" : [x_start, y_start],
                                        "resolution" : [x_len, y_len]
                                    }
                                    x is vertical and y is horizontal.
                                    (x_start, y_start)------------------(x_len)
                                    .                                  .
                                    .                                  .
                                    .-----------------------------------(y_len)
        @return Tuple - (detected_color, modified_frame) or (Exception string, original_frame)
        """
        try:
            # Detect the color for the frame here.
            x, y = frame_size["start_coordinate"]    # Starting point.
            w, h = frame_size["resolution"]          # Area.
            requested_detection_area = frame[y:y + h, x:x + w]
            hsv_frame = cv2.cvtColor(requested_detection_area, cv2.COLOR_BGR2HSV)

            # Create a mask using the color range.
            red_mask = cv2.inRange(hsv_frame, ImageProcessing.ColorTolerance.red_lower_color, ImageProcessing.ColorTolerance.red_upper_color)
            blue_mask = cv2.inRange(hsv_frame, ImageProcessing.ColorTolerance.blue_lower_color, ImageProcessing.ColorTolerance.blue_upper_color)
            green_mask = cv2.inRange(hsv_frame, ImageProcessing.ColorTolerance.green_lower_color, ImageProcessing.ColorTolerance.green_upper_color)
            white_mask = cv2.inRange(hsv_frame, ImageProcessing.ColorTolerance.white_lower_color, ImageProcessing.ColorTolerance.white_upper_color)
            turquiose_mask = cv2.inRange(hsv_frame, ImageProcessing.ColorTolerance.turquiose_lower_color, ImageProcessing.ColorTolerance.turquiose_upper_color)
            # Apply some morphological operations (like dilation) to smooth the mask.
            red_mask = cv2.dilate(red_mask, None, iterations=2)
            blue_mask = cv2.dilate(blue_mask, None, iterations=2)
            green_mask = cv2.dilate(green_mask, None, iterations=2)
            white_mask = cv2.dilate(white_mask, None, iterations=2)
            turquiose_mask = cv2.dilate(turquiose_mask, None, iterations=2)

            # Find contours in the mask to locate the LED region (optional).
            red_contours, _ = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            blue_contours, _ = cv2.findContours(blue_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            green_contours, _ = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            white_contours, _ = cv2.findContours(white_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            turquiose_contours, _ = cv2.findContours(turquiose_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Filter contours based on area to ignore small noise.
            red_filtered_contours = [contour for contour in red_contours if cv2.contourArea(contour) > 50]
            blue_filtered_contours = [contour for contour in blue_contours if cv2.contourArea(contour) > 50]
            green_filtered_contours = [contour for contour in green_contours if cv2.contourArea(contour) > 50]
            white_filtered_contours = [contour for contour in white_contours if cv2.contourArea(contour) > 50]
            turquiose_filtered_contours = [contour for contour in turquiose_contours if cv2.contourArea(contour) > 50]

            # If there are any contours, calculate the average color inside the region. 
            if red_filtered_contours:
                color = 'RED'
            elif blue_filtered_contours:
                color = 'BLUE'
            elif green_filtered_contours:
                color = 'GREEN'
            elif turquiose_filtered_contours:
                color = 'TURQUOISE'
            elif white_filtered_contours:
                color = 'WHITE'
            else:
                color = 'NONE'

            # Mark the frame with the color found.
            cv2.rectangle(frame, (0, 38), (50, 50), (0,0,0), -1)
            cv2.putText(frame, str(color), (2, 47), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1)
            return (color, frame)
        except:
            # We send the frame back with the exception message.
            return (traceback.format_exc(), frame)
        
    @staticmethod
    def read_barcode(filename : str):
        """! Reads QR, Bar type, Data Matrix. Displays all results.
        @param filename    Image file location (full path) to detect barcode in.
        @return     All detected barcodes (list). 
                    Each detection has
                    - text
                    - format
                    - content_type
                    - position
                    Exception string if issues or no detections.
        """
        try:
            image = cv2.imread(filename, 0)
            results = zxingcpp.read_barcodes(image)
            if len(results) == 0:
                raise Exception('No barcodes detected.')
            return results
        except:
            return traceback.format_exc()
    