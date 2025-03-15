python_arr=[0, 0, 0, 0, 0, 47, 0, 16, 1, 4, 0, 20, 40, 0, 0, 0, 0, 1, 0, 0, 1, 247, 160, 0, 3, 134, 160, 0, 1, 7, 208, 0, 0, 5, 220, 0, 0, 3, 232, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
cpp=[0,0,0,0,0,47,0,16,1,4,0,20,40,0,0,0,0,1,0,0,1,0,160,0,0,134,160,0,1,7,208,0,0,5,220,0,0,3,232,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


for i in range(len(python_arr)):
    if python_arr[i]!=cpp[i]:
        print(f"index {i} is different: python={python_arr[i]}, cpp={cpp[i]}")

print(f"python length={len(python_arr)}, cpp length={len(cpp)}")

print(f"python_arr[21,22,23,24]={python_arr[21:25]}")
print(f"cpp[21,22,23,24]={cpp[21:25]}")

def decimal_to_hexadecimal(value):
        byte_array = value.to_bytes(4, byteorder='big')
        # print(hex(byte_array[0]))
        # print(hex(byte_array[1]))
        # print(hex(byte_array[2]))
        # print(hex(byte_array[3]))
        return byte_array

print(decimal_to_hexadecimal(260000))