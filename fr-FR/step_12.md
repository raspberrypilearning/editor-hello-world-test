<h2 class="c-project-heading--task">Nombres aléatoires</h2>

--- task ---

➡️ Choisir un nombre aléatoire pour le lancer de dés.

--- /task ---

Utilise la fonction `randint` que tu as importée pour choisir un nombre aléatoire entre 1 et 6 pour le lancer de dés.

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 12
---

# Définitions de fonctions
def roule_de():
    print(f'Tu as obtenu un {randint(1, 6)}')

--- /code ---

**Test :** clique sur le bouton **Exécuter**.
Maintenant, lorsque tu exécutes ton code, un nouveau nombre aléatoire entre 1 et 6 sera choisi à chaque fois.

<div class="c-project-output">
```
Bonjour 🌍🌎🌏
Bienvenue sur Python 🐍
Python 🐍 est bon en maths !
12345678987654321
La date et l'heure sont 2023-11-21 16:02:12.535000
Tu as obtenu un 6
```
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

`randint` est l'abréviation d'entier aléatoire. Les entiers sont des nombres entiers.

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Vérifie tes parenthèses et accolades si tu obtiens une erreur. Note que le même nombre peut être choisi plusieurs fois. C'est aléatoire !

</div>
