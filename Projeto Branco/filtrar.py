def contains(arr, valor, rm=False):
    for index in range(len(arr)):
        if arr[index]["id"] == valor:
            if rm:
                return index
            else:
                return True
    return False
