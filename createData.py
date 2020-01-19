from anytree import Node, RenderTree
from anytree.search import find

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

#print(arrData)


def addNode(node, crew, tags):
    print(node, crew, tags)
    
    tagLen = len(tags)
    
    #keep current children
    children = []
    for child in node.children:
        children.append(child)
    
    if tagLen > 1:
        if find(node, lambda node: node.name==tags[0], maxlevel=node.depth+2):
            print('taglen>1 && find')
            newChild = Node(tags[0], parent=node)
            addNode(find(node, lambda node: node.name==tags[0], maxlevel=node.depth+2), crew, tags[1:])
        else:
            print('taglen>1 && !find')
            addNode(Node(tags[0], parent=node), crew, tags[1:])
    elif tagLen == 1:
        if find(node, lambda node: node.name==tags[0], maxlevel=node.depth+2):
            if not hasattr(find(node, lambda node: node.name==tags[0], maxlevel=node.depth+2), 'result'):
                print('taglen==1 && find && not hasattr')
                find(node, lambda node: node.name==tags[0], maxlevel=node.depth+2).result = crew
                return
            else:
                print('taglen==1 && find && hasattr')
                print("duplicate!")
                return
        else:
            print('taglen==1 && !find')
            newChild = Node(tags[0], parent=node, result=crew)
    else:
        print('taglen==0')
        return
# End addNode()
    
#make dictionaries from array
dicCrew = {}    #column = 1
dicTag = {}     #column != 1

crewIdx = len(dicCrew)
tagIdx = len(dicTag)

cols = []

rNode = Node("rNode")

inputCrew = -1
inputTags = []

for row in arrData:
    if row[0] not in dicCrew.values():
        dicCrew[crewIdx] = row[0]
        crewIdx += 1
    
    cols = row[1:]
    
    for col in cols:
        if col not in dicTag.values():
            dicTag[tagIdx] = col
            tagIdx += 1
    # End col loop
    
    #change crew to key according to dictionary
    for k, v in dicCrew.items():
        if row[0] == v:
            inputCrew = k
    
    #change tags
    inputTags.clear()
    inputTags = [-1 for _ in range(len(cols))]
    
    for k, v in dicTag.items():
        if v in cols:
            inputTags[cols.index(v)] = k
    
    inputTags.sort()
    
    print(rNode, inputCrew, inputTags)
    addNode(rNode, inputCrew, inputTags)
# End row loop

#print(dicCrew)
#print(dicTag)

print(RenderTree(rNode))