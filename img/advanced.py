import random
import time

def password_generator(pass_count, pass_length):
    """
    Bu fonksiyon belirtilen sayıda ve belirtilen uzunlukta şifre üretir.
    :param pass_count: Oluşturulacak şifre sayısı
    :param pass_length: Oluşturulacak şifre uzunluğu
    :return: Belirtilen sayıda ve uzunlukta şifre listesi
    """
    s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
    password_list = []
    for i in range(pass_count):
        password = "".join(random.sample(s, pass_length))
        password_list.append(password)
    return password_list

def write_to_file(passwords):
    """
    Bu fonksiyon oluşan şifre listesini dosyaya yazar
    :param passwords: Oluşan şifre listesi
    """
    current_time = time.strftime("%Y-%m-%d_%H-%M-%S", time.gmtime())
    filename = "generated_passwords_" + current_time + ".txt"
    with open(filename, "w") as f:
        f.write("Şifreler " + current_time + " tarihinde oluşturuldu\n")
        for i, password in enumerate(passwords):
            f.write(f"Şifre {i + 1}: {password}\n")
        print(f"Şifreler {filename} dosyasına kaydedildi.")

def main():
    pass_count = int(input("Kaç adet şifre oluşturmak istersiniz: "))
    pass_length = int(input("Şifre uzunluğu kaç karakter olmalı: "))
    passwords = password_generator(pass_count, pass_length)
    for i, password in enumerate(passwords):
        print(f"Şifre {i + 1}: {password}")
    write_to_file(passwords)

if __name__ == "__main__":
    main()
