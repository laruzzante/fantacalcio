#!/usr/bin/env python3

## Livio Ruzzante
## Randomizzatore del listone fantacalcio

import random

with open('/mnt/c/Users/livio/fantacalcio/listone_mantra_22.08.2021.tsv') as f:
    print(f"\nFile listone: {f}\n")
    lines = f.readlines()

print("Premi INVIO per estrarre un calciatore...\n")
print("ID\tRuolo\tNome\tSquadra\tQuotazione")

i=0
size=len(lines)

while len(lines) > 0:
    i += 1
    input()
    j = random.choice(range(len(lines)))
    print(f"{lines[j].strip()} ------- {i}/{size}")
    lines.pop(j)
