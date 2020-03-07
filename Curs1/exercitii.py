header1 = 'Name'
header2 = 'Age'
name = 'Mihai'
age = 24
header_row = f'| {header1:10} | {header2:10} |'
print(header_row)
print('-' * len(header_row))
print(f"| {name:10} | {age:10} |")

print(f'{"left":^20}')

print('{0} met {1}'.format("Amma", "BOb"))