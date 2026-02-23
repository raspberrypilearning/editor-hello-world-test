## Questionnaire rapide

--- question ---
---
legend: Question 1 sur 3
---

Ce code définit la variable `monde` pour qu'elle contienne le texte '🌍🌎🌏' (les trois différents emojis monde) :

--- code ---
---
language: python
---

monde = '🌍🌎🌏'

--- /code ---

Quel code utilise correctement la variable `monde` et affiche Bonjour 🌍🌎🌏 ?

![La zone de sortie du Code Editor avec Bonjour 🌍🌎🌏 affiché.](images/quiz1.png)

--- choices ---

- ( )

--- code ---
---
language: python
---

output('Bonjour' monde)

--- /code ---

--- feedback ---

Pas tout à fait, `output` n'est pas le moyen d'afficher des messages à l'écran.

--- /feedback ---

- ( )

--- code ---
---
language: python
---

print('Bonjour' monde)

--- /code ---

--- feedback ---

Pas tout à fait, en Python `print` affiche des messages à l'écran, mais il manque quelque chose dans cet exemple.

--- /feedback ---

- (x)

--- code ---
---
language: python
---

print(f'Bonjour {monde}')

--- /code ---

--- feedback ---

C'est correct, en Python, `print(f'')` affiche des messages à l'écran. La sortie du texte est entre guillemets simples `'`, et les accolades `{}` sont utilisées pour imprimer la variable `monde`.

--- /feedback ---

- ( )

--- code ---
---
language: python
---

print('Bonjour {monde}')

--- /code ---

--- feedback ---

Pas tout à fait, en Python `print` affiche des messages à l'écran, mais il manque quelque chose dans cet exemple.

--- /feedback ---

--- /choices ---

--- /question ---
