from flask import Flask, render_template, request, jsonify
from cipher_util.cipher_tool import caesar_text_cipher
import json

cipher_api = Flask(__name__)  # Initialize Flask Application

@cipher_api.route('/')
def caesar_ciphering():
    params = request.args.get('params')  # Get query param from URL 

    if params is None:
        return jsonify({'ERROR': 'No params provided'}), 400  # Bad request

    try:
        dict_ = json.loads(params)  # Convert raw JSON object to python dictionary
    except json.JSONDecodeError as error:
        return jsonify({'ERROR': str(error)}), 400  # Bad request

    # Get values associated with the keys
    text = dict_.get('string')
    key = dict_.get('key')
    crypt_bool = dict_.get('encrypt')

    # Check if the text was provided
    if text is None:
        return jsonify({'ERROR': 'There is no text provided to cipher'}), 400  # Bad request (invalid parameters)

    if key is not None:
        try:
            key = int(key)
        except ValueError:
            return jsonify({'ERROR': 'Key must be an integer'}), 400  # Bad request

    ciphered = caesar_text_cipher(text , key=key , encrypt=crypt_bool)  # Encrypt/decrypt text

    return jsonify(ciphered)  # Return JSON response wrapped in dict

if __name__ == '__main__':
    cipher_api.run(debug=True)
