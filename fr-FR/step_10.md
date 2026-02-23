<h2 class="c-project-heading--task">Lancer un dé</h2>

--- task ---

➡️ Créer une fonction pour simuler le lancement d'un dé.

➡️ Appeler la fonction pour exécuter le code qu'elle contient.

--- /task ---

Crée une fonction appelée `roule_de()`, qui imprime le nombre 4.

--- code ---
---
language: python
line_numbers: true
line_number_start: 9
line_highlights: 10, 11
---

# Définitions de fonctions
def roule_de():
    print(f'Tu as obtenu un {4}')

# Mettre le code à exécuter ci-dessous

--- /code ---

Ensuite, appelle la fonction en bas de ton code.

--- code ---
---
language: python
line_numbers: true
line_number_start: 18
line_highlights: 19
---
print(f'La date et l'heure sont {datetime.now()}')
roule_de()

--- /code ---

**Test :** clique sur le bouton **Exécuter**.
Tu devrais voir ceci lorsque tu exécutes ton code.

<div class="c-project-output">
```
Bonjour 🌍🌎🌏
Bienvenue sur Python 🐍
Python 🐍 est bon en maths !
12345678987654321
La date et l'heure sont 2023-11-21 15:55:33.038000
Tu as obtenu un 4
```
</div>

<div class="c-project-callout c-project-callout--tip">

### Astuce

Tu peux utiliser la touche **Tab** de ton clavier pour insérer 4 espaces. Appuyer sur **Maj** et **Tab** supprimera les 4 espaces.

</div>

<div class="c-project-callout c-project-callout--debug">

### Déboguer

Vérifie que tu as des parenthèses `()` et deux points `:` à la fin de ta définition de fonction. Vérifie également que tu utilises des parenthèses `()` lorsque tu appelles ta fonction.

</div>
