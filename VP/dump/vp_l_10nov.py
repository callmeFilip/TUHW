# with open('lorem.txt') as f:
#     print(f.read())
# STRING = 'Curabitur non interdum lectus. \
#     Vivamus auctor dui sit amet consequat euismod. \
#     Phasellus justo elit, vehicula non lacus non, \
#     dignissim egestas purus. Ut mattis ligula ut est rhoncus, \
#     vitae euismod risus fringilla. Lorem ipsum dolor sit amet, \
#     consectetur adipiscing elit. Aliquam vitae feugiat lectus. \
#     Aliquam erat volutpat. Sed id nibh malesuada, convallis risus quis, \
#     tempor mi. Pellentesque semper leo quis nulla ultricies, ac consequat \
#     lectus semper. Class aptent taciti sociosqu ad litora torquent per \
#     conubia nostra, per inceptos himenaeos.123 '


# with open('lorem.txt', 'r') as f:
#     for line in f:
#         print(line.upper())

# with open('lorem.txt', 'a') as f:
#     f.write(STRING)

# with open('lorem.txt', 'rb') as f:
#     for line in f:
#         print(line)

# otvarqne na json ot python
# import json

# json.dump(x, f)  # zapisva sudurjanieto na x vuv fail f

# dump - serielizirane na obekta v textov file

# json.load(f)  # zarejda ot file v programata


# with open('data.json') as f:
#     data = json.load(f)

# print(type(data), data)

# result = []
# for block in data:
#     if block['key'].startswith('B'):
#         print(block)

# with open('result.json', 'w') as f:
#     json.dump(result, f)


# otvarqne na csv (excel) file
import csv

data = []

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['row1', 'row2'])
    for obj in data:
        writer.writerow(obj)
