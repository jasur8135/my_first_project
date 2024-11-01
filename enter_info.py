"""Salom bu dastur oila azolarini royhatga oladi"""
from idlelib.iomenu import encoding


def enter_safe_mem(fay_name):
    m=1
    with open(fay_name, 'a', encoding='utf-8') as file:
        print(f'Siz hozir oila azolarini royhatga olish dasturidasiz!')
        n=int(input(f'Iltimos oilangizda nechta azo borligini kiriting:  '))

        while m<(n+1):
            ism = input('{m}-azoning ismini kiriting: ').title()
            familiya = input('{m}-azoning familiyasini kiriting: ').title()
            yosh = input('{m}-azoning yoshini kiriting: ')
            joy= input('{m}-azoning yashash joyini kiriting: ').title()
            qiziqishlari = input("{m}-azoning qiziqishlarini kiriting (vergul bilan ajrating): ")

            # Ma'lumotlarni faylga yozish
            file.write(f"Ism: {ism}\n")
            file.write(f"Familiya: {familiya}\n")
            file.write(f"Yosh: {yosh}\n")
            file.write(f"Yashash joyi: {joy}\n")
            file.write(f"Qiziqishlari: {qiziqishlari}\n")
            file.write("\n")  # Yangi yozuv uchun bo'sh satr
            m=m+1

    print("Ma'lumotlar muvaffaqiyatli saqlandi.")


