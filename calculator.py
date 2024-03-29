operators = ["+", "-", "*", "//", "/", "%", "**"]


def calculator(a, b, operand):
    if operand not in operators:
        return "Invalid operator"

    if a is None or b is None:
        return "Input 2 numbers"

    if operand == "+":
        return a + b
    elif operand == "-":
        return a - b
    elif operand == "*":
        return a * b
    elif operand == "//":
        return a // b
    elif operand == "/":
        return a / b
    elif operand == "%":
        return a % b
    elif operand == "**":
        return a ** b


if __name__ == "__main__":
    x = float(input())
    operand = input()
    y = float(input())
    rez = calculator(x, y, operand)
    print("Result: ", rez)
