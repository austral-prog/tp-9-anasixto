def create_inventory(items):
    #Creo un diccionario vacío  
    inventory = {}
    #Recorrer los elementos de la lista
    for item in items:
        #Si el artículo ya está en el diccionario, incrementar su valor
        if item in inventory:
            inventory[item] += 1
        #Si no lo está dejar el valor en uno
        else:
            inventory[item] = 1
    
    return inventory


def add_items(inventory, items):

    for item in items:

        if item in inventory:
            inventory[item] += 1

        else:
            inventory[item] = 1
   
    return inventory


def decrement_items(inventory, items):

    for item in items:

        if item in inventory:
            value = inventory[item]

            if value > 0:

                inventory[item] -= 1

        else:
            inventory[item] = 1
    
    return inventory


def remove_item(inventory, item):

    inventory.pop(item, None)
    
    return inventory


def list_inventory(inventory):

    my_inventory = []

    for key, value in inventory.items():
        if value > 0:
            my_inventory.append((key, value))
    return my_inventory
