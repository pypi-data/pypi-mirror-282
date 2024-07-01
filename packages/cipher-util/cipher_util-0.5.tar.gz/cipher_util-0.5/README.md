# Caesar Cipher API

## Overview
This project implements a simple API using Flask for encrypting and decrypting text using the Caesar cipher.

## Files
- `caesar_cipher.py`: Contains the `CaesarCipher` class for text encryption and decryption.
- `cipher_tool.py`: Utilizes the `CaesarCipher` class to provide a ciphering function.
- `cipher_api.py`: Flask application for exposing the ciphering functionality as a web API.

## Usage
1. **Start the Flask server:**

2. **Access the API using a web browser or curl:**
   - **Endpoint:** http://localhost:5000/
   - **Method:** GET
   - **Parameters (as JSON):**
     ```json
     {
         "string": "Hello Data Engineers",
         "key": 3,
         "encrypt": true
     }
     ```

3. **Examples:**
   - **Encrypt text:**
     ```
     http://localhost:5000/?params={"string":"Hello Data Engineers","key":3,"encrypt":true}
     ```
   - **Decrypt text:**
     ```
     http://localhost:5000/?params={"string":"KHOOR GDWD HPSOHUHV","key":3,"encrypt":false}
     ```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or support, contact me at omarshaker212@gmail.com.
