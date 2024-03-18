def je_palindrom(text):
    return text == text[::-1]

def najdi_dalsi_palindrom(od_cisla, soustava, dalsi_palindrom):
    if soustava < 2 or soustava > 36:
        return 0

    cislo = od_cisla + 1
    while True:
        cislo_text = format(cislo, '0' + str(soustava))
        if je_palindrom(cislo_text):
            dalsi_palindrom[0] = cislo
            return 1
        cislo += 1

od_cisla = 12
soustava = 7
dalsi_pal = [0]
uspech = najdi_dalsi_palindrom(od_cisla, soustava, dalsi_pal)
if uspech:
    print("Nalezený palindrom:", dalsi_pal[0])
else:
    print("Nepodařilo se najít palindrom.")
