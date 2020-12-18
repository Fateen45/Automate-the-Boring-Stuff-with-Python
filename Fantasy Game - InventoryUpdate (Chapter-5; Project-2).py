inv = {'gold coin': 42, 'rope': 1} #It is the dictionary represented as the initial inventory before it gets updated by our defined functions.
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby'] #The list from which items will be added to the initial inventory to update it.





def addToInventory(Inventory, addedItems): #This function will be used to update the initial inventory by including the items of 'dragonLoot' in the initial inventory and also incrementing the value of each key by 1 according to each new item added from 'dragonLoot'.
                                           #The values in general and the incremented values of the keys are represented as the amount of each item.
                                           #'inv' and 'dragonLoot' will be passed to the parameters 'Inventory' and 'addedItems' as arguments, respectively.

    for i in addedItems: #As the argument passed to 'addedItems' will be 'dragonLoot', this for-loop will iterate 5 times because of the 5 items in it.                   

        Inventory.setdefault(i, 0) #In a running iteration of the loop, the current item passed to i from 'addedItems' will be checked whether it exists in 'inv'. If an item doesn't exist in 'inv', then that item represented as a key in the dictionary will be paired with the value 0.

        Inventory[i] = Inventory[i] + 1 #The value inside the dictionary of the represented key of the item passed to i, whether the item exists as a key in the dictionary or not, will be incremented by 1.
                                        #As a result, each new item without any repetition will be represented as only a single piece item inside the updated inventory; Also, in the case of the repetition of an existing item, the number of incrementations will be done accordingly to represent the exact amount of an item inside the updated inventory.

    return Inventory #The updated 'inv', the dictionary, will be returned as the return value of this function.
                     #Important: As 'inv' is a dictionary data type, any changes made to it inside this function by the use of its local variables will also result in making the same changes to 'inv' outside the function, that is, the original one. Whereas, in the case of non-list data types, the variables and the values stored inside a function are destroyed when the function returnsdef displayInventory(UpdatedInventory):
                     #Important: So, the return statement isn't necessary for running this program, but it can be used. The return statement would've been necessary if the return value of this function were assigned to a variable, and then that variable was used as the argument for the final function's parameter (Example: "V = addToInventory(stuff, unlocked)", and then "displayInventory(V)".



def displayInventory(UpdatedInventory): #Finally, this function will be used to show/print out the updated inventory.
    
    print('Inventory:')

    TotalItems = 0 #It's set to 0 so that the calculation for determining the total amount of all the items together stays correct.
                   #Whereas, incrementation done in the previous function was for calculating the total amount of individual items.

    for k, v in UpdatedInventory.items(): #This for-loop will iterate the tuples returned by parameter.items(), one after another.

        print(v, k) #v = integer values from the dictionary, and k = string values from the dictionary. These values from the updated inventory/dictionary will be printed out.

        TotalItems = TotalItems + v #Because of successive iterations of the loop, all the integers will be summed in the last iteration. And, this summed value will be the total number of items together.

    print('Total number of items: ' + str(TotalItems)) #After the loop is over, the total number of items is printed out.



addToInventory(inv, dragonLoot) #First function called.

displayInventory(inv) #Final function called.
