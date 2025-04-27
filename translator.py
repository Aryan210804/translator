from googletrans import Translator

translator = Translator()
txt = input("Write here: ")
output = translator.translate(txt, dest='en')
print(output.text)
