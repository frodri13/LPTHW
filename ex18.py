def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")

def print_none():
    print("I've got nothing.")

print_two("fabio", "rodriguez")
print_two_again("fabio", "rodriguez")
print_one("First!")
print_none()