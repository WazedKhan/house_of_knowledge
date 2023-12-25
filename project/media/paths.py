import os


def get_image_path(instance, filename):
    clean_filename = os.path.basename(filename)  # Get clean filename
    return f"image/{instance.uid}/{clean_filename}"  # Construct path within the 'image' directory
