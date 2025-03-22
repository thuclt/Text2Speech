# Convert text to speech conversion
from gtts import gTTS
# Import Os module to start the audio file
import os 
  
# my_text = 'Convert this Text to Speech'
my_text = 'Tôi là Nguyễn Hoàng Lương. Quê tại Hà Nội'

# Init language English = en, Vietnamese = vi

# language = 'en'
language = 'vi'


my_obj = gTTS(text=my_text, lang=language, slow=False)

# Save audio converted file
my_obj.save("output.mp3")
  
# Play audio converted file
os.system("start output.mp3") 

