
person = {
    "name": {
    "first_name": "Benno",
    "last_name": "Müller",
    },
    "hobbies": {
        "Skifahren",
        "Mathe",
        "Mathe"
    },
    "age": 23,
}
print(person)

print(person.get("name", None))
print(person.get("name").get("first_name"))