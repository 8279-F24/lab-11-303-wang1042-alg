
contacts_input = input().strip()
search_name = input().strip()

contacts = {}
pairs = contacts_input.split()

for pair in pairs:
    name, phone = pair.split(',')
    contacts[name] = phone

print(contacts[search_name])