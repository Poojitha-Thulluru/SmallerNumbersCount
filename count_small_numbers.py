
def get_small_numbers_array(nums_array: list) -> list:
    counts = []
    for index in range(len(nums_array)):
        count = 0
        if index == len(nums_array):
            count = 0
        for j in range(index+1, len(nums_array)):
            if nums_array[index] > nums_array[j]:
                count += 1
        counts.append(count)
    return counts


try:
    num_array = list(map(int, input("Enter integers separated by space : ").split()))
    print("The output array is : ", get_small_numbers_array(num_array))
except ValueError:
    print("Invalid Input, Please enter only integer")
