# we are creating a string with 4 empty spaces to be filled out
formatter = "{} {} {} {}"

# by using the format method for the string we created previously,
# we can fill each space with one of these elements
print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))