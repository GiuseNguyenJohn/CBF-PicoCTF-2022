#!/usr/bin/python3

encoded = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V8450214}1"

rows = []
# number of columns = 3
# the column number that was shifted = 3
# direction of shift = -1
for x in range(0, len(encoded), 3):
    rows.append(encoded[x:x+3])

# add items to the beginning of the row list based on the shift
for x in range(0, 1):
    rows.insert(0, "")

rows.append("    ")

decoded = ""
for row_number in range(0, len(rows) - 1):
    row = rows[row_number + 1]
    repaired_row = ""
    first_part = rows[row_number][:-1]
    shifted_letter = row[-1]
    repaired_row += first_part + shifted_letter
    decoded += repaired_row

print(decoded)
