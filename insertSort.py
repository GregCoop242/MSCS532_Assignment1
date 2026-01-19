#Insert Sort in Monotonically Decreasing Order with input array
def insertion_sort_decreasing(arr):


    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


if __name__ == "__main__":
    try:
        array = [int(x) for x in input("Enter whole numbers seperated by commas: ").split(",")]
    except ValueError:
        print("Invalid input. Please enter whole numbers only.")
        exit(1)
    #array = [74, 32, 10000, 19, 1, 3]
    print("Original array:", array)

    sorted_array = insertion_sort_decreasing(array)
    print("Sorted in monotonically decreasing order:", sorted_array)
