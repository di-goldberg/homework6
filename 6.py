try:
    n = int(input('Введите количество элементов массива'))
except ValueError:
    print('Введено неверное значение. Убедитесь в достоверности введенных данных и попробуйте еще раз')
else:
    array = 0 * n
    try:
        for i in range(0, n):
            array = int(input('Введите элемент'))
    except ValueError:
        print('Введено неверное значение. Убедитесь в достоверности введенных данных и попробуйте еще раз')
    else:
        try:
            delta = int(input('Введите delta'))
        except ValueError:
            print('Введено неверное значение. Убедитесь в достоверности введенных данных и попробуйте еще раз')
        else:
            result = array.count(min(array) + delta)
            print(result)