#SPDX-License: MIT
#Author: Teymur babayev
from re import A
import colorama
from colorama import Fore
import locale
import sys
# Set the encoding to UTF-8
sys.stdout.reconfigure(encoding='utf-8')
təyinolunmuş = {}
def yaz(*dat):
    dat = ''.join(map(str, dat))
    print(str(dat))

def oxu(ask = ""):
    dat = input(ask)
    return dat   


def doğru():
    return True
def yanlış():
        return False

def kömək():
    yaz('''Bu funksiya sizə bu modul haqqında məlumat vermək üçündü
        By sayda deyilən funsiyaları işlətmək üçün axırlarına () qoyun
        məsələn: yaz('Salam')
        Burada 'Salam' arqumentdi və yaz funksiyadı
        Bəzi funksiyalarda arqument boş qala bilər(məsələn: oxu() funksiyası istifadəçinin yazdığını oxumaq üçündü) vəya birdən çox arqument(məsələn: ) ola bilər
        Bütün funksiyalar:
        yaz("Mətn") yazmaq üçün
        oxu("Sual") klaviaturada yazanı oxumaq üçün
        əgər(Şərt,'funksiya', yoxsa='funksiya') şərt düzəltmək üçün
        nəqədərki(Şərt,'funksiya') şərtli dövrlər yaratmaq üçün
        cəm(ədəd,ədəd) iki ədədi toplamaq üçündür
        ədəd("ədəd") Mətni ədədə çevirmək üçün
        sətir(ədəd) ədədi sətirə çevirmək üçün
        doğru(Misal) Misalın doğruluğunu təkrarlamaq üçün məs. (n=1)=doğru()
        yanlış(Misal) Misalın yanlışlığını təkrarlamaq üçün məs. (n=1)=yanlış()
        təyin(dəyişən adı, dəyişənin dəyəri) - qlobal obyekt yaratmaq üçün , qlobal obyekti çağırmaq üçün təyinolunmuş['dəyişən adı']
        ''')
def təyin(arg,b):
   təyinolunmuş[arg] = b
   
def cəm(a,b):
    if type(a) == int and type(b) == int:
        return a+b
    else:
        print(Fore.RED + 'Pyaze cəm funksiyasında xəta: Sadəcə ədədlər toplanıla bilər')
        print(Fore.WHITE + "0")

def ədəd(dat):
    try:
        a =  int(dat)
    except:
        print(Fore.RED + f'Pyaze ədəd funksiyasında xəta: {dat} ədədə çevrilə bilmir')
        print(Fore.WHITE + "0")
        a = None
    return a
def sətir(dat):
    return str(dat)
def əgər(cond,funk, yoxsa = None):
    if (cond):
        exec(funk)
    elif yoxsa != None:
        exec(yoxsa)

def nəqədərki(cond,funk):
    while cond:
        exec(funk)