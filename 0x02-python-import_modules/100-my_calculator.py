#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc
    ops = ["+", "-", "*", "/"]
    l = sys.argv
    if len(l) != 4:
        (print("{}"
         .format("Usage: ./100-my_calculator.py <a> <operator> <b>")))
        exit(1)
    if not l[2] in ops:
        (print("{}"
         .format("Unknown operator. Available operators: +, -, * and /")))
        exit(1)
    a = int(l[1])
    b = int(l[3])
    op = l[2]
    result = (calc.add(a, b)
              if op is "+" else calc.sub(a, b)
              if op is "-" else calc.mul(a, b)
              if op is "*" else calc.div(a, b)
              if op is "/" else 0)
    print("{} {} {} = {}".format(a, op, b, result))
