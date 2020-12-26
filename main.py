while True:
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        num3 = int(input("Введите третье число: "))
        num4 = int(input("Введите четвертое число: "))
        print('Выберите математический знак')
        print("+ для сложения чисел")
        print("- для вычитания чисел")
        print("/ для деления чисел")
        print("* для умножения чисел")
        operation = input('Введите знак для операций: ')

        if operation == '+':
            print('результат составил: ', num1 + num2 + num3 + num4)

        elif operation == '-':
            print('результат составил: ', num1 - num2 - num3 - num4)

        elif operation == '*':
            print('результат составил: ', num1 * num2 * num3 * num4)

        elif operation == '/':
            print('результат составил: ', num1 / num2 / num3 / num4)

        else:
            print('Вы ввели неправильный знак, Попробуйте еще раз')

        print('Continue or stop')
        stop_or_continue = input('')
        if stop_or_continue == "stop":
            break

    except ValueError:
        print('Введенна буква , введите число')