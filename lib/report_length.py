def report_length(string):
    if string == "":
        raise StringEmptyException("String is empty") 
    if type(string) != str:
        raise TypeError("Input is not string")
    length = len(string)
    return f"This string was {length} characters long."

class StringEmptyException(Exception):
    pass
