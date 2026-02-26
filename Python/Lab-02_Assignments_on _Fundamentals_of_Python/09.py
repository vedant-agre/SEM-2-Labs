'''26/02/2026

H hours, M minutes and S seconds are passed since the midnight 
(0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60). 
Determine the angle (in degrees) of the hour hand on the clock face right now.'''


h = int(input())
m = int(input())
s = int(input())


angle = (h * 30) + (m * 0.5) + (s * 30 / 3600)

print(angle)