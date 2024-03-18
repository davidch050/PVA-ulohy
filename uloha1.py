def jsou_platne_vstupy(delka_krychle, bod1, bod2):
    if not (isinstance(delka_krychle, int) and delka_krychle > 0):
        return False
    for bod in (bod1, bod2):
        if not all(isinstance(hodnota, int) for hodnota in bod):
            return False
        if not all(0 <= hodnota <= delka_krychle for hodnota in bod):
            return False
    return True

def spocitej_vzdálenost(delka_krychle, bod1, bod2):
    if not jsou_platne_vstupy(delka_krychle, bod1, bod2):
        print("Neplatný vstup. Zadejte prosím platné číselné hodnoty.")
        return

    if delka_krychle not in (bod1[2], bod2[2]):  
        return sum(abs(x - y) for x, y in zip(bod1, bod2))  
    else:  
        mozne_cesty = [
            (delka_krychle - bod1[1]) + (delka_krychle - bod2[1]) + abs(bod1[0] - bod2[0]), 
            bod1[1] + bod2[1] + abs(bod1[0] - bod2[0]), 
            (delka_krychle - bod1[0]) + (delka_krychle - bod2[0]) + abs(bod1[1] - bod2[1]),
            bod1[0] + bod2[0] + abs(bod1[1] - bod2[1])
        ]
        return min(mozne_cesty)

def main():
    try:
        delka_krychle = int(input("Zadejte velikost krychle: "))
        bod1 = [int(input(f"Zadejte souřadnici {osa} pro bod 1: ")) for osa in "xyz"]
        bod2 = [int(input(f"Zadejte souřadnici {osa} pro bod 2: ")) for osa in "xyz"]
    except ValueError:
        print("Neplatný vstup. Zadejte prosím platné číselné hodnoty.")
    else:
        print(spocitej_vzdálenost(delka_krychle, bod1, bod2))

if __name__ == "__main__":
    main()

