
with open('sample.text', mode='') as my_file:


def isKeyord(key):
    keywords = {"int", "float", "true", "false", "if", "else", "then", "endif", "while", "whileend", "do", "doend", "for", "forend", "input", "output", "and", "or", "not", "bool"}
    if key in keywords:
        return true
    else:
        return false


def isOperator(key):
    operators = {"*", "+", "=", "/", ">", "<", "%"}
    if key in operators:
        return true
    else:
        return false


def isSeperator(key):
    seperators = {"'", "(", ")", "{", "}", "[", "]", ",", ".", ":", ";", " "}
    if key in seperators:
        return true
    else:
        return false
