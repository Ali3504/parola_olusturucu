import random
a = int(input("Şifre kaç basamaklı olsun"))
karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
parola = ""
for i in range(a):
    parola += (random.choice(karakter))

print(parola)   
    
    
