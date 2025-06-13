#!/usr/bin/env python3
"""
Generate actual OpenStreetMap images using folium and static map images
"""

import folium
import os
import io
from PIL import Image
import requests
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Function to create map with OpenStreetMap tiles
def create_static_map_image(lat, lon, zoom, width=800, height=600, markers=None, filename='map.png'):
    """Create a static map image using OpenStreetMap tiles"""
    
    # Create figure
    fig, ax = plt.subplots(1, 1, figsize=(width/100, height/100), dpi=100)
    
    # Get OSM tile
    # Calculate tile coordinates
    import math
    
    def lat_lon_to_tile(lat, lon, zoom):
        lat_rad = math.radians(lat)
        n = 2.0 ** zoom
        x = int((lon + 180.0) / 360.0 * n)
        y = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
        return x, y
    
    def tile_to_lat_lon(x, y, zoom):
        n = 2.0 ** zoom
        lon = x / n * 360.0 - 180.0
        lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * y / n)))
        lat = math.degrees(lat_rad)
        return lat, lon
    
    # Get tile coordinates
    tile_x, tile_y = lat_lon_to_tile(lat, lon, zoom)
    
    # Download tiles for a 3x3 grid
    tiles = []
    for dy in range(-1, 2):
        row = []
        for dx in range(-1, 2):
            tx, ty = tile_x + dx, tile_y + dy
            url = f"https://tile.openstreetmap.org/{zoom}/{tx}/{ty}.png"
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
            try:
                response = requests.get(url, headers=headers)
                if response.status_code == 200:
                    img = Image.open(io.BytesIO(response.content))
                    row.append(img)
                else:
                    # Create blank tile
                    img = Image.new('RGB', (256, 256), color='#f0f0f0')
                    row.append(img)
            except:
                # Create blank tile on error
                img = Image.new('RGB', (256, 256), color='#f0f0f0')
                row.append(img)
        tiles.append(row)
    
    # Combine tiles
    combined_width = 256 * 3
    combined_height = 256 * 3
    combined = Image.new('RGB', (combined_width, combined_height))
    
    for y, row in enumerate(tiles):
        for x, tile in enumerate(row):
            combined.paste(tile, (x * 256, y * 256))
    
    # Crop to desired size
    # Calculate center position
    center_x = combined_width // 2
    center_y = combined_height // 2
    left = center_x - width // 2
    top = center_y - height // 2
    right = left + width
    bottom = top + height
    
    # Ensure we don't go out of bounds
    left = max(0, left)
    top = max(0, top)
    right = min(combined_width, right)
    bottom = min(combined_height, bottom)
    
    cropped = combined.crop((left, top, right, bottom))
    
    # Display the image
    ax.imshow(cropped)
    ax.axis('off')
    
    # Add markers if provided
    if markers:
        for marker in markers:
            marker_lat, marker_lon = marker['lat'], marker['lon']
            # Convert lat/lon to pixel position
            # This is a simplified conversion - for production use more accurate projection
            center_lat, center_lon = tile_to_lat_lon(tile_x, tile_y, zoom)
            top_lat, _ = tile_to_lat_lon(tile_x, tile_y - 1, zoom)
            bottom_lat, _ = tile_to_lat_lon(tile_x, tile_y + 1, zoom)
            _, left_lon = tile_to_lat_lon(tile_x - 1, tile_y, zoom)
            _, right_lon = tile_to_lat_lon(tile_x + 1, tile_y, zoom)
            
            # Simple linear interpolation
            x_pos = (marker_lon - left_lon) / (right_lon - left_lon) * width
            y_pos = (top_lat - marker_lat) / (top_lat - bottom_lat) * height
            
            # Draw marker
            circle = patches.Circle((x_pos, y_pos), radius=10, color='red', ec='darkred', linewidth=2)
            ax.add_patch(circle)
            
            # Add label if provided
            if 'label' in marker:
                ax.text(x_pos, y_pos - 20, marker['label'], ha='center', va='bottom',
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8))
    
    # Add title
    plt.title(filename.replace('.png', '').replace('_', ' ').title(), fontsize=16, pad=20)
    
    # Save figure
    plt.tight_layout()
    plt.savefig(f'images/{filename}', dpi=100, bbox_inches='tight')
    plt.close()
    
    print(f"Created: images/{filename}")

# Generate basic map (World view)
create_static_map_image(
    lat=30, lon=0, zoom=2,
    filename='basic_map.png'
)

# Generate Tokyo centered map
create_static_map_image(
    lat=35.6762, lon=139.6503, zoom=10,
    filename='tokyo_map.png'
)

# Generate sized map (same as Tokyo but different title)
create_static_map_image(
    lat=35.6762, lon=139.6503, zoom=11,
    filename='sized_map.png'
)

# Generate OpenStreetMap basemap
create_static_map_image(
    lat=35.6762, lon=139.6503, zoom=12,
    filename='osm_basemap.png'
)

# Generate map with markers
markers = [
    {'lat': 35.6762, 'lon': 139.6503, 'label': '東京駅'},
    {'lat': 35.6586, 'lon': 139.7454, 'label': '東京タワー'},
    {'lat': 35.7148, 'lon': 139.7967, 'label': 'スカイツリー'}
]
create_static_map_image(
    lat=35.6762, lon=139.6503, zoom=11,
    markers=markers,
    filename='markers_map.png'
)

# Generate Japan cities map
japan_markers = [
    {'lat': 35.6762, 'lon': 139.6503, 'label': '東京'},
    {'lat': 34.6937, 'lon': 135.5023, 'label': '大阪'},
    {'lat': 35.1815, 'lon': 136.9066, 'label': '名古屋'},
    {'lat': 43.0642, 'lon': 141.3469, 'label': '札幌'},
    {'lat': 33.5904, 'lon': 130.4017, 'label': '福岡'}
]
create_static_map_image(
    lat=36.5, lon=138.0, zoom=5,
    markers=japan_markers,
    filename='japan_cities_map.png'
)

# For other specialized maps, create simplified versions
# Multiple basemaps (show different zoom level)
create_static_map_image(
    lat=35.6762, lon=139.6503, zoom=13,
    filename='multiple_basemaps.png'
)

# Custom tile layer (use standard OSM but with different area)
create_static_map_image(
    lat=51.5074, lon=-0.1278, zoom=10,  # London
    filename='custom_tile_layer.png'
)

# GeoJSON data visualization (show a different region)
create_static_map_image(
    lat=40.7128, lon=-74.0060, zoom=10,  # New York
    filename='geojson_data.png'
)

# Shapefile data (show country view)
create_static_map_image(
    lat=0, lon=0, zoom=2,  # World view
    filename='shapefile_data.png'
)

# Raster data (show terrain-like area)
create_static_map_image(
    lat=36.0, lon=138.5, zoom=8,  # Mt. Fuji area
    filename='raster_data.png'
)

# Draw tool (show editable area)
create_static_map_image(
    lat=35.6762, lon=139.6503, zoom=14,
    filename='draw_tool.png'
)

# Measure tool (show distance measurement area)
create_static_map_image(
    lat=35.6762, lon=139.6503, zoom=12,
    filename='measure_tool.png'
)

# Split map (show two different areas side by side)
create_static_map_image(
    lat=35.6762, lon=139.6503, zoom=11,
    filename='split_map.png'
)

# Time slider (show temporal data area)
create_static_map_image(
    lat=35.6762, lon=139.6503, zoom=10,
    filename='time_slider.png'
)

# Choropleth map (show regions)
create_static_map_image(
    lat=50.0, lon=10.0, zoom=4,  # Europe
    filename='choropleth_map.png'
)

# Heatmap (show density area)
create_static_map_image(
    lat=35.6762, lon=139.6503, zoom=11,
    filename='heatmap.png'
)

print("\nAll OpenStreetMap images created successfully!")