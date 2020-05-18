from anytree import Node, RenderTree
from anytree.search import find, findall

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

def searchAddNode(CurNode, crew, tags):
    #print('\n', CurNode, crew, tags)
    
    tagLen = len(tags)
    
    #keep current children
    children = []
    childrenName = []
    for child in CurNode.children:
        children.append(child)
        childrenName.append(child.name)
    
    if tagLen > 1:
        if tags[0] in childrenName:
            #print('taglen>1 && find')
            #print(node, crew, tags)
            #print(RenderTree(node), '\n')
            searchAddNode(children[childrenName.index(tags[0])], crew, tags[1:])
        else:
            #print("###############33")
            #print('taglen>1 && !find')
            #print(node, crew, tags)
            #print(RenderTree(node), '\n')
            searchAddNode(Node(tags[0], parent=CurNode), crew, tags[1:])
    elif tagLen == 1:
        if tags[0] in childrenName:
            if not hasattr(children[childrenName.index(tags[0])], 'result'):
                #print('taglen==1 && find && not hasattr')
                #print('\n', CurNode, crew, tags)
                #print(dicTag)
                #print(find(CurNode, filter_ = lambda node: node.name==tags[0], maxlevel=CurNode.depth+1))
                children[childrenName.index(tags[0])].result = crew
                return
            else:
                #print('taglen==1 && find && hasattr')
                print("duplicate!")
                return
        else:
            #print('taglen==1 && !find')
            Node(tags[0], parent=CurNode, result=crew)
    else:
        #print('taglen==0')
        return
# End searchAddNode()

#make dictionaries from array
dicCrew = {}    #column = 1
dicTag = {}     #column != 1

crewIdx = len(dicCrew)
tagIdx = len(dicTag)

cols = []

root = Node("root")

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
    
    searchAddNode(root, inputCrew, inputTags)
# End row loop

#print(dicCrew)
#print(dicTag)

#print(RenderTree(root))