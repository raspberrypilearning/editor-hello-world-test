<h2 class="c-project-heading--task">Multiplier les chaînes</h2>

--- task ---

➡️ Stocker le nombre aléatoire dans une variable.
➡️ Multiplier le nombre par l'emoji 🔥 pour imprimer l'emoji un nombre de fois égal au lancer de dés.

--- /task ---

En Python, tu peux multiplier des chaînes de caractères telles que des emojis ou des mots entiers par un nombre, afin qu'elles s'impriment plusieurs fois.

Stocke le nombre aléatoire dans une variable appelée `roule`.

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 12
---

# Définitions de fonctions
def roule_de():
    roule = randint(1,6)

--- /code ---

Multiplie le nombre aléatoire stocké dans `roule` par l'emoji 🔥 et imprime le résultat.

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 13
---

# Définitions de fonctions
def roule_de():
    roule = randint(1,6)
    print(f'Tu as obtenu un {roule} {feu * roule}')

--- /code ---

**Test :** clique sur le bouton **Exécuter**.
Ton code de sortie devrait ressembler à ceci :

<div class="c-project-output">
```
Bonjour 🌍🌎🌏
Bienvenue sur Python 🐍
Python 🐍 est bon en maths !
12345678987654321
La date et l'heure sont 2023-11-21 16:14:45.140000
Tu as obtenu un 4 🔥🔥🔥🔥
```
</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Vérifie que toutes tes parenthèses sont identiques à celles de l’exemple de code ci-dessus.

</div>
