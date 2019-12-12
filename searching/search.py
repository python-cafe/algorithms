# Vídeo BUSCA BINÁRIA: https://youtu.be/EgLE5HwRy_M
# Busca binária
def binary_search(array, item, begin=0, end=None):
    if end is None:
        end = len(array)-1
    if begin <= end:
        m = (begin + end)//2
        if array[m] == item:
            return m
        if item < array[m]:
            return binary_search(array, item, begin, m-1)
        else:
            return binary_search(array, item, m+1, end)
    return None

# lista = [2,3,4]
# binary_search(lista, 4, 0, len(lista)-1)
# binary_search(lista, 4)