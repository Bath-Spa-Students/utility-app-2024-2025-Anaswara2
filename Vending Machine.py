#Vending Machine
"""
Your task is to create a Vending Machine program using the Python programming language.
The program should demonstrate your knowledge of programming and make use of the techniques introduced over the course of the module. 
Your application should be accompanied by a development document.
"""

import tkinter as tk
from tkinter import messagebox

#The variable "inventory" consists of the menu of snacks, drinks and candy.
inventory={
    "Snacks": {"Walkers Crisps": [10, 1.5], 
               "Cookies": [1, 2.0],
               "Doritos": [3, 2.5], 
               "Croissant": [5, 4.5], 
               "Granola Bars": [7, 5], 
               "Cheez-it Crackers": [5, 2], 
               "Oreo": [10, 2.5] },
    "Drinks": {"Coca Cola": [7, 1.0], 
               "Mango Juice": [8, 2.2], 
               "Orange Juice": [10, 1.2], 
               "Apple Juice": [5, 1.2], 
               "Water": [10, 0.8], 
               "Pepsi": [6, 1.2], 
               "Mountain Dew": [9, 1.2], 
               "Chocolate Milk": [8, 2.2],},
    "Candy": {"Kitkat": [4, 1.8], 
              "Lollipop": [9, 0.5],
              "Cadbury Dairy Milk Bar": [7, 2],
              "Snickers": [8, 1.8],
              "Twix Bar": [4, 1.8],
              "Kinder Bueno":[8,1.2]},
}

#Initialzing an empty list with the variable "cart".
cart=[]

#Function to update the cart and the menu.
def add_to_cart(category, item):
    if inventory[category][item][0] > 0:
        #Appending an item to the cart.
        cart.append((item, inventory[category][item][1]))
        inventory[category][item][0] -= 1
        messagebox.showinfo("Added to Cart", f"{item} has been added to your cart.")
    else:
        messagebox.showwarning("Out of Stock", f"Sorry, {item} is out of stock!")

    #Suggest items from other categories
    other_categories=[cat for cat in inventory.keys() if cat!=category]
    for next_category in other_categories:
        suggestion=f"Would you like to explore {next_category}?"
        if messagebox.askyesno("Suggestion", suggestion):
            show_items(next_category) #Show items from the selected category.
            break  #Exit after user has selected a category
    else:
        #Displays this message after the user has selected all the items
        messagebox.showinfo("No More Suggestions", "Thank you for your selection!") 
        
#function to display the items.
def show_items(category):
    #function to add item in the cart.
    def add_item(item):
        add_to_cart(category, item)

#Options window will be displayed with the items and add item button.
    items_window = tk.Toplevel()
    items_window.title(f"{category} Options")
    items_window.configure(bg="#1c3d80")
    items_window.geometry("1920x1080")

#for loop used to display the items in the respective categories.
    for item, details in inventory[category].items():
        tk.Label(items_window, text=f"{item} - Price: ${details[1]} - Quantity: {details[0]}", font=("Roboto Mono", 12), fg="white", bg="#1c3d80").pack(pady=10)
        tk.Button(items_window, text=f"Add {item}", font=("Roboto Mono", 12), command=lambda i=item: add_item(i)).pack(pady=5)

    tk.Button(items_window, text="Done", font=("Roboto Mono", 13), command=items_window.destroy).pack(pady=20)

#function to display the main page
def welcome_page():
    def go_to_category(category):
        show_items(category)

    welcome_window = tk.Tk()
    welcome_window.title("Vending Machine")
    welcome_window.configure(bg="#16336e")
    welcome_window.geometry("1920x1080")

    tk.Label(welcome_window, text="Welcome to Anaswara's Vending Machine!\nPlease choose your category:", font=("Cooper Black", 30,"bold"), fg="white", bg="#16336e").pack(pady=40)

#for loop used to display all the categories .
    for category in inventory.keys():
        #category will be displayed as buttons
        tk.Button(welcome_window, text=category, font=("Roboto Mono", 20), command=lambda c=category: go_to_category(c)).pack(pady=20)

#button will be displayed to view the cart
    tk.Button(welcome_window, text="View Cart", font=("Roboto Mono", 20), command=lambda: show_cart(welcome_window)).pack(pady=40)

    welcome_window.mainloop()

#function to display the cart.
def show_cart(root_window):
    root_window.destroy()
    cart_window = tk.Tk()
    cart_window.title("Cart")
    cart_window.configure(bg="#16336e")
    cart_window.geometry("1920x1080")

#if statement to check whether the cart is empty
    if not cart:
        #displays a text if its empty
        tk.Label(cart_window, text="Your cart is empty.", font=("Roboto Mono", 20),fg="white", bg="#16336e").pack(pady=40)
        #shows a back button to go to the menu page.
        tk.Button(cart_window, text="Back", font=("Roboto Mono", 18), command=lambda: [cart_window.destroy(), welcome_page()]).pack(pady=40)
        return


    tk.Label(cart_window, text="Your Cart:", font=("Cooper Black", 24),fg="white", bg="#16336e").pack(pady=40)
    total = 0

#for loop to display the items and its price, the user chooses.
    for item, price in cart:
        tk.Label(cart_window, text=f"{item} - ${price}", font=("Roboto Mono", 22),fg="white",bg="#16336e").pack(pady=10)
        total += price

#displays the total amount.
    tk.Label(cart_window, text=f"Total: ${total:.2f}", font=("Roboto Mono", 22), fg="white",bg="#16336e").pack(pady=40)

#function to display the payment window
    def proceed_to_payment():
        cart_window.destroy()
        payment_page(total)

    tk.Button(cart_window, text="Proceed to Payment", font=("Roboto Mono", 24), command=proceed_to_payment).pack(pady=40)

#prints the total amount paid and will display the change using the if else condition.
def payment_page(total):
    def process_payment():
        try:
            amount_paid = float(payment_entry.get())
            if amount_paid < total:
                messagebox.showerror("Insufficient Payment", "The amount paid is less than the total.")
            else:
                change = amount_paid - total
                messagebox.showinfo("Payment Successful", f"Payment successful! Your change is ${change:.2f}")
                payment_window.destroy()
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid amount.")

#displays the payment window
    payment_window = tk.Tk()
    payment_window.title("Payment")
    payment_window.configure(bg="#fce4ec")
    payment_window.geometry("1920x1080")

    tk.Label(payment_window, text=f"Total Amount: ${total:.2f}", font=("Cooper Black", 28), bg="#fce4ec").pack(pady=40)
    tk.Label(payment_window, text="Enter Payment:", font=("Roboto Mono", 22), bg="#fce4ec").pack(pady=20)
    payment_entry = tk.Entry(payment_window, font=("Roboto Mono", 24))
    payment_entry.pack(pady=20)

    tk.Button(payment_window, text="Submit Payment", font=("Roboto Mono", 24), command=process_payment).pack(pady=40)

# Run the vending machine
welcome_page()
