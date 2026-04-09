# In `prestiti.py` (usa `from .libri import info_libro, libro_disponibile`):

# 1. Definisci `crea_utente(nome: str, cognome: str) -> dict`.
# 2. Definisci `crea_biblioteca() -> dict`:
#    Restituisce un dizionario con i campi `libri` (lista) e `prestiti` (dizionario).
# 3. Definisci `aggiungi_libro(biblioteca: dict, libro: dict) -> None`.
# 4. Definisci `presta_libro(biblioteca: dict, utente: dict, libro: dict) -> bool`:
#    Se il libro è disponibile decrementa le copie, registra il prestito e restituisce `True`.
#    Se non ci sono copie disponibili, restituisce `False`.
# 5. Definisci `restituisci_libro(biblioteca: dict, utente: dict, libro: dict) -> bool`:
#    Se l'utente ha preso in prestito quel libro, lo rimuove e restituisce la copia alla biblioteca.
#    Altrimenti restituisce `False`.

# Nel `main()`:
# - Crea almeno 3 utenti.
# - Crea una biblioteca e aggiungi i libri.
# - Presta un libro esaurito e stampa il risultato.
# - Stampa l'informazione del libro dopo il prestito.

# ---

def crea_utente(nome: str, cognome: str) -> dict:
    try:
        nome = str(input("Come ti chiami: "))
        cognome = str(input("Qual'è il tuo cognome: "))
    except ValueError:
        print("Deve essere una stringa valida")

def crea_biblioteca() -> dict:
    pass