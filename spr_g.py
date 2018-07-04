import speech_recognition as sr


def speak_n_go():
    sample_rate = 48000
    # Chunk is like a buffer. It stores 2048 samples (bytes of data)
    # here.
    # it is advisable to use powers of 2 such as 1024 or 2048
    chunk_size = 2048
    # Initialize the recognizer
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=sample_rate,
                       chunk_size=chunk_size) as source:
        # energy threshold based on the surrounding noise level
        r.adjust_for_ambient_noise(source)
        print("Say Something")
        # listens for the user's input
        audio = r.listen(source)

        try:
            print("okay processing")
            text = r.recognize_google(audio)
            print("you said: " + text)

        # error occurs when google could not understand what was said

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")

        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service;{0}".format(e))


def file_n_go(audio_file_path):
    with sr.AudioFile(audio_file_path) as source:
        # reads the audio file. Here we use record instead of
        # listen
        r = sr.Recognizer()
        audio = r.record(source)
    try:
        # for testing purposes, we're just using the default API key
        # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        # instead of `r.recognize_google(audio)`
        print("You said: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
