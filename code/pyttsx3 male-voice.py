import pyttsx3                                                                  # importing the pyttsx3 library
engine = pyttsx3.init()                                                         # invokes the pyttsx3.Engine instance
f = open(r'C:\Users\fly2n\Desktop\TTS\male-voice-demo.txt')                     # opening a sample text file in read mode
s = f.readlines()                                                               # reading the text line-by-line
engine.setProperty('rate',160)                                                  # setting the speech rate
engine.setProperty('volume','50')                                               # setting the speech volume
voices = engine.getProperty('voices')                                           # importing voices from pyttsx3
engine.setProperty('voice', voices[0].id)                                       # index '0' indicates male voice
engine.say(s)                                                                   # getting a direct voice output
engine.save_to_file(s,'C:\\Users\\fly2n\\Desktop\\TTS\\male-voice-demo.mp3')    # saving as an mp3 file
engine.runAndWait()                                                             # executing the complete program




