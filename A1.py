def bubble_sort(arr):
    n = len(arr)  # Nustatome pagal masyvo ilgį
    
    for i in range(n):  # Einame per visus elementus
        for j in range(0, n-i-1):  # Einame per likusius elementus
            if arr[j] > arr[j+1]:  # Jei esamas elementas yra didesnis už kitą
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Apkeičiame elementus vietomis
    
    return arr  # Grąžiname surikiuotą masyvą

my_list = [64, 34, 25, 12, 22, 11, 90]  # Sukuriame pavyzdinį elementų sąrašą
sorted_list = bubble_sort(my_list)  # Iškviečiame rikiavimo funkciją
print(sorted_list)  # Spausdiname surikiuotą sąrašą