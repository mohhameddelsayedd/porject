def count_sort(input_array):
    M = max(input_array)
    count_array = [0] * (M + 1)
    for num in input_array:
        count_array[num] += 1
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]
    output_array = [0] * len(input_array)
    for i in range(len(input_array) - 1, -1, -1):
        output_array[count_array[input_array[i]] - 1] = input_array[i]
        count_array[input_array[i]] -= 1
    return output_array
if __name__ == "__main__":
    input_array = [2,0,3,1,5,7,9,6,8,4,10]
    output_array = count_sort(input_array)
    for num in output_array:
        print(num, end=" ")
