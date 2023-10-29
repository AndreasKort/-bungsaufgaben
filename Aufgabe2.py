def caesar_verschluesseln(text, schluessel):  # Funktion zur Verschlüsselung
    verschluesselter_text = ""  # Erstellen einer leeren Zeichenfolge für den verschlüsselten Text
    for zeichen in text:  # Schleife, die jedes Zeichen in 'text' durchläuft
        if zeichen.isalpha():  # Überprüfen, ob das Zeichen ein Buchstabe ist
            if zeichen.isupper():  # Großbuchstabe oder Kleinbuchstabe?
                verschiebung = 65  # 65 ist der ASCII-Wert für Großbuchstaben 'A'
            else:
                verschiebung = 97  # 97 ist der ASCII-Wert für Kleinbuchstaben 'a'
            verschluesselter_zeichen = chr((ord(zeichen) - verschiebung + schluessel) % 26 + verschiebung)  # Berechnen des verschlüsselten Zeichens
            verschluesselter_text += verschluesselter_zeichen  # Hinzufügen des verschlüsselten Zeichens
        else:
            verschluesselter_text += zeichen  # wenn ein Zeichen kein Buchstabe ist, bleibt es gleich (z.B. '1234' oder ',' oder '.')
    return verschluesselter_text  # Rückgabe des verschlüsselten Textes, um fortzufahren

def caesar_entschluesseln(verschluesselter_text, schluessel):  # Funktion zur Entschlüsselung
    return caesar_verschluesseln(verschluesselter_text, -schluessel)  # Der Verschlüsselungsschlüssel wird negativ verwendet

def main():  # Benutzerinteraktion
    text = input("Geben Sie den Text ein: ")  # Eingabe des zu verschlüsselnden oder zu entschlüsselnden Textes
    schluessel = int(input("Geben Sie den Verschlüsselungsschlüssel ein (eine ganze Zahl zwischen -25 und +25): "))  # Eingabe des Verschlüsselungsschlüssels
    modus = input("Möchten Sie verschlüsseln oder entschlüsseln? (v/e): ").lower()  # Auswahl des Verschlüsselungs- oder Entschlüsselungsmodus

    if modus == 'v':  # Verschlüsselung des Textes
        verschluesselter_text = caesar_verschluesseln(text, schluessel)
        print("Verschlüsselter Text:", verschluesselter_text)
    elif modus == 'e':
        klartext = caesar_entschluesseln(text, schluessel)  # Entschlüsselung des Textes
        print("Entschlüsselter Text:", klartext)
    else:
        print("Ungültige Eingabe. Bitte wählen Sie 'v' für Verschlüsselung oder 'e' für Entschlüsselung.")

if __name__ == "__main__":
    main()  # Start des Programms hoffendlich
