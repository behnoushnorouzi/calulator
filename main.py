import re

print("Our Magical Calculator")
print("type 'quit' to exit\n")

previous = 0
run = True


def perform_math():
    equation = ""
    global run
    global previous

    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Goodbye! see you soon!")
        run = False
    else:
        # clean the entry data
        equation = re.sub('[a-zA-Z,.:;()]', '', equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    perform_math()

