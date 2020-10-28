from pytesseract import image_to_string
import os
from PIL.Image import open as opener
from urllib.parse import quote_plus as urlsafe

# CONSTANTS
INPUT_DIR = "/Users/sumuk/Desktop"
RUNNING_LIST = []


def process_text(path_to_img):
    im = opener(path_to_img)
    text = image_to_string(im)
    return text.replace('\n', ' ')

def directory_scanner():
    global INPUT_DIR
    global RUNNING_LIST
    path = INPUT_DIR
    files = (file for file in os.listdir(path)
             if os.path.isfile(os.path.join(path, file)))
    for file in files:
        RUNNING_LIST.append(file)


def url_maker_and_saver(text):
    global INPUT_DIR
    text = f'[{text}](https://google.com/search?q={urlsafe(str(text))})'
    with open(INPUT_DIR + '/' + 'links.md', "a+") as f:
        f.write(text + '\n\n')


def main():
    global RUNNING_LIST
    directory_scanner()
    try:
        RUNNING_LIST.remove('.localized')
        RUNNING_LIST.remove('.DS_Store')
        RUNNING_LIST.remove('links.md')
    except ValueError:
        pass

    for i in RUNNING_LIST:
        i = INPUT_DIR + '/' + i
        url_maker_and_saver(process_text(i))



if __name__ == "__main__":
    main()
