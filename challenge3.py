import cryptotools

input_string = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
input_string_binary = cryptotools.string_to_binary(input_string, "hex")

input_string_length = len(input_string)

high_score = 0
highest_decode = ""
for i in range(256):
    score = 0
    key = cryptotools.char_to_binary(i, 'decimal') * (input_string_length/2)
    xor_result = cryptotools.xor(input_string_binary,key)
    decoded = cryptotools.binary_to_ascii(xor_result)
    
    for char in decoded:
      if char.upper() in "ABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890":
          score += 1
    if score > high_score:
      high_score = score
      highest_decode = decoded
      
print(highest_decode)
