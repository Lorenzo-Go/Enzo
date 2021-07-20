products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

def get_product(code):
    return products[code]

def get_property(code,property):
    return products[code][property]

def main():
    INPUT = ""
    all_orders = {}
    list_of_orders = []
    total = 0
    for i in products:
        list_of_orders.append(i)
        list_of_orders.sort(reverse=True)
    while not("/" in INPUT):
        INPUT = input().split(",")
        if INPUT[0] in all_orders:
            all_orders[INPUT[0]] +=int(INPUT[1])
        elif INPUT[0] in list_of_orders:
            all_orders.setdefault(INPUT[0],int(INPUT[1]))
    with open("receipt.txt","w") as receipt:
        receipt.write("==")
        receipt.write("\nCODE\t\t\t\tNAME\t\t\t\tQUANTITY\t\tSUBTOTAL")
        for i in list_of_orders:
            if i in all_orders:
                name = get_property(i,"name")
                subtotal = all_orders[i]*get_property(i,"price")
                receipt.write(f"\n{i}")
                receipt.write(f"\t\t\t{name}")
                receipt.write(f"\t\t\t{all_orders[i]}")
                receipt.write(f"\t\t\t{subtotal}")
                total += all_orders[i]*get_property(i,"price")
        receipt.write(f"\n\nTotal:\t\t\t\t\t\t\t\t\t\t\t{total}")
        receipt.write("\n==")

main()
