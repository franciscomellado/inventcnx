from PIL import Image


def resize_image(image_path):
    img = Image.open(image_path)
    if img.height > 250 or img.width > 250:
        output_size = (250, 250)
        img.thumbnail(output_size)
        img.save(image_path)
