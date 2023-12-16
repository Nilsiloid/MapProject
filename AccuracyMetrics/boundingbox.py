import cv2
from PIL import Image

image = cv2.imread('map_266.png')

# Define the coordinates of the bounding box
x, y, width, height = 193, 16, 284, 25
x1, y1, width1, height1 = 191, 18, 292, 32

# shifting x,y from center of image to top left
x = x - (width//2)
y = y - (height//2)

x1 = x1 - (width1//2)
y1 = y1 - (height1//2)

# Draw the bounding box on the image
color = (0, 255, 0)  # BGR color format (green in this case)
thickness = 2
color1 = (255, 0, 0)

cv2.rectangle(image, (x, y), (x + width, y + height), color, thickness)

cv2.rectangle(image, (x1, y1), (x1 + width1, y1 + height1), color1, thickness)

# Display the image
cv2.imshow('Image with Bounding Box', image)
cv2.waitKey(0)
cv2.destroyAllWindows()