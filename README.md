# translator
📝 Simple Text Translator (using googletrans)
This is a basic Python program that translates user input text into English using the googletrans library.

📋 Requirements
Python 3.x

googletrans==4.0.0-rc1

To install the required library, run:
pip install googletrans==4.0.0-rc1

🚀 How It Works
The program asks the user to input some text.

It uses Google Translate API (through the googletrans library) to translate the text into English.

Finally, it prints the translated text.

🧩 Code Example
from googletrans import Translator
translator = Translator()
txt = input("Write here: ")
output = translator.translate(txt, dest='en')
print(output.text)

🌟 Usage Example

Write here: Hola amigo
Hello friend

⚠️ Notes
Make sure you have a working internet connection.

Sometimes googletrans may throw errors if Google updates its backend API.

If you face import errors, use the correct version:
pip install googletrans==4.0.0-rc1

📚 Future Improvements
Add a simple GUI using Tkinter.

Allow users to select both source and target languages.

📌 Author
Developed with ❤️ using Python by Aryan Kumar Ojha

