# Liste oluşturmak
mylist = [1, 2, 3, 4,]
print(mylist)
print(type(mylist))

#listenin uzunluğu
print(f"listenin uzunluğu:"{len(mylist)})

#Listeler içeriğinde farklı sınıflardan örneklendirilen nesneleri barındırabilir.

empty_list = []
one_element = ["one"]
mixed_list = ["one", 2, 3.4, True, False, None, 1j, [1, [1, 2]], (2, 3), {"key": "value"}, range(1,10)]

# Listenin elemanlarına erişme (indexing)
print(mixed_list[0])
print(mixed_list[0][2])
print(mixed_list[7][1][1])
print(mixed_list[9]["key"].title())
print(mixed_list[9]["key"].title()[:3])

#Listede birden çok elemana erişmek (Range Of Indexes)
print(mixed_list[:2])
print(mixed_list[3:5])
print(mixed_list[1:7:2])


lists_in_list = [
    [
        [1,2],
        [3,4],
    ],
    [
        [5,6],
        [7,8]
    ]
]
print(type(lists_in_list))
print(len(lists_in_list))
print(len(lists_in_list[1]))
print(len(lists_in_list[1][0]))
print(lists_in_list[1][0][1])

# List eddition
list1 = [4, 8]
list2 = [6, 2]
print(list1 + list2)
print([list1, list2])
print(list1 + list2 +list1)
print(list1 + list2 +list1 + 5)
print(list1 + list2 +list1 + [5])

# Liste elemanı değiştrme
first_list = ["orange", "apple"]
second_list =["grapes", "avocado"]

first_list[0] = "banana"
print(first_list)

fruit_list = first_list + second_list

fruit_list[1:3] =["cherry", "melon"]

fruit_list[1:3] = ["watermelon"]

print(fruit_list)

fruit_list += ["orange"]

fruit_list += "orange"
fruit_list += 5 # TypeError: 'int' object is not interable

numbers = [1, 2, 3, 4, 5]
numbers += 1
#Yukarıdaki toplama işlemi numpy kütüphanesi ile yapılabilir

import numpy

numbers_array = np.array(numbers)
numbers_array += 1


# Listeden eleman silme

print(numbers)
del numbers[3]
print(numbers)

# Aritmetik işlemler
scores = [90, 55, 67, 88, 100, 22, 34]

print(len(scores)) #n = 7
print(max(scores))
print(min(scores))
print(sum(scores))

print(round(sum(scores)) / len(scores), 2)

import math
import statistics

help(math)
help(statistics)

statistics.mean(scores)
statistics.median(scores)
statistics.mode(scores)

from statistics import mean, median, mode
print(f"Mean: {round(mean(scores), 2)}\nMedian: {median(scores)}\nMode: {mode(scores)}")

from numpy import mean, std, var, median, percentile
print(np.mean(scores))
print(np.std(scores))
print(np.var(scores))
print(np.median(scores))
print(np.percentile(scores))