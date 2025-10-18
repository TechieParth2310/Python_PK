# 2. Movie Ticket Pricing

# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.

UserAge = int(input('Pls Enter your age :- '))
Day = input("Enter The Day u want a ticket :- ")
price = 12 if UserAge>=18 else 8
# Adult_Price = 12;
# Children_Price = 8;
discount = 2;

if(UserAge>18):
    if(Day=='Wednesday'):
        print(f"Movie ticket price is ${price-discount}")
    else:
        print(f"Movie ticket price is ${price}")
else:
    if(Day=='Wednesday'):
        print(f"Movie ticket price is ${price-discount}")
    else:
        print(f"Movie ticket price is ${price}")
