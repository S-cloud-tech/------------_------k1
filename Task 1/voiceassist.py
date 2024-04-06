import speech_recognition as sr
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"You said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        print("Sorry, I didn't get that. Please try again.")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

def main():
    speak("Hello! I am your voice assistant. How can I help you?")
    
    while True:
        query = listen()

        if "hello" in query:
            speak("Hello! How can I assist you?")
        elif "goodbye" in query:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("I'm sorry, I didn't understand that. Please try again.")

if __name__ == "__main__":
    main()
