# Apply a single range update on the difference array
def update(diff, l, r, x):
    print("update1",diff,l,r,x)
    diff[l] += x
    if r + 1 < len(diff):
        diff[r + 1] -= x
    print("update2",diff,l,r,x)


# Apply range updates using difference array technique
def diffArray(arr, opr):
    n = len(arr)

    # Create difference array 
    diff = [0] * n

    # Apply each operation [l, r, val] on the diff array
    for l, r, val in opr:
        update(diff, l, r, val)

    # Build the result by applying prefix sum over diff
    res = arr[:]
    res[0] += diff[0]
    print("\n\n")
    print(res,diff)
    for i in range(1, n):
        print(i,res,diff)
        diff[i] += diff[i - 1]
        print(diff)
        res[i] += diff[i]
        print(res)

    return res

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    opr = [[1, 3, 10], [2, 4, -5]]

    res = diffArray(arr, opr)

    for num in res:
        print(num, end=" ")
    print()