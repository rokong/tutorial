#open txt file
try:
    f = open("data.txt", "r")
    lines = f.readlines()
except:
    print("Error in opening and reading data from txt file")
finally:
    f.close()

#transforming data into array
arrData = []

data = ""
for line in lines:
    data = line.replace("\n", "")
    data = data.rstrip("\t")
    arrData.append(data.split('\t'))

print(arrData)

#make dictionaries from array
dicCrew = {}    #column = 1
dicTag = {}     #column != 1

crewIdx = len(dicCrew)
tagIdx = len(dicTag)
for row in arrData:
    if row[0] not in dicCrew.values():
        dicCrew[crewIdx] = row[0]
        crewIdx += 1
    
    for col in row[1:]:
        if col not in dicTag.values():
            dicTag[tagIdx] = col
            tagIdx += 1
    # End col loop
# End row loop

print(dicCrew)
print(dicTag)