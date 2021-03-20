from flask import Flask
from string import ascii_lowercase

app = Flask(__name__)


@app.route('/encode/<text>/<int:shift>')
def encode(text, shift):
    encoded_text = ''
    for i in text:
        if i.lower() in ascii_lowercase:
            if i.isupper():
                encoded_text += ascii_lowercase[(ascii_lowercase.index(i.lower()) + shift)
                                                % len(ascii_lowercase)].upper()
            else:
                encoded_text += ascii_lowercase[(ascii_lowercase.index(i.lower()) + shift)
                                                % len(ascii_lowercase)]
        else:
            encoded_text += i
    return {'encoded_text': encoded_text}


@app.route('/decode/<text>/<int:shift>')
def decode(text, shift):
    encoded_text = ''
    for i in text:
        if i.lower() in ascii_lowercase:
            if i.isupper():
                encoded_text += ascii_lowercase[(ascii_lowercase.index(i.lower()) - shift + len(ascii_lowercase))
                                                % len(ascii_lowercase)].upper()
            else:
                encoded_text += ascii_lowercase[(ascii_lowercase.index(i.lower()) - shift + len(ascii_lowercase))
                                                % len(ascii_lowercase)]
        else:
            encoded_text += i
    return {'encoded_text': encoded_text}


if __name__ == '__main__':
    app.run(debug=True)
