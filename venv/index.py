from PIL import Image, ImageFile
import glob
import PIL.Image
PIL.Image.MAX_IMAGE_PIXELS = 933120000
ImageFile.LOAD_TRUNCATED_IMAGES = True


types = ("*.png","*.jpg","*.jpeg","*.gif","*jfif")
files_grabbed = []

for files in types:
    files_grabbed.extend(glob.glob(files))

print(f"Finded files: {len(files_grabbed)}")

for i in files_grabbed:
    img = Image.open(i)
   
    if img.height > 1 or img.width > 1:
        output_size = (1600, 1400)
        img.thumbnail(output_size)
        img.save(f"output/{i}")