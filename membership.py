membership = input("тип членство(золото , серебро , обычный,)")
amount = float(input("Сумма покупки:"))
discount = 0
if membership == "золото":
   if amount > 100:
       discount = 0.20
   else:
       discount = 0.10
elif membership == "серебро":
   if amount > 100:
       discount = 0.15
   else:
       discount = 0.5
elif membership == "обычный":
   if amount > 100:
       discount = 0.5
   else:
       discount = 0
else:
       discount = 0
       print("не корректный тип членства")
print(f"Ваша скидка:{amount * discount}")
