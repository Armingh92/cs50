names_list = ["Albors", "Arsalan", "Baran", "Armin", "Saina"]
familys_list = ["Moridany", "Soltani nejad", "fazely", "Ghalandar mahale", "Salary"]
full_name = []
for i in range (0, len(names_list)):
    full_name.append(f"{names_list[i]} {familys_list[i]}")

print(full_name)