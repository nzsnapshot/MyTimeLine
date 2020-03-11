from random import choice

possibilities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

winning_ticket = [ ]
print("lets see what the winning ticket is")
while len(winning_ticket) < 4:
    pulled_item = choice(possibilities)

    if pulled_item not in winning_ticket:
        print(f"We have pulled a {pulled_item}")
        winning_ticket.append(pulled_item)

print(f"If you your ticket has the following: {winning_ticket}. Congratulations you have won fuckall cunt")



