# ==  → ტოლობა
# >   → მეტობა
# <   → ნაკლებობა
# >=  → მეტობა ან ტოლობა
# <=  → ნაკლებია ან ტოლია

print(5 == 5)       # true
print(10 == 3)      # false
print('a' == 'a')   # true
print(3.5 == 3.5)   # true
print('abc' == 'ABC') #false

print(7 > 5)        # True
print(2 > 8)        # False
print(3.5 > 3)      # True
print(10 > 10)      # False
print(-1 > -2)      # True

print(3 < 4)        # True
print(9 < 2)        # False
print(5 < 5)        # False
print(-3 < 0)       # True
print(100 < 101)    # True

print(5 >= 5)       # True
print(6 >= 2)       # True
print(4 >= 5)       # False
print(3.3 >= 3.3)   # True
print(-1 >= -1)     # True

print(5 <= 6)       # True
print(9 <= 8)       # False
print(10 <= 10)     # True
print(-2 <= -1)     # True
print(0 <= 0)       # True

# ლოგიკური ოპერატორები გვაძლევენ საშუალებას შევაერთოთ რამდენიმე  პირობა და ისინი აბრუნებენ True ან False მნიშვნელობას.

# და  –აბრუნებს სიმართლეს მაშინ როცა ორივე პირობა მართალია.
# ან  – აბრუნებს სიმართლეს თუნდაც ერთი იყოს მართალი.

print(5 > 3 and 4 > 2)    # True and True → True
print(10 == 10 and 2 > 3) # True and False → False
print(1 < 2 and 3 < 1)    # True and False → False

print(5 > 3 or 2 > 10)    # True or False → True
print(10 == 5 or 7 < 2)   # False or False → False
print(3 < 5 or 1 == 1)    # True or True → True

user_number = int(input("შეიყვანეთ რიცხვი: "))
my_number = 10

if user_number > my_number:
    print("თქვენი რიცხვი მეტია 10-ზე.")
else:
    print("თქვენი რიცხვი ნაკლებია ან ტოლია 10-ის.")

