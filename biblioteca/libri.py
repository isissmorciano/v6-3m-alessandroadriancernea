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
    return {
        "titolo": titolo,
        "autore": autore,
        "genere": genere,
        "copie_disponibili": copie_disponibili
    }

def info_libro(libro: dict) -> str:
    libro = {
        "titolo": "",
        "autore": "George Orwell",
        "genere": "Fantascienza",
        "copie_disponibili": 1
    }
    return libro

def libro_disponibile(libro: dict) -> bool:
    for libro in libri:
        if libro["copie_disponibili"] >= 1:
                 return True
        elif libro["copie_disponibili"] < 1:
             return False
        


# In `libri.py`:

# 1. Definisci `filtra_per_genere(libri: list[dict], genere: str) -> list[dict]`:
#    Restituisce una nuova lista con solo i libri che appartengono al genere indicato.

# 2. Definisci `libri_disponibili(libri: list[dict]) -> list[dict]`:
#    Restituisce una nuova lista con solo i libri che hanno copie disponibili.

# 3. Definisci `cerca_per_autore(libri: list[dict], autore: str) -> list[dict]`:
#    Restituisce una nuova lista con i libri scritti dall'autore indicato.

# Nel `main()`:
# - Filtra i libri di un genere specifico e stampa i titoli.
# - Stampa i titoli dei libri disponibili.
# - Cerca i libri di un autore e stampa i titoli trovati.

# ---


def filtra_per_genere(libri: list[dict], genere: str) -> list[dict]:
     tipo = []
     chiedere = str(input("Che genere di libro cerchi?: ")).lower()
     if chiedere == tipo:
        for libro in libri:
            if libro["genere"] == tipo:
                tipo == libro["genere"]
                tipo += 1
            elif libro["genere"] != tipo:
                tipo == 1

def libri_disponibili(libri: list[dict]) -> list[dict]:
     lista = []
     chiedere = str(input("Che libro stai cercando?: "))
     for i in chiedere:
        if libri["copie_disponibili"] >= 1:
            lista += 1
        elif libri["copie_disponibili"] == 1:
            lista == 1

def cerca_per_autore(libri: list[dict], autore: str) -> list[dict]:
     pass