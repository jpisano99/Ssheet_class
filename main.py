from Ssheet_class import Ssheet

sheet_name = 'jim'
# sheet_name = 'Tetration On-Demand POV Status'

my_sheet = Ssheet(sheet_name)
print (help(Ssheet))

print('My ID IS', my_sheet.id)
print(my_sheet.columns)

if my_sheet.id == -1:
    sheet_name = 'delete me'
    col_dict = [
        {'title': 'col1',
            'type': 'CHECKBOX',
            'symbol': 'STAR'},

        {'title': 'col2',
            'primary': True,
            'type': 'TEXT_NUMBER'}
        ]
    print(col_dict)

    my_sheet.create_sheet(sheet_name, col_dict)
    print(my_sheet.id)
    print(my_sheet.columns)
