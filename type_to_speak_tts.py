import os
import subprocess
from googletrans import Translator, LANGUAGES
from gtts import gTTS, lang as gtts_langs
import pygame
import time

# Function to install packages
def install_package(package_name):
    try:
        subprocess.check_call([os.sys.executable, '-m', 'pip', 'install', package_name])
    except subprocess.CalledProcessError as e:
        print(f"Failed to install package: {package_name}")
        print(e)
        return False
    return True

# Check and install required packages
def check_and_install_packages():
    packages = {
        'googletrans': 'googletrans==4.0.0-rc1',
        'gtts': 'gtts',
        'pygame': 'pygame'
    }
    
    for package, install_name in packages.items():
        while True:
            try:
                __import__(package)
                print(f"Module '{package}' is already installed.")
                break
            except ImportError:
                print(f"Module '{package}' is not installed. Attempt to install...")
                if install_package(install_name):
                    print(f"Module '{package}' installed successfully!")
                    break
                else:
                    print(f"Failed to install module '{package}', try again.")
                    user_input = input(f"Type 'y' to continue or 'n' to stop installation: ").strip().lower()
                    if user_input == 'n':
                        print(f"Abandon installation of module '{package}', exiting the program.")
                        exit()

# Function to select language
def select_language():
    supported_languages = sorted(set(gtts_langs.tts_langs().keys()).intersection(set(LANGUAGES.keys())))
    print("Please select a language:")
    for i, lang_code in enumerate(supported_languages, 1):
        print(f"{i}. {LANGUAGES[lang_code].title()} ({lang_code})")
    
    while True:
        choice = input("Select a language by number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(supported_languages):
            return supported_languages[int(choice) - 1]
        else:
            print("Invalid input, please try again.")

# Function to translate text
def translate_text(text, target_language_code):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=target_language_code)
        return translated.text
    except Exception as e:
        print(f"Translation failed: {e}")
        return None

# Function to translate and speak using gTTS
def translate_and_speak_gtts(text, target_language_code):
    translated_text = translate_text(text, target_language_code)
    if translated_text is None:
        return
    
    print(f"Translated text ({LANGUAGES[target_language_code]}): {translated_text}")
    
    tts = gTTS(text=translated_text, lang=target_language_code)
    
    # Save gTTS audio to a file
    mp3_filename = "temp.mp3"
    tts.save(mp3_filename)
    
    # Play MP3 file using pygame
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_filename)
    pygame.mixer.music.play()
    
    # Wait until the audio finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    # Unload and delete the MP3 file
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()  # Unload the file
    os.remove(mp3_filename)  # Delete the file

# Main loop
def main():
    check_and_install_packages()
    
    while True:
        # Select language
        target_language_code = select_language()
        
        # User input
        user_input = input("Enter the text you want to translate: ")
        
        # Translate and TTS
        translate_and_speak_gtts(user_input, target_language_code)

if __name__ == "__main__":
    main()
