from sympy.parsing.sympy_parser import Symbol, parse_expr
from sympy import diff
from scipy.optimize import fminbound
from math import sqrt


def init_symbols_list(count):
    symbols = []
    for i in range(count):
        symbols.append(Symbol('x' + str(i + 1)))
    return symbols


def get_gradient(function, symbols, current_x):
    subs = dict(zip(symbols, current_x))
    gradient = []
    for symbol in symbols:
        gradient.append(diff(function, symbol).evalf(subs=subs))
    return gradient


def create_h_expr(function, symbols, current_x, gradient):
    subs = []
    h = Symbol('h')
    for i in range(len(symbols)):
        subs.append((symbols[i], -h * gradient[i] + current_x[i]))
    return function.subs(subs)


def find_argmin_h_expr(h_expr):
    h = Symbol('h')
    func = lambda x: h_expr.evalf(subs={h: x})
    solution = fminbound(func, x1=0, x2=1)
    return solution


def check_stop_condition(gradient, epsilon):
    norm = 0
    for elem in gradient:
        norm += elem * elem
    return sqrt(norm) <= epsilon


def main():
    symbols = init_symbols_list(2)
    input_func = input('Func: ')
    func = parse_expr(input_func)
    current_x = [0, 0]

    while 1:
        iter = iter + 1
        gradient = get_gradient(func, symbols, current_x)
        if check_stop_condition(gradient, 0.001):
            break
        h_expr = create_h_expr(func, symbols, current_x, gradient)
        h = find_argmin_h_expr(h_expr)

        for i in range(len(current_x)):
            current_x[i] = current_x[i] - h * gradient[i]
        print(current_x)


if __name__ == '__main__':
    main()