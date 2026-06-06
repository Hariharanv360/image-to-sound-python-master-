from PIL import Image
from gtts import gTTS
from pytesseract import image_to_string
import pytesseract

# If Tesseract is not in PATH, explicitly set the path to tesseract.exe
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_sound(path_to_image):
    """
    Function for converting an image to sound
    """
    try:
        loaded_image = Image.open(path_to_image)
        decoded_text = image_to_string(loaded_image)
        cleaned_text = " ".join(decoded_text.split("\n"))
        print(cleaned_text)

        if not cleaned_text.strip():
            raise ValueError("No text found in image.")

        sound = gTTS(cleaned_text, lang="en")
        sound.save("sound.mp3")
        print("Sound saved as sound.mp3")
        return True
    except Exception as bug:
        print("The bug thrown while executing the code:\n", bug)
        return False


if __name__ == "__main__":
    image_to_sound("image.jpg")
    input("Press Enter to exit...")
from PIL import Image
from gtts import gTTS
from pytesseract import image_to_string
import pytesseract

# If Tesseract is not in PATH, explicitly set the path to tesseract.exe
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_sound(path_to_image):
    """
    Function for converting an image to sound
    """
    try:
        loaded_image = Image.open(path_to_image)
        decoded_text = image_to_string(loaded_image)
        cleaned_text = " ".join(decoded_text.split("\n"))
        print(cleaned_text)

        if not cleaned_text.strip():
            raise ValueError("No text found in image.")

        sound = gTTS(cleaned_text, lang="en")
        sound.save("sound.mp3")
        print("Sound saved as sound.mp3")
        return True
    except Exception as bug:
        print("The bug thrown while executing the code:\n", bug)
        return False


if __name__ == "__main__":
    image_to_sound("image.jpg")
    input("Press Enter to exit...")
