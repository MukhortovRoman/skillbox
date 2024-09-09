def maximum_of_two(num_1, num_2):
    return max(num_1, num_2)


def maximum_of_three(x, num_3):
    print(max(x, num_3))


def main():
    num_1 = int(input('Введите первое число: '))
    num_2 = int(input('Введите второе число: '))
    num_3 = int(input('Введите третье число: '))

    x = maximum_of_two(num_1, num_2)
    maximum_of_three(x, num_3)


if __name__ == '__main__':
    main()