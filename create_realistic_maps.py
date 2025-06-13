#!/usr/bin/env python3
"""
Create realistic-looking map images using matplotlib
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Circle, Rectangle, Polygon
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import os

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

def create_map_background(ax, extent=None):
    """Create a map-like background with coastlines and grid"""
    if extent is None:
        extent = [-180, 180, -90, 90]
    
    ax.set_xlim(extent[0], extent[1])
    ax.set_ylim(extent[2], extent[3])
    
    # Add grid
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # Add some land masses (simplified continents)
    # Africa
    africa = Polygon([(-20, 35), (50, 35), (50, -35), (20, -35), (-20, 0)], 
                     facecolor='#e8dcc6', edgecolor='#666666', linewidth=1)
    ax.add_patch(africa)
    
    # Europe
    europe = Polygon([(-10, 70), (40, 70), (40, 35), (-10, 35)], 
                     facecolor='#e8dcc6', edgecolor='#666666', linewidth=1)
    ax.add_patch(europe)
    
    # Asia
    asia = Polygon([(40, 70), (180, 70), (180, 0), (100, 0), (40, 35)], 
                   facecolor='#e8dcc6', edgecolor='#666666', linewidth=1)
    ax.add_patch(asia)
    
    # North America
    north_america = Polygon([(-170, 70), (-50, 70), (-50, 10), (-120, 10), (-170, 30)], 
                           facecolor='#e8dcc6', edgecolor='#666666', linewidth=1)
    ax.add_patch(north_america)
    
    # South America
    south_america = Polygon([(-80, 10), (-35, 10), (-35, -55), (-70, -55), (-80, -20)], 
                           facecolor='#e8dcc6', edgecolor='#666666', linewidth=1)
    ax.add_patch(south_america)
    
    # Australia
    australia = Polygon([(110, -10), (155, -10), (155, -45), (110, -45)], 
                       facecolor='#e8dcc6', edgecolor='#666666', linewidth=1)
    ax.add_patch(australia)
    
    # Set ocean color
    ax.set_facecolor('#c6e2ff')

def create_japan_background(ax):
    """Create a simplified Japan map background"""
    ax.set_xlim(125, 150)
    ax.set_ylim(25, 50)
    ax.grid(True, alpha=0.3, linestyle='--')
    
    # Main islands (very simplified)
    # Honshu
    honshu = Polygon([(130, 33), (141, 33), (141.5, 38), (140, 41), (136, 37), (130, 35)], 
                     facecolor='#e8dcc6', edgecolor='#666666', linewidth=1)
    ax.add_patch(honshu)
    
    # Hokkaido
    hokkaido = Polygon([(140, 42), (146, 42), (146, 45.5), (140, 45.5)], 
                       facecolor='#e8dcc6', edgecolor='#666666', linewidth=1)
    ax.add_patch(hokkaido)
    
    # Kyushu
    kyushu = Polygon([(129, 31), (132, 31), (132, 34), (129, 34)], 
                     facecolor='#e8dcc6', edgecolor='#666666', linewidth=1)
    ax.add_patch(kyushu)
    
    # Shikoku
    shikoku = Polygon([(132.5, 32.5), (134.5, 32.5), (134.5, 34), (132.5, 34)], 
                      facecolor='#e8dcc6', edgecolor='#666666', linewidth=1)
    ax.add_patch(shikoku)
    
    ax.set_facecolor('#c6e2ff')

def create_tokyo_street_map(ax):
    """Create a simplified Tokyo street map"""
    ax.set_xlim(139.5, 139.8)
    ax.set_ylim(35.6, 35.75)
    ax.grid(True, alpha=0.2, linestyle='--')
    
    # Background
    ax.set_facecolor('#f5f5f5')
    
    # Major roads (simplified)
    roads = [
        [(139.5, 35.68), (139.8, 35.68)],  # Horizontal road
        [(139.65, 35.6), (139.65, 35.75)],  # Vertical road
        [(139.55, 35.6), (139.75, 35.75)],  # Diagonal road
        [(139.75, 35.6), (139.55, 35.75)],  # Another diagonal
    ]
    
    for road in roads:
        ax.plot([road[0][0], road[1][0]], [road[0][1], road[1][1]], 
                color='#ffffff', linewidth=4, zorder=1)
        ax.plot([road[0][0], road[1][0]], [road[0][1], road[1][1]], 
                color='#cccccc', linewidth=3, zorder=2)
    
    # Parks (green areas)
    parks = [
        Circle((139.7, 35.69), 0.01, facecolor='#90EE90', edgecolor='#228B22'),
        Circle((139.62, 35.66), 0.008, facecolor='#90EE90', edgecolor='#228B22'),
    ]
    for park in parks:
        ax.add_patch(park)
    
    # Water (river)
    river_x = np.linspace(139.5, 139.8, 100)
    river_y = 35.63 + 0.02 * np.sin(10 * (river_x - 139.5))
    ax.fill_between(river_x, river_y - 0.005, river_y + 0.005, 
                    color='#87CEEB', alpha=0.7, edgecolor='#4682B4')

def save_map(fig, filename, title):
    """Save map with title"""
    plt.title(title, fontsize=16, pad=20)
    plt.tight_layout()
    plt.savefig(f'images/{filename}', dpi=100, bbox_inches='tight', facecolor='white')
    plt.close()
    print(f"Created: images/{filename}")

# 1. Basic Map (World view)
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
create_map_background(ax)
ax.plot(0, 30, 'bo', markersize=8)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
save_map(fig, 'basic_map.png', 'Basic Interactive Map')

# 2. Tokyo centered map
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
create_tokyo_street_map(ax)
ax.plot(139.6503, 35.6762, 'ro', markersize=12)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
save_map(fig, 'tokyo_map.png', 'Map Centered on Tokyo')

# 3. Sized map
fig, ax = plt.subplots(1, 1, figsize=(8, 5))
create_tokyo_street_map(ax)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
save_map(fig, 'sized_map.png', 'Map with Custom Size')

# 4. OpenStreetMap basemap
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
create_tokyo_street_map(ax)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
save_map(fig, 'osm_basemap.png', 'OpenStreetMap Basemap')

# 5. Multiple basemaps
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
create_tokyo_street_map(ax)
# Add some styling to simulate different basemap
ax.set_facecolor('#e8e8e8')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
save_map(fig, 'multiple_basemaps.png', 'Multiple Basemaps')

# 6. Custom tile layer (London)
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.set_xlim(-0.3, 0.05)
ax.set_ylim(51.4, 51.6)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_facecolor('#f5f5f5')
# Thames river
river_x = np.linspace(-0.3, 0.05, 100)
river_y = 51.5 + 0.02 * np.sin(15 * (river_x + 0.15))
ax.fill_between(river_x, river_y - 0.01, river_y + 0.01, 
                color='#87CEEB', alpha=0.7, edgecolor='#4682B4')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
save_map(fig, 'custom_tile_layer.png', 'Custom Tile Layer')

# 7. Map with markers
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
create_tokyo_street_map(ax)
# Tokyo Station
ax.plot(139.6503, 35.6762, 'ro', markersize=10, label='東京駅')
# Tokyo Tower
ax.plot(139.7454, 35.6586, 'ro', markersize=10, label='東京タワー')
# Skytree
ax.plot(139.7967, 35.7148, 'ro', markersize=10, label='スカイツリー')
ax.legend()
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
save_map(fig, 'markers_map.png', 'Map with Markers')

# 8. GeoJSON data (New York)
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.set_xlim(-74.1, -73.9)
ax.set_ylim(40.65, 40.8)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_facecolor('#f5f5f5')
# Manhattan island
manhattan = Polygon([(-74.02, 40.7), (-73.97, 40.7), (-73.93, 40.78), (-73.95, 40.8), (-74.01, 40.77)], 
                   facecolor='#e8dcc6', edgecolor='#666666', linewidth=1)
ax.add_patch(manhattan)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
save_map(fig, 'geojson_data.png', 'GeoJSON Data Visualization')

# 9. Shapefile data (World)
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
create_map_background(ax)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
save_map(fig, 'shapefile_data.png', 'Shapefile Data Visualization')

# 10. Raster data (Mt. Fuji area - use contours)
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.set_xlim(138, 139)
ax.set_ylim(35.5, 36.5)
# Create elevation-like data
x = np.linspace(138, 139, 50)
y = np.linspace(35.5, 36.5, 50)
X, Y = np.meshgrid(x, y)
# Simulate Mt. Fuji elevation
Z = 3000 * np.exp(-((X-138.5)**2 + (Y-36.0)**2)*10)
contour = ax.contourf(X, Y, Z, levels=10, cmap='terrain')
plt.colorbar(contour, ax=ax, label='Elevation (m)')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
save_map(fig, 'raster_data.png', 'Raster Data Visualization')

# 11. Draw tool
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
create_tokyo_street_map(ax)
# Add drawn polygon
polygon = Polygon([(139.64, 35.67), (139.66, 35.68), (139.67, 35.67), (139.65, 35.66)], 
                 facecolor='blue', alpha=0.3, edgecolor='blue', linewidth=2)
ax.add_patch(polygon)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
save_map(fig, 'draw_tool.png', 'Drawing Tool Interface')

# 12. Measure tool
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
create_tokyo_street_map(ax)
# Add measurement line
ax.plot([139.6403, 139.6603], [35.6762, 35.6762], 'g-', linewidth=2)
ax.plot([139.6403, 139.6603], [35.6762, 35.6762], 'go', markersize=8)
# Add distance label
ax.text(139.6503, 35.678, '2.2 km', ha='center', va='bottom', 
        bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
save_map(fig, 'measure_tool.png', 'Measurement Tool Interface')

# 13. Split map
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
create_tokyo_street_map(ax1)
ax1.set_title('Terrain View')
create_tokyo_street_map(ax2)
ax2.set_facecolor('#e8e8e8')
ax2.set_title('Satellite View')
plt.suptitle('Split Screen Map', fontsize=16, y=1.02)
plt.tight_layout()
plt.savefig('images/split_map.png', dpi=100, bbox_inches='tight', facecolor='white')
plt.close()
print("Created: images/split_map.png")

# 14. Time slider
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
create_tokyo_street_map(ax)
# Add time indicator
ax.text(0.5, 0.02, 'Time: 2024-01-01 12:00', transform=ax.transAxes, 
        ha='center', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
save_map(fig, 'time_slider.png', 'Time Slider Interface')

# 15. Japan cities map
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
create_japan_background(ax)
# Add major cities
cities = {
    '東京': (139.6503, 35.6762),
    '大阪': (135.5023, 34.6937),
    '名古屋': (136.9066, 35.1815),
    '札幌': (141.3469, 43.0642),
    '福岡': (130.4017, 33.5904),
    '仙台': (140.8694, 38.2682),
    '広島': (132.4553, 34.3853),
    '京都': (135.7681, 35.0116)
}
for city, (lon, lat) in cities.items():
    ax.plot(lon, lat, 'ro', markersize=8)
    ax.text(lon, lat + 0.5, city, ha='center', va='bottom', fontsize=10)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
save_map(fig, 'japan_cities_map.png', 'Major Cities of Japan')

# 16. Choropleth map (Europe)
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
ax.set_xlim(-10, 30)
ax.set_ylim(35, 60)
ax.grid(True, alpha=0.3, linestyle='--')
ax.set_facecolor('#c6e2ff')
# European countries (simplified)
countries = [
    Polygon([(-10, 36), (-6, 42), (0, 43), (0, 36)], facecolor='#ff9999'),  # Spain
    Polygon([(0, 42), (8, 45), (8, 36), (0, 36)], facecolor='#99ff99'),     # France
    Polygon([(7, 47), (15, 47), (15, 42), (7, 42)], facecolor='#9999ff'),   # Italy
    Polygon([(5, 52), (15, 52), (15, 47), (5, 47)], facecolor='#ffff99'),   # Germany
]
for country in countries:
    ax.add_patch(country)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
save_map(fig, 'choropleth_map.png', 'Choropleth Map')

# 17. Heatmap
fig, ax = plt.subplots(1, 1, figsize=(8, 6))
create_tokyo_street_map(ax)
# Generate heatmap data
np.random.seed(42)
n_points = 100
x = np.random.normal(139.6503, 0.05, n_points)
y = np.random.normal(35.6762, 0.05, n_points)
# Create heatmap
heatmap, xedges, yedges = np.histogram2d(x, y, bins=20, range=[[139.5, 139.8], [35.6, 35.75]])
extent = [xedges[0], xedges[-1], yedges[0], yedges[-1]]
im = ax.imshow(heatmap.T, extent=extent, origin='lower', cmap='hot', alpha=0.6, aspect='auto')
plt.colorbar(im, ax=ax, label='Density')
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
save_map(fig, 'heatmap.png', 'Heat Map Visualization')

print("\nAll realistic map images created successfully!")