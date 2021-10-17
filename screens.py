from PIL import Image, ImageOps
import os
# Inspired with
# https://medium.com/geekculture/create-your-screenshots-for-the-stores-with-python-and-pil-c11e0dc8c07d
# https://pypi.org/project/ScreenshotFormat/
print('Started')
# sources_dir strucuture must be EXACT to {dir}/{iphone|ipad}/{lc}, example: directory/ipad/en
sources_dir = "test/sources"
results_dir = "test/results"
# background for padded areas
bg_path = 'test/bg1.jpg'

# https://help.apple.com/app-store-connect/#/devd1093d90d
# For iPhone, screenshots for 6.5-inch iPhone Xs Max and 5.5-inch devices (iPhone 6s Plus, iPhone 7 Plus, iPhone 8 Plus) are required. These screenshots will scale down for smaller device sizes.
# For iPad, screenshots for 12.9-inch iPad Pro (2nd generation) and 12.9-inch iPad Pro (3rd generation) are required. These screenshots will scale down for smaller device sizes.
#
# https://help.apple.com/app-store-connect/#/dev4e413fcb8
# dimensions are from here: 6,5", 5,5", iPad 12,9pro (2,3 gen are the same) tuples of (height, width)

resolutions =  { "iphone": [
                    (2778, 1284), (2208, 1242)
                  ],
                  "ipad":  [
                    (2732, 2048)
                  ] 
                }

def listdir(path):
  return [f for f in os.listdir(path) if not f.startswith('.')]


def save_screenshot(img, path, file_name):
  try:
    os.makedirs(path)
  except IOError:
    pass
  img.save(f"{path}/{file_name}")
 

for platform in listdir(sources_dir):
  platform_dir = f"{sources_dir}/{platform}"
  lc_folders = listdir(platform_dir)
  print(f"Performing {platform}")
  for lc in lc_folders:
    images_dir = f"{platform_dir}/{lc}"
    print(f"reading images in {images_dir}")
    images = listdir(images_dir)
    for image in images: 
      f = f"{images_dir}/{image}"
      i = 0
      for height, width  in resolutions[platform]:
        try:
          screenshot = Image.open(f)
          # bg =  ImageOps.fit(Image.open('test/bg1.jpg'), (width, height))
          bg =  Image.open(bg_path)
          fitted =  ImageOps.contain(screenshot, (width, height))
          fwidth, fheight = fitted.size
          # orange background empty image
          processed_image = Image.new('RGBA', (width, height), color=(232, 106, 28))
          processed_image.paste(bg)
          processed_image.paste(fitted, (int(width/2 - fwidth/2), int(height/2 - fheight/2)))
          save_screenshot(processed_image, f"{results_dir}/{platform}/{lc}/{height}x{width}/", file_name=f"{platform}_{lc}_{height}x{width}_{image}")
          i += 1
        except IOError:
          print(f"Error in processing")
print('Finished')