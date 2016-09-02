import Image
r = Image.open('r_extract.bmp').convert('RGB')
g = Image.open('g_extract.bmp').convert('RGB')
b = Image.open('b_extract.bmp').convert('RGB')
 
bin = ''

for x in range(r.size[0]):
    bin += str(r.getpixel((x, 0))[0] & 1)
    bin += str(g.getpixel((x, 0))[1] & 1)
    bin += str(b.getpixel((x, 0))[2] & 1)
 
print bin
""" 
M4z :

Salut,
c’est un write_up fraîchement intéressant, je vous en remercie🙂.
Cependant j’aurai une question :
Pour quelle raison, lorsque en rajoutant avec une boucle for sur la img.size[1] ‘est a dire la hauteur, je n’obtiens pas le même résultats.

voici un exemple pour illustrer mes propos :


for x in range(img.size[0]):
    for y in range(img.size[1]):
        lsb += str(img.getpixel((x, y))[0] & 1)

Merci, bien cordialement & keep pwning guys😉 
----------------------
Hexpresso :

Salut M4z,

A priori, tu fais deux boucles toi (for x et for y), ce qui va « balayer » l’image de gauche à droite sur toute sa surface. Or, le script dans le writeup ne fait pas cela. Il balaye juste UNE SEULE FOIS les images de gauche à droite en restant sur la même ligne😉

J’espère que mon explication est correcte et te seras utile !

"""
