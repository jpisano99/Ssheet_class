from Ssheet_class import Ssheet

sheet_name = 'Coverage'
# sheet_name = 'Tetration On-Demand POV Status'

my_sheet = Ssheet(sheet_name)
# print (help(Ssheet))

print('My ID IS', my_sheet.id)
print(my_sheet.columns)
print(my_sheet.col_name_idx)
print(my_sheet.col_id_idx)

# # Add Rows Example
# Look up the col_id for the 'tsa'
my_col_id = my_sheet.col_name_idx['tsa']

cell_data = []  # List of cell data
my_rows = []  # List of rows that includes cell data

cell_data.append({
    'column_id': my_col_id,
    'value': 'Jim',
    'strict': False})

my_rows.append(cell_data)
my_sheet.add_rows(my_rows)
my_sheet.refresh()





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
