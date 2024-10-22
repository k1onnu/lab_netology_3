
def min_breaks(n, m, results = {}):

#Проверка 1x1
    if n == 1 and m == 1:
        return 0

#Проверка на значение в памяти
    if(n, m) in results:
        return results[(n, m)]

# Если одна из сторон равна 1, то кол-во разломов равно другой стороне минус один
    if n == 1:
        cuts = m - 1
    elif m == 1:
        cuts = n - 1
    else:
        # Иначе делаем разрезы как по вертикали, так и по горизонтали
        vertical_splits = min_breaks(n, 1, results) + min_breaks(n, m - 1, results) + 1
        horizontal_splits = min_breaks(1, m, results) + min_breaks(n - 1, m, results) + 1
        cuts = min(vertical_splits, horizontal_splits)

    #Записываем в results
    results[n, m] = cuts
    return cuts

print(min_breaks(3,3))