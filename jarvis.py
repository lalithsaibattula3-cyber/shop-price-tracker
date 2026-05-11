import google.generativeai as genai
import pyttsx3

# Gemini API key
genai.configure(api_key="AIzaSyBQSvpoUkYoZFWexywjrC49UShmKflNs_I")

# Load model
model="gemini-1.5-flash-8b"

# Voice engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 170)


def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()


print("Jarvis AI Started 😎")

while True:
    user = input("You: ")

    if user.lower() == "exit":
        speak("Goodbye Lalith!")
        break

    try:
        response = model.generate_content(user)
        reply = response.text

        print("Jarvis:", reply)
        speak(reply)

    except Exception as e:
        print("Error:", e)


