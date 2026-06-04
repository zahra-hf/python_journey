#Write a program that receives the purchase amount from the user and displays the final amount.

amount = int(input())
if amount > 50000:
    final_amount = amount * 0.8
elif 20000 <= amount <= 50000:
    final_amount = amount * 0.9
else:
    final_amount = amount
    
print(int(final_amount))