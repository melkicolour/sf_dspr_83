
"""Угадай число от 0 до 100, меньше чем за 20 попыток, компьютер сам загадывает и сам угадывает"""


import numpy as np

def optimal_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    min_number = 0
    max_number = 101
    
    while True:
        count+=1
        predict_number = np.random.randint(min_number, max_number) # предполагаемое число
        middle_number = round((min_number+max_number) // 2) # середина интервала
        if middle_number > number:
            max_number = middle_number
        elif middle_number < number:
            min_number = middle_number
        else:
            print(f'Компьютер угадал число за {count} попыток. Это число: {number}')
            break # конец игры и выход из цикла если компьютер угадал 
        
    return(count) 
    
def score_game(optimal_predict) -> int:
    """за какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        optimal_predict (_type_): функция угадывания числа

    Returns:
        int: среднее количество угадываний
    """
    count_ls = []
    np.random.seed(1) # фиксирует сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # задали список чисел
    for number in random_array:
        count_ls.append(optimal_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угвдывает число в среднем за: {score} попыток')
    return(score)


print(f' Количество попыток: {optimal_predict(52)}')