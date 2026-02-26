'''26/02/26

10. Given integer coordinates of three vertices of a rectangle whose sides are parallel to the coordinate axes, 
find the coordinates of the fourth vertex of the rectangle. In the first test the three given vertices are 
(1, 4), (1, 6), (7, 4). The fourth vertex is thus (7, 6).'''

# Input coordinates
x1 = int(input("Enter x coord of 1st Vertice"))
y1 = int(input("Enter y coord of 1st Vertice")) 
x2 = int(input("Enter x coord of 2nd Vertice"))
y2 = int(input("Enter y coord of 2nd Vertice"))
x3 = int(input("Enter x coord of 3rd Vertice"))
y3 = int(input("Enter y coord of 3rd Vertice")) 

# The fourth vertex is simply the XOR of the three knowns
x4 = x1 ^ x2 ^ x3
y4 = y1 ^ y2 ^ y3

print(f"The fourth vertex is: ({x4}, {y4})")