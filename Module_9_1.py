def apply_all_func(int_list, *functions):
    result = {}
    try:
        for func in functions:
            result[func.__name__] = func(int_list)
        return result
    except TypeError:
        print('Ошибка типа данных в списке: для одного их элементов функция невыполнима')






print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))