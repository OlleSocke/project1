gerichte = ["Pizza", "Sauerkraut", "Paella", "Hamburger", "Alfajores"]
laender = ["Italien", "Deutschland", "Spanien", "USA"]

zippy = zip(laender, gerichte)
print(zippy)

for x in zippy:
    print(x)

#wenn eine Liste länger: zip immer nur so lang wie kürzeste Liste