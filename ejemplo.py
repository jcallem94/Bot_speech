import speech_recognition as speech_recog

def speech():
    mic = speech_recog.Microphone()
    recog = speech_recog.Recognizer()

    with mic as audio_file:
        recog.adjust_for_ambient_noise(audio_file)
        audio = recog.listen(audio_file)
        return recog.recognize_google(audio, language="en-GB")
    
mic = speech_recog.Microphone()
recog = speech_recog.Recognizer()

with mic as audio_file:
    print("Por favor, hable")

    recog.adjust_for_ambient_noise(audio_file)
    audio = recog.listen(audio_file)

    print("Conversión de voz a texto...")
    print("Usted dijo: " + recog.recognize_google(audio, language="en-GB"))

