from PIL import Image, ImageDraw, ImageFont

def create_overlay(base_image_path, map_image_path, place_name, latitude, longitude, Adressline1, Adressline2, date_time, note):
    # Load the base image
    base_image = Image.open(base_image_path)
    base_image = base_image.convert("RGBA")

    # Define the size and position for the overlay
    overlay_height = 240  # Double the height
    overlay_position = (240, base_image.height - overlay_height - 40)  # Adjusted position to move it upward

    # Create an overlay image with a transparent background
    overlay = Image.new("RGBA", base_image.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Draw a rounded rectangle for the overlay
    overlay_mask = Image.new("L", base_image.size, 0)
    overlay_mask_draw = ImageDraw.Draw(overlay_mask)
    overlay_mask_draw.rounded_rectangle([overlay_position, (base_image.width - 20, base_image.height - 50)], fill=128, radius=15)

    # Draw a rounded rectangle with a transparent grey background
    draw.rounded_rectangle([overlay_position, (base_image.width - 20, base_image.height - 50)], fill=(180, 180, 180, 180), radius=15)

    # Load a font
    font = ImageFont.truetype("arial.ttf", 40)  # Double the font size
    small_font = ImageFont.truetype("arial.ttf", 28)  # Double the small font size
    text_color = (255, 255, 255)  # White color

    # Add texts to the overlay
    

    # Load the map image
    map_image = Image.open(map_image_path)
    map_image = map_image.convert("RGBA")  # Ensure it has an alpha channel

    # Resize map image to fit within the overlay
    map_image = map_image.resize((200, 230), Image.LANCZOS)  # Double the size

    # Create a mask for the rounded corners of the map image
    map_mask = Image.new("L", map_image.size, 0)
    map_mask_draw = ImageDraw.Draw(map_mask)
    map_mask_draw.rounded_rectangle([0, 0, 200, 230], fill=255, radius=15)

    # Create a new image to hold the rounded map image
    rounded_map_image = Image.new("RGBA", map_image.size)
    rounded_map_image.paste(map_image, (0, 0), map_mask)

    # Paste the rounded map image on the base image
    base_image.paste(rounded_map_image, (20, base_image.height - 280), rounded_map_image)

    # Apply the overlay mask to the overlay
    overlay.putalpha(overlay_mask)
    draw.text((250, base_image.height - 275), place_name, fill=text_color, font=font)
    draw.text((253, base_image.height - 195), f"Lat: {latitude}  Long: {longitude}", fill=text_color, font=small_font)
    draw.text((253, base_image.height - 230), Adressline1, fill=text_color, font=small_font)
    draw.text((253, base_image.height - 160), Adressline2, fill=text_color, font=small_font)
    draw.text((253, base_image.height - 125), date_time, fill=text_color, font=small_font)
    draw.text((253, base_image.height - 90), note, fill=text_color, font=small_font)

    # Merge the overlay with the base image
    combined_image = Image.alpha_composite(base_image, overlay)
    

    # Convert the image to 'RGB' and save
    rgb_image = combined_image.convert('RGB')
    output_path = "Rs_imageq.jpg"
    rgb_image.save(output_path)
    print(f"Overlay applied successfully! Image saved as {output_path}")

# Example usage
create_overlay(
    "RS.jpeg",  # Replace with the path to your base image
    "Map.jpeg",  # Replace with the path to your map image
    "Chickmagalur, KA, India", 
    "13.3161° N", "75.7720° E",  # Latitude and Longitude
    "Kote, Chickmagalur,", 
    "577101, KA, India",
    "Monday, 27 February 2022 15:40",
    "Note: Captured by GPS Map Camera"
)
