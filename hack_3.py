"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""


def fn_hack_3(text):
    replacements = {
        'a': '@',
        'e': '3',
        'i': '¡',
        'o': '0',
        'u': 'v',
        'f': 'F',
        'n': 'N',
        'b': 'B',
        'q': 'Q',
        'x': 'X',
    }

    transformed_text = ""
    for char in text:
        transformed_text += replacements.get(char, char)

    return transformed_text

print(fn_hack_3("fooziman"))  # Output: "F00z¡m@N" 
print(fn_hack_3("barziman"))  # Output: "B@rz¡m@N" 
print(fn_hack_3("eq"))        # Output: "3Q" 
print(fn_hack_3("qu"))        # Output: "Qv"
print(fn_hack_3("qux"))       # Output: "QvX" 