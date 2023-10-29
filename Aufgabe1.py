# die von der aufgabe vorgegebenen werte
mathematik = [80, 85, 90, 78, 92, 88, 76, 89, 95, 82]
physik = [75, 88, 82, 79, 91, 86, 77, 90, 94, 81]
chemie = [70, 84, 88, 76, 89, 82, 74, 87, 92, 79]

summe_mathematik = sum(mathematik)
anzahl_schueler_mathematik = len(mathematik)
durchschnitt_mathematik = summe_mathematik / anzahl_schueler_mathematik

summe_physik = sum(physik)
anzahl_schueler_physik = len(physik)
durchschnitt_physik = summe_physik / anzahl_schueler_physik

summe_chemie = sum(chemie)
anzahl_schueler_chemie = len(chemie)
durchschnitt_chemie = summe_chemie / anzahl_schueler_chemie

print("Durchschnittsnote Mathematik:", durchschnitt_mathematik)
print("Durchschnittsnote Physik:", durchschnitt_physik)
print("Durchschnittsnote Chemie:", durchschnitt_chemie)

beste_mathematik = max(mathematik)
schlechteste_mathematik = min(mathematik)
beste_physik = max(physik)
schlechteste_physik = min(physik)
beste_chemie = max(chemie)
schlechteste_chemie = min(chemie)

print("Beste Note Mathematik:", beste_mathematik)
print("Schlechteste Note Mathematik:", schlechteste_mathematik)
print("Beste Note Physik:", beste_physik)
print("Schlechteste Note Physik:", schlechteste_physik)
print("Beste Note Chemie:", beste_chemie)
print("Schlechteste Note Chemie:", schlechteste_chemie)

gesamtdurchschnitt = (durchschnitt_mathematik + durchschnitt_physik + durchschnitt_chemie) / 3

print("Gesamtdurchschnittsnote:", gesamtdurchschnitt)
