__author__ = u'james.morris'
import speech_recognition as sr
import os

if __name__ == u"__main__":
    accuracy = 75.0
    filePath = os.getcwd() + os.sep + u"testdata" + os.sep
    fileTranscribe = "test.wav"

    r = sr.Recognizer()
    with sr.WavFile(fileTranscribe) as source:  # use "test.wav" as the audio source
        audio = r.record(source)  # extract audio data from the file

    try:
        list = r.recognize(audio, True)  # generate a list of possible transcriptions

        print(u"Possible transcriptions:")

        for prediction in list:
            if (prediction[u"confidence"] * 100) > accuracy:
                print(" " + prediction[u"text"] + u" (" + str(prediction[u"confidence"] * 100) + u"%)")

    except LookupError:  # speech is unintelligible
        print(u"Could not understand audio")
