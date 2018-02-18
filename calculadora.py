#!/usr/bin/python3

import sys


def suma(operando1, operando2):
    return operando1 + operando2


def resta(operando1, operando2):
    return operando1 - operando2


def multiplicacion(operando1, operando2):
    return operando1 * operando2


def division(operando1, operando2):
    return operando1 / operando2


def exponente(operando1, operando2):
    return operando1 ** operando2

funciones = {
    "suma": suma,
    "resta": resta,
    "multiplicacion": multiplicacion,
    "division": division,
    "elevacion": exponente
}

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit("usage: [operador][operando1][operando2]")
    _, funcion, op1, op2 = sys.argv
    try:
        operando1 = float(op1)
        operando2 = float(op2)
        solucion = funciones[operacion](operando1, operando2)
        print(str(solucion))
    except ValueError:
        sys.exit("No estan permitidos operandos que no sean de tipo numerico")
