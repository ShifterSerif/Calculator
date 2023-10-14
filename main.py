# use space to separate numbers and operators for single line?

def main():
    print("Enter a number or symbol to add to equation. Enter '=' to solve equation. Enter 'q' to backspace.")
    i = 0
    operations = 0
    inputs = []
    while True:
        choice = input()
        if choice == '=':
            break
        elif choice.isdigit():
            choice = int(choice)
        elif choice == '+' or choice == '-' or choice == '*' or choice == '/' or choice == '^':
            operations += 1
        else:
            print("Invalid input")
            continue
        inputs.append(choice)
        if choice == 'q':
            inputs.pop()
            inputs.pop()
    result = inputs[0]
    while operations > 0:
        if inputs[i+1] == '+':
            result += inputs[i+2]
        elif inputs[i+1] == '-':
            result -= inputs[i+2]
        elif inputs[i+1] == '*':
            result *= inputs[i+2]
        elif inputs[i+1] == '/':
            result /= inputs[i+2]
        elif inputs[i+1] == '^':
            result **= inputs[i+2]
        operations -= 1
        i += 2
    print(inputs)
    print(result)


main()
