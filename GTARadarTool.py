from PIL import Image
import os

def combine_tiles(tiles, tile_width, tile_height, output_file):
    # Compute the maximum x and y values to determine the grid size
    max_x = max(tile["x"] for tile in tiles)
    max_y = max(tile["y"] for tile in tiles)

    # Create a blank image with the appropriate size
    combined_image = Image.new("RGB", (tile_width * max_x, tile_height * max_y))

    for tile in tiles:
        try:
            # Open the image file
            img = Image.open(tile["file"])
            # Paste it into the correct position in the combined image
            combined_image.paste(
                img, ((tile["x"] - 1) * tile_width, (tile["y"] - 1) * tile_height)
            )
        except Exception as e:
            print(f"Error processing file {tile['file']}: {e}")

    # Save the combined image
    combined_image.save(output_file)
    print("Radar exported successfully")

if __name__ == "__main__":
    size = 512
    tiles = [
	{"x": 1, "y": 0, "file": 'img/radar00.png'},
	{"x": 2, "y": 0, "file": 'img/radar01.png'},
	{"x": 3, "y": 0, "file": 'img/radar02.png'},
	{"x": 4, "y": 0, "file": 'img/radar03.png'},
	{"x": 5, "y": 0, "file": 'img/radar04.png'},
	{"x": 6, "y": 0, "file": 'img/radar05.png'},
	{"x": 7, "y": 0, "file": 'img/radar06.png'},
	{"x": 8, "y": 0, "file": 'img/radar07.png'},
	{"x": 9, "y": 0, "file": 'img/radar08.png'},
	{"x": 10, "y": 0, "file": 'img/radar09.png'},
	{"x": 11, "y": 0, "file": 'img/radar10.png'},
	{"x": 12, "y": 0, "file": 'img/radar11.png'},
	{"x": 1, "y": 1, "file": 'img/radar12.png'},
	{"x": 2, "y": 1, "file": 'img/radar13.png'},
	{"x": 3, "y": 1, "file": 'img/radar14.png'},
	{"x": 4, "y": 1, "file": 'img/radar15.png'},
	{"x": 5, "y": 1, "file": 'img/radar16.png'},
	{"x": 6, "y": 1, "file": 'img/radar17.png'},
	{"x": 7, "y": 1, "file": 'img/radar18.png'},
	{"x": 8, "y": 1, "file": 'img/radar19.png'},
	{"x": 9, "y": 1, "file": 'img/radar20.png'},
	{"x": 10, "y": 1, "file": 'img/radar21.png'},
	{"x": 11, "y": 1, "file": 'img/radar22.png'},
	{"x": 12, "y": 1, "file": 'img/radar23.png'},
	{"x": 1, "y": 2, "file": 'img/radar24.png'},
	{"x": 2, "y": 2, "file": 'img/radar25.png'},
	{"x": 3, "y": 2, "file": 'img/radar26.png'},
	{"x": 4, "y": 2, "file": 'img/radar27.png'},
	{"x": 5, "y": 2, "file": 'img/radar28.png'},
	{"x": 6, "y": 2, "file": 'img/radar29.png'},
	{"x": 7, "y": 2, "file": 'img/radar30.png'},
	{"x": 8, "y": 2, "file": 'img/radar31.png'},
	{"x": 9, "y": 2, "file": 'img/radar32.png'},
	{"x": 10, "y": 2, "file": 'img/radar33.png'},
	{"x": 11, "y": 2, "file": 'img/radar34.png'},
	{"x": 12, "y": 2, "file": 'img/radar35.png'},
	{"x": 1, "y": 3, "file": 'img/radar36.png'},
	{"x": 2, "y": 3, "file": 'img/radar37.png'},
	{"x": 3, "y": 3, "file": 'img/radar38.png'},
	{"x": 4, "y": 3, "file": 'img/radar39.png'},
	{"x": 5, "y": 3, "file": 'img/radar40.png'},
	{"x": 6, "y": 3, "file": 'img/radar41.png'},
	{"x": 7, "y": 3, "file": 'img/radar42.png'},
	{"x": 8, "y": 3, "file": 'img/radar43.png'},
	{"x": 9, "y": 3, "file": 'img/radar44.png'},
	{"x": 10, "y": 3, "file": 'img/radar45.png'},
	{"x": 11, "y": 3, "file": 'img/radar46.png'},
	{"x": 12, "y": 3, "file": 'img/radar47.png'},
	{"x": 1, "y": 4, "file": 'img/radar48.png'},
	{"x": 2, "y": 4, "file": 'img/radar49.png'},
	{"x": 3, "y": 4, "file": 'img/radar50.png'},
	{"x": 4, "y": 4, "file": 'img/radar51.png'},
	{"x": 5, "y": 4, "file": 'img/radar52.png'},
	{"x": 6, "y": 4, "file": 'img/radar53.png'},
	{"x": 7, "y": 4, "file": 'img/radar54.png'},
	{"x": 8, "y": 4, "file": 'img/radar55.png'},
	{"x": 9, "y": 4, "file": 'img/radar56.png'},
	{"x": 10, "y": 4, "file": 'img/radar57.png'},
	{"x": 11, "y": 4, "file": 'img/radar58.png'},
	{"x": 12, "y": 4, "file": 'img/radar59.png'},
	{"x": 1, "y": 5, "file": 'img/radar60.png'},
	{"x": 2, "y": 5, "file": 'img/radar61.png'},
	{"x": 3, "y": 5, "file": 'img/radar62.png'},
	{"x": 4, "y": 5, "file": 'img/radar63.png'},
	{"x": 5, "y": 5, "file": 'img/radar64.png'},
	{"x": 6, "y": 5, "file": 'img/radar65.png'},
	{"x": 7, "y": 5, "file": 'img/radar66.png'},
	{"x": 8, "y": 5, "file": 'img/radar67.png'},
	{"x": 9, "y": 5, "file": 'img/radar68.png'},
	{"x": 10, "y": 5, "file": 'img/radar69.png'},
	{"x": 11, "y": 5, "file": 'img/radar70.png'},
	{"x": 12, "y": 5, "file": 'img/radar71.png'},
	{"x": 1, "y": 6, "file": 'img/radar72.png'},
	{"x": 2, "y": 6, "file": 'img/radar73.png'},
	{"x": 3, "y": 6, "file": 'img/radar74.png'},
	{"x": 4, "y": 6, "file": 'img/radar75.png'},
	{"x": 5, "y": 6, "file": 'img/radar76.png'},
	{"x": 6, "y": 6, "file": 'img/radar77.png'},
	{"x": 7, "y": 6, "file": 'img/radar78.png'},
	{"x": 8, "y": 6, "file": 'img/radar79.png'},
	{"x": 9, "y": 6, "file": 'img/radar80.png'},
	{"x": 10, "y": 6, "file": 'img/radar81.png'},
	{"x": 11, "y": 6, "file": 'img/radar82.png'},
	{"x": 12, "y": 6, "file": 'img/radar83.png'},
	{"x": 1, "y": 7, "file": 'img/radar84.png'},
	{"x": 2, "y": 7, "file": 'img/radar85.png'},
	{"x": 3, "y": 7, "file": 'img/radar86.png'},
	{"x": 4, "y": 7, "file": 'img/radar87.png'},
	{"x": 5, "y": 7, "file": 'img/radar88.png'},
	{"x": 6, "y": 7, "file": 'img/radar89.png'},
	{"x": 7, "y": 7, "file": 'img/radar90.png'},
	{"x": 8, "y": 7, "file": 'img/radar91.png'},
	{"x": 9, "y": 7, "file": 'img/radar92.png'},
	{"x": 10, "y": 7, "file": 'img/radar93.png'},
	{"x": 11, "y": 7, "file": 'img/radar94.png'},
	{"x": 12, "y": 7, "file": 'img/radar95.png'},
	{"x": 1, "y": 8, "file": 'img/radar96.png'},
	{"x": 2, "y": 8, "file": 'img/radar97.png'},
	{"x": 3, "y": 8, "file": 'img/radar98.png'},
	{"x": 4, "y": 8, "file": 'img/radar99.png'},
	{"x": 5, "y": 8, "file": 'img/radar100.png'},
	{"x": 6, "y": 8, "file": 'img/radar101.png'},
	{"x": 7, "y": 8, "file": 'img/radar102.png'},
	{"x": 8, "y": 8, "file": 'img/radar103.png'},
	{"x": 9, "y": 8, "file": 'img/radar104.png'},
	{"x": 10, "y": 8, "file": 'img/radar105.png'},
	{"x": 11, "y": 8, "file": 'img/radar106.png'},
	{"x": 12, "y": 8, "file": 'img/radar107.png'},
	{"x": 1, "y": 9, "file": 'img/radar108.png'},
	{"x": 2, "y": 9, "file": 'img/radar109.png'},
	{"x": 3, "y": 9, "file": 'img/radar110.png'},
	{"x": 4, "y": 9, "file": 'img/radar111.png'},
	{"x": 5, "y": 9, "file": 'img/radar112.png'},
	{"x": 6, "y": 9, "file": 'img/radar113.png'},
	{"x": 7, "y": 9, "file": 'img/radar114.png'},
	{"x": 8, "y": 9, "file": 'img/radar115.png'},
	{"x": 9, "y": 9, "file": 'img/radar116.png'},
	{"x": 10, "y": 9, "file": 'img/radar117.png'},
	{"x": 11, "y": 9, "file": 'img/radar118.png'},
	{"x": 12, "y": 9, "file": 'img/radar119.png'},
	{"x": 1, "y": 10, "file": 'img/radar120.png'},
	{"x": 2, "y": 10, "file": 'img/radar121.png'},
	{"x": 3, "y": 10, "file": 'img/radar122.png'},
	{"x": 4, "y": 10, "file": 'img/radar123.png'},
	{"x": 5, "y": 10, "file": 'img/radar124.png'},
	{"x": 6, "y": 10, "file": 'img/radar125.png'},
	{"x": 7, "y": 10, "file": 'img/radar126.png'},
	{"x": 8, "y": 10, "file": 'img/radar127.png'},
	{"x": 9, "y": 10, "file": 'img/radar128.png'},
	{"x": 10, "y": 10, "file": 'img/radar129.png'},
	{"x": 11, "y": 10, "file": 'img/radar130.png'},
	{"x": 12, "y": 10, "file": 'img/radar131.png'},
	{"x": 1, "y": 11, "file": 'img/radar132.png'},
	{"x": 2, "y": 11, "file": 'img/radar133.png'},
	{"x": 3, "y": 11, "file": 'img/radar134.png'},
	{"x": 4, "y": 11, "file": 'img/radar135.png'},
	{"x": 5, "y": 11, "file": 'img/radar136.png'},
	{"x": 6, "y": 11, "file": 'img/radar137.png'},
	{"x": 7, "y": 11, "file": 'img/radar138.png'},
	{"x": 8, "y": 11, "file": 'img/radar139.png'},
	{"x": 9, "y": 11, "file": 'img/radar140.png'},
	{"x": 10, "y": 11, "file": 'img/radar141.png'},
	{"x": 11, "y": 11, "file": 'img/radar142.png'},
	{"x": 12, "y": 11, "file": 'img/radar143.png'}
    ]
    dest = "img_out/radar.png"

    print("Radar-merger started")
    combine_tiles(tiles, size, size, dest)
