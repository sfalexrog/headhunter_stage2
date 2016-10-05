#!/usr/bin/env python3


def get_water(isle):
    '''
    Подсчитывает количество воды, остающейся на острове после дождей
    :param isle: "Матрица" (список списков) с клетками острова
    :return: Количество воды, оставшейся на острове
    '''



def read_island(size_x, size_y):
    '''
    Считывает "остров" заданного размера
    :param size_x: Количество клеток по горизонтали
    :param size_y: Количество клеток по вертикали
    :return: "Матрица" (список списков) с клетками острова
    '''
    isle = []
    for y in range(size_y):
        isle_line = [int(i) for i in input().split()]
        isle.append(isle_line)
    return isle


if __name__ == '__main__':
    num_islands = int(input())
    for isle_n in range(num_islands):
        isle_y, isle_x = (int(i) for i in input().split())
        isle = read_island(isle_x, isle_y)
