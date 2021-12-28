from csv import QUOTE_NONNUMERIC
from csv import reader as csv_reader
from os import listdir, path

from numpy import array
from PIL import Image as pil_module

ColourList = list[list]


def read_from_csv(file_name: str) -> ColourList:
    reader = csv_reader(
        open(file_name, "r", newline=""),
        delimiter=" ",
        quotechar='"',
        quoting=QUOTE_NONNUMERIC,
    )
    return [row for row in reader]


def get_list_of_files_recursively(directory_name: str) -> list[str]:
    """
    Get list of all files within directory and its subdirectories by
    recursively iterating through all entities within directory
    :param directory_name: directory to form list of files from
    :return: list of all filenames
    """
    listOfFile = listdir(directory_name)
    allFiles = []
    # Iterate over all the entries
    for entry in listOfFile:
        fullPath = path.join(directory_name, entry)
        if path.isdir(fullPath):
            allFiles += get_list_of_files_recursively(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles


def read_from_folder(folder_path: str) -> ColourList:
    paths_to_images = get_list_of_files_recursively(folder_path)
    images_data = (pil_module.open(path).getdata() for path in paths_to_images)
    return [item for sublist in images_data for item in array(sublist)]


def read_from_single_image(image_path: str) -> ColourList:
    return list(pil_module.open(image_path).getdata())


def read_dataset(path_to_dataset: str) -> ColourList:
    if path.isdir(path_to_dataset):
        return read_from_folder(path_to_dataset)
    file_extension = path_to_dataset.split(".")[-1]
    if file_extension == "csv":
        return read_from_csv(path_to_dataset)
    elif file_extension in ("png", "jpg", "jpeg", "tiff"):
        read_from_single_image(path_to_dataset)
    else:
        raise TypeError(
            f"Wrong dataset provided!"
            f"{path_to_dataset} is neither folder nor correct file "
            f"format (must be one of ('png', 'jpg', 'jpeg', 'tiff'))"
        )
