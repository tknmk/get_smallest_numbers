import sys

# sample lists
num_1 = [1,2,3,1,4,6]
num_2 = [1,2,3,5]
num_3 = [-1,-2,-3]



def print_smallest_nums(arr):

    arr_size = len(arr)
    if arr_size < 2:
        print ("Invalid Input")
        return

    first = second = sys.maxsize
    for i in range(0, arr_size):

        if arr[i] < first:
            second = first
            first = arr[i]

        elif (arr[i] < second and arr[i] != first):
            second = arr[i];

    if (second == sys.maxsize):
        print ("There is No second smallest number.")
    else:
        print ('The smallest numnber is',first,'and' \
              ' second smallest number is',second)


print_smallest_nums(num_3)
