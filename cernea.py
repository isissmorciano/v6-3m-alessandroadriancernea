def main():
    from biblioteca import libri
    from biblioteca.libri import crea_libro, info_libro
    
    # l1 = {
    #     "titolo": "Borbadamenti",
    #     "autore": "Trump",
    #     "genere": "nuovo",
    #     "copie_disponibili": 14
    # }
    
    l1: dict = crea_libro(titolo="1984", 
                    autore="George Orwell",  
                    genere="Fantascienza",  
                    copie_disponibili=1, 
                    )

    print(l1)


    l1_stringa: str = info_libro(libro=l1)
    print(l1_stringa)

    l2: dict = crea_libro(titolo="Dragonball",
                    autore="Goku",
                    genere="Manga",
                    copie_disponibili=5
                    )
    
    print(l2)

    l2_stringa: str =info_libro(libro=l2)
    print(l2_stringa)

    l3: dict = crea_libro(titolo="gesu",
                    autore="dio",
                    genere="reale",
                    copie_disponibili=6
                    )
    
    print(l3)

    l3_stringa: str = info_libro(libro=l3)
    print(l3_stringa)

    l4: dict = crea_libro(titolo="Ricetta",
                    autore="Mamma",
                    genere="Librocibo",
                    copie_disponibili=1
                    )
    
    print(l4)

    l4_stringa: str = info_libro(libro=l4)
    print(l4_stringa)

    utenti: dict = {
        "nome e cognome"
        "Giorgio": "frigo",
        "Carmelo": "fighello",
        "Rtx5090": "espensivo"
    }












if __name__ == "__main__":
    main()