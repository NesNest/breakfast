import random as rm
"""shall we start making tha 'recipe' & 'sauce' object"""
class Recipe:
        def __init__(self, name, ingredients, instruccions=" ", sauce=None):
            self.name = name
            self.ingredients = ingredients
            self.instruccions = instruccions
            self.sauce = sauce
        
class Sauce:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        
        
s1 = Sauce("salsa verde para banar", [["tomate", 6, "un"], ["chile serrano", 3, "un"], ["cebolla", 1, "un"], ["ajo", 2, "un"], ["cilantro", 1, "un"]])
s2 = Sauce("salsa roja para banar", [["tomate", 6, "un"], ["chile guajillo", 3, "un"], ["chile de árbol", 2, "un"], ["cebolla", 1, "un"], ["ajo", 2, "un"]])

r1 = Recipe("Chilaquiles verdes", [["tortilla", .4, "kg"], ["cebolla", 0.5, "un"], ["ajo", 1, "un"], ["queso panela", .25, "kg"], ["crema", .25, "lt"]], "Primero, prepara la salsa verde. Para ello, hierve los tomates en agua hasta que estén suaves. Luego, retíralos del agua y quítales la piel. Licúa los tomates junto con los chiles serranos, la cebolla, los dientes de ajo y el cilantro hasta obtener una salsa suave y homogénea. \nEn una sartén grande, calienta un poco de aceite y agrega la salsa verde. Cocina la salsa a fuego medio durante unos minutos hasta que comience a hervir. \nMientras tanto, corta las tortillas de maíz en triángulos o tiras. Puedes dejarlas secar al aire durante unas horas o hornearlas a baja temperatura en el horno para que estén un poco crujientes. \nCuando la salsa verde esté caliente, agrega las tortillas cortadas a la sartén y mézclalas bien para que queden cubiertas por la salsa. Cocina los chilaquiles a fuego medio durante unos 5-7 minutos, revolviendo ocasionalmente, hasta que las tortillas estén suaves pero aún algo crujientes. \nMientras se cocinan los chilaquiles, corta la cebolla en rodajas finas y pica finamente el diente de ajo.\nUna vez que los chilaquiles estén listos, sirve en platos individuales y decora con rodajas de cebolla fresca.\nCorta el queso panela en cubos pequeños y agrégalo sobre los chilaquiles.\nPor último, decora con crema al gusto y sirve caliente", s1)
r2 = Recipe("Chilaquiles rojos", [["tortilla", .4, "kg"], ["cebolla", 0.5, "un"], ["ajo", 1, "un"], ["queso panela", .25, "kg"], ["crema", .25, "lt"]], "Primero, prepara la salsa roja. Hierve los tomates en agua hasta que estén suaves. Luego, retíralos del agua y quítales la piel. Licúa los tomates junto con los chiles guajillos, los chiles de árbol, la cebolla y los dientes de ajo hasta obtener una salsa suave y homogénea. \nEn una sartén grande, calienta un poco de aceite y agrega la salsa roja. Cocina la salsa a fuego medio durante unos minutos hasta que comience a hervir. \nMientras tanto, corta las tortillas de maíz en triángulos o tiras. Puedes dejarlas secar al aire durante unas horas o hornearlas a baja temperatura en el horno para que estén un poco crujientes. \nCuando la salsa roja esté caliente, agrega las tortillas cortadas a la sartén y mézclalas bien para que queden cubiertas por la salsa. Cocina los chilaquiles a fuego medio durante unos 5-7 minutos, revolviendo ocasionalmente, hasta que las tortillas estén suaves pero aún algo crujientes. \nMientras se cocinan los chilaquiles, corta la cebolla en rodajas finas y pica finamente el diente de ajo. \nUna vez que los chilaquiles estén listos, sirve en platos individuales y decora con rodajas de cebolla fresca. \nDesmenuza el queso fresco y agrégalo sobre los chilaquiles. \nPor último, decora con crema al gusto y sirve caliente.", s2)
r3 = Recipe("Huevos con Salsa de Pizza", [["huevo", 2, "un"], ["salsa de pizza", 1, "un"], ["queso mozzarella rallado", 0.25, "kg"], ["orégano seco", 0.25, "kg"]], "Calienta el aceite de oliva en una sartén a fuego medio. Agrega los huevos a la sartén y cocínalos al gusto (revuélvelos si deseas huevos revueltos o déjalos enteros para huevos fritos). Mientras los huevos se cocinan, calienta la salsa de pizza en una cacerola pequeña a fuego medio. Una vez que los huevos estén listos, colócalos en un plato. Vierte la salsa de pizza caliente sobre los huevos. Espolvorea el queso mozzarella rallado sobre la salsa de pizza. Espolvorea el orégano seco, la sal y la pimienta al gusto. Decora con perejil fresco picado si lo deseas.")

options = [r1, r2, r3]
"""number = int(input("¿Cuántas recetas? "))"""
"""newlist = rm.sample(options, number)"""
def suma(r1, r2):
    recipe1 = r1.ingredients
    recipe2 = r2.ingredients
    newingredients = []
    
    for i in range(len(recipe2)):
        count = 0
        newingredients.append([])
        for j in range(len(recipe1)):
            if recipe2[0][0] in recipe1[j]: 
                suming = recipe2[0][1] + recipe1[j][1]
                newingredients[i].append(recipe2[0][0])
                newingredients[i].append(suming)
                newingredients[i].append(recipe2[0][2])
                recipe2.remove(recipe2[0])
                recipe1.remove(recipe1[j])
                break        
            else:
                count += 1
                if count >= len(recipe1):
                    newingredients[i].append(recipe2[0][0])
                    newingredients[i].append(recipe2[0][1])
                    newingredients[i].append(recipe2[0][2])
                    recipe2.remove(recipe2[0])
    newingredients += recipe1           

    return newingredients
def buylist(recipes):
    total = []
    for recipe in recipes:
        total.append(suma(recipe[0], recipe[1]))
        
    
    

suma(r1, r3)
    
        
        