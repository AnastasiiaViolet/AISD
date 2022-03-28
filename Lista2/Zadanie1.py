import random

licz_prIn = 0
licz_poIn = 0
tab_sort = []

def insertionSort_Mal(tab):
    global  licz_poIn
    prz_tab = []
    for j in range(1, len(tab)):
        key = tab[j]
        i = j - 1
        if len(prz_tab) != 0:
            prz_tab = []
        prz_tab.extend(tab)
        while i >= 0 and key > tab[i]:
            tab[i + 1] = tab[i]
            prz_Insert(prz_tab, tab)
            i -= 1
            licz_poIn += 1
            if len(tab) < 50:
                print(tab)
        tab[i + 1] = key
        prz_Insert(prz_tab, tab)
        if len(tab) < 50:
            print(tab)

def insertionSort_Ros(tab):
    global licz_poIn
    prz_tab = []
    for j in range(1, len(tab)):
        key = tab[j]
        i = j - 1
        if len(prz_tab) != 0:
            prz_tab = []
        prz_tab.extend(tab)
        while i >= 0 and key < tab[i]:
            tab[i + 1] = tab[i]
            prz_Insert(prz_tab, tab)
            i -= 1
            licz_poIn += 1
            if len(tab) <= 50:
                print(tab)
        tab[i + 1] = key
        prz_Insert(prz_tab, tab)
        if len(tab) <= 50:
            print(tab)

def prz_Insert(prz_tab,tab):
    global licz_prIn
    if prz_tab != tab:
       licz_prIn += 1

licz_poM = 0
licz_prM = 0
tab = []
def mergeSort_Mal(arr):
    global licz_poM
    global licz_prM
    if len(arr) > 1:

        mid = len(arr) // 2


        L = arr[:mid]


        R = arr[mid:]


        mergeSort_Mal(L)


        mergeSort_Mal(R)

        cop_tab = []
        i = j = k = 0
        cop_tab.extend(arr)

        print(arr)
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = L[i]
                i += 1
                licz(arr, cop_tab)

                cop_tab = []
                cop_tab.extend(arr)
            else:
                arr[k] = R[j]
                j += 1
                licz(arr, cop_tab)

                cop_tab = []
                cop_tab.extend(arr)
            licz_poM += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            licz(arr, cop_tab)


        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            licz(arr,cop_tab)

def mergeSort_Ros(arr):
    global licz_poM
    global licz_prM
    if len(arr) > 1:

        mid = len(arr) // 2

        L = arr[:mid]


        R = arr[mid:]


        mergeSort_Ros(L)


        mergeSort_Ros(R)

        cop_tab = []
        i = j = k = 0
        cop_tab.extend(arr)
        #print(arr)
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
                licz(arr, cop_tab)
                cop_tab = []
                cop_tab.extend(arr)
            else:
                arr[k] = R[j]
                j += 1
                licz(arr, cop_tab)
                cop_tab = []
                cop_tab.extend(arr)
            k += 1
            licz_poM += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            licz(arr, cop_tab)

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            licz(arr, cop_tab)


def licz(arr,cop_arr):
    global licz_prM
    global  licz_prQ
    if (arr != cop_arr):
        licz_prM += 1
        licz_prQ += 1
        if len(arr) <= 50:
            print(arr)


licz_poQ = 0
licz_prQ = 0
def partition_Mal(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    cop_arr = []
    cop_arr.extend(arr)
    global licz_poQ
    global licz_prQ
    for j in range(low, high):

        if arr[j] >= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            licz(arr,cop_arr)
            cop_arr = []
            cop_arr.extend(arr)
        licz_poQ += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    licz(arr, cop_arr)
    return (i + 1)
def partition_Ros(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    cop_arr = []
    cop_arr.extend(arr)
    global  licz_poQ
    global  licz_prQ
    for j in range(low, high):

        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            licz(arr,cop_arr)
            cop_arr = []
            cop_arr.extend(arr)
        licz_poQ += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    licz(arr, cop_arr)
    return (i + 1)

def quickSort(arr, low, high,gen):
    if len(arr) == 1:
        return arr
    if low < high:
        if gen == "3":
            pi = partition_Mal(arr, low, high)
        else:
            pi = partition_Ros(arr, low, high)
        quickSort(arr, low, pi - 1,gen)
        quickSort(arr, pi + 1, high,gen)

def generator1(gen,alg,n):
    print("Tablica", tab)
    if gen == "1":
        gen = input(" 2 Rosnąco \n 3 Malyjąco\n ")
        i =n
        while i !=0:
            liczba = random.randint(1,n)
            # for q in range(1,51):
            h =1
            while h:
                for q in tab:
                    if q ==liczba:
                        liczba=random.randint(1,n)
                for q in tab:
                    if q ==liczba:
                        liczba=random.randint(1,n)
                tab.append(liczba)
                h = 0
            i -= 1

        random.shuffle(tab)
        print("Tablica", tab)
        tab_sort.extend(tab)
        # print("Tablica", tab)
        generator2_3(gen,alg,n)
def generator2_3(gen,alg,n):
    if tab == []:
        while n != 0:
            liczba = int(input("Podaj liczbę: "))
            for pow in tab:
                if pow == liczba:
                    liczba = int(input("Podaj innu liczbu: "))
            tab.append(liczba)
            n -= 1
        tab_sort.extend(tab)
        print("Tablica",tab)
    if gen == "2":
        if alg == "1":
            insertionSort_Ros(tab)
            print("Tablica", tab)
            print("Liczba porównań męzy kłuczmi: ", licz_poIn)
            print("Liczba przestawań męzy kłuczmi: ", licz_prIn)
        if alg == "2":
            mergeSort_Ros(tab)
            print("Tablica",tab)
            print("Liczba porównań męzy kłuczmi: ", licz_poM)
            print("Liczba przestawań męzy kłuczmi: ", licz_prM)
        if alg == "3":
            m = len(tab)
            quickSort(tab, 0, m - 1,gen)
            print("Tablica", tab)
            print("Liczba porównań męzy kłuczmi: ", licz_poQ)
            print("Liczba przestawań męzy kłuczmi: ", licz_prQ)
    if gen == "3":
        if alg == "1":
            insertionSort_Mal(tab)
            print("Tablica",tab)
            print("Liczba porównań męzy kłuczmi: ", licz_poIn)
            print("Liczba przestawań męzy kłuczmi: ", licz_prIn)
        if alg == "2":
            mergeSort_Mal(tab)
            print("Tablica",tab)
            print("Liczba porównań męzy kłuczmi: ", licz_poM)
            print("Liczba przestawań męzy kłuczmi: ", licz_prM)
        if alg == "3":
             m= len(tab)
             quickSort(tab,0, m-1,gen)
             print("Tablica", tab)
             print("Liczba porównań męzy kłuczmi: ", licz_poQ)
             print("Liczba przestawań męzy kłuczmi: ", licz_prQ)
def porownanie_tab(tab,tab_sort,n):
    i = 0
    while i != n:
        if tab[i] == tab_sort[i]:
            i += 1
            continue
        else:
            return False

    return True


if __name__ == '__main__':
    n = int(input("Podaj długość tablicy :"))

    gen = input("Podaj generator 1 liczb losowych, 2 Rosnącą , 3 Malejącą : ")

    print(" 1 INSERTION SORT \n 2 MERGE SORT\n 3 QUICK SORT\n ")
    metod = input("Podajaj metod sortowania :")
    if gen == "1":
        generator1(gen,metod,n)
    if gen == "2" or gen == "3":
        generator2_3(gen,metod,n)

    tab_sort.sort()
    if porownanie_tab(tab,tab_sort,n):
        print("Poprawnie posortowana",tab_sort)
    tab_sort.reverse()
    if porownanie_tab(tab,tab_sort,n):
        print(tab_sort)

