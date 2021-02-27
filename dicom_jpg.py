import numpy as np
import pydicom
from PIL import ImageTk, Image


ds = pydicom.dcmread('the path to the image') # Put the right path of the image that you want to convert
new_image = ds.pixel_array.astype(float) # Convert the values into float

scaled_image = (np.maximum(new_image, 0) / new_image.max()) * 255.0

scaled_image = np.uint8(scaled_image)
final_image = Image.fromarray(scaled_image)

final_image.show() # Display the Image

final_image.save('image.jpg') # Save the image as JPG
final_image.save('image.png') # Save the image as PNG