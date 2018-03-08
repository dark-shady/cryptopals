import sys
base64characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def char_to_binary(char_to_convert, original_format):
    '''
    Convert single character to 8 bit binary number.
    '''

    if original_format == "ascii":
        int_value = int(ord(char_to_convert))
    elif original_format == "hex":
        int_value = int(char_to_convert, 16)

    binary_value = ""
    for i in range(7, -1, -1):
        if int_value / 2**i < 1:
            binary_value += '0'
        else:
            binary_value += '1'
            int_value -= 2**i
    return binary_value


def binary_to_ascii_char(binary_number):
    '''
    Convert 6 bit binary number to integer by iterating from 5 to 0 and checking against 1 or 0 in binary_number in corresponding index.
    '''

    int_value = 0
    binary_number = binary_number[::-1]
    for i in range(5, -1, -1):
        if binary_number[i] == '1':
            int_value += 2**i
    return base64characters[int_value]


def string_to_binary(string_to_convert, original_format):
    '''
    Convert ascii/hex string to binary string
    '''

    binary_output = ""
    for character in string_to_convert:
        if original_format == "ascii":
            binary_output += char_to_binary(character, "ascii")
        elif original_format == "hex":
            # Only want 4 least significant bits for HEX to remove leading zeros
            binary_output += char_to_binary(character, "hex")[4:]
    return binary_output


def binary_to_base64(string_to_convert):
    '''
    Convert binary string to base64 string
    '''

    length_of_string, string_index = len(string_to_convert), 0
    base64_output = ""
    while string_index < length_of_string:
        remaining_bits = length_of_string - string_index

        if remaining_bits == 4:
            # Padding 1 character
            base64_output += binary_to_ascii_char(string_to_convert[string_index:string_index+4] + "00")
            base64_output += "="
        elif remaining_bits == 2:
            # Padding 2 characters
            base64_output += binary_to_ascii_char(string_to_convert[string_index:string_index+2] + "0000")
            base64_output += "=="
        else:
            # No padding
            base64_output += binary_to_ascii_char(string_to_convert[string_index:string_index+6])
        string_index += 6

    return base64_output


def base64(string_to_convert, original_format):
    if original_format == "ascii":
        binary_string = string_to_binary(string_to_convert, "ascii")
    elif original_format == "hex":
        binary_string = string_to_binary(string_to_convert, "hex")

    return binary_to_base64(binary_string)


def test():
    test_string2_ascii = "Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure."
    test_string2_base64 = "TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4="
    test_string2_hex = "4d616e2069732064697374696e677569736865642c206e6f74206f6e6c792062792068697320726561736f6e2c2062757420627920746869732073696e67756c61722070617373696f6e2066726f6d206f7468657220616e696d616c732c2077686963682069732061206c757374206f6620746865206d696e642c20746861742062792061207065727365766572616e6365206f662064656c6967687420696e2074686520636f6e74696e75656420616e6420696e6465666174696761626c652067656e65726174696f6e206f66206b6e6f776c656467652c2065786365656473207468652073686f727420766568656d656e6365206f6620616e79206361726e616c20706c6561737572652e"
    assert(base64(test_string2_ascii, "ascii") == test_string2_base64)
    assert(base64(test_string2_hex, "hex") == test_string2_base64)

    test_string3_ascii = "Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure"
    test_string3_base64 = "TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZQ=="
    test_string3_hex = "4d616e2069732064697374696e677569736865642c206e6f74206f6e6c792062792068697320726561736f6e2c2062757420627920746869732073696e67756c61722070617373696f6e2066726f6d206f7468657220616e696d616c732c2077686963682069732061206c757374206f6620746865206d696e642c20746861742062792061207065727365766572616e6365206f662064656c6967687420696e2074686520636f6e74696e75656420616e6420696e6465666174696761626c652067656e65726174696f6e206f66206b6e6f776c656467652c2065786365656473207468652073686f727420766568656d656e6365206f6620616e79206361726e616c20706c656173757265"
    assert(base64(test_string3_ascii, "ascii") == test_string3_base64)
    assert(base64(test_string2_hex, "hex") == test_string2_base64)

    test_string4_ascii = "Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasur"
    test_string4_base64 = "TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3Vy"
    test_string4_hex = "4d616e2069732064697374696e677569736865642c206e6f74206f6e6c792062792068697320726561736f6e2c2062757420627920746869732073696e67756c61722070617373696f6e2066726f6d206f7468657220616e696d616c732c2077686963682069732061206c757374206f6620746865206d696e642c20746861742062792061207065727365766572616e6365206f662064656c6967687420696e2074686520636f6e74696e75656420616e6420696e6465666174696761626c652067656e65726174696f6e206f66206b6e6f776c656467652c2065786365656473207468652073686f727420766568656d656e6365206f6620616e79206361726e616c20706c6561737572"
    assert(base64(test_string4_ascii, "ascii") == test_string4_base64)
    assert(base64(test_string2_hex, "hex") == test_string2_base64)

    print("Tests passed!")


if __name__ == "__main__":
    test_string_ascii = "Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure."
    test_string_base64 = "TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4="
    test_string_hex = "4d616e2069732064697374696e677569736865642c206e6f74206f6e6c792062792068697320726561736f6e2c2062757420627920746869732073696e67756c61722070617373696f6e2066726f6d206f7468657220616e696d616c732c2077686963682069732061206c757374206f6620746865206d696e642c20746861742062792061207065727365766572616e6365206f662064656c6967687420696e2074686520636f6e74696e75656420616e6420696e6465666174696761626c652067656e65726174696f6e206f66206b6e6f776c656467652c2065786365656473207468652073686f727420766568656d656e6365206f6620616e79206361726e616c20706c6561737572652e"
    if len(sys.argv) > 2:
        # Argument supplied
        if sys.argv[1].lower() not in ["hex", "ascii"]:
            print("Format: base64.py hex/ascii STRING")
            exit(1)
        print(base64(sys.argv[2], "ascii"))
    else:
        # Default to test string
        print(base64(test_string_ascii, "ascii"))
        print(base64(test_string_hex, "hex"))
        test()
