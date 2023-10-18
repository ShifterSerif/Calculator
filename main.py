# use space to separate numbers and operators for single line?

def onebyone():
    print("Enter a number or symbol to add to equation. Enter '=' to solve equation. Enter 'b' to backspace.")
    i = 1
    inputs = []
    while True:
        choice = input()
        if choice == '=':
            break
        elif choice.isdigit():
            choice = float(choice)
        elif choice != '+' and choice != '-' and choice != '*' and choice != '/' and choice != '^':
            print("Invalid input")
            continue
        inputs.append(choice)
        if choice == 'b':
            inputs.pop()
            inputs.pop()
    result = inputs[0]
    while i < len(inputs):
        if inputs[i] == '+':
            result += inputs[i+1]
        elif inputs[i] == '-':
            result -= inputs[i+1]
        elif inputs[i] == '*':
            result *= inputs[i+1]
        elif inputs[i] == '/':
            result /= inputs[i+1]
        elif inputs[i] == '^':
            result **= inputs[i+1]
        i += 2
    print(inputs)
    print(result)


def allatonce():
    print("Enter an equation to solve. Use spaces to separate numbers and operators.")
    equation = input().split()
    result = float(equation[0])
    i = 1
    while i < len(equation):
        if equation[i] == '+':
            result += float(equation[i+1])
        elif equation[i] == '-':
            result -= float(equation[i+1])
        elif equation[i] == '*':
            result *= float(equation[i+1])
        elif equation[i] == '/':
            result /= float(equation[i+1])
        elif equation[i] == '^':
            result **= float(equation[i+1])
        i += 2
    print(result)


# onebyone()
allatonce()