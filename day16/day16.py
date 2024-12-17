from prettytable import PrettyTable
table = PrettyTable()
table.field_names = ["Nombre","Edad","Pais"]
table.add_rows([
    ["Ignacio",19,"Arg"],
    ["Manuel",15,"Arg"]
])
table.align = "l"
print(table)