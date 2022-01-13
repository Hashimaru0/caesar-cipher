# Caesar Cipher
It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.\
The simple script can be used to scramble/descramble text files.

![alt text](https://upload.wikimedia.org/wikipedia/commons/4/4a/Caesar_cipher_left_shift_of_3.svg)
## Usage

```python
import string
# get all characters
all_alphabets = (string.ascii_uppercase, string.ascii_lowercase, string.punctuation)
# scramble is True to scramble and False to descramble, shift is number of letters down the alphabet 
scramble(scramble, shift, all_alphabets)
```