from gtts import gTTS
from pygame import mixer

def text_to_speech(text, lang = 'en'):
    myobj = gTTS(text=text, lang=lang, slow=False)
    myobj.save("welcome.mp3")
    mixer.init()

    mixer.music.load("welcome.mp3")
    mixer.music.play()

    while mixer.music.get_busy():
        pass

if __name__ == "__main__":
    girdi_text = input("Seslendirmek istediğiniz metni giriniz:")
    text_dili = input("Seslendirmek istediğinizin dilin kodunu giriniz:")

    text_to_speech(girdi_text, lang=text_dili)
