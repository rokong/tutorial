from anytree import Node, RenderTree
from anytree.search import findall
import createData as data

def transTags(tags, dic):
    result = []
    
    for k, v in dic.items():
        if v in tags:
            result.insert(tags.index(v), k)
    
    result.sort()
    
    return result
    
# End transTags()

def ResultAndPath(node):
    print("<"+data.dicCrew[node.result]+"> ", end="")
    
    for e in node._path[1:-1]:
        print(data.dicTag[e.name], end=", ")
    
    print(data.dicTag[node.name])
    
    return
# End ResultAndPath()

def searchResult(node, restMine):
    #print(node, restMine)
    
    if hasattr(node, 'result'):
        ResultAndPath(node)
    
    if node.is_leaf:
        #print("is leaf")
        return
    
    for i in restMine:
        #print(i, type(i))
        for j in node.children:
            #print("print j.name", j.name, type(j))
            if i == j.name:
                #print("before recursive")
                searchResult(j, restMine[restMine.index(i)+1:])
    
    return
# End Search()

# Start Main
if __name__=="__main__":
    
    #set root data source
    rootNode = data.root
    
    print("\n\n\n\n")
    print(RenderTree(rootNode))
    
    print(len(findall(rootNode, lambda node : node.is_leaf==True)))
    
    #print(data.dicTag)
    
    myTags = []
    
    tag = ""
    for i in range(5):
        #tag = input(str(i+1)+'번째 태그를 입력하세요 : ')
        if tag:
            myTags.insert(i, tag)
    
    myTags = ['군중제어', '메이어']
    
    #transforming
    myTags = transTags(myTags, data.dicTag)
    
    #print(myTags)
    
    #search
    print('\n<조합 가능한 대원들>')
    searchResult(rootNode, myTags)
# End Main