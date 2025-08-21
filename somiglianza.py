from glob import glob 
from os import chdir

from face_recognition import load_image_file, face_encodings, face_distance

miaFoto = load_image_file('miaFoto.png')
fotoPiuSomigliante = face_encodings(miaFoto)[0]

chdir('personaggi_pubblici')

personaggiPubblici = {} 

for fotoPersonaggioPubblico in glob('*.png'): 
    immaginaDaConfrontare = load_image_file(fotoPersonaggioPubblico)
    encImmaginaDaConfrontare = face_encodings(immaginaDaConfrontare)[0] 
    distance = face_distance([fotoPiuSomigliante], encImmaginaDaConfrontare)     
    personaggiPubblici[fotoPersonaggioPubblico] = distance 

classifica = sorted(personaggiPubblici, key=personaggiPubblici.get)

print('PRIMI 3 IN CLASSIFICA') 
for personaggio in classifica[:3]:
    print(personaggio)

print('ULTIMO CLASSIFICATO')
print(classifica[-1])
