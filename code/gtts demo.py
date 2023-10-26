from gtts import gTTS                                                       # importing gTTS package
import os                                                                   # importing the in-built os function in python
f = open(r'C:\Users\fly2n\Desktop\TTS\gtts-demo.txt')                       # opening the sample text file in read mode
engine = gTTS(text = f.readline(), lang='en', tld='co.uk',slow=False)       # specifying the text input, language, accent and speed
engine.save("C:\\Users\\fly2n\\Desktop\\TTS\\gtts-demo.mp3")                # saving the converted audio file in mp3 format
os.system("start gtts-demo.mp3")                                            # playing the generated file in the default audio player



