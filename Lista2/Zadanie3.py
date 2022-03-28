#import pylab
import random
import numpy
licz_pr = 0
licz_po = 0
licz_pr_sr = 0
licz_po_sr = 0
tab = []


def dualPivotQuickSort(arr, low, high,gen):
    if low < high:

        if gen == "2":
            lp, rp = partition_ros(arr, low, high)
        else:
            lp, rp = partition_mal(arr, low, high)

        dualPivotQuickSort(arr, low, lp - 1,gen)
        dualPivotQuickSort(arr, lp + 1, rp - 1,gen)
        dualPivotQuickSort(arr, rp + 1, high,gen)


def  partition_ros(arr, low, high):
    global licz_po
    cop_arr = []
    cop_arr.extend(arr)
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]
        licz(arr,cop_arr)
        cop_arr = []
        cop_arr.extend(arr)
    licz_po += 1

    j = k = low + 1
    g = high - 1
    p = arr[low]
    q = arr[high]

    while k <= g:


        if arr[k] < p:
            arr[k], arr[j] = arr[j], arr[k]
            j += 1
            licz(arr, cop_arr)
            cop_arr = []
            cop_arr.extend(arr)
        licz_po += 1

        if arr[k] >= q:

            while arr[g] > q and k < g:
                g -= 1

            arr[k], arr[g] = arr[g], arr[k]
            licz(arr, cop_arr)
            cop_arr = []
            cop_arr.extend(arr)
            g -= 1

            if arr[k] < p:

                arr[k], arr[j] = arr[j], arr[k]
                licz(arr, cop_arr)
                cop_arr = []
                cop_arr.extend(arr)
                j += 1
            licz_po += 1
        licz_po += 1
        k += 1

    j -= 1
    g += 1

    arr[low], arr[j] = arr[j], arr[low]
    licz(arr, cop_arr)
    cop_arr = []
    cop_arr.extend(arr)
    arr[high], arr[g] = arr[g], arr[high]
    licz(arr, cop_arr)
    cop_arr = []
    cop_arr.extend(arr)

    return j, g
def  partition_mal(arr, low, high):
    global  licz_po
    cop_arr = []
    cop_arr.extend(arr)
    if arr[low] < arr[high]:

        arr[low], arr[high] = arr[high], arr[low]
        licz(arr,cop_arr)
        cop_arr = []
        cop_arr.extend(arr)
    licz_po += 1
    j = k = low + 1
    g = high - 1
    p = arr[low]
    q = arr[high]

    while k <= g:
        if arr[k] > p:

            arr[k], arr[j] = arr[j], arr[k]
            j += 1
            licz(arr, cop_arr)
            cop_arr = []
            cop_arr.extend(arr)
        licz_po += 1
        if arr[k] <= q:

            while arr[g] > q and k < g:
                g -= 1

            arr[k], arr[g] = arr[g], arr[k]
            licz(arr, cop_arr)
            cop_arr = []
            cop_arr.extend(arr)
            g -= 1

            if arr[k] > p:

                arr[k], arr[j] = arr[j], arr[k]
                licz(arr, cop_arr)
                cop_arr = []
                cop_arr.extend(arr)
                j += 1
            licz_po += 1
        licz_po += 1
        k += 1

    j -= 1
    g += 1


    arr[low], arr[j] = arr[j], arr[low]
    licz(arr, cop_arr)
    cop_arr = []
    cop_arr.extend(arr)
    arr[high], arr[g] = arr[g], arr[high]
    licz(arr, cop_arr)
    cop_arr = []
    cop_arr.extend(arr)

    return j, g
def partition_Mal(arr, low, high):
    i = (low - 1)
    pivot = arr[high]
    cop_arr = []
    cop_arr.extend(arr)
    global licz_po
    global licz_pr
    for j in range(low, high):

        if arr[j] >= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            licz(arr,cop_arr)
            cop_arr = []
            cop_arr.extend(arr)
        licz_po += 1
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    licz(arr, cop_arr)
    return (i + 1)
def partition_Ros(arr, low, high):
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
def licz(arr,cop_arr):
    global  licz_pr
    if (arr != cop_arr):
        licz_pr += 1
        if len(arr) < 50:
            print(arr)
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
        while n !=0:
            liczba = random.randint(1,n)
            # for q in range(1,51):
            i =1
            while i:
                for q in tab:
                    if q ==liczba:
                        liczba=random.randint(1,n)
                for q in tab:
                    if q ==liczba:
                        liczba=random.randint(1,n)
                tab.append(liczba)
                i = 0
            n -= 1
        random.shuffle(tab)
        print(tab)
        generator2_3(gen,alg,n)
def generator2_3(gen,alg,n):
    if tab == []:
        for q in range(1, n + 1):
            tab.append(q)
        random.shuffle(tab)
        print(tab)
    #print("Tablica",tab)
    if gen == "2":
        if alg == "1":
            m = len(tab)
            quickSort(tab, 0, m - 1,gen)
            print("Tablica", tab)
            print("Liczba porównań męzy kłuczmi: ", licz_po)
            print("Liczba przestawań męzy kłuczmi: ", licz_pr)
        if alg == "2":
            # while True:
            #     p = int(input("Podaj p: "))
            #     q = int(input("Podaj q: "))
            #     if p < q:
            #         print(n2-1)
            #         if q <= (n2-1):
            #             break
            #
            #     else:
            #         print("podaj inne")
            #         continue
            m = len(tab)
            dualPivotQuickSort(tab,0,m-1,gen)
            print("Tablica", tab)
            print("Liczba porównań męzy kłuczmi: ", licz_po)
            print("Liczba przestawań męzy kłuczmi: ", licz_pr)
    if gen == "3":
        if alg == "1":
             m = len(tab)
             quickSort(tab,0, m-1,gen)
             print("Tablica", tab)
             print("Liczba porównań męzy kłuczmi: ", licz_po)
             print("Liczba przestawań męzy kłuczmi: ", licz_pr)
        if alg == "2":
            # while True:
            #     p = int(input("Podaj p: "))
            #     q = int(input("Podaj q: "))
            #     if p < q:
            #         print(n2-1)
            #         if q <= (n2-1):
            #             break
            #
            #     else:
            #         print("podaj inne")
            #         continue
            m = len(tab)
            dualPivotQuickSort(tab,0,m-1,gen)
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
    with open("Porownania_k=100_Q") as file:
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
    with open("Porownania_k=100_Q2") as file:
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
    with open("Przestawien_k=100_Q2") as file:
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
            line_po2 += line

    print("Porownania",porownan)
    print("Porownania",porownan2)
    print("Porownania", porownan3)

def date_zapisz(licz_po,licz_pr):
    with open("Porownania","a+") as file:
        file.write(licz_po)
    with open("Przestawien","a+") as file:
        file.write(licz_pr)


if __name__ == '__main__':
     k = 1
     wq = [100, 200, 400,500, 600,700, 800, 1000]
   # wq = [100,200,400,600,800,1000]
     n = int(input("Podaj długość tablicy :"))

     gen = input("Podaj generator 1 liczbe losowe 2 Rosnącą , 3 Malejącą : ")

     print(" 1 QUICK SORT\n 2 Duo")
     metod = input("Podajaj metod sortowania :")
     while k != 0:

            #print(tab)
        if gen == "1" :
            generator1(gen, metod, n)
        if gen == "2" or gen == "3":
            generator2_3(gen,metod,n)
        print(tab)
        tab = []
        licz_po_sr += licz_po
        licz_pr_sr += licz_pr
        k -=1
        licz_po = 0
        licz_pr = 0
     date_zapisz(str(licz_po_sr/n) + ",", str(licz_pr_sr/n) + ",")
     # date_zapisz( str(n* numpy.log(n)) + ",","")
   # data_odczyt()
        # file =
        # x = file.readline()
        # y = file.readline()
        # print(x,type(x))
        # print(y, type(y))

   # pylab.suptitle('Wykres Porownań')
   # pylab.plot(wq,porownan,"r")
    #pylab.plot(wq,porownan2,"b")
    #pylab.plot(wq, porownan3, "g")
    #pylab.legend(('k=1',"k=10"))
   # pylab.legend(("quickSort","dualPivotQuickSort"))
    #pylab.savefig("k=100PoQduObcy.jpg")
    #pylab.show()
