import cryptotools

string1 = "1c0111001f010100061a024b53535009181c"
string2 = "686974207468652062756c6c277320657965"
expected = "746865206b696420646f6e277420706c6179"

string1_binary = cryptotools.string_to_binary(string1, "hex")
string2_binary = cryptotools.string_to_binary(string2, "hex")
expected_binary = cryptotools.string_to_binary(expected, "hex")

xor_result = cryptotools.xor(string1_binary, string2_binary)
assert(xor_result == expected_binary)
