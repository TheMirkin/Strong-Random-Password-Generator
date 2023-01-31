import random
pass_length = int(input("Şifre uzunluğu kaç karakter olmalı: "))
s="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
p =  "".join(random.sample(s,pass_length ))
print (p)