# In `libri.py`:

# 1. Definisci `crea_libro(titolo: str, autore: str, genere: str, copie_disponibili: int) -> dict`:
#    Crea e restituisce un dizionario con i campi `titolo`, `autore`, `genere`, `copie_disponibili`.

# 2. Definisci `info_libro(libro: dict) -> str`:
#    Restituisce una stringa con il formato:
#    `1984 di George Orwell (Fantascienza) - Copie disponibili: 1`

# 3. Definisci `libro_disponibile(libro: dict) -> bool`:
#    Restituisce `True` se il libro ha almeno una copia disponibile.

# Nel `main()` del tuo file principale (`cognome.py`):
# - Crea almeno 4 libri diversi.
# - Stampa le informazioni di ogni libro.

# ---


def crea_libro(titolo: str, autore: str, genere: str, copie_disponibili: int) -> dict:
    libri = {
        "titolo": titolo,
        "autore": autore,
        "genere": genere,
        "copie_disponibili": copie_disponibili
    }

def info_libro(libro: dict) -> str:
    pass

def libro_disponibile(libro: dict) -> bool:
    for libro in libri:
        if libro[copie_disponibili] >= 1:
                 return True
        elif libro[copie_disponibili] < 1:
             return False