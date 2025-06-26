import json
import pandas as pd
from openpyxl import load_workbook
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.utils import get_column_letter

# Load the devex.json file
with open('devex.json', 'r') as f:
    data = json.load(f)

properties = data['trigger']['userInputs']['properties']
#print(json.dumps(properties))
# Prepare data for Excel
rows = []
headers = ['Field', 'Title', 'Type', 'Enum', 'Description']
for key, prop in properties.items():
    # Check for nested 'items' property with 'enum'
    if 'items' in prop and isinstance(prop['items'], dict) and 'enum' in prop['items']:
        enum_list = prop['items']['enum']
    else:
        enum_list = prop.get('enum', []) if 'enum' in prop else []
    enum_str = ",".join(str(e) for e in enum_list)
    row = {
        'Field': key,
        'Title': prop.get('title', ''),
        'Type': prop.get('type', ''),
        'Enum': enum_str,  # This will be used for dropdown
        'Description': prop.get('description', '')
    }
    rows.append(row)

df = pd.DataFrame(rows, columns=headers)

# Write to Excel
excel_path = 'devex_survey.xlsx'
df.to_excel(excel_path, index=False)

# Add data validation for enum fields in the Enum column only
wb = load_workbook(excel_path)
ws = wb.active

enum_col_idx = headers.index('Enum') + 1
enum_col_letter = get_column_letter(enum_col_idx)

for idx, row in enumerate(rows, start=2):  # start=2 to skip header
    if row['Enum']:
        dv = DataValidation(type="list", formula1=f'"{row["Enum"]}"', allow_blank=True)
        ws.add_data_validation(dv)
        dv.add(f'{enum_col_letter}{idx}')  # Apply to the Enum cell only
        ws[f'{enum_col_letter}{idx}'].value = ""

wb.save(excel_path)
print(f"Excel file '{excel_path}' created with survey properties.")
