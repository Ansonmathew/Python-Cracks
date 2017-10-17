# Import pyttsx
import pyttsx

#create connection 
engine = pyttsx.init()
engine.say('Hello from Python...')
# play
engine.runAndWait()
