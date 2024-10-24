import os
plik_nazwa = "Plik.txt"

# Bezwzględna ścieżka skryptu, który jest uruchamiany
bezwzgledna_sciezka_z_plikiem = os.path.abspath(__file__)
bezwzgledna_sciezka_bez_pliku = os.path.dirname(bezwzgledna_sciezka_z_plikiem) 
print(bezwzgledna_sciezka_z_plikiem)
print(bezwzgledna_sciezka_bez_pliku)

#utworzenie pliku txt

# #przypisanie do zmiennej plik wyniku funkcji open
# # plik = open("Plik.txt") #tak domyślnie otwiera plik do odczytu
# # print(plik)
# #do zapisu z parametrem "w" jak write z czyszczeniem tego co było wcześniej zawarte
# plik = open(bezwzgledna_sciezka_bez_pliku + "\Plik.txt", "a") #tryb a - append czyli dołączać. Będziemy nadpisywać plik
# plik = open("Plik.txt", "w")
# print(plik.writable()) #funkcja zwraca czy obiekt plik jest możliwy do zapisu

# if plik.writable():
#     plik.write(input("Wprowadź tekst ") + "\n")

# #zapisanie w zmiennej ilosci wprowadzonych znaków
# if plik.writable():
#     ileZnakow = plik.write(input("Wrzuć tekst") + "\n")
#     print("znaków we wprowadzonym wyrazie: ", ileZnakow)

#zamknięcie pliku dla zwolnienia pamięci
# plik.close()

#odczyt zawartosci pliku
# plik = open(bezwzgledna_sciezka_bez_pliku + "\\Plik.txt", "r")
# if plik.readable():
#    tekst = plik.read()
#    print(tekst)
# print("--- \n")
# plik.close()

# # inne sposoby odczytu pliku. Tworzenie listy
# plik = open(bezwzgledna_sciezka_bez_pliku + '\\Plik.txt', "r")
# if plik.readable():
#    print("Zawartosc pliku: ")
#    tekst = plik.readlines()
#    print(tekst)
# # petla dla wyswietlania zawartosci w pliku
# for l in tekst:
#    print(l)

# sposob na liste z użyciem for
plik = open(bezwzgledna_sciezka_bez_pliku + '\\Plik.txt', "r")
if plik.readable():
    print("Zawartość plikuu: ")
    for l in plik:
        print(l)


print(plik.readlines()) #zmienna plik już została zczytana dlatego zwraca pustą listę
plik.close()
