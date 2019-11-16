import random
from sorting import selection_sort, bubble_sort, insertion_sort
from sorting import mergesort, quicksort


any_numbers = random.sample(range(1, 1000), 42)

already_sorted = [1, 2, 3, 4, 5, 6, 9, 20, 22, 23, 28, 
                    32, 34, 39, 40, 42, 76, 87, 99, 112]

inversed = [117, 90, 88, 83, 81, 77, 74, 69, 64, 63, 51,
            50, 49, 42, 41, 34, 32, 29, 28, 22, 16, 8, 6, 5, 3, 1]

repeated = [7, 7, 7, 7, 7, 1, 1, 9, 9, 0, 4, 4, 4, 5, 4, 5, 7, 1,]

if __name__ == "__main__":
    test_cases = {'Números aleatórios': any_numbers, 
                    'Já ordenados': already_sorted, 
                    'Ordem inversa': inversed, 
                    'Elementos repetidos': repeated
                }
    print("*******************************")
    for name, lista in test_cases.items():
        print("\nCaso de teste: {}".format(name))
        print(lista)
        quicksort(lista)
        print("\n Ordenado:")
        print(lista)
    print("*******************************")