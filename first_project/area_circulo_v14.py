from math import pi
import sys
import errno

def help():
    print('e necessario informar o raio do circulo')
    print('sintaxe: {} <raio>'. format(sys.argv[0][2:]))

def circulo(raio):
    return pi * float(raio) ** 2

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help ()
        sys.exit(errno.EPERM)

    if not sys.argv[1].isnumeric():
        help()
        print('o raio deve ser um valor numerico')

        raio = sys.argv[1]
        area = circulo(raio)
        print('area do circulo', area)
