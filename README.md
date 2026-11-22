# Testowanie i Jakość Oprogramowania

# Autor
Imię i nazwisko: Ilona Hrabovenko

# Temat projektu
Aplikacja do wyszukiwania przepisów na podstawie składników

# Opis projektu
Projekt polega na stworzeniu aplikacji internetowej umożliwiającej wyszukiwanie przepisów kulinarnych na podstawie składników, które użytkownik posiada w domu.

Aplikacja pozwala na:
- wyświetlanie wszystkich dostępnych przepisów,
- wyszukiwanie przepisów na podstawie jednego lub kilku składników,
- wyświetlanie składników potrzebnych do przygotowania potrawy,
- wyświetlanie czasu przygotowania dania,
- wyświetlanie komunikatu w przypadku braku wyników wyszukiwania.

Baza aplikacji zawiera 50 przykładowych przepisów kulinarnych.


# Uruchomienie aplikacji

# Wymagania
- Python 3.10 lub nowszy
- pip

# Instalacja

1. Sklonuj repozytorium:

```bash
git clone ADRES_REPOZYTORIUM
```

2. Przejdź do katalogu projektu:

```bash
cd recipe-search-app
```

3. Utwórz środowisko wirtualne:

```bash
python -m venv .venv
```

4. Aktywuj środowisko wirtualne.

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

macOS / Linux:

```bash
source .venv/bin/activate
```

5. Zainstaluj wymagane biblioteki:

```bash
pip install -r requirements.txt
```

6. Uruchom aplikację:

```bash
python app.py
```