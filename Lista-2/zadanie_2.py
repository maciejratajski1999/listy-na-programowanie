from PIL import Image

def create_thumbnail(image_file_path, size_tuple, destination_path = "miniatura.jpg"):
    '''Tworzy miniaturę obrazka

    :param image_file_path: (str) - ścieżka do obrazka
    :param size_tuple: (tuple of integers) - rozmiary miniatury
    :param destination_path: (str) - ścieżka w której wygeneruje się miniatura

    '''
    image = Image.open(image_file_path)
    image.thumbnail(size_tuple)
    image.save(destination_path)



