from anytree import Node, RenderTree

def ResultAndPath(node):
    print("<"+node.result+"> ", end="")
    
    for e in node._path[1:-1]:
        print(e.name, end=", ")
    
    print(node.name)
    
    return
# End ResultAndPath()

def searchResult(node, restMine):
    if hasattr(node, 'result'):
        ResultAndPath(node)
    
    if node.is_leaf:
        return
    
    for i in restMine:
        for j in node.children:
            if i == j.name:
                searchResult(j, restMine[restMine.index(i)+1:])
    
    return
# End Search()

root = Node("root", children=[
    Node("0", children=[
        Node("1", result="a" , children=[
            Node("2", result="b")
        ]),
        Node("2", result="c")]),
    Node("1", children=[
        Node("3", result="d")
    ])
])

# Start Main
print(RenderTree(root))

searchResult(root, ["0", "1", "2"])
