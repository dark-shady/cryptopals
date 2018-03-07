import sys
base64characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def ascii_char_to_binary(ascii_char):
    '''
    Convert single ascii character to 8 bit binary number.
    '''

    int_value = int(ord(ascii_char))
    binary_value = ""
    for i in range(7, -1, -1):
        if int_value / 2**i < 1:
            binary_value += '0'
        else:
            binary_value += '1'
            int_value -= 2**i
    return binary_value


def binary_to_int(binary_number):
    '''
    Convert 6 bit binary number to integer be iterating from 5 to 0 and checking against 1 or 0 in binary_number in corresponding index.
    '''

    int_value = 0
    binary_number = binary_number[::-1]
    for i in range(5, -1, -1):
        if binary_number[i] == '1':
            int_value += 2**i
    return int_value


def three_char_to_binary(three_char_string):
    '''
    Convert a string that is 3 characters long to a 24 bit binary number.
    '''

    if three_char_string[1] == '\0':
        # 2 character padding
        return ascii_char_to_binary(three_char_string[0]) + '0000\0' + '\0'
    elif three_char_string[2] == '\0':
        # 1 character padding
        return ascii_char_to_binary(three_char_string[0]) + ascii_char_to_binary(three_char_string[1]) + '00\0'
    else:
        # 0 character padding
        return ascii_char_to_binary(three_char_string[0]) + ascii_char_to_binary(three_char_string[1]) + ascii_char_to_binary(three_char_string[2])


def tribinary_to_quadint(tri_octet_binary):
    '''
    Input 24 bit binary number, split it into four 6 bit chunks, and find integer value of the each 6 bit chunk.
    '''

    if tri_octet_binary[12] == '\0':
        # 2 character padding
        return (binary_to_int(tri_octet_binary[0:6]), binary_to_int(tri_octet_binary[6:12]), '\0', '\0')
    elif tri_octet_binary[18] == '\0':
        # 1 character padding
        return(binary_to_int(tri_octet_binary[0:6]), binary_to_int(tri_octet_binary[6:12]), binary_to_int(tri_octet_binary[12:18]), '\0')
    else:
        return(binary_to_int(tri_octet_binary[0:6]), binary_to_int(tri_octet_binary[6:12]), binary_to_int(tri_octet_binary[12:18]), binary_to_int(tri_octet_binary[18:24]))


def quadint_to_ascii(ascii_int):
    return base64characters[ascii_int]


def base64(string_to_convert):
    index_of_string, string_length = 0, len(string_to_convert)
    output_string = ""
    while string_length > index_of_string:

        if string_length - index_of_string <= 4:
            chars_left = string_length - index_of_string
            three_character_slice = string_to_convert[index_of_string:index_of_string+chars_left] + '\0'*(3 - chars_left)
        else:
            # Grab next three characters
            three_character_slice = string_to_convert[index_of_string:index_of_string+4]

        # Convert three characters to binary, convert to 24 bit binary to four 6 bit, convert each 6 bit into an ascii int
        quadint = tribinary_to_quadint(three_char_to_binary(three_character_slice))

        for ascii_int in quadint:
            if ascii_int == '\0':
                output_string += '='
            else:
                output_string += quadint_to_ascii(ascii_int)
        index_of_string += 3
    return output_string


def test():
    test_string2 = "Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure."
    test_string2_base64 = "TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4="
    assert(base64(test_string2) == test_string2_base64)

    test_string3 = "Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure"
    test_string3_base64 = "TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZQ=="
    assert(base64(test_string3) == test_string3_base64)

    test_string4 = "Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasur"
    test_string4_base64 = "TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3Vy"
    assert(base64(test_string4) == test_string4_base64)

    print("Tests passed!")


if __name__ == "__main__":
    test_string = "Man is distinguished, not only by his reason, but by this singular passion from other animals, which is a lust of the mind, that by a perseverance of delight in the continued and indefatigable generation of knowledge, exceeds the short vehemence of any carnal pleasure."
    test_string_base64 = "TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4="

    print(base64(test_string))
    test()
