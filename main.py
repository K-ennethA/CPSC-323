import re

regex = re.compile(r'\!.*?\!')


def isKeyword(key):
    keywords = {"int", "float", "true", "false", "if", "else", "then", "endif", "while", "whileend", "do", "doend", "for", "forend", "input", "output", "and", "or", "not", "bool"}
    if key in keywords:
        return True
    else:
        return False


def isOperator(key):
    operators = {"*", "+", "=", "/", ">", "<", "%"}
    if key in operators:
        return True
    else:
        return False


def isSeperator(key):
    seperators = {"'", "(", ")", "{", "}", "[", "]", ",", ".", ":", ";", " "}
    if key in seperators:
        return True
    else:
        return False


with open('input.txt', mode='r') as input:
    with open('output.txt', mode='w') as output:
        output.write('TOKENS Lexemes\n')
        for line in input:
            result = regex.search(line)
            if(result):
                output.write('comment\n')
            for word in line.split():
                if(isKeyword(word)):
                    output.write(f'Keyword = {word}\n')
                elif(isOperator(word)):
                    output.write(f'Operator = {word}\n')
                elif(isSeperator(word)):
                    output.write(f'Seperator = {word}\n')
