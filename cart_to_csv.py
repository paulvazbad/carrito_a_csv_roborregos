import json
import argparse
import csv
# Argument definition

parser = argparse.ArgumentParser(description='Processa un carrito de steren.')
parser.add_argument('--file', type=str, default='cart.json',
                    nargs='?', help='name of the json file (default cart.json)')
arguments = parser.parse_args()
# Open json


print("Opening " + arguments.file)

# valid keys

valid_keys = ['qty',
              'product_sku',
              'product_id',
              'product_name',
              'product_url',
              'product_price_value']

try:
    with open(arguments.file, encoding="utf8") as json_file:
        data = json.load(json_file)
        items = data["items"]
        print("Items en el carrito: " + str(len(items)))
        print('Procesando: ')
        for index, item in enumerate(items):
            print(".", end = '')
            updated = {key: (item[key]) for key in valid_keys}
            items[index] = updated
except IOError:
    print("I/O error")
print("\n")
csv_file = "output.csv"
try:
    print("Generando output.csv...")
    with open(csv_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=items[0].keys(),  delimiter=',',
                                quoting=csv.QUOTE_MINIMAL)
        writer.writeheader()
        print('Escribiendo: ')
        for item in items:
            print(".", end = '')
            writer.writerow(item)
    print('\n')
    print("Finalizado :)")
except IOError:
    print("I/O error")
