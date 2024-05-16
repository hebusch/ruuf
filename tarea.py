def max_cantidad_paneles_rectangulo(a, b, x, y):
    if x < a or y < b:
        if x < b or y < a:
            return 0
    return (x * y) // (a * b)


if __name__ == '__main__':
    print('\nRectangulo:')
    print('Ejemplo 1_1:', max_cantidad_paneles_rectangulo(1, 2, 2, 4))
    print('Ejemplo 1_2:', max_cantidad_paneles_rectangulo(1, 2, 3, 5))
    print('Ejemplo 1_3:', max_cantidad_paneles_rectangulo(2, 2, 1, 10))
