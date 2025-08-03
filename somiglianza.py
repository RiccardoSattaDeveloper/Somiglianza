# Importa le librerie necessarie.
from glob import glob # serve per trovare tutti i file con un certo pattern (in questo caso, *.png).
from os import chdir # serve per cambiare la directory di lavoro.

# La libreria 'face_recognition' è utilizzata per il riconoscimento facciale.
# Il modulo 'load_image_file' serve per caricare un'immagine da un file
# Il modulo 'face_encodings' serve per generare una codifica numerica del volto nell'immagine.
# Il modulo 'face_distance' serve per calcolare la distanza tra due codifiche facciali.
from face_recognition import load_image_file, face_encodings, face_distance

miaFoto = load_image_file('miaFoto.png') # Carica la mia foto.
fotoPiuSomigliante = face_encodings(miaFoto)[0] # Codifica il volto nella mia foto.

chdir('personaggi_pubblici') # Cambia la directory di lavoro per accedere alle foto dei personaggi pubblici.

personaggiPubblici = {} # Inizializza un dizionario vuoto per memorizzare i nomi dei file e le distanze facciali.

for fotoPersonaggioPubblico in glob('*.png'): # Itera su tutti i file PNG nella directory corrente.
    immaginaDaConfrontare = load_image_file(fotoPersonaggioPubblico) # Per ogni personaggio pubblico, carica l'immagine...
    encImmaginaDaConfrontare = face_encodings(immaginaDaConfrontare)[0] # ... e genera la codifica facciale.
    distance = face_distance([fotoPiuSomigliante], encImmaginaDaConfrontare)     # Calcola la distanza tra la mia foto e la foto del personaggio pubblico.
    personaggiPubblici[fotoPersonaggioPubblico] = distance # Salva la distanza nel dizionario 'personaggiPubblici' usando il nome del file come chiave.

# Ordina i personaggi pubblici in base alla loro distanza facciale dal vincitore.
# Il metodo 'sorted' crea una lista ordinata di chiavi del dizionario.
# 'key=personaggiPubblici.get' indica che l'ordinamento deve essere basato sui valori del dizionario (le distanze).
# Di default, l'ordinamento è crescente, quindi il primo elemento sarà quello con la distanza minore (più somigliante).
classifica = sorted(personaggiPubblici, key=personaggiPubblici.get)

print('PRIMI 3 IN CLASSIFICA') # Stampa i primi 3 classificati.
for personaggio in classifica[:3]: # Itera sui primi 3 elementi della lista 'classifica'.
    print(personaggio)

print('ULTIMO CLASSIFICATO') # Stampa l'ultimo classificato.
print(classifica[-1]) # L'ultimo classificato è l'ultimo elemento della lista ordinata, cioè quello con la distanza maggiore.