#!/usr/bin/env python3


def get_basin_cell_info(isle, x, y):
    if y <= 0 or y >= len(isle) - 1:
        return (False, -1, {})
    if x <= 0 or x >= len(isle[y]) - 1:
        return (False, -1, {})
    wall_height = min(isle[y][x - 1], isle[y][x + 1],
                      isle[y - 1][x], isle[y + 1][x])
    extents = {(wx, wy) for wx, wy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1))
               if isle[wy][wx] <= isle[y][x]}
    if wall_height >= isle[y][x]:
        return (True, wall_height - isle[y][x], extents)
    return (False, -1, {})


floodfill_mask = []
floodfill_set = {}


def clear_flood_mask(isle):
    floodfill_mask = [[False for _ in range(len(isle[i]))] for i in range(len(isle))]


def find_local_min(isle, x_start = 1, y_start = 1):
    for y in range(y_start, len(isle) - 1):
        for x in range(x_start, len(isle[y]) - 1):
            if isle[y][x] <= isle[y][x - 1] and\
               isle[y][x] <= isle[y][x + 1] and\
               isle[y][x] <= isle[y - 1][x] and\
               isle[y][x] <= isle[y + 1][x]:
                return (x, y)
    return (-1, -1)


def get_surrounding_cells(cell_coord_set):
    result = set()
    for cell in cell_coord_set:
        result.add((cell[0] + 1, cell[1]))
        result.add((cell[0] - 1, cell[1]))
        result.add((cell[0], cell[1] + 1))
        result.add((cell[0], cell[1] - 1))
    result -= cell_coord_set
    return result


def floodfill(isle, x, y):
    '''
    Пытаемся заполнить текущую клетку и клетки, соседние с ней. Если заполнение
    невозможно (напрмиер, клетка является граничной или не собирает воду), возвращаем
    0. Иначе возвращаем объём воды, который скапливается в окрестности точки.
    :param isle: "Матрица" (список списков) с клетками острова
    :param x: Координата x заполняемой клетки
    :param y: Координата y заполняемой клетки
    :return: Объём воды, накопленный в данной и соседних клетках
    '''
    adjacent_cells = set()
    cell_info = get_basin_cell_info(isle, x, y)
    if (cell_info[0] == False):
        return 0
    filled_cells = {(x, y)}
    water_depth = 0
    adjacent_cells |= cell_info[2]
    while(len(adjacent_cells) > 0):
        adj_cell_coords = adjacent_cells.pop()
        filled_cells.add(adj_cell_coords)
        adj_cell_info = get_basin_cell_info(isle, adj_cell_coords[0], adj_cell_coords[1])
        # Среди соседних клеток не может быть таких, которые бы не могли быть
        # клетками "бассейна".
        if adj_cell_info[0] == False:
            return 0
        for cell in adj_cell_info[2]:
            if cell not in filled_cells:
                adjacent_cells.add(cell)
    enclosing_cells = get_surrounding_cells(filled_cells)
    wall_height = min(isle[c[1]][c[0]] for c in enclosing_cells)
    for c in filled_cells:
        cell_depth = wall_height - isle[c[1]][c[0]]
        assert(cell_depth >= 0)
        water_depth += cell_depth
        isle[c[1]][c[0]] = wall_height
    return water_depth


def get_water(isle):
    '''
    Подсчитывает количество воды, остающейся на острове после дождей
    :param isle: "Матрица" (список списков) с клетками острова
    :return: Количество воды, оставшейся на острове
    '''
    if len(isle) < 3 or len(isle[0]) < 3:
        return 0
    local_min = find_local_min(isle)
    if local_min == (-1, -1):
        return 0
    delta_water = floodfill(isle, local_min[0], local_min[1])
    total_water = delta_water
    while(delta_water > 0):
        local_min = find_local_min(isle, local_min[0], local_min[1])
        if local_min == (-1, -1):
            local_min = find_local_min(isle)
            if local_min == (-1, -1):
                return total_water
        delta_water = floodfill(isle, local_min[0], local_min[1])
        total_water += delta_water
    return total_water


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
        print(get_water(isle))
