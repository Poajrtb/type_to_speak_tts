import os
import subprocess
from googletrans import Translator, LANGUAGES
from gtts import gTTS
import pygame
import time

# 모듈 설치 함수
def install_package(package_name):
    try:
        subprocess.check_call([os.sys.executable, '-m', 'pip', 'install', package_name])
    except subprocess.CalledProcessError as e:
        print(f"패키지 설치 실패: {package_name}")
        print(e)
        return False
    return True

# 모듈 확인 및 설치
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
                    print(f"Module '{package}' installed complete!")
                    break
                else:
                    print(f"Failed to install module '{package}', try again.")
                    user_input = input(f"Type 'y' to continue or 'n' to stop installation: ").strip().lower()
                    if user_input == 'n':
                        print(f"Abandon installation of module '{package}', exit the program.")
                        exit()

# 언어 선택 함수
def select_language():
    print("Please select a language:")
    print("1. Korean")
    print("2. Japanese")
    print("3. English")
    print("4. Chinese")
    print("5. Russian")
    print("6. Spanish")
    print("7. Polish")
    print("8. Nepali")
    print("9. British English")
    print("10. French")
    print("11. Portuguese")
    
    while True:
        choice = input("Select (1/2/3/4/5/6/7/8/9/10/11): ")
        if choice in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]:
            return int(choice)
        else:
            print("Invalid input, please try again.")

# 번역 함수
def translate_text(text, target_language_code):
    translator = Translator()
    try:
        translated = translator.translate(text, dest=target_language_code)
        return translated.text
    except Exception as e:
        print(f"Translation failed: {e}")
        return None

# gTTS를 사용한 번역 및 TTS 출력 함수
def translate_and_speak_gtts(text, target_language_code):
    translated_text = translate_text(text, target_language_code)
    if translated_text is None:
        return
    
    print(f"Translated text ({LANGUAGES[target_language_code]}): {translated_text}")
    
    tts = gTTS(text=translated_text, lang=target_language_code)
    
    # gTTS 음성을 파일로 저장
    mp3_filename = "temp.mp3"
    tts.save(mp3_filename)
    
    # pygame을 사용하여 MP3 파일 재생
    pygame.mixer.init()
    pygame.mixer.music.load(mp3_filename)
    pygame.mixer.music.play()
    
    # 음성이 끝날 때까지 대기
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    # MP3 파일 언로드 및 삭제
    pygame.mixer.music.stop()
    pygame.mixer.music.unload()  # 파일 언로드
    os.remove(mp3_filename)  # 파일 삭제

# 메인 루프
def main():
    check_and_install_packages()
    
    while True:
        # 언어 선택
        language_choice = select_language()
        # 언어 코드 매핑
        language_codes = {1: 'ko', 2: 'ja', 3: 'en', 4: 'zh-cn', 5: 'ru', 6: 'es', 7: 'pl', 8: 'ne', 9: 'en', 10: 'fr', 11: 'pt'}
        target_language_code = language_codes[language_choice]
        
        # 사용자 입력
        user_input = input("Enter the text you want to translate: ")
        
        # 번역 및 TTS
        translate_and_speak_gtts(user_input, target_language_code)

if __name__ == "__main__":
    main()
