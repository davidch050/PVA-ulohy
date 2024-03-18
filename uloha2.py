def jsou_kolinearni(A, B, C):
    return (B[1] - A[1]) * (C[0] - B[0]) == (C[1] - B[1]) * (B[0] - A[0])

def stred(Bod_A, Bod_B, Bod_C):
    if jsou_kolinearni(Bod_A, Bod_B, Bod_C):
        if Bod_A[0] <= Bod_B[0] <= Bod_C[0] or Bod_C[0] <= Bod_B[0] <= Bod_A[0]:
            return Bod_B
        elif Bod_B[0] <= Bod_A[0] <= Bod_C[0] or Bod_C[0] <= Bod_A[0] <= Bod_B[0]:
            return Bod_A
        else:
            return Bod_C
    else:
        return None

def zpracuj_vstup(vstupni_text):
    try:
        souradnice = [float(souradnice) for souradnice in vstupni_text.split()]
        if len(souradnice) != 2:
            raise ValueError("Neplatný formát vstupu")
        return tuple(souradnice)
    except ValueError:
        raise ValueError("Neplatný formát vstupu")

def main():
    try:
        bod = lambda nazev: zpracuj_vstup(input(f"{nazev}:\n"))
        A, B, C = bod("Bod A"), bod("Bod B"), bod("Bod C")

        if len(set([A, B, C])) < 3:
            print("Některé body splývají.")
        elif jsou_kolinearni(A, B, C):
            print("Body leží na jedné přímce.")
            stredni_bod = stred(A, B, C)
            if stredni_bod:
                print(f"Střední bod je {'A' if stredni_bod == A else 'B' if stredni_bod == B else 'C'}.")
        else:
            print("Body neleží na jedné přímce.")
    except ValueError as e:
        print("Chyba:", e)

if __name__ == "__main__":
    main()

