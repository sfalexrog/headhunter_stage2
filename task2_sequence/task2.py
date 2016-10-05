#!/usr/bin/env python3


def merge(prefix, suffix):
    '''
    Сливает вместе заданные префикс и суффикс, избавляясь от перекрытия внутри них.
    :param prefix: Строка-префикс, возможно, содержащая часть суффикса
    :param suffix: Строка-суффскс, возможно, соредращая часть префикса
    :return: Кратчайшее возможное слияние префикса и суффикса
    '''
    if (prefix == ''):
        return suffix
    if (suffix == ''):
        return prefix
    retval = prefix + suffix
    max_overlay_length = min(len(prefix), len(suffix))
    for i in range(1, max_overlay_length):
        overlay = suffix[:i]
        prefix_pos = prefix.rfind(overlay)
        if (prefix_pos > 0) and prefix[prefix_pos:] == overlay:
            retval = prefix + suffix[i:]
    return retval


def find_sequence(s):
    '''
    Пытается в данной последовательности символов увидеть возрастающую
    последовательность чисел (как требуется в задании)
    :param s: Указанная последовательность
    :return: Кортеж, первым элементом которого будет первое полностью
    записанное число в последовательности, а вторым - смещение этого числа
    относительно начала последовательности.
    '''
    # Особый случай: пусть строка целиком состоит из нулей, тогда наименьшее
    # подходящее нам число - единица и столько нулей, сколько нам передали.
    if int(s) == 0:
        return (int('1' + s), -1)
    candidates = []
    # Перебираем все возможные варианты длины числа (от 1 до полной длины
    # последовательности - 1; в случае, если число не будет наидено,
    # идём дальше)
    retval = (-1, -1)
    for nlen in range(1, len(s)):
        # Перебираем возможные длины префиксов
        for prefix_len in range(nlen):
            candidate_s = s[prefix_len:prefix_len + nlen]
            # Игнорируем строки, начинающиеся с 0
            if candidate_s[0] == '0':
                continue
            candidate = int(candidate_s)
            # Сравниваем наиденное число с числом-префиксом: ожидается, что
            # число-префикс будет на 1 меньше данного
            cprefix = candidate - 1
            cprefix_str = str(cprefix)[-prefix_len:]
            if (prefix_len > 0) and (s[0:prefix_len] != cprefix_str):
                # Переходим к следующей длине префикса
                continue
            # Сравниваем число с оставшимися
            num_count = (len(s) - prefix_len) // nlen
            fits = True
            start = prefix_len + nlen
            candidate_next = candidate
            candidate_next_str = str(candidate_next)
            while start + len(candidate_next_str) < len(s):
                candidate_next += 1
                candidate_next_str = str(candidate_next)
                real_next = s[start:start + len(candidate_next_str)]
                if (candidate_next_str != real_next):
                    fits = False
                    break
                start += len(candidate_next_str)
            # Если число не подходит - переходим к следующему префиксу/числу
            if (not fits):
                continue
            # Наконец, проверяем постфикс (то, что не вошло целиком)
            #start -= len(str(candidate_next))
            postfix = s[start:]
            candidate_next += 1
            candidate_next_prefix = str(candidate_next)[:len(postfix)]
            if (postfix == candidate_next_prefix):
                # Число наидено!
                #print('Number found! {}, offset {}'.format(candidate, prefix_len))
                candidates.append((candidate, prefix_len))
    # Предполагаем, что число либо целиком записано в последовательности,
    # либо ни разу целиком в него не вошло. Рассматриваем
    modulo = 1
    for i in range(len(s)):
        left_suffix = s[:i]
        right_prefix = s[i:]
        # Пропускаем префиксы, начинающиеся с нуля
        if right_prefix[0] == '0':
            modulo *= 10
            continue
        right_suffix = str((int(left_suffix) + 1) % modulo) if len(left_suffix) > 0 else ''
        right_suffix_len = len(right_suffix)
        left_suffix_len = len(left_suffix)
        if right_suffix_len < left_suffix_len:
            right_suffix = '0' * (left_suffix_len - right_suffix_len) + right_suffix
        # "Съедаем" совпадающие символы у префикса и суффикса
        num_merge = merge(right_prefix, right_suffix)
        number = int(num_merge)
        # Проверяем, не подойдёт ли нам предыдущее число
        number_len = len(num_merge)
        potential_seq = str(number - 1) + num_merge
        potential_seq_pos = potential_seq.find(s)
        if potential_seq_pos < number_len:
            candidates.append((number - 1, -potential_seq_pos))
        else:
            candidates.append((number, i))
        modulo *= 10
    retval = min(candidates, key=lambda x: x[0])
    # print('Number not found :(')
    return retval


def get_number_position(num):
    '''
    Определяет, начиная с какого знака в последовательности содержится
    число num.
    :param num: Число, которое надо найти в последовательности
    :return: Позиция, на которой стоит указанное число
    '''
    start = 1
    # "Шаг" - сколько знаков нам надо будет "пропускать" (то есть сколько
    # значащих цифр есть в десятичной записи числа)
    step = 1
    # Величина "отрезка", на котором мы ищем число (9 для 1-значных, 90
    # для 2-значных и т.д.)
    length = 9
    while length < num:
        num -= length
        start += step * length
        step += 1
        length *= 10
    # print('num: {}, start: {}, step: {}, length: {}'.format(num, start, step, length))
    return start + (num - 1) * step

def get_sequence_pos(s):
    '''
    По заданной последовательности s находит её первое вхождение в последовательность,
    указанную в условии задачи
    :param s: Заданная подпоследовательность
    :return: Положение первого вхождения в последовательность, указанную в условии
    задачи
    '''
    num, offset = find_sequence(s)
    return get_number_position(num) - offset

if __name__ == '__main__':
    pass