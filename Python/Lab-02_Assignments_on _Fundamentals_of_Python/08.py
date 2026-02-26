#26-02-2026
'''8. A school decided to replace the desks in three classrooms. Each desk sits two students. 
Given the number of students in each class, print the smallest possible number of desks that can be purchased. 
The program should read three integers: the number of students in each of the three classes, a, b and c respectively. 
In the first test there are three groups. The first group has 20 students and thus needs 10 desks. 
The second group has 21 students, so they can get by with no fewer than 11 desks. 
11 desks is also enough for the third group of 22 students. So we need 32 desks in total.'''

a = int(input("Number of students in class 1: "))
b = int(input("Number of students in class 2: "))
c = int(input("Number of students in class 3: "))

no_of_desk_a = (a//2)+(a%2)
no_of_desk_b = (b//2)+(b%2)
no_of_desk_c = (c//2)+(c%2)

print("Total number of benches required: ",no_of_desk_a+no_of_desk_b+no_of_desk_c)