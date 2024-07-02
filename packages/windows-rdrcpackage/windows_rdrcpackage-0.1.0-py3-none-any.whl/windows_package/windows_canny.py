import tkinter as tk
from tkinter import filedialog

import cv2
import numpy as np
import time
import os


def trace_contours(edge_image):
    # Placeholder for where you would implement contour tracing in FPGA
    # This function simulates tracing edges by finding non-zero pixels
    contours = []
    visited = np.zeros_like(edge_image, dtype=bool)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 4-connectivity

    for i in range(edge_image.shape[0]):
        for j in range(edge_image.shape[1]):
            if edge_image[i, j] != 0 and not visited[i, j]:
                contour = []
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    if not visited[x, y]:
                        visited[x, y] = True
                        contour.append((x, y))
                        for dx, dy in directions:
                            xn, yn = x + dx, y + dy
                            if 0 <= xn < edge_image.shape[0] and 0 <= yn < edge_image.shape[1]:
                                if edge_image[xn, yn] != 0 and not visited[xn, yn]:
                                    stack.append((xn, yn))
                if contour:
                    contours.append(contour)
    return contours


def process_image(image_path, background_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    background = cv2.imread(background_path, cv2.IMREAD_GRAYSCALE)
    blurred_bg = cv2.GaussianBlur(background, (5, 5), 0)
    cv2.imshow('raw', image)
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))

    start_time = time.time()

    # Apply Gaussian blur to smooth the image
    blurred = cv2.GaussianBlur(image, (5, 5), 0)
    cv2.imshow('blurred', blurred)

    # Background subtraction
    print(blurred.shape, blurred_bg.shape)
    bg_sub = cv2.subtract(blurred_bg, blurred)
    cv2.imshow('bg_sub', bg_sub)

    # Apply threshold
    _, binary = cv2.threshold(bg_sub, 10, 255, cv2.THRESH_BINARY)
    # binary = cv2.adaptiveThreshold(bg_sub, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 3, 2)
    cv2.imshow('binary', binary)

    # Erode and dilate to remove noise
    dilate1 = cv2.dilate(binary, kernel, iterations = 2)
    cv2.imshow('dilate1', dilate1)
    erode1 = cv2.erode(dilate1, kernel, iterations = 2)
    cv2.imshow('erode1', erode1)
    erode2 = cv2.erode(erode1, kernel, iterations = 1)
    cv2.imshow('erode2', erode2)
    dilate2 = cv2.dilate(erode2, kernel, iterations = 1)
    cv2.imshow('dilate2', dilate2)



    # Apply Canny edge detector to find edges
    edges = cv2.Canny(erode2, 50, 150)
    cv2.imshow('canny edges', edges)

    # Trace contours from the edge image
    contours = trace_contours(edges)

    end_time = time.time()
    dif_time = end_time - start_time
    print(dif_time)

    # Prepare an image to draw the contours
    contour_image = np.zeros_like(image)

    # Draw each contour
    for contour in contours:
        for x, y in contour:
            contour_image[x, y] = 255

    # Show the resulting image
    cv2.imshow('Processed Image', contour_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


root = tk.Tk()
root.withdraw()
background_path = filedialog.askopenfilename(
    title="請選取背景圖片"
)
print(background_path)
background = cv2.imread(background_path, cv2.IMREAD_GRAYSCALE)

root = tk.Tk()
root.withdraw()
image_folder_path = filedialog.askdirectory(
    title="請選取圖片資料夾")

file_info_list = []
def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            image_path= os.path.join(root, file)
            #kind = filetype.guess(file_path)
            _, extension = os.path.splitext(file)
            extension = extension.lower() 
            if extension in ['.tiff', '.tif', '.jpg', '.jpeg', '.png']:  # 只添加圖像文件
                print(f'找到圖像文件: {image_path}')
                file_info_list.append(image_path)
            else:
                print(f'跳過非圖像文件: {image_path}')
                
scan_directory(image_folder_path)

for image_path in file_info_list:
    print(f"Processing: {image_path}")
    process_image(image_path, background_path)
