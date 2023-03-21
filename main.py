# Import PrettyTable class from prettytable library
from prettytable import PrettyTable

# Create object for PrettyTable class
table = PrettyTable()
# print(table)

# Add column to the table created
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
# print(table)

# Change the alignment of the data in table to left aligned
print(table.align)
table.align = "l"
print(table)