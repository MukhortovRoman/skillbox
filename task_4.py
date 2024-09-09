def first_num_count(first):
    first_num_count = 0
    temp = first
    while temp > 0:
        first_num_count += 1
        temp = temp // 10

    return first_num_count


def change_number(num, digit):
    num_1 = first_num_count(num)
    last_digit = num % 10
    first_digit = num // 10 ** (num_1 - 1)
    between_digits = num % 10 ** (num_1 - 1) // 10
    first_s = last_digit * 10 ** (num_1 - 1) + between_digits * 10 + first_digit

    return first_s


def main():
    first_n = int(input("\nВведите первое число: "))
    while first_n < 100:
        print('В первом числе меньше трех цифр.')
        first_n = int(input("Введите первое число: "))
    change_number(first_n, 'первое')
    print('Изменное число:', change_number(first_n, ''))

    first_m = int(input("\nВведите второе число: "))
    while first_m < 1000:
        print('В втором числе меньше четырех цифр')
        first_m = int(input("Введите второе число: "))
    change_number(first_m, 'второе')
    print('Изменное число:', change_number(first_m, ''))

    print('\nСумма чисел:', change_number(first_n, '') + change_number(first_m, ''))


if __name__ == '__main__':
    main()
