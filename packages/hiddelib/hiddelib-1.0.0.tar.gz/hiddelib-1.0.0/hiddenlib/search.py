import csv

def dbsearch(filename, keyword):
    results = []

    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if keyword in row.values():
                results.append(row)

    return results
