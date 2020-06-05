adressbuch = ["Moskau", "Dortmund", "Tokyo"]

for entry in adressbuch:
    print(entry)

print(30*'*')

name = "Melone"
for buchstabe in name:
    if buchstabe == "l":
        continue
    print(buchstabe)