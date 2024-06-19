from beautifultable import BeautifulTable
subtable = BeautifulTable()
subtable.rows.append(["Game Master", 1])
subtable.rows.append(["Jugador", 2])
subtable.border.left = ''
subtable.border.right = ''
subtable.border.top = ''
subtable.border.bottom = ''#------------------------
table = BeautifulTable()
table.columns.header = ["Elija el rol con el que \nfuncionará su cuenta y escoja enter: "]
table.rows.append([subtable])
table.columns.padding_left[0] = 0
table.columns.padding_right[0] = 0
table.set_style(BeautifulTable.STYLE_SEPARATED)

def chooseGMoJ(a):
    if(a=='1'):
        choice="GM"
        print("Game Master")
    elif(a=='2'):
        choice="J"
        print("Jugador")
    else:
        print("Porfavor, escoja una de las funciones mostradas: ")
    return choice

#TESTEO
print(table)
b = input("Value: ")
chooseGMoJ(b)

print(chooseGMoJ)
#TESTEO