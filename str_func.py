def capitalize_string(input_string):
    """
    Takes a string as input and returns it in all uppercase letters.

    Parameters:
    - input_string (str): The input string.

    Returns:
    - str: The input string in uppercase.
    """
    return input_string.upper()

def capitalize_words(input_string):
    """
    Capitalizes the first letter of each word in the input string.

    :param input_string: The input string.
    :return: The input string with the first letter of each word capitalized.
    """
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

