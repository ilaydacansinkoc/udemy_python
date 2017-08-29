cevap = input("Üçgen mi, Dörtgen mi?")
if (cevap == "Dörtgen"):
    kenar_1 = float(input("Kenar 1 i giriniz\n"))
    kenar_2 = float(input("Kenar 2 i giriniz\n"))
    kenar_3 = float(input("Kenar 3 i giriniz\n"))
    kenar_4 = float(input("Kenar 4 i giriniz\n"))

    if (kenar_1 == kenar_2 == kenar_3 == kenar_4):
        print("Kare")
    elif ((kenar_1 == kenar_2 or kenar_3 == kenar_4) or
              (kenar_1 == kenar_3 or kenar_2 == kenar_4) or
              (kenar_1 == kenar_4 or kenar_3 == kenar_2)):
        print("Dikdörgen")
    else:
        print("Sıradan Dörtgen")
elif (cevap == "Üçgen"):
    kenar_1 = float(input("Kenar 1 i giriniz\n"))
    kenar_2 = float(input("Kenar 2 i giriniz\n"))
    kenar_3 = float(input("Kenar 3 i giriniz\n"))

    if ((abs(kenar_1 - kenar_2) < kenar_3 < abs(kenar_1 + kenar_2))
        or (abs(kenar_1 - kenar_3) < kenar_2 < abs(kenar_1 + kenar_3))
            or (abs(kenar_3 - kenar_2) < kenar_1 < abs(kenar_3 + kenar_2))):

        if (kenar_1 == kenar_2 == kenar_3):
            print("Eşkenar Üçgen")
        elif ((kenar_1 == kenar_2) or (kenar_1 == kenar_3)):
            print("İkizkenar Üçgen")
        else:
            print("Çeşitkenar Üçgen")
    else:
        print("Üçgen Belirtmez.")