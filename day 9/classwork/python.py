# ლოგიკური ოპერატორები გვაძლევენ საშუალებას შევაერთოთ რამდენიმე პირობა და ისინი აბრუნებენ True ან False მნიშვნელობას.

# და  –აბრუნებს სიმართლეს მაშინ როცა ორივე პირობა მართალია.
# ან  – აბრუნებს სიმართლეს თუნდაც ერთი იყოს მართალი.

name = input("შეიყვანეთ თქვენი სახელი: ")

if name == "ixvi":
    print("სახელი ემთხვევა სიტყვას 'ixvi'")
else:
    print("სახელი არ ემთხვევა სიტყვას 'ixvi'")

    number = int(input("შეიყვანეთ რიცხვი: "))

if number > 50:
    print("რიცხვი მეტია 50-ზე.")
else:
    print("რიცხვი ნაკლებია ან ტოლია 50-ის.")

user_toy = input("შეიყვანეთ თქვენი საყვარელი სათამაშო: ")
my_toy = "lego"

if user_toy == my_toy:
    print("ჩვენ გვიყვარს ერთი და იგივე სათამაშო!")
else:
    print("ჩვენ სხვადასხვა სათამაშოები გვიყვარს.")

    print(True and False and True or False and True and False and True and False or True and False or True or False)

# True and False → False
# False and True → False
# False and True → False
# False and True → False
# False or True → True
# True and False → False
# False or True → True
# True or False → True ანუ იქნება პასუხი სიმართლე