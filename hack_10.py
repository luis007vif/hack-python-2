"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_9(s):
    dictionary = {}
    for key, value in s.items():
        if key == "foo":
            new_value = value.capitalize().replace("k", "")
            dictionary["Foo"] = new_value
    return dictionary

result = {"foo":"fookziman","bar":"barziman"}
dictionary = fn_hack_9(result)
print(dictionary)
