from anytree import Node, RenderTree
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
    
    '''
    rootNode = Node("root", children=[
        Node("0", children=[
            Node("1", result="a" , children=[
                Node("2", result="b")
            ]),
            Node("2", result="c")]),
        Node("1", children=[
            Node("3", result="d")
        ])
    ])
    '''
    
    #set root data source
    rootNode = data.root
    
    #print default data
    print(RenderTree(rootNode), '\n')
    
    myTags = ['메딕', '서포트', '프틸', '와파린']
    
    myTags = transTags(myTags, data.dicTag)
    
    #search
    searchResult(rootNode, myTags)
# End Main