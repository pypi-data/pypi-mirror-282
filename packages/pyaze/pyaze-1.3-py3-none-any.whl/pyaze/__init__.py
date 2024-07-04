# SPDX-License-Identifier: MIT
# Author: Teymur Babayev

import colorama
from colorama import Fore
import sys

# Set the encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')
təyinolunmuş = {}

def yaz(*dat):
    dat = ''.join(map(str, dat))
    print(str(dat))

def oxu(ask=""):
    dat = input(ask)
    return dat   

def doğru():
    return True

def yanlış():
    return False

def kömək():
    yaz('''
    Bu funksiya sizə bu modul haqqında məlumat vermək üçündür
    Bu modulda işlədilə bilən funksiyalar:
    - yaz("Mətn") - Mətn yazmaq üçün
    - oxu("Sual") - Klaviaturadan daxil ediləni oxumaq üçün
    - əgər(Şərt, 'funksiya', yoxsa='funksiya') - Şərt yerinə yetirən funksiyaları çağırmaq üçün
    - nəqədərki(Şərt, 'funksiya') - Şərt doğru olduqda funksiyanı təkrarlamaq üçün
    - cəm(ədəd, ədəd) - İki ədədi toplamaq üçün
    - çıx(a, b) - İki ədədi çıxmaq üçün
    - vur(a, b) - İki ədədi vurmaq üçün
    - böl(a, b) - İki ədədi bölmək üçün
    - ədəd("Mətn") - Mətni ədədə çevirmək üçün
    - sətir(ədəd) - Ədədi mətinə çevirmək üçün
    - təyin(dəyişən adı, dəyişənin dəyəri) - Qlobal dəyişən yaratmaq üçün
    - fayl_yaz(fayl_adı, mətn) - Fayla mətn yazmaq üçün
    - fayl_oxu(fayl_adı) - Fayldan mətn oxumaq üçün
    ''')

def təyin(arg, b):
    təyinolunmuş[arg] = b

def cəm(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    else:
        yaz(Fore.RED + 'Pyaze cəm funksiyasında xəta: Sadəcə ədədlər toplanıla bilər')
        yaz(Fore.WHITE + "0")

def çıx(a, b):
    if type(a) == int and type(b) == int:
        return a - b
    else:
        yaz(Fore.RED + 'Pyaze çıx funksiyasında xəta: Sadəcə ədədlər çıxıla bilər')
        yaz(Fore.WHITE + "0")

def vur(a, b):
    if type(a) == int and type(b) == int:
        return a * b
    else:
        yaz(Fore.RED + 'Pyaze vur funksiyasında xəta: Sadəcə ədədlər vurula bilər')
        yaz(Fore.WHITE + "0")

def böl(a, b):
    if type(a) == int and type(b) == int:
        try:
            return a / b
        except ZeroDivisionError:
            yaz(Fore.RED + 'Pyaze böl funksiyasında xəta: 0-a bölmə mümkün deyil')
            yaz(Fore.WHITE + "0")
    else:
        yaz(Fore.RED + 'Pyaze böl funksiyasında xəta: Sadəcə ədədlər bölünə bilər')
        yaz(Fore.WHITE + "0")

def ədəd(dat):
    try:
        return int(dat)
    except ValueError:
        yaz(Fore.RED + f'Pyaze ədəd funksiyasında xəta: {dat} ədədə çevrilə bilmir')
        yaz(Fore.WHITE + "0")
        return None

def sətir(dat):
    return str(dat)

def əgər(cond, funk, yoxsa=None):
    if cond:
        exec(funk)
    elif yoxsa is not None:
        exec(yoxsa)

def nəqədərki(cond, funk):
    while cond:
        exec(funk)

def fayl_yaz(fayl_adı, mətn):
    try:
        with open(fayl_adı, 'w', encoding='utf-8') as f:
            f.write(mətn)
    except Exception as e:
        yaz(Fore.RED + f'Pyaze fayl yazma funksiyasında xəta: {e}')
        yaz(Fore.WHITE + "0")

def fayl_oxu(fayl_adı):
    try:
        with open(fayl_adı, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        yaz(Fore.RED + f'Pyaze fayl oxuma funksiyasında xəta: {e}')
        yaz(Fore.WHITE + "0")
        return None
