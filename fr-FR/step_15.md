<h2 class="c-project-heading--task">Changer le dé</h2>

--- task ---

➡️ Modifier les données d’entrée en un entier.
➡️ Génèrer un nombre aléatoire compris entre 1 et le nombre de faces saisi par l'utilisateur.

--- /task ---

Les entrées sont toujours stockées sous forme de texte, mais nous devons utiliser l'entrée stockée dans `max` pour spécifier le plus grand nombre qui pourrait être obtenu.

`max` est une chaîne, elle doit donc être changée en un entier `int()`.

--- code ---
---
language: python
line_numbers: true
line_number_start: 10
line_highlights: 14
---

# Définitions de fonctions
def roule_de():
    max = input('Combien de faces y a-t-il sur ton dé ?')
    print(f'C\'est un D {max}')
    roule = randint(1, int(max))
    print(f'Tu as obtenu un {roule} {feu * roule}')

--- /code ---

**Test :** clique sur le bouton **Exécuter**.
Voici ce que tu devrais voir :

<div class="c-project-output">
```
Bonjour 🌍🌎🌏
Bienvenue sur Python 🐍
Python 🐍 est bon en maths !
12345678987654321
La date et l'heure sont 2023-11-21 16:27:24.101000
Combien de faces y a-t-il sur ton dé ?:12
C'est un D 12
Tu as obtenu un 5 🔥🔥🔥🔥🔥
```
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

La modification d’un type de données en un autre type de données est appelée **type casting**.

</div>