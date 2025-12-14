from PIL import Image
from django.core.files.base import ContentFile
from io import BytesIO
import uuid, math, re, os

def Update_file(file, type, fileuuid, folder='post/'):
    ext = file.name.split('.')[-1].lower()
    new_name = f"{fileuuid}.webp" if type == 'Image' else f"{fileuuid}.{ext}"
    full_path = folder + "image/" + new_name if type == "Image" else folder + "video/" + new_name

    if type == "Image":
        img = Image.open(file)

        if img.mode not in ("RGB", "RGBA"):
            img = img.convert("RGB")

        img_w = img.width - 100 if img.width > 300 else img.width - 50
        img_h = img.height - 100 if img.height > 300 else img.height - 50
        img.thumbnail((img_w, img_h))

        buffer = BytesIO()
        img.save(buffer, format=img.format or 'JPEG')
        file_content = ContentFile(buffer.getvalue())
        return full_path, file_content
    
    else:
        return full_path, file


def calculate_read_time(text, wpm=200):
    """
    Calculate the estimated reading time for a given text.
    :param text: The text to calculate the reading time for.
    :param wpm: Words per minute (default is 200).
    :return: Estimated reading time in minutes.
    """
    words = re.findall(r'\w+', text)
    word_count = len(words)
    read_time_mins = math.ceil(word_count / wpm)
    
    return read_time_mins