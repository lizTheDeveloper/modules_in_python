from PIL import Image, ImageEnhance, ImageOps

def summer_tone(image_path):
    # Load the image
    img = Image.open(image_path)

    # Enhance color to increase saturation
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.5)  # Increase this value to enhance colors more

    # Modify the image with a warm color balance
    # Create a color transform matrix for a warm tone
    matrix = [
        1.4, 0.0, 0.0, 0,  # Red channel increased
        0.0, 1.2, 0.0, 0,  # Green channel slightly increased
        0.0, 0.0, 0.9, 0   # Blue channel slightly decreased
    ]
    img = img.convert('RGB', matrix)

    # Optionally enhance brightness
    brightness_enhancer = ImageEnhance.Brightness(img)
    img = brightness_enhancer.enhance(1.2)  # Adjust brightness

    # Save the modified image
    img.save('summer_toned_image.jpg')
    img.show()

# Use the function
summer_tone('moons.jpg')
