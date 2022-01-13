import string

#== Scrambles txt1 to txt2 OR descrambles txt2 ===#

def scramble(scramble, shift, alphabets):
  shift = shift % 26
  text = ''
  file_to_open = 'txt1.txt' if scramble else 'txt2.txt'
  
  with open(file_to_open, 'r') as f:
    text = f.read()

  def shiftAlphabet(alph): # Shifts each character group
    return alph[shift:] + alph[:shift]
  
  shifted_alphabets = tuple(map(shiftAlphabet, alphabets)) # Maps every alphabet
  
  alphabets = ''.join(alphabets)
  shifted_alphabets = ''.join(shifted_alphabets)

  if(scramble): # If scramble or descramble
    table = str.maketrans(alphabets, shifted_alphabets)
  else:
    table = str.maketrans(shifted_alphabets, alphabets)

  scrambled_text = text.translate(table) # Scrambles/descrambles it

  with open('txt2.txt', 'w') as f:
    f.write(scrambled_text)

all_alphabets = (string.ascii_uppercase, string.ascii_lowercase, string.punctuation)
scramble(True, 5, all_alphabets)

