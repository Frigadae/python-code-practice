"""
Selection sort and Bubble sort
"""

def selectSort(array):
    for i in range(len(array)):
        min = i
        #find the min value
        for j in range(i+1, len(array)):
            if array[j] < array[min]:
                min = j
        #swap
        if min != i:
            temp = array[i]
            array[i] = array[min]
            array[min] = temp
    return array

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array)-i-1):
            #if next val is smaller, swap the cells
            if array[j] > array[j+1]:
                array[j+1], array[j] = array[j], array[j+1]
    return array

def main():
    array = [4,3,2,6,5,1]
    result = selectSort(array)
    print("output: ", result)
    print()
    print("---")
    print()
    array = [4,3,2,6,5,1]
    result = bubbleSort(array)
    print("output: ", result)
    
main()
