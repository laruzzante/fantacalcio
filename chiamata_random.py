#!/usr/bin/env python3

## Livio Ruzzante
## Randomizzatore del listone fantacalcio

import random
import pandas as pd

xls = pd.ExcelFile(r"Quotazioni_Fantacalcio_Ruoli_Mantra.xlsx")
sheetX = xls.parse(0, header=1)

print(f"\nFile listone: {xls}\n")

print(sheetX)

random_df = sheetX.sample(n=len(sheetX.index))

print("\n--- Randomizzazione listone effettuata ---")

random_df.to_csv('listone_randomizzato.tsv', sep='\t')

print("\n--- File salvato in 'listone_randomizzato.tsv' ---\n")

print("--- Premere INVIO per estrarre un calciatore ---")


for index, row in random_df.iterrows():
    input()
    print(row.to_frame().T)


# with open('Quotazioni_Fantacalcio_Ruoli_Mantra.xlsx') as f:
#     print(f"\nFile listone: {f}\n")
#     lines = f.readlines()
#     header1 = lines.pop(1) # Titolo file
#     header2 = lines.pop(2) # Nomi colonne

# print(lines)

# print("Premi INVIO per estrarre un calciatore...\n")
# print(f'{header2}')
# #print(f"ID\tRuolo\tNome\tSquadra\tQuotazione")

# i=0
# size=len(lines)

# while len(lines) > 0:
#     i += 1
#     input()
#     j = random.choice(range(len(lines)))
#     print(f"{lines[j].strip()} ------- {i}/{size}")
#     lines.pop(j)
