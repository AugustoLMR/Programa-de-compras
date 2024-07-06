from customer import Customer
from item import Item
from seller import Seller

cantidades_compradas = []
indices_seleccionados = []

seller = Seller("DICストア")
for i in range(10):
    Item("CPU", 40830, seller)
    Item("Memory", 13880, seller)
    Item("Motherboard", 28980, seller)
    Item("Power Supply Unit", 8980, seller)
    Item("PC Case", 8727, seller)
    Item("3.5 inches HDD", 10980, seller)
    Item("2.5 inch SSD", 13370, seller)
    Item("M.2 SSD", 12980, seller)
    Item("CPU Cooler", 13400, seller)
    Item("Graphics Board", 23800, seller)



print("🤖 Please tell me your name")
customer = Customer(input())

print("🏧 Please enter the amount you would like to charge to your wallet")
customer.wallet.deposit(int(input()))

print("🛍️ Start Shopping")
end_shopping = False
while not end_shopping:
    print("📜 Product List")
    seller.show_items()
    
    print("️️⛏ Please enter item number")
    number = int(input())
    indices_seleccionados.append(number)
    
    print("⛏ Please enter the quantity of goods")
    quantity = int(input())
    cantidades_compradas.append(quantity)

    items = seller.pick_items(number, quantity)
    for item in items:
        customer.cart.add(item)
    print("🛒 Contents of cart")
    customer.cart.show_items()
    print(f"🤑 Total amount: {customer.cart.total_amount()}")

    print("😭 Would you like to finish shopping? (yes/no)")
    end_shopping = input() == "yes"

print("💸 Do you wish to confirm your purchase? (yes/no)")
if  input() == "yes":
    customer.cart.check_out()
    print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈results┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
    print(f"️🛍️ ️{customer.name}´s property")
    customer.cart.show_items()
    print(f"😱👛 {customer.name}'s wallet balance: {customer.wallet.balance - customer.cart.total_amount()}")
    
    print(f"📦 {seller.name} Inventory Status")
    
    seller.show_items_after_purchase(indices_seleccionados, cantidades_compradas) # metodo que creé que modifica la cantidad del producto luego de la compra#
    
    print(f"😻👛 {seller.name} wallet balance: {customer.cart.total_amount()}")

    print("🛒 Contents of cart")
    customer.show_items()
    print(f"🌚 total amount: 0")

    print("🎉 end")
    
