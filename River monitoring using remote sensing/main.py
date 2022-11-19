# import module
from PIL import Image, ImageChops

# assign images
img1 = Image.open("Jamuna river data1973.png")
#img2 = Image.open("Jamuna river data1973.png")

img2 = Image.open("Jamuna river data1980.png")

# finding difference
diff = ImageChops.difference(img1, img2)

# showing the difference
diff.show()