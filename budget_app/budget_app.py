class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
        
    def deposit(self, amount, description = ""):
        self.ledger.append({'amount': amount, 'description': description})
    
    def withdraw(self, amount, description = ""):
       #implement if condition for balance
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False
    
    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)
    
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, amount):
       return self.get_balance() >= amount
    
    def __str__(self):
        output = self.name.center(30, '*') + '\n'
        for item in self.ledger:
            output += f"{item['description'][:23].ljust(23)}{item['amount']:>7.2f}\n" #keep description if under 23. Over 23 troncate. Align left and fill spaces until 23
        output += f"Total: {self.get_balance():.2f}" #align right, 7 char, 2 decimal
        return output
        

def create_spend_chart(categories):
    spent = []
    for category in categories:
        cat_spent = sum(-item["amount"] for item in category.ledger if item["amount"] < 0)
        spent.append(cat_spent)
    
    total_spent = sum(spent)
    percentages = [int((amount / total_spent) * 100) for amount in spent]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:3d}| "
        for percentage in percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"
    
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"

    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += f"{category.name[i]}  "
            else:
                chart += "   "
        if i < max_name_length - 1:
            chart += "\n"

    return chart

# Test
food = Category("Food")
clothing = Category("Clothing")
Auto = Category("Auto")

food.deposit(1000, "initial deposit")
food.withdraw(105.55)
clothing.deposit(1000, "initial deposit")
clothing.withdraw(33.40)
Auto.deposit(1000, "initial deposit")
Auto.withdraw(15.89)

print(food)
#print(clothing)
print(create_spend_chart([food, clothing, Auto]))
