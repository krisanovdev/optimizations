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


def delta(first, second):
    result = []
    for i in range(len(first)):
        result.append(first[i] - second[i])
    return result


def norm(vector):
    result = 0.0
    for item in vector:
        result += item**2
    return sqrt(result)


def main():
    dimension = int(input('Input dimension (num of variables): '))
    current_x = [int(x) for x in input('Input init guess (x0, splitted by spaces): ').split()]

    if len(current_x) != dimension:
        raise RuntimeError('Length of x0 not equal to dimension!')

    symbols = init_symbols_list(dimension)
    func = parse_expr(input('Input function: '))
    epsilon = float(input('Input accuracy (epsilon): '))

    iteration = 0
    while 1:
        gradient = get_gradient(func, symbols, current_x)
        h_expr = create_h_expr(func, symbols, current_x, gradient)
        h = find_argmin_h_expr(h_expr)

        prev_x = current_x.copy()
        for i in range(len(current_x)):
            current_x[i] = current_x[i] - h * gradient[i]
        print('Iteration №{}: x = {}'.format(iteration, current_x))

        norm_delta_last_two = norm(delta(prev_x, current_x))
        if norm_delta_last_two < epsilon:
            break

        iteration += 1

    print("Solution: {}".format(current_x))
    print("Norm of delta of two last x: {}".format(norm_delta_last_two))
    print('Gradient norm: {}'.format(norm(gradient)))


if __name__ == '__main__':
    main()
