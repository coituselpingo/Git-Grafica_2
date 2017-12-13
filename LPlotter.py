
def turtle_sentence(expresion):
    carry = ""
    for letter in expresion:
        if letter == "F" or letter == "+" or letter == "-" or letter == "[" or letter == "]":
            carry += letter
        else:
            pass

    return carry



def LPlotter(expresion, angle, legth):

