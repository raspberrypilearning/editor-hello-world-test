<h2 class="c-project-heading--task">Obtenir une entrée</h2>

--- task ---

➡️ Permettre à la personne qui utilise ton programme de saisir des données.

--- /task ---

Tu peux utiliser `input()` pour demander à la personne utilisant ton programme de saisir du texte et de l'enregistrer en tant que variable.

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 12-13
---

# Définitions de fonctions
def roule_de():
    max = input('Combien de faces y a-t-il sur ton dé ?')
    print(f'C\'est un D {max}')
    roule = randint(1,6)
    print(f'Tu as obtenu un {roule} {feu * roule}')

--- /code ---

**Test :** clique sur le bouton **Exécuter**.
Assure-toi d'appuyer sur la touche <kbd>Entrée</kbd> après avoir saisi le nombre de faces.
Tu devrais voir ceci lorsque tu exécutes ton code.

<div class="c-project-output">
```
Bonjour 🌍🌎🌏
Bienvenue sur Python 🐍
Python 🐍 est bon en maths !
12345678987654321
La date et l'heure sont 2023-11-21 16:20:41.323000
Combien de faces y a-t-il sur ton dé ?
20 
C'est un D 20
Tu as obtenu un 1 🔥
```
</div>
