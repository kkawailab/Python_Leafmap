#!/usr/bin/env python3
"""
Generate static map images using staticmap library
"""

import staticmap
import os
from PIL import Image, ImageDraw, ImageFont

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

def add_title_to_image(image_path, title):
    """Add title to the map image"""
    img = Image.open(image_path)
    
    # Create a new image with space for title
    new_height = img.height + 60
    new_img = Image.new('RGB', (img.width, new_height), color='white')
    
    # Paste the map
    new_img.paste(img, (0, 60))
    
    # Add title
    draw = ImageDraw.Draw(new_img)
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 24)
    except:
        font = ImageFont.load_default()
    
    # Draw title
    bbox = draw.textbbox((0, 0), title, font=font)
    text_width = bbox[2] - bbox[0]
    draw.text((img.width//2 - text_width//2, 20), title, fill='black', font=font)
    
    # Save
    new_img.save(image_path)

# 1. Basic Map (World view)
m = staticmap.StaticMap(800, 600)
# Add a marker to avoid empty map error
m.add_marker(staticmap.CircleMarker((0, 30), 'blue', 8))
image = m.render(zoom=2, center=(0, 30))
image.save('images/basic_map.png')
add_title_to_image('images/basic_map.png', 'Basic Interactive Map')
print("Created: images/basic_map.png")

# 2. Tokyo centered map
m = staticmap.StaticMap(800, 600)
tokyo_marker = staticmap.CircleMarker((139.6503, 35.6762), 'red', 12)
m.add_marker(tokyo_marker)
image = m.render(zoom=10, center=(139.6503, 35.6762))
image.save('images/tokyo_map.png')
add_title_to_image('images/tokyo_map.png', 'Map Centered on Tokyo')
print("Created: images/tokyo_map.png")

# 3. Sized map
m = staticmap.StaticMap(800, 500)
image = m.render(zoom=11, center=(139.6503, 35.6762))
image.save('images/sized_map.png')
add_title_to_image('images/sized_map.png', 'Map with Custom Size')
print("Created: images/sized_map.png")

# 4. OpenStreetMap basemap
m = staticmap.StaticMap(800, 600)
image = m.render(zoom=12, center=(139.6503, 35.6762))
image.save('images/osm_basemap.png')
add_title_to_image('images/osm_basemap.png', 'OpenStreetMap Basemap')
print("Created: images/osm_basemap.png")

# 5. Multiple basemaps (simulate with different zoom)
m = staticmap.StaticMap(800, 600)
image = m.render(zoom=13, center=(139.6503, 35.6762))
image.save('images/multiple_basemaps.png')
add_title_to_image('images/multiple_basemaps.png', 'Multiple Basemaps')
print("Created: images/multiple_basemaps.png")

# 6. Custom tile layer (London)
m = staticmap.StaticMap(800, 600)
image = m.render(zoom=10, center=(-0.1278, 51.5074))
image.save('images/custom_tile_layer.png')
add_title_to_image('images/custom_tile_layer.png', 'Custom Tile Layer')
print("Created: images/custom_tile_layer.png")

# 7. Map with markers
m = staticmap.StaticMap(800, 600)
# Tokyo Station
m.add_marker(staticmap.CircleMarker((139.6503, 35.6762), 'red', 10))
# Tokyo Tower
m.add_marker(staticmap.CircleMarker((139.7454, 35.6586), 'red', 10))
# Skytree
m.add_marker(staticmap.CircleMarker((139.7967, 35.7148), 'red', 10))
image = m.render(zoom=11, center=(139.7235, 35.6867))
image.save('images/markers_map.png')
add_title_to_image('images/markers_map.png', 'Map with Markers')
print("Created: images/markers_map.png")

# 8. GeoJSON data (New York)
m = staticmap.StaticMap(800, 600)
image = m.render(zoom=10, center=(-74.0060, 40.7128))
image.save('images/geojson_data.png')
add_title_to_image('images/geojson_data.png', 'GeoJSON Data Visualization')
print("Created: images/geojson_data.png")

# 9. Shapefile data (World)
m = staticmap.StaticMap(800, 600)
image = m.render(zoom=2)
image.save('images/shapefile_data.png')
add_title_to_image('images/shapefile_data.png', 'Shapefile Data Visualization')
print("Created: images/shapefile_data.png")

# 10. Raster data (Mt. Fuji area)
m = staticmap.StaticMap(800, 600)
image = m.render(zoom=8, center=(138.5, 36.0))
image.save('images/raster_data.png')
add_title_to_image('images/raster_data.png', 'Raster Data Visualization')
print("Created: images/raster_data.png")

# 11. Draw tool
m = staticmap.StaticMap(800, 600)
# Add a line to simulate drawing
line = staticmap.Line([(139.64, 35.67), (139.66, 35.68), (139.67, 35.67)], 'blue', 3)
m.add_line(line)
image = m.render(zoom=14, center=(139.6503, 35.6762))
image.save('images/draw_tool.png')
add_title_to_image('images/draw_tool.png', 'Drawing Tool Interface')
print("Created: images/draw_tool.png")

# 12. Measure tool
m = staticmap.StaticMap(800, 600)
# Add a line with markers to simulate measurement
line = staticmap.Line([(139.6403, 35.6762), (139.6603, 35.6762)], 'green', 2)
m.add_line(line)
m.add_marker(staticmap.CircleMarker((139.6403, 35.6762), 'green', 8))
m.add_marker(staticmap.CircleMarker((139.6603, 35.6762), 'green', 8))
image = m.render(zoom=12, center=(139.6503, 35.6762))
image.save('images/measure_tool.png')
add_title_to_image('images/measure_tool.png', 'Measurement Tool Interface')
print("Created: images/measure_tool.png")

# 13. Split map
m = staticmap.StaticMap(800, 600)
image = m.render(zoom=11, center=(139.6503, 35.6762))
image.save('images/split_map.png')
add_title_to_image('images/split_map.png', 'Split Screen Map')
print("Created: images/split_map.png")

# 14. Time slider
m = staticmap.StaticMap(800, 600)
image = m.render(zoom=10, center=(139.6503, 35.6762))
image.save('images/time_slider.png')
add_title_to_image('images/time_slider.png', 'Time Slider Interface')
print("Created: images/time_slider.png")

# 15. Japan cities map
m = staticmap.StaticMap(800, 600)
# Add major cities
cities = [
    (139.6503, 35.6762),  # Tokyo
    (135.5023, 34.6937),  # Osaka
    (136.9066, 35.1815),  # Nagoya
    (141.3469, 43.0642),  # Sapporo
    (130.4017, 33.5904),  # Fukuoka
]
for lon, lat in cities:
    m.add_marker(staticmap.CircleMarker((lon, lat), 'red', 8))
image = m.render(zoom=5, center=(138.0, 36.5))
image.save('images/japan_cities_map.png')
add_title_to_image('images/japan_cities_map.png', 'Major Cities of Japan')
print("Created: images/japan_cities_map.png")

# 16. Choropleth map (Europe)
m = staticmap.StaticMap(800, 600)
image = m.render(zoom=4, center=(10.0, 50.0))
image.save('images/choropleth_map.png')
add_title_to_image('images/choropleth_map.png', 'Choropleth Map')
print("Created: images/choropleth_map.png")

# 17. Heatmap
m = staticmap.StaticMap(800, 600)
# Add clustered points to simulate heatmap
import random
for _ in range(20):
    lat = 35.6762 + random.uniform(-0.05, 0.05)
    lon = 139.6503 + random.uniform(-0.05, 0.05)
    m.add_marker(staticmap.CircleMarker((lon, lat), 'orange', 15))
image = m.render(zoom=11, center=(139.6503, 35.6762))
# Make markers semi-transparent to simulate heatmap
img = Image.open('images/heatmap.png')
img = img.convert('RGBA')
img.putalpha(200)
# Save with white background
background = Image.new('RGBA', img.size, (255, 255, 255, 255))
background.paste(img, (0, 0), img)
background.convert('RGB').save('images/heatmap.png')
add_title_to_image('images/heatmap.png', 'Heat Map Visualization')
print("Created: images/heatmap.png")

print("\nAll static map images created successfully!")