
import random
#import pylab
licz_pr = 0
licz_po = 0
licz_pr_sr = 0
licz_po_sr = 0
tab = []
def insertionSort(tab):
    global licz_po
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
            licz_po += 1
            if len(tab) < 50:
                print(tab)
        tab[i + 1] = key
        prz_Insert(prz_tab, tab)
        if len(tab) < 50:
            print(tab)

def prz_Insert(prz_tab,tab):
    global licz_pr
    if prz_tab != tab:
       licz_pr += 1



def mergeSort(arr):
    global licz_po
    global licz_pr
    if len(arr) > 1:

        mid = len(arr) // 2


        L = arr[:mid]


        R = arr[mid:]


        mergeSort(L)


        mergeSort(R)

        cop_tab = []
        i = j = k = 0
        cop_tab.extend(arr)

        #print(arr)
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                licz_po += 1
                i += 1
                licz(arr, cop_tab)

                cop_tab = []
                cop_tab.extend(arr)
            else:
                arr[k] = R[j]
                licz_po += 1
                j += 1
                licz(arr, cop_tab)

                cop_tab = []
                cop_tab.extend(arr)
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
            licz(arr, cop_tab)


def licz(arr,cop_arr):
    global licz_pr
    if (arr != cop_arr):
        licz_pr += 1
        if len(arr) < 50:
            print(arr)


def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    cop_arr = []
    cop_arr.extend(arr)
    global  licz_po
    global  licz_pr
    for j in range(low, high):

        if arr[j] <= pivot:

            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            licz(arr,cop_arr)
            cop_arr = []
            cop_arr.extend(arr)
        licz_po += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    licz(arr, cop_arr)
    return (i + 1)

def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

def generator2_3(gen,alg,n):
    if tab == []:
        for q in range(1, n + 1):
            tab.append(q)
        random.shuffle(tab)
        print(tab)
    if gen == "2":
        if alg == "1":
            insertionSort(tab)
           # print("Tablica", tab)
            # print("Liczba porównań męzy kłuczmi: ", licz_po)
            # print("Liczba przestawań męzy kłuczmi: ", licz_pr)
        if alg == "2":
            mergeSort(tab)
           # print("Tablica",tab)
            # print("Liczba porównań męzy kłuczmi: ", licz_po)
            # print("Liczba przestawań męzy kłuczmi: ", licz_pr)
        if alg == "3":
            m = len(tab)
            quickSort(tab, 0, m - 1)
            print("Tablica", tab)
            print("Liczba porównań męzy kłuczmi: ", licz_po)
            print("Liczba przestawań męzy kłuczmi: ", licz_pr)

porownan = []
porownan2 = []
porownan3 = []
def data_odczyt():
    global  porownan
    global porownan2
    global porownan3

    line_po = ""
    with open("Porownania") as file:
        while True:
                line = file.read(1)
                if not line :
                    break
                if line == "\n":
                   break
                if line == ",":
                    porownan.append(float(line_po))
                    line_po = ""
                    continue
                line_po += line


    line_po1 = ""
    with open("Przestawien") as file:
        while True:
                line = file.read(1)
                if not line:
                    break
                if line == "\n":
                    break
                if line == ",":
                    porownan2.append(float(line_po1))
                    line_po1 = ""
                    continue
                line_po1 += line

    line_po2 = ""
    with open("Porownania_k=100_Q") as file:
        while True:
            line = file.read(1)
            if not line:
                break
            if line == "\n":
                break
            if line == ",":
                porownan3.append(float(line_po2))
                line_po2 = ""
                continue
            line_po2  += line

    print("Porownania",porownan)
    print("Porownania",porownan2)
    print("Porownania", porownan3)

def date_zapisz(licz_po,licz_pr):
    with open("Porownania","a+") as file:
        file.write(licz_po)
    with open("Przestawien","a+") as file:
        file.write(licz_pr)


if __name__ == '__main__':
    k = 100
    wq = [100,200,400,600,800,1000]
    wq2 = [50,100,150,200,250,300]
    n = int(input("Podaj długość tablicy :"))

    gen = "2"

    print(" 1 INSERTION SORT \n 2 MERGE SORT\n 3 QUICK SORT\n ")
    metod = input("Podajaj metod sortowania :")
    while k != 0:
        for q in range(1, n + 1):
            tab.append(q)
        random.shuffle(tab)
        # print(tab)
           #  if gen == "1":
           #      generator1(gen,metod,n)
        if gen == "2" or gen == "3":
            generator2_3(gen,metod,n)
        print(tab)
        tab = []
        licz_po_sr += licz_po
        licz_pr_sr += licz_pr
        k -=1
        licz_po = 0
        licz_pr = 0
    print(licz_pr_sr)
    date_zapisz(str(licz_po_sr/n) + ",", str(licz_pr_sr/n) + ",")
    data_odczyt()
        # file =
        # x = file.readline()
        # y = file.readline()
        # print(x,type(x))
        # print(y, type(y))

    # pylab.suptitle('Wykres Przestawień')
    # #pylab.plot(wq2,porownan,"r")
    # pylab.plot(wq,porownan2,"b")
    # pylab.plot(wq, porownan3, "g")
    # pylab.legend(('mergeSort',"quickSort"))
    # #pylab.legend(('insertionSort', 'mergeSort',"quickSort"))
    # pylab.savefig("k=100PoObce2.jpg")
    # pylab.show()

