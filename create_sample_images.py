#!/usr/bin/env python3
"""
Create sample placeholder images for Leafmap tutorial
"""

from PIL import Image, ImageDraw, ImageFont
import os

# Create images directory if it doesn't exist
os.makedirs('images', exist_ok=True)

# Define image information
images = [
    ('basic_map.png', '基本的な地図', 'Basic interactive map'),
    ('tokyo_map.png', '東京中心の地図', 'Map centered on Tokyo'),
    ('sized_map.png', 'サイズ設定済み地図', 'Map with custom size'),
    ('osm_basemap.png', 'OpenStreetMapベースマップ', 'OpenStreetMap basemap'),
    ('multiple_basemaps.png', '複数ベースマップ', 'Multiple basemaps'),
    ('custom_tile_layer.png', 'カスタムタイルレイヤー', 'Custom tile layer'),
    ('markers_map.png', 'マーカー付き地図', 'Map with markers'),
    ('geojson_data.png', 'GeoJSONデータ', 'GeoJSON data visualization'),
    ('shapefile_data.png', 'Shapefileデータ', 'Shapefile data visualization'),
    ('raster_data.png', 'ラスターデータ', 'Raster data visualization'),
    ('draw_tool.png', '描画ツール', 'Drawing tool interface'),
    ('measure_tool.png', '測定ツール', 'Measurement tool interface'),
    ('split_map.png', '分割画面マップ', 'Split screen map'),
    ('time_slider.png', 'タイムスライダー', 'Time slider interface'),
    ('japan_cities_map.png', '日本の主要都市マップ', 'Major cities of Japan'),
    ('choropleth_map.png', 'コロプレスマップ', 'Choropleth map'),
    ('heatmap.png', 'ヒートマップ', 'Heat map visualization'),
]

# Create each image
for filename, title_jp, title_en in images:
    # Create a new image with light gray background
    img = Image.new('RGB', (800, 600), color='#f0f0f0')
    draw = ImageDraw.Draw(img)
    
    # Draw a border
    draw.rectangle([10, 10, 790, 590], outline='#333333', width=2)
    
    # Draw a map-like background
    # Draw grid lines
    for x in range(50, 750, 50):
        draw.line([(x, 50), (x, 550)], fill='#cccccc', width=1)
    for y in range(50, 550, 50):
        draw.line([(50, y), (750, y)], fill='#cccccc', width=1)
    
    # Add some map-like elements
    # Draw a "coastline"
    draw.arc([100, 150, 300, 350], 0, 180, fill='#0066cc', width=3)
    draw.arc([400, 200, 600, 400], 45, 225, fill='#0066cc', width=3)
    
    # Add some "markers" for maps that should have them
    if 'marker' in filename or 'cities' in filename:
        marker_positions = [(200, 250), (350, 300), (500, 280), (550, 350)]
        for pos in marker_positions:
            draw.ellipse([pos[0]-10, pos[1]-10, pos[0]+10, pos[1]+10], fill='#ff0000', outline='#800000')
    
    # Add text
    try:
        # Try to use a better font if available
        font_title = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", 36)
        font_subtitle = ImageFont.truetype("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", 24)
    except:
        # Fall back to default font
        font_title = ImageFont.load_default()
        font_subtitle = ImageFont.load_default()
    
    # Draw title background
    draw.rectangle([0, 0, 800, 100], fill='#333333')
    
    # Draw titles (use simple text without anchor for compatibility)
    # English subtitle only (to avoid Japanese encoding issues)
    text_bbox = draw.textbbox((0, 0), title_en, font=font_subtitle)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    draw.text((400 - text_width//2, 50 - text_height//2), title_en, fill='white', font=font_subtitle)
    
    # Add Leafmap logo placeholder
    draw.rectangle([720, 520, 780, 580], fill='#4CAF50', outline='#2E7D32', width=2)
    lm_bbox = draw.textbbox((0, 0), 'LM', font=font_subtitle)
    lm_width = lm_bbox[2] - lm_bbox[0]
    lm_height = lm_bbox[3] - lm_bbox[1]
    draw.text((750 - lm_width//2, 550 - lm_height//2), 'LM', fill='white', font=font_subtitle)
    
    # Save the image
    img.save(f'images/{filename}')
    print(f'Created: images/{filename}')

print("\nAll sample images created successfully!")