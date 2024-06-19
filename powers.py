from beautifultable import BeautifulTable

def chooseElement(a):
    if a == '1':
        element = "Fuego"
        print("Poder de Fuego")
    elif a == '2':
        element = "Hielo"
        print("Poder de Hielo")
    elif a == '3':
        element = "Agua"
        print("Poder de Agua")
    else:
        print("Por favor, elija una de las opciones mostradas.")
        element = None
    return element

subtable = BeautifulTable()
subtable.rows.append(["Fuego", 1])
subtable.rows.append(["Hielo", 2])
subtable.rows.append(["Agua", 3])
subtable.border.left = ''
subtable.border.right = ''
subtable.border.top = ''
subtable.border.bottom = ''

table = BeautifulTable()
table.columns.header = ["Elija el poder elemental: "]
table.rows.append([subtable])
table.columns.padding_left[0] = 0
table.columns.padding_right[0] = 0
table.set_style(BeautifulTable.STYLE_SEPARATED)

# TESTEO
print(table)
b = input("Valor: ")
element_choice = chooseElement(b)
print(f"Elegiste: {element_choice}")
