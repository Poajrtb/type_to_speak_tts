# VB-Audio Virtual Apps

## Download and Install VB-Cable:

**Download link:** https://vb-audio.com/Cable/

1. From the VB-Cable Download page, download the VB-Cable.
2. Run and install the downloaded file.
3. Set VB-Cable as the default audio device:
   - In Windows, navigate to Control Panel > Hardware and Sound > Sound.
   - On the Play tab, set VB-Cable as the default device.

## Discord Settings:

1. Open Discord and click User Settings (tooth wheel icon).
2. Go to the Voice and Video section.
3. On the input device, select VB-Cable.

## Enable Stereo Mix:

1. Go to Control Panel > Hardware and Sound > Sound.
2. On the Recording tab, locate and enable the Stereo Mix. If it is not listed, you can make it visible by right-clicking in a blank space and selecting Show Disabled Devices.
3. In Discord, go to Voice and Video and set the input device to Stereo Mix.

## Alternative Method: Using an Audio Mixer or a Hardware Mixer

You can use a hardware mixer or audio mixer to mix multiple audio sources and enter them into Discord, which requires hardware and setup, and physical equipment.

One of the methods above (VB-Cable or Stereo Mix) is generally a more accessible and software-based solution.

## Audio Mixer Software

To play audio input through a microphone, you may need the following audio mixer software:

1. **VB-Audio Cable:**
   - VB-Cable provides a virtual audio cable to route audio.
   - Install VB-Cable to send sound output to a virtual cable.

2. **Soundflower (Mac only):**
   - Soundflower is a software for macOS that allows routing audio to a virtual device.
   - Download and install Soundflower.

3. **Loopback (Mac only):**
   - Loopback provides more powerful features and allows routing audio to a virtual device on macOS.
   - Download and install Loopback.

4. **Audio Switcher:**
   - Audio Switcher is a utility for Windows that makes it easy to switch between audio devices.
   - Download and install Audio Switcher.

These software tools help you set the audio output to a virtual device, allowing you to capture the audio in your Python code and use it as a microphone input.

## Discord Settings

To use the audio captured by pyaudio as the microphone input in Discord, you need to install and configure a virtual audio cable software like VB-Audio Cable or Voicemeeter.

1. **VB-Audio Cable Setup:**
   - Download and install VB-Audio Cable from the official website.
   - In Sound Settings, set the Playback device to CABLE Input and the Recording device to CABLE Output.
   - In Discord, go to User Settings > Voice & Video and set the Input Device to CABLE Output.

2. **Voicemeeter Setup:**
   - Download and install Voicemeeter from the official website.
   - In Voicemeeter, set the Hardware Input to VB-Audio Cable.
   - Set the Virtual Input as the Input Device in Discord.

How to use it

1.Please install python 3.8+
2.Please install pip install -r requirements.txt
3.open type_to_speak_tts.py
Enjoy!
