def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    #first attempt:
    # reversed_phrase = ""
    # for letter in reversed(phrase):
    #     reversed_phrase += letter
    # return reversed_phrase

    #better version, via slice notation:
    return phrase[::-1]
