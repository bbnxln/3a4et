def get_row(rowIndex):
    row = [1]
    for _ in range(rowIndex):
        new_row = [1]
        for i in range(len(row) - 1):
            new_row.append(row[i] + row[i + 1])
        new_row.append(1)
        row = new_row
    return row
