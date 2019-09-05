# Program to find the sum of Diagonals in a Square Matrix

a = [[1,2,3], 
     [4,5,6], 
     [7,8,9]]
a_len = len(a)  
a_down=0
a_up=0

for x in range(a_len):
    for y in range(a_len):
        # a_down only in case of a00, a11, a22
        # Condition: first and second index are always equal
        if x == y:
            a_down = a_down + (a[x][y])
        # a_up only in case of a02, a11, a20
        # Condition: first and second index always sums up as the length of array minus 1
        if x + y == a_len-1:
            a_up = a_up + (a[x][y])
            
print(a_down)
print(a_up)
