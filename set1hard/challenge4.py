import cryptotools

def find_xor(input_string):
  input_string_binary = cryptotools.string_to_binary(input_string, "hex")
  
  input_string_length = len(input_string)
  
  high_score = 0
  highest_decode = ""
  for i in range(256):
      score = 0
      key = cryptotools.char_to_binary(i, 'decimal') * int((input_string_length / 2))
      xor_result = cryptotools.xor(input_string_binary,key)
      decoded = cryptotools.binary_to_ascii(xor_result)
      
      for char in decoded:
        if char.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890":
            score += 1
      if score > high_score:
        high_score = score
        highest_decode = decoded
        
  return highest_decode
  
with open("file.txt") as f:
    high_score = 0
    highest_decode = ""
    for line in f:
        score = 0
        decoded = find_xor(line.rstrip('\n'))
        for char in decoded:
          if char.upper() in "ETAOIN SHRDLU":
            score += 2
          if char.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890":
            score += 1
          if score > high_score:
            high_score = score
            highest_decode = decoded
            print(highest_decode)
    print(highest_decode)
