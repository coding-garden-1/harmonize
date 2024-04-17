from PIL import Image, ImageDraw, ImageFont, ImageFilter
import os
import math

def thumbnail_generate(user_input):
    # Function to resize an image with cropping
    def crop_resize_image(image_path, output_path, target_size):
        img = Image.open(image_path)
        width, height = img.size

        # Calculate cropping coordinates
        left = (width - target_size[0]) / 2
        top = (height - target_size[1]) / 2
        right = (width + target_size[0]) / 2
        bottom = (height + target_size[1]) / 2

        # Crop and save the image
        img_cropped = img.crop((left, top, right, bottom))
        img_cropped.save(output_path)
    from PIL import Image

# Define the dimensions of the image
    width = 800
    height = 600

    # Create a new black image
    background = Image.new('RGB', (width, height), color='black')

    # Save the image
    background.save("Background.jpg")

    # Load a predetermined background image
    background_path = "background.jpg"  # Replace with your image file path
    img = Image.open(background_path)
    draw = ImageDraw.Draw(img)

    # Prompt user for text input

    # Load the "naratifcondensed-bolditalic.otf" font
    font_path = "naratifcondensed-bolditalic.otf"  # Replace with your font file path
    font_size = 144
    font = ImageFont.truetype(font_path, font_size)
    line_height = 165
    text_width = 5
    # Set initial position
    text_position = (300, 300)
    text_color = "white"
    outline_color = "black"

    # Add a blurred drop shadow at an 80-degree angle
    shadow_offset = 0.15  # Adjust this value to control the proximity of the shadow
    shadow_angle = 45  # Set the desired angle in degrees

    # Convert the angle to radians
    shadow_angle_rad = math.radians(shadow_angle)

    # Reset text position for the actual text
    text_position = (300, 300)

    for phrase in user_input.split('\n'):
        words = phrase.split()

        if len(words) >= 3:
            first_word_length = len(words[0])
            for i in range(1, len(words)):
                word_length = len(words[i])
                if word_length < first_word_length / 2:
                    # Add spaces to center the current word
                    spaces_to_add = first_word_length // 2 - word_length
                    words[i] = " " * spaces_to_add + words[i]

        for word in words:
            # Calculate shadow position based on the angle
            shadow_offset_x = int(shadow_offset * line_height * math.cos(shadow_angle_rad))
            shadow_offset_y = int(shadow_offset * line_height * math.sin(shadow_angle_rad))
            shadow_position = (text_position[0] + shadow_offset_x, text_position[1] + shadow_offset_y)

            # Add a blurred drop shadow for each word
            shadow_text = Image.new("RGBA", img.size, (0, 0, 0, 0))
            shadow_draw = ImageDraw.Draw(shadow_text)
            shadow_draw.text(shadow_position, word, font=font, fill=(0, 0, 0, 128))
            shadow_text = shadow_text.filter(ImageFilter.GaussianBlur(radius=5))

            # Paste the shadow onto the original image
            img.paste(shadow_text, (0, 0), shadow_text)

            # Draw the outline for the actual text with increased width
            for offset in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
                outline_position = (text_position[0] + offset[0], text_position[1] + offset[1])
                draw.text(outline_position, word, font=font, fill=outline_color)

            # Draw the actual text
            draw.text(text_position, word, font=font, fill=text_color)

            # Move to the next line
            text_position = (text_position[0], text_position[1] + line_height + 10)

    # Resize the image with cropping to 1280x720
    crop_resize_image(background_path, "resized_background.jpg", (1280, 720))

    # Save the thumbnail
    output_path = "thumbnail_with_text_effects.jpg"
    img.save(output_path)

