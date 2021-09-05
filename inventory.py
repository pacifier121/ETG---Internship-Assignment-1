import json
import time

def startInventory():
    inv = {
        10001 : {"name" : "Dairy Milk", "category" : "chocolates", "brand" : "Cadbury", "price" : 20, "qty" : 50},
        10002 : {"name" : "Maggi", "category" : "fast food", "brand" : "Nestle", "price" : 10, "qty" : 30},
        10003 : {"name" : "Slice", "category" : "cold drinks", "brand" : "PepsiCo", "price" : 50, "qty" : 25},
        10004 : {"name" : "Coke", "category" : "cold drinks", "brand" : "Coca Cola", "price" : 30, "qty" : 30},
        10005 : {"name" : "Dairy Milk Silk", "category" : "chocolates", "brand" : "Cadbury", "price" : 80, "qty" : 30},
        10006 : {"name" : "Parle-G", "category" : "biscuits", "brand" : "Parle", "price" :  10, "qty" : 60},
        10007 : {"name" : "Bourbon", "category" : "biscuits", "brand" : "Britannia", "price" :  20, "qty" : 50},
        10008 : {"name" : "Lays", "category" : "chips", "brand" : "PepsiCo", "price" :  20, "qty" : 65},
        10009 : {"name" : "Kitkat", "category" : "chocolates", "brand" : "Nestle", "price" : 10, "qty" : 55},
        10010 : {"name" : "Kurkure", "category" : "chips", "brand" : "PepsiCo", "price" :  15, "qty" : 60},

        10011 : {"name" : "Chocolate Pastries", "category" : "cakes", "brand" : "Nutella", "price" : 25, "qty" : 50},
        10012 : {"name" : "Snickers", "category" : "chocolate", "brand" : "Mars", "price" : 20, "qty" : 45},
        10013 : {"name" : "Bingo", "category" : "chips", "brand" : "ITC", "price" : 15, "qty" : 45},
        10014 : {"name" : "Amul Butter", "category" : "dairy", "brand" : "Amul", "price" : 20, "qty" : 30},
        10015 : {"name" : "Cornetto", "category" : "ice-cream", "brand" : "Vadilal", "price" : 30, "qty" : 40},
        10016 : {"name" : "Instant Coffee", "category" : "coffee powder", "brand" : "Nescafe", "price" :  40, "qty" : 40},
        10017 : {"name" : "Act II Popcorn", "category" : "popcorn", "brand" : "Conagra Brands", "price" :  20, "qty" : 50}
    }
    return inv

try:
    file = open('record.json', 'r')
    txt = file.read()
    inv = json.loads(txt)
    file.close()

    saveFile = open('transactions.json', 'r')
    saveTxt = saveFile.read()
    trans = json.loads(saveFile)
    saveFile.close()
    
except Exception:
    inv = startInventory()
    file = open('record.json', 'w')
    js = json.dumps(inv)
    file.write(js)
    file.close()

    saveFile = open('transactions.json', 'w')
    trans = {'lastTransactionId' : 100000}
    initialData = json.dumps(trans)
    saveFile.write(initialData)

while True:
    print("Enter what you want to do : ")
    print("1. Display all items")
    print("2. Purchase an item")
    print("3. Search for a product with it's\n\ta) Name\n\tb) Brand \n\tc) Category\n\t(Enter 3 immediately followed by letter)")
    print("4. Display transaction history")
    cmd = input()
    if (cmd == "1"):
        line = "{:15}{:20}{:20}{:20}{:10}{:10}".format("Product ID", "Product Name", "Category", "Brand", "Price", "Quantity")
        print(line)
        for key in inv:
            pro = inv[key]
            line = "{:15}{:20}{:20}{:20}{:10}{:5}".format(str(key), pro["name"], pro["category"], pro["brand"], str(pro["price"]), str(pro["qty"]))
            print(line)
    elif (cmd == "2"):
        pid = int(input("Enter product ID : "))
        n = int(input("Enter the quantity : "))
        try:
            if (inv[pid]["qty"] < n):
                print("Not enough quantity of the product! Please select lower quantity")
            else:
                inv[pid]['qty'] -= n
                transID = int(trans['lastTransactionId']) + 1
                trans['lastTransactionId'] = str(transID)
                trans[transID] = {"id" : pid, 'name' : inv[pid]['name'], "time" : time.ctime(), "qty" : str(n), "total" : str(n * inv[pid]['price'])}
                print("{} items of {} have been purchased".format(str(n), inv[pid]['name']))
        except Exception:
            print("Sorry, couldn't purchase the product specified")
    elif (cmd.startswith("3")):
        cmds = {"a" : "name", "b" : "brand", "c" : "category"}
        try:
            cmd = cmd[1:]
            searchType = cmds[cmd]
            search = input("Enter the {} of the product : ".format(searchType))
            flag = False
            keys = []
            for key in inv:
                if (inv[key][searchType] == search):
                    flag = True
                    keys.append(key)
            if (flag):
                line = "{:15}{:20}{:20}{:20}{:10}{:10}".format("Product ID", "Product Name", "Category", "Brand", "Price", "Quantity")
                print(line)
                for k in keys:
                    pro = inv[k]
                    line = "{:15}{:20}{:20}{:20}{:10}{:5}".format(str(k), pro["name"], pro["category"], pro["brand"], str(pro["price"]), str(pro["qty"]))
                    print(line)
            else:
                print("Couldn't find the product you were looking for")
        except Exception:
            print("Invalid search command")
    elif (cmd == '4'):
        try:
            print("{:15}{:15}{:25}{:30}{:10}{:15}".format("Trans. ID", "Product ID", "Product Name", "TimeStamp", "Qty.", "Total"))
            for key in trans:
                if (key != 'lastTransactionId'):
                    row = trans[key]
                    line = "{:15}{:15}{:25}{:30}{:10}{:15}".format(str(key), str(row['id']), row['name'], row['time'], row['qty'], row['total']) 
                    print(line)
                    
        except Exception:
            print("Couldn't get the transaction history")
    elif (cmd == "exit"):
        break

    js = json.dumps(inv)
    file = open('record.json', 'w')
    file.write(js)
    file.close()

    transTxt = json.dumps(trans)
    saveFile = open('transactions.json', 'w')
    saveFile.write(transTxt)
    saveFile.close()

    print("-" * 50)