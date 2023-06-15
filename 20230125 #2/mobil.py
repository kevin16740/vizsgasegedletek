from Employee import Employee

employees: list[Employee] = []

f = open('mobil.csv','r',encoding='utf-8')
for row in f:
    employees.append(Employee(row))
f.close()

print(f'{len(employees)} dolgozónak van céges telefonja.')

count = 0
for item in employees:
    if item.department == 'Informatika':
        count += 1
print(f'Az informatika osztályon {count} embernek van mobiltelefonja.')

