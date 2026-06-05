def maxSubarraySum(arr):
    current_sum = arr[0]
    max_sum = arr[0]

    for i in range(1,len(arr)):
        current_sum = max(arr[i] ,current_sum + arr[i])
        max_sum = max(current_sum,max_sum)

    return max_sum

if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    print(arr)
    print(maxSubarraySum(arr))