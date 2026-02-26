'''
26/02/26

11. There was a set of cards with numbers from 1 to N. 
One of the card is now lost. Determine the number on that 
lost card given the numbers for the remaining cards.
Given a number N, followed by N − 1 integers - representing the numbers on the remaining cards 
(distinct integers in the range from 1 to N). Find and print the number on the lost card.
'''


n = int(input("Enter N: "))


expected_sum = (n * (n + 1)) // 2


actual_sum = 0
print(f"Enter the {n-1} cards:")
for i in range(n - 1):
    card = int(input())
    actual_sum += card


lost_card = expected_sum - actual_sum

print(f"The lost card is: {lost_card}")