# Convert text to speech conversion
from gtts import gTTS
# Import Os module to start the audio file
import os

# Read text from file
fh = open("test.rtf", "r", encoding="utf-8")
my_text = fh.read().replace("\n", " ")

# Init language English = en, Vietnamese = vi

# language = 'en'
language = 'vi'

output = gTTS(text=my_text, lang=language, slow=False)

# Save audio converted file
output.save("output.mp3")
fh.close()

# Play audio converted file
os.system("start output.mp3")
