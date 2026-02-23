# importations
from datetime import datetime
from random import randint

monde = '🌍🌎🌏'
python = 'Python 🐍'
feu = '🔥'

# Définitions de fonctions        
def roule_de():
    max = input('Combien de faces y a-t-il sur ton dé ?')
    print(f'C\'est un D {max}')
    roule = randint(1, int(max))
    print(f'Tu as obtenu un {roule} {feu * roule}')
    
# Mettre le code à exécuter ci-dessous
print(f'Bonjour {monde}')
print(f'Bienvenue sur {python}')
print(f'{python} est bon en maths !')
print(f'{111111111 * 111111111}')
print(f'La date et l\'heure sont {datetime.now()}')
roule_de() # Appel la fonction lancer de dés
print(f'J\'❤️ ...')   
print(f'... me rend 😃')   
print(f'Je voudrais faire ... avec {python}')
