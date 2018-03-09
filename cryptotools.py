base64characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def repeating_key_xor(string_to_convert, key):
    output = ""
    i = 0
    for c in string_to_convert:
        c_binary = string_to_binary(c, "ascii")
        output += xor(c_binary, string_to_binary(key[i % len(key)],"ascii")) + " "
        i += 1
        
    return output

def binary_to_hex(string_to_convert):
    """
    Convert binary string to HEX string
    Args:
        string_to_convert (string): binary string
    Returns:
        string of HEX values with no spaces
    """
    return ''.join('{0:02x}'.format(int(a, 2)) for a in string_to_convert.split())

def binary_to_ascii(string_to_convert):
    """
    Convert binary string to ASCII string
    Args:
        string_to_convert (string): binary string
    Returns:
        ascii_string (string): ASCII string
    """
    
    length_of_string, string_index = len(string_to_convert), 0
    ascii_string = ""
    
    while string_index < length_of_string:
        ascii_string += binary_to_ascii_char(string_to_convert[string_index:string_index+8])
        string_index += 8
    return ascii_string

def binary_to_ascii_char(binary_string):
    """
    Convert 8 bit binary number to ASCII character
    Args:
        binary_string (string): 8 bit binary string
    Returns:
        ascii_char (chr): ASCII character
    """
    int_value = 0
    binary_string = binary_string[::-1]
    for i in range(7, -1, -1):
        if binary_string[i] == '1':
            int_value += 2**i
    return chr(int_value)
    
def char_to_binary(char_to_convert, original_format):
    """
    Convert single character to 8 bit binary number
    Args:
        char_to_convert (string): single character
        original_format (string): original format of the character (HEX/ASCII)
    Returns:
        binary_value (string): 8 bit binary number
    """

    if original_format == "ascii":
        int_value = int(ord(char_to_convert))
    elif original_format == "hex":
        int_value = int(char_to_convert, 16)
    elif original_format == "decimal":
        int_value = int(char_to_convert)
        
    binary_value = ""
    for i in range(7, -1, -1):
        if int_value / 2**i < 1:
            binary_value += '0'
        else:
            binary_value += '1'
            int_value -= 2**i
    return binary_value


def binary_to_base64_char(binary_number):
    """
    Convert 6 bit binary number to base64 character
    Args:
        binary_number (string): 6 bit binary number
    Returns:
        base64characters (string): binary_number converted to base64 character
    """

    int_value = 0
    binary_number = binary_number[::-1]
    for i in range(5, -1, -1):
        if binary_number[i] == '1':
            int_value += 2**i
    return base64characters[int_value]


def string_to_binary(string_to_convert, original_format):
    """
    Convert ascii/hex string to binary string
    Args:
        string_to_convert (string): ASCII/HEX string
        original_format (string): original format of the string (HEX/ASCII)
    Returns:
        binary_output (string): string_to_convert converted to a string of binary numbers
    """

    binary_output = ""
    for character in string_to_convert:
        if original_format == "ascii":
            binary_output += char_to_binary(character, "ascii")
        elif original_format == "hex":
            # Only want 4 least significant bits for HEX to remove leading zeros
            binary_output += char_to_binary(character, "hex")[4:]
    return binary_output


def binary_to_base64(string_to_convert):
    """
    Convert binary string to base64 string
    Args:
        string_to_convert (string): a string of binary numbers
    Returns:
        base64_output (string): string_to_convert converted to a string of base64 characters
    """

    length_of_string, string_index = len(string_to_convert), 0
    base64_output = ""
    while string_index < length_of_string:
        remaining_bits = length_of_string - string_index

        if remaining_bits == 4:
            # Padding 1 character
            base64_output += binary_to_base64_char(string_to_convert[string_index:string_index+4] + "00")
            base64_output += "="
        elif remaining_bits == 2:
            # Padding 2 characters
            base64_output += binary_to_base64_char(string_to_convert[string_index:string_index+2] + "0000")
            base64_output += "=="
        else:
            # No padding
            base64_output += binary_to_base64_char(string_to_convert[string_index:string_index+6])
        string_index += 6

    return base64_output


def base64(string_to_convert, original_format):
    """
    Main function.  Decides how to convert string based on input of the string's original format
    Args:
        string_to_convert (string): ASCII/HEX string
        original_format (string): original format of the string (HEX/ASCII)
    Returns:
        String of base64 characters
    """

    if original_format == "ascii":
        binary_string = string_to_binary(string_to_convert, "ascii")
    elif original_format == "hex":
        binary_string = string_to_binary(string_to_convert, "hex")

    return binary_to_base64(binary_string)


def xor(string1, string2):
    """
    Take two binary strings and XOR them
    Args:
        string1 (string): binary string
        string2 (string): binary string
    Returns:
        A binary string of the XOR results of string1 and string2
 
    Raises:
        TypeError: string1 and string2 are not equal size
    """
    string_length = len(string1)
    if string_length != len(string2):
        raise TypeError('string1 and string2 must be the same size')

    i = 0
    xor_result = ""
    while i < string_length:
      if string1[i] == string2[i]:
        xor_result += '0'
      elif string1[i] == '1' or string2[i] == '1':
        xor_result += '1'
      i +=1
    return xor_result
