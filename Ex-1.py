#!/usr/bin/env python
# coding: utf-8

# ## Image-Handling-and-Pixel-Transformations-Using-OpenCV
# NAME     :MOHAMMAD FAIZAL SK
# REG.NO   :212223240092

# In[4]:


import cv2
import matplotlib.pyplot as plt


# In[5]:


# Read the image using OpenCV
img = cv2.imread('exp1image.jpeg', cv2.IMREAD_COLOR)


# In[6]:


# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[7]:


# Display the image using Matplotlib
plt.imshow(img_rgb, cmap='viridis')  # You can change 'viridis' to another cmap or use None for RGB images
plt.title("Original Image")
plt.axis('off')  # Removes axis ticks and labels
plt.show()

Step2:
o Draw a line from the top-left to the bottom-right of the image.

o Draw a circle at the center of the image. 

o Draw a rectangle around a specific region of interest in the image. 

o Add the text "OpenCV Drawing" at the top-left corner of the image.Draw a line from the top-left to the bottom-right of the image
# In[8]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 


# In[9]:


# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[10]:


img_rgb.shape


# In[11]:


# Draw a line from top-left to bottom-right
line_img = cv2.line(img_rgb, (0, 0), (768, 600), (255, 0, 0), 2) # cv2.line(image, start_point, end_point, color, thickness)


# In[12]:


plt.imshow(line_img, cmap='viridis')  
plt.title("Image with Line")
plt.axis('off')  
plt.show()

Draw a circle at the center of the image.
# In[13]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 

# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[14]:


img_rgb.shape


# In[15]:


circle_img = cv2.circle(img_rgb,(400,300),150,(255,0,0),10) # cv2.circle(image, center, radius, color, thickness)


# In[16]:


plt.imshow(circle_img, cmap='viridis')  
plt.title("Image with Circle")
plt.axis('off')  
plt.show()

Draw a rectangle around  the whole image
# In[17]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 

# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[18]:


img.shape


# In[19]:


# Draw a rectangle around the Whole image
rectangle_img = cv2.rectangle(img_rgb, (0, 0), (768, 600), (0, 0, 255), 10)  # cv2.rectangle(image, start_point, end_point, color, thickness)


# In[20]:


plt.imshow(rectangle_img, cmap='viridis')  
plt.title("Image with Rectangle")
plt.axis('off')  
plt.show()

Add the text "OpenCV Drawing" at the top-left corner of the image.
# In[21]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 

# Convert BGR (OpenCV's default) to RGB (Matplotlib's expected color order)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# In[22]:


# Add text to the image
text_img = cv2.putText(img_rgb, "OpenCV Drawing", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 10)  ## cv2.putText(image, text, position, font, font_scale, color, thickness)


# In[23]:


plt.imshow(text_img, cmap='viridis')  
plt.title("Image with Text")
plt.axis('off')  
plt.show()

Step3:
o Convert the image from RGB to HSV and display it.
    
o Convert the image from RGB to GRAY and display it. 

o Convert the image from RGB to YCrCb and display it. 
    
o Convert the HSV image back to RGB and display it.
# In[24]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 


# In[25]:


image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# In[ ]:


# Original RGB Image
plt.imshow(image_rgb)
plt.title("Original RGB Image")
plt.axis("off")


# In[ ]:


# Convert RGB to HSV
image_hsv = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2HSV)


# In[ ]:


# HSV Image
plt.imshow(image_hsv)
plt.title("HSV Image")
plt.axis("off")


# In[ ]:


# Convert RGB to GRAY
image_gray = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2GRAY)


# In[ ]:


# Grayscale Image
plt.imshow(image_gray, cmap='gray')
plt.title("Grayscale Image")
plt.axis("off")


# In[ ]:


# Convert RGB to YCrCb
image_ycrcb = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2YCrCb)


# In[ ]:


# YCrCb Image
plt.imshow(image_ycrcb)
plt.title("YCrCb Image")
plt.axis("off")


# In[ ]:


# Convert HSV back to RGB
image_hsv_to_rgb = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2RGB)


# In[ ]:


plt.imshow(image_hsv_to_rgb)
plt.title("HSV to RGB Image")
plt.axis("off")

Step4:
o Access and print the value of the pixel at coordinates (100, 100). 

o Modify the color of the pixel at (200, 200) to white.
# In[ ]:


# Modify a block of pixels (300x300) to white, starting from (200, 200)
image[200:500, 200:500] = [255, 255, 255]  # Rows: 200-499, Columns: 200-499


# In[ ]:


# Convert BGR to RGB for displaying with Matplotlib
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


# In[ ]:


# Display the modified image
plt.imshow(image_rgb)
plt.title("Image with 300x300 White Block")
plt.axis("off")
plt.show()

Step5:
o Resize the original image to half its size and display it.
# In[ ]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 


# In[ ]:


image.shape


# In[ ]:


# Resize the image to half its size
resized_image = cv2.resize(image, (768 // 2, 600 // 2))  # (new_width, new_height)


# In[ ]:


# Convert BGR to RGB for displaying with Matplotlib
resized_image_rgb = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)


# In[ ]:


resized_image_rgb.shape


# In[ ]:


# Display the resized image
plt.imshow(resized_image_rgb)
plt.title("Resized Image (Half Size)")
plt.axis("off")
plt.show()

Step6:
o Crop a region of interest (ROI) from the image (e.g., a 100x100 pixel area starting at (50, 50)) and display it.
# In[ ]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 


# In[ ]:


image.shape


# In[ ]:


# Crop a 300x300 region starting from (50, 50)
roi = image[50:350, 50:350]  # Rows: 50-349, Columns: 50-349


# In[ ]:


# Convert BGR to RGB for displaying with Matplotlib
roi_rgb = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)


# In[ ]:


# Display the cropped region (ROI)
plt.imshow(roi_rgb)
plt.title("Cropped Region of Interest (ROI)")
plt.axis("off")
plt.show()

Step7:
o Flip the original image horizontally and display it. 

o Flip the original image vertically and display it.
# In[ ]:


# Load the image
image = cv2.imread('Qno. 1.jpg') 


# In[ ]:


# Flip the image horizontally (left-right)
flipped_horizontally = cv2.flip(image, 1)


# In[ ]:


# Convert BGR to RGB for displaying with Matplotlib
flipped_horizontally_rgb = cv2.cvtColor(flipped_horizontally, cv2.COLOR_BGR2RGB)


# In[ ]:


# Horizontal flip
plt.imshow(flipped_horizontally_rgb)
plt.title("Flipped Horizontally")
plt.axis("off")


# In[ ]:


# Flip the image vertically (up-down)
flipped_vertically = cv2.flip(image, 0)


# In[ ]:


# Convert BGR to RGB for displaying with Matplotlib
flipped_vertically_rgb = cv2.cvtColor(flipped_vertically, cv2.COLOR_BGR2RGB)


# In[ ]:


# Vertical flip
plt.imshow(flipped_vertically_rgb)
plt.title("Flipped Vertically")
plt.axis("off")

Step8:
o Save the final modified image to your local directory.
# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




