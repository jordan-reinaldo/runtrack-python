def arrondir_notes(notes):
   
    notes_arrondies = []
    for note in notes:
        # Échec si la note est inférieure à 40
        if note < 40:
            notes_arrondies.append(note)
            continue

        # Trouver le prochain multiple de 5
        prochain_multiple_de_5 = ((note // 5) + 1) * 5

        # Arrondir la note si elle est à moins de 3 points du prochain multiple de 5
        if prochain_multiple_de_5 - note < 3:
            notes_arrondies.append(prochain_multiple_de_5)
        else:
            notes_arrondies.append(note)

    return notes_arrondies

exemple_notes = [33, 38, 73, 67, 40, 82, 83]
notes_arrondies = arrondir_notes(exemple_notes)
print(exemple_notes)
print(notes_arrondies)

