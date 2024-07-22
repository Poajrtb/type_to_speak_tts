import os
import subprocess
import pygame
import time
from googletrans import Translator, LANGUAGES
from gtts import gTTS, lang as gtts_langs
import pyperclip

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

# Function to display a message using pygame
def show_message(message):
    pygame.init()
    screen = pygame.display.set_mode((400, 200))
    pygame.display.set_caption("Message")
    
    font = pygame.font.Font(None, 36)
    text_surface = font.render(message, True, (255, 255, 255))
    screen.fill((0, 0, 0))
    screen.blit(text_surface, (50, 80))
    pygame.display.update()
    
    # Display the message for 2 seconds
    time.sleep(2)
    
    pygame.quit()

# Function to translate and speak using gTTS
def translate_and_speak_gtts(text, target_language_code):
    translated_text = translate_text(text, target_language_code)
    if translated_text is None:
        return
    
    print(f"Translated text ({LANGUAGES[target_language_code]}): {translated_text}")
    
    # Copy translated text to clipboard
    pyperclip.copy(translated_text)
    print("Translated text has been copied to clipboard.")
    
    # Show message using pygame
    show_message("복사가 되었습니다")
    
    print("To exit the program, press Ctrl+C.")
    
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
    try:
        while True:
            # Select language
            target_language_code = select_language()
            
            # User input
            user_input = input("Enter the text you want to translate: ")
            
            # Translate and TTS
            translate_and_speak_gtts(user_input, target_language_code)
    except KeyboardInterrupt:
        print("\nProgram exited by user.")

if __name__ == "__main__":
    main()
