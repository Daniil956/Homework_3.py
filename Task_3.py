t = {"AEIOULNSTRАВЕИНОРСТ": 1, "DGДКЛМПУ": 2, "BCMБГЁЬЯ": 3,
     "FHVWYЙЫ": 4, "ЖЗХЦЧK": 5, " JХШЭЮ": 8, "QZФЩЪ": 10}

word = input("Enter word: ")
print(sum(i[1] for i in t.items() for j in word if j.upper() in i[0]))
