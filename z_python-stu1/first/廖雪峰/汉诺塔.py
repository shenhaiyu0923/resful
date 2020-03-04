# -*- coding: utf-8 -*-
def move(n, a, b, c):
    global step
    if n == 1:
        step = step + 1
        print(step, '.', a, '-->', c)
    else:
        move(n - 1, a, c, b)
        step = step + 1
        print(step, '.', a, '-->', c)
        move(n - 1, b, a, c)


def main():
    move(3, 'A', 'B', 'C')


if __name__ == '__main__':
    global step
    step = 0
    main()