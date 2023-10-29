# die von der aufgabe vorgegebenen werte
mathematik = [80, 85, 90, 78, 92, 88, 76, 89, 95, 82]
physik = [75, 88, 82, 79, 91, 86, 77, 90, 94, 81]
chemie = [70, 84, 88, 76, 89, 82, 74, 87, 92, 79]

notenstatistik_mathematik = 0
for note in mathematik:
        if note >= 90:
            notenstatistik_mathematik += 1

notenstatistik_physik = 0
for note in physik:
        if note >= 90:
            notenstatistik_physik += 1

notenstatistik_chemie = 0
for note in chemie:
        if note >= 90:
            notenstatistik_chemie += 1


print("Anzahl der Schüler mit mindestens 90 in Mathematik:", notenstatistik_mathematik)
print("Anzahl der Schüler mit mindestens 90 in Physik:", notenstatistik_physik)
print("Anzahl der Schüler mit mindestens 90 in Chemie:", notenstatistik_chemie)

notenverteilung_mathematik = {note: mathematik.count(note) for note in set(mathematik)}
notenverteilung_physik = {note: physik.count(note) for note in set(physik)}
notenverteilung_chemie = {note: chemie.count(note) for note in set(chemie)}

print("Notenverteilung Mathematik:", notenverteilung_mathematik)
print("Notenverteilung Physik:", notenverteilung_physik)
print("Notenverteilung Chemie:", notenverteilung_chemie)