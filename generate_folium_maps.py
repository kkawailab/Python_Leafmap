#!/usr/bin/env python3
"""
Generate map images using folium (HTML) and then convert to images
"""

import folium
import os

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)
os.makedirs('html_maps', exist_ok=True)

# Function to create and save folium map
def create_folium_map(lat, lon, zoom, markers=None, filename='map.html', title='Map'):
    """Create a folium map and save as HTML"""
    
    # Create map
    m = folium.Map(location=[lat, lon], zoom_start=zoom)
    
    # Add markers if provided
    if markers:
        for marker in markers:
            folium.Marker(
                [marker['lat'], marker['lon']],
                popup=marker.get('label', ''),
                tooltip=marker.get('label', '')
            ).add_to(m)
    
    # Save map
    m.save(f'html_maps/{filename}')
    print(f"Created: html_maps/{filename}")
    
    # Create a note file about the map
    note_filename = filename.replace('.html', '_info.txt')
    with open(f'images/{note_filename}', 'w') as f:
        f.write(f"Map: {title}\n")
        f.write(f"Center: {lat}, {lon}\n")
        f.write(f"Zoom: {zoom}\n")
        if markers:
            f.write(f"Markers: {len(markers)}\n")
            for marker in markers:
                f.write(f"  - {marker.get('label', 'Unnamed')}: {marker['lat']}, {marker['lon']}\n")

# Generate basic map (World view)
create_folium_map(
    lat=30, lon=0, zoom=2,
    filename='basic_map.html',
    title='Basic Interactive Map'
)

# Generate Tokyo centered map
create_folium_map(
    lat=35.6762, lon=139.6503, zoom=10,
    filename='tokyo_map.html',
    title='Map Centered on Tokyo'
)

# Generate sized map
create_folium_map(
    lat=35.6762, lon=139.6503, zoom=11,
    filename='sized_map.html',
    title='Map with Custom Size'
)

# Generate OpenStreetMap basemap
create_folium_map(
    lat=35.6762, lon=139.6503, zoom=12,
    filename='osm_basemap.html',
    title='OpenStreetMap Basemap'
)

# Generate map with markers
markers = [
    {'lat': 35.6762, 'lon': 139.6503, 'label': '東京駅'},
    {'lat': 35.6586, 'lon': 139.7454, 'label': '東京タワー'},
    {'lat': 35.7148, 'lon': 139.7967, 'label': 'スカイツリー'}
]
create_folium_map(
    lat=35.6762, lon=139.6503, zoom=11,
    markers=markers,
    filename='markers_map.html',
    title='Map with Markers'
)

# Generate Japan cities map
japan_markers = [
    {'lat': 35.6762, 'lon': 139.6503, 'label': '東京'},
    {'lat': 34.6937, 'lon': 135.5023, 'label': '大阪'},
    {'lat': 35.1815, 'lon': 136.9066, 'label': '名古屋'},
    {'lat': 43.0642, 'lon': 141.3469, 'label': '札幌'},
    {'lat': 33.5904, 'lon': 130.4017, 'label': '福岡'},
    {'lat': 38.2682, 'lon': 140.8694, 'label': '仙台'},
    {'lat': 34.3853, 'lon': 132.4553, 'label': '広島'},
    {'lat': 35.0116, 'lon': 135.7681, 'label': '京都'}
]
create_folium_map(
    lat=36.5, lon=138.0, zoom=5,
    markers=japan_markers,
    filename='japan_cities_map.html',
    title='Major Cities of Japan'
)

print("\nAll folium maps created successfully!")
print("\nNote: The HTML maps have been created in the 'html_maps' directory.")
print("To view them as images, you would need to:")
print("1. Open each HTML file in a browser")
print("2. Take screenshots")
print("3. Save them in the images directory")
print("\nAlternatively, we'll create better placeholder images with map-like appearance.")