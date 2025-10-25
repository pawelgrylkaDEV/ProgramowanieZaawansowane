import math

list_imiona = ["Anna", "Bartek", "Kasia", "Piotr"]
list_oceny = [4.5, 3.0, 5.0, 4.0]

polaczone_dane = list(zip(list_imiona, list_oceny))
print(f"Polaczone dane (zip): {polaczone_dane}")

print("-" * 30)

print("Obliczanie pierwiastka kwadratowego (math.sqrt()):")

try:
    przykładowa_liczba_str = input("Podaj liczbe nieujemna do obliczenia pierwiastka: ")
    przykładowa_liczba = float(przykładowa_liczba_str)

    if przykładowa_liczba < 0:
        raise ValueError("Nie mozna obliczyc pierwiastka kwadratowego z liczby ujemnej.")

    wynik_pierwiastek = math.sqrt(przykładowa_liczba)

    print(f"Pierwiastek kwadratowy z {przykładowa_liczba} wynosi: {wynik_pierwiastek}")

except ValueError as e:
    print(f"\nBlad (Wyjatek ValueError): {e}")
    print("Upewnij sie, ze wprowadzasz poprawna liczbe nieujemna.")

except KeyboardInterrupt:
    print("\n\nOperacja przerwana przez uzytkownika.")

finally:
    print("-" * 30)
    print("Koniec sekcji testowej modulu math i obslugi wyjatkow.")