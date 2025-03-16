import speech_recognition as sr
def listen():
    """Capture voice input from the correct Bluetooth microphone"""
    recognizer = sr.Recognizer()

    # Find correct mic index
    mic_index = None
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        if "Wings Phantom Pro" in name and "Headset" in name:
            mic_index = index
            break

    if mic_index is None:
        print("Error: Could not find 'Wings Phantom Pro' microphone.")
        return None

    print(f"Using device index: {mic_index} - {sr.Microphone.list_microphone_names()[mic_index]}")

    with sr.Microphone(device_index=mic_index) as source:
        print("Listening through Wings Phantom Pro...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
        
        try:
            audio = recognizer.listen(source, timeout=None)  # ⬅️ Removed timeout
            print("Processing audio...")
            text = recognizer.recognize_google(audio).lower()
            print("Recognized:", text)  # Debugging output
            return text
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return None
        except sr.RequestError:
            print("Could not request results, check your internet connection.")
            return None
        except Exception as e:
            print("Error:", str(e))
            return None
