"""
generic script

text: "fooziman" output => "oozima" 
text: "barziman" output => "arzima" 
text: "qux" output => "qux" 
"""


def fn_hack_4(texto):
    if len(texto) > 3:
        return texto[1:-1]
    else:
        return texto


print(fn_hack_4("fooziman"))  # Output: "oozima"
print(fn_hack_4("barziman"))  # Output: "arzima"
print(fn_hack_4("qux")) # Output: "qux"S
