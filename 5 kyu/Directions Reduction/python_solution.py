def dirReduc(arr):
    

    i = 0
    while i < len(arr):

        if i != len(arr) - 1:
            if arr[i] == "NORTH" and arr[i + 1] == "SOUTH":
                arr.pop(i + 1)
                arr.pop(i)
                i = 0
            elif arr[i] == "SOUTH" and arr[i + 1] == "NORTH":
                arr.pop(i + 1)
                arr.pop(i)
                i = 0
            elif arr[i] == "EAST" and arr[i + 1] == "WEST":
                arr.pop(i + 1)
                arr.pop(i)
                i = 0
            elif arr[i] == "WEST" and arr[i + 1] == "EAST":
                arr.pop(i + 1)
                arr.pop(i)
                i = 0
            else:
                i += 1
        else:
            return arr
    return arr
