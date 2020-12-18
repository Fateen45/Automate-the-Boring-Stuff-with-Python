Inventory = {'arrow': 12, 'gold coin': 42, 'rope': 1,
             'torch': 6, 'dagger': 1} #The dictionary of items in the inventory.

def displayInventory(parameter): #Here this 'parameter' is the parameter that will be passed Inventory as an argument.

    print('Inventory:')

    item_total = 0 #It's set to 0 so that the calculation stays correct.

    for k, v in parameter.items(): #This for-loop will iterate the tuples returned by parameter.items(), one after another.
        print(str(v) + ' ' + k) #v = integer values from the dictionary, and k = string values from the dictionary.
        item_total += v #item_total = item_total + v
                        #Because of successive iterations of the loop, all the integers will be summed in the last iteration. And, this summed value will be the total number of items.
    print('Total number of items: ' + str(item_total)) #After the loop is over, the total number of items is printed out.

displayInventory(Inventory)
