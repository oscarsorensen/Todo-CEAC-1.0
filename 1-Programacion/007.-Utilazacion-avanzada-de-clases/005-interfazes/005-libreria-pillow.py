from PIL import Image

# Open the image
img = Image.open("billed.jpg")

# Ensure image is loaded (and not lazy)
img = img.convert("RGB")

# Get the first pixel (top-left corner)
first_pixel = img.getpixel((5, 120))

# Print the pixel tuple
print(first_pixel)