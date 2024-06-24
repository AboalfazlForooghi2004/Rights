def hoghoghe(saat , poole):

    if saat > 8:
        return "errore! khaili kar mi koni"
    elif poole < 2 :
        return "khai kam hoghoghe megiri"
    else:
        koldaranad = saat * poole
        return koldaranad

a =int(input("plese saat "))
b = int(input("plese poole "))
saat = a
poole = b
print(hoghoghe(saat,poole))
