# Burrows-Wheeler-Transformation 19.-23.07.2021 Programmierkurs

import numpy as np

sequenz = 'TACTGAGAT$'
print(sequenz)
print()
print('1st Step: TRANSFORAMTION')
print('_________________________________')
print('zyklische Verschiebung - Rotation')
print()


# Aufgabe 13
def rotation(String):
    wort = len(String)  # Länge eines Strings
    liste = []
    for i in range(wort):#i-te Stelle meiner Länge meines Strings
        r = String[i:] + String[:i]  # Roationsbefehl - wichtig!
        #fängt von links an zu rotieren
        liste.append(r)# in die leere Liste füllen
        print(r)
    print()

 
    return liste #Ergebnis der Funktion

np.random.randint

x1 = rotation(sequenz) #Call der Funktion

# Schreib zu jeder rotation aus, welche rotationsnummer es war
index = range(len(x1))  # Länge der Sequenz
sortierte_zip_sequenz = sorted(zip(x1, index))  #  rotierte Sequenz und
# index wird ausgegeben - beides sortiert


for x in sortierte_zip_sequenz:  # untereinander stehen, in jeder Zeile ausgegeben
    print(x)


# # diesen Abschnitt würde ich gerne nochmal verstehen
# def lastSortiert(
#         sortierte_sequenz):  # Diese Funktion nimmt die letzten Buchstaben
#     # jeder Zeile raus und fügt diese zusammen
#     string = ""
#     for a in range(len(sortierte_sequenz)):
#         x = sortierte_sequenz[a][0][-1]
#         string += x
#     return string

def lastSortiert(rotierte_sequenzen):
    """gib mir den letzten Buchstaben jeder sequenz aus"""
    result = ''
    for sequenz in rotierte_sequenzen:#Liste der rotierten Sequenzen
        result += sequenz[-1]
        #gib mir den letzten Buchstaben 
        #und füge es dem String hinz

    return result # Ausgabe meiner Funktion

print()
#nur der String wird hier nochmal eingefügt
x1 = []
for tup in sortierte_zip_sequenz:
    # von jedem Tupel nimm den String 
    #und füge der Liste x1 zu
    x1.append(tup[0])
    
# von dieser Liste aus Strings werden die letzten Buchstaben rausgezogen
letzte_Spalte = lastSortiert(x1)  # Call der Funktion



print(letzte_Spalte)

print("_________________________________________")
print()
print("BWT sortiert - Index Nummer")
print()

erste_Spalte = sorted(letzte_Spalte)
# print(erste_Spalte)

for x in erste_Spalte:  # BWT Index Nummer nach alphabet sortiert
    print(x)

print("__________________________________________")
print()
print("BWT - Index Nummer")
print()

for x in letzte_Spalte:  # BWT Index Nummer
    print(x)

print()

print("2nd Step: RÜCKTRANSFORMATION")
print("__________________________________________")
print()


# Aufgabe 16
def find_rep_number(sequenz): #Wiederholungen in der rechten Spalte
#wieviele Buchstaben habe ich jeweils
    """

    RECHTE SPALTE!!!!!!!
    TTGGATAA$C --- [0,1,0,1,0,2,1,2,0,0]  # python zählt ab 0!
    @param sequenz:
    @return:
    """
    # (1) finde die einzigartigen Buchstaben.
    uniques = set(sequenz)# Erzeuge eine Menge der einzigartigen Buchstaben
    #jeder Buchstabe kommt im set nur einmal vor
    

    # (2) erzeuge ein dictionary, mit der Anzahl an "wie oft habe ich den
    # Buchstaben gesehen"
    # Am Anfang 0 mal gesehen
    # ergebnis: {'T':0, 'G':0, 'A':0, '$':0} "counter dictionary"
    unique_counters = {}
    for k in uniques:
        unique_counters[k] = 0

    # (3) lies von links durch die sequenz und schau im dictionary nach wie
    # oft dieser schon gesehen wurde. Update dann das dictionary (weil wir ja
    #  jetzt einen mehr gesehen haben)
    rep_number = []# generiert mir eine Liste von Zahlen
    for v in sequenz:
        rep_number.append(unique_counters[v])
        unique_counters[v] += 1  # update das dictionary

    return rep_number #Ausgabe der Funktion


# find_rep_number(sequenz= 'ACTGAAC$')  # [0, 0, 0, 0, 1, 2, 1, 0] sollte es
# aussehen

def finde_rep_dict(sequenz):
    """
    Position bestimmen aufgabe 17

    LINKE SPALTE!!!!
    @param sequenz:
    @result

    @example:
    sequenz = 'ACTGAAC$'
    finde_rep_dict('ACTGAAC$')
    {'T': [2], 'A': [0, 4, 5], '$': [7], 'G': [3], 'C': [1, 6]}
    """
    uniques = set(sequenz)#generiert die Menge der einzigartigen Buchstaben

    # initialisiere ein dictionary mit leeren listen für jeden Buchstaben
    # ergebnis: {'B': [], '$': [], 'N': [], 'A': []}
    index_dict = {}
    for k in uniques:
        index_dict[k] = []# leere Liste wird hinzugefügt

    # füge die indexposition des Buchstabens dem Dictionary hinzu.
    for i, letter in enumerate(sequenz):# enumerate = Index (Aufzählen)
    #Ausgabe des Indexes und den Wert an der Stelle des Indexes
        index_dict[letter].append(i)

    return index_dict # Ausgabe der Funktion


# finde_rep_dict('ACTGAAC$')

def ruecktransformation(rechte_spalte):
    # (0) Sortiere die rechte_spalte alphabetisch und 
    
    linke_spalte = ''.join(sorted(rechte_spalte))  
    # join damit string statt liste
    
    #finde die einzigartigen Buchstaben.
    uniques = set(rechte_spalte)

    # (1) Erzeuge ein dictionary, dass für jeden Buchstaben die
    # Indexpositionen angibt, an den der Buchstabe in dem sortierten string
    # ("linke_spalte") zu finden ist.
    linke_spalte_ind = finde_rep_dict(linke_spalte)
    #Funktionsaufruf - Position bestimmen
    #Call einer Funktion
    
    
    # (2) wie sehen die anzahl an wiederolungen aus?
    rep_number = find_rep_number(rechte_spalte)# Call der Funktion
    #wie oft habe ich den Buchstaben schon gesehen - von links lesen

    # (3) führe die transformation durch
    index = 0  # start index in der rechten spalte
    letter_rechts = rechte_spalte[index]#Welcher Buchstabe ist an dieser Indexposition
    result = [letter_rechts]  # Anfangsbuchstabe an dieser position dem Ergebnis hinzufügen
    for i in range(len(rechte_spalte) - 1):  # iteriere über die länge der
        # rechten spalte. -1 weil wir den erste wert schon eingetragen haben.
        #einen Schritt weniger wiederholen, da wir den ersten Buchstaben schon haben

        # die wievielte wiederholung von diesem Buchstaben ist es in der
        # rechten spalte?
        rep_of_letter_rechts = rep_number[index] #genau so[0, 0, 1, 0, 0, 1, 2] 

        # blauer pfeil nach links
        # a) Schau in der rechten Spalte für den aktuellen Buchstaben nach,
        # die wievielte wiederholung dieses Buchstabens es ist (
        # =rep_of_letter_rechts).
        # b) Schau in der linken spalte (dictionary der indexpositionen der
        # wdh.s) nach wo die indexposition dieses rep_of_letter_rechts ist.
        # = Das ergebnis ist der index, an dem wir in der rechten spalte wieder
        # nachschauen wollen was dort für ein buchstabe steht.
        #KERNELEMENT!!!!!!
        letter_rechts = rechte_spalte[index]
        index = linke_spalte_ind[letter_rechts][rep_of_letter_rechts]
        #KERNELEMENT!!!!!!
        # linke_spalte_ind = {'T': [2], 'A': [0, 4, 5], '$': [7], 'G': [3], 'C': [1, 6]}
        #letter_rechts ist 'A'
        #A': [0, 4, 5] ist das linke_spalte_ind[letter_rechts]
        #[0, 4, 5] [rep_of_letter_rechts] Anzahl der Wiederholung, die wir schon kennen
        #KERNELEMENT!!!!!!

        print('rechte spalte: ', list(rechte_spalte), '\n',
              'buchstaben wiederholung:', rep_number, '\n',
              'dh. der buchstabe', letter_rechts,
              'wurde bis dahin', rep_of_letter_rechts, 'mal gesehen\n',

              'schaue in der linken spalte, ',
              letter_rechts, ':', linke_spalte_ind[letter_rechts],
              'nach, wo die ', rep_of_letter_rechts, 'wiederholung seht. Hier:',
              index)

        # pfeil nach rechts
        # schau nach was für ein buchstabe rechts steht.
        letter_rechts = rechte_spalte[index]
        print('In der rechten Spalte steht an der ', index, 'indexposition',
              'der Buchstabe ', letter_rechts)

        # schreib das Ergebnis aus
        result.append(letter_rechts)

    # Sortiere die Buchstaben in umgekehrter Reihenfolge
    print()
    return ''.join(reversed(result))


print(ruecktransformation(rechte_spalte='TTGGATAA$C'))

#print(ruecktransformation(rechte_spalte='TTGGATAA$C'))
