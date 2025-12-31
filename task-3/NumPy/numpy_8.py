import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def rgb_histogram(image_path):

    # --- טעינת התמונה ---
    image = Image.open(image_path)
    image_np = np.array(image)

    # --- הפרדת ערוצי RGB ---
    r = image_np[:, :, 0]
    g = image_np[:, :, 1]
    b = image_np[:, :, 2]

    # ---  חישוב היסטוגרמות מהתמונה שהוספתי---
    hist_r, _ = np.histogram(r, bins=256, range=(0, 255))
    hist_g, _ = np.histogram(g, bins=256, range=(0, 255))
    hist_b, _ = np.histogram(b, bins=256, range=(0, 255))

    # ---גרף צבעים- הצגת ההיסטוגרמה ---
    plt.figure(figsize=(12, 5))
    plt.plot(hist_r, color='red', label='Red channel')
    plt.plot(hist_g, color='green', label='Green channel')
    plt.plot(hist_b, color='blue', label='Blue channel')
    plt.title(f"RGB Histogram for {image_path}")
    plt.xlabel("Pixel value")
    plt.ylabel("Frequency")
    plt.legend()
    plt.show()

# --- קריאה לדוגמה ---
rgb_histogram("see.jpg")  # החליפי בשם הקובץ שלך
