#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    
    args = sys.argv[1:]
    args_count = len(args)
    valid_operators = ["+", "-", "*", "/"]
    
    if args_count != 3:
        print("Usage: ./custom_calculator.py <operand1> <operator> <operand2>")
        exit(1)
    elif args[1] not in valid_operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        operand1 = int(args[0])
        operand2 = int(args[2])
        
        if args[1] == "+":
            print("{:d} + {:d} = {:d}".format(operand1, operand2, add(operand1, operand2)))
        elif args[1] == "-":
            print("{:d} - {:d} = {:d}".format(operand1, operand2, sub(operand1, operand2)))
        elif args[1] == "*":
            print("{:d} * {:d} = {:d}".format(operand1, operand2, mul(operand1, operand2)))
        elif args[1] == "/":
            print("{:d} / {:d} = {:d}".format(operand1, operand2, div(operand1, operand2)))
