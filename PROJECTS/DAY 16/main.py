import turtle
from prettytable import PrettyTable

x = PrettyTable()


x.align = "r"
print(x.align)
names = ['Rohit', 'Mohitashdbakwd', 'Tohit']
marks = [10,20,30]
x.add_column("NAME", names)
x.add_column("Math", marks)
print(x)