def is_palindrome(input_string):
    """
    Check if an input string is a palindrome (reads the same backward as forward)

    Args:
        input_string (str): The input string.

    Returns:
        True if the input string is a palindrome, otherwise False.
    """
    input_string = str(input_string).lower().replace(" ", "")
    return input_string == input_string[::-1]


def remove_spaces(input_string):
    """
    Removes spaces from an input string using list comprehension.

    Args:
        input_string (str): The input string.

    Returns:
        A list containing the remaining characters.
    """
    return [char for char in input_string if char != ' ']


def count_characters(input_string):
    """
    Counts the occurrences of each character from an input string (case-insensitive).

    Args:
        input_string (str): The input string.

    Returns:
        dictionary: A dictionary where keys are characters and values are their occurrences.
    """
    dictionary = {}
    for char in input_string:
        dictionary[char] = dictionary.get(char, 0) + 1

    return dictionary
