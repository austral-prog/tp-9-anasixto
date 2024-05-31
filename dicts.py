def create_inventory(items):
    #Creo un diccionario vacío  
    inventory = {}
    #Recorrer los elementos de la lista
    for item in items
        #Si el artículo ya está en el diccionario, incrementar su valor
        if item in inventory:
            inventory[item] += 1
        #Si no lo está dejar el valor en uno
        else:
            inventory[item] = 1
    
    return inventory


def add_items(inventory, items):

    if item in items:
        inventory[item] += 1

    else:
        inventory[item] = 1
   
    return inventory


def decrement_items(inventory, items):

    inventory = {}

    for item in items

        if item in inventory:
            inventory[item] -= 1

        else:
            inventory[item] = 1
    
    return inventory


def remove_item(inventory, item):

    inventory.pop(item, None)
    
    return inventory


def list_inventory(inventory):

    for item in list_inventory.items():

        key = item[0]
        value = item[1]

        print(key)
        print(value)
        
    return inventory

