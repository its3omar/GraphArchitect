# ui.py
import time
import networkx as nx
import matplotlib.pyplot as plt
import heapq

from Logic import (
    Nodes, Edges,
    AddNode_logic, RemoveNode_logic, AddEdge_logic, RemoveEdge_logic,
    DFS_logic, BFS_logic, isConnectedLogic, isEulerLogic, isTreeLogic,
    TypePruferEncodeLogic, KruskalLogic, AStar_logic
)

Colors = {}
EdgeColors = {}  # لتلوين الحواف

# ---------------------------------
#            UI PART
# ---------------------------------
def DrawGraph():
    G = nx.Graph()
    # إضافة العقد
    G.add_nodes_from(Nodes)
    # إضافة الحواف مع الوزن
    for e in Edges:
        G.add_edge(e[0], e[2], weight=e[1])

    plt.clf()
    pos = nx.spring_layout(G, seed=42)  # ثبات ترتيب العقد

    # ألوان العقد
    node_colors = [Colors.get(n, "lightblue") for n in Nodes]

    # ألوان الحواف
    def get_edge_color(u, v):
        return EdgeColors.get((u, v)) or EdgeColors.get((v, u)) or "black"

    edge_colors = [get_edge_color(u, v) for u, v in G.edges()]

    # رسم الرسم البياني
    nx.draw(
        G, pos,
        with_labels=True,
        node_color=node_colors,
        edge_color=edge_colors,
        node_size=1000,
        font_size=12,
        width=2
    )

    # رسم أوزان الحواف
    edge_labels = {(e[0], e[2]): e[1] for e in Edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='blue', font_size=10)

    plt.title("Live Graph Visualization")
    plt.pause(0.1)


def RecolorToDefault():
    for n in Nodes:
        Colors[n] = "lightblue"
    for e in Edges:
        EdgeColors[(e[0], e[2])] = "black"
    DrawGraph()


# ------- UI Versions of actions -------
def AddNode_UI(n):
    if AddNode_logic(n):
        Colors[n] = "lightblue"
        DrawGraph()

def RemoveNode_UI(n):
    if RemoveNode_logic(n):
        Colors.pop(n, None)
        DrawGraph()

def AddEdge_UI(a, b):
    if AddEdge_logic(a, b):
        DrawGraph()

def RemoveEdge_UI(a, b):
    if RemoveEdge_logic(a, b):
        DrawGraph()


# ---------- DFS UI ----------
def DFS_UI(start):
    order = DFS_logic(start)
    prev = None
    for node in order:
        Colors[node] = "yellow"
        if prev:
            EdgeColors[(prev, node)] = "yellow"
        DrawGraph()
        time.sleep(1)
        prev = node
    RecolorToDefault()


# ---------- BFS UI ----------
def BFS_UI(start):
    order = BFS_logic(start)
    visited_nodes = set()
    for node in order:
        Colors[node] = "red"
        for prev in visited_nodes:
            if (prev, node) in EdgeColors or (node, prev) in EdgeColors:
                EdgeColors[(prev, node)] = "red"
        visited_nodes.add(node)
        DrawGraph()
        time.sleep(1)
    RecolorToDefault()


# ---------- Connectivity UI ----------
def isConnected_UI():
    if isConnectedLogic():
        for n in Nodes:
            Colors[n] = "lime"
    else:
        for n in Nodes:
            Colors[n] = "red"
    DrawGraph()
    time.sleep(1)
    RecolorToDefault()


# ---------- Euler UI ----------
def isEuler_UI():
    situation = isEulerLogic()
    if situation == 1:
        for n in Nodes:
            Colors[n] = "lime"
    elif situation == 0:
        for n in Nodes:
            Colors[n] = "red"
    elif situation == 2:
        for n in Nodes:
            Colors[n] = "orange"
    DrawGraph()
    time.sleep(1)
    RecolorToDefault()


# ---------- Tree UI ----------
def isTree_UI():
    if isTreeLogic():
        for n in Nodes:
            Colors[n] = "lime"
        for e in Edges:
            EdgeColors[(e[0], e[2])] = "brown"
    else:
        for n in Nodes:
            Colors[n] = "red"
    DrawGraph()
    time.sleep(1)
    RecolorToDefault()


# ---------- Prufer UI ----------
def TypePruferEncode_UI():
    prufer_list = TypePruferEncodeLogic()
    if prufer_list == -1:
        for n in Nodes:
            Colors[n] = "red"
        DrawGraph()
        time.sleep(1)
        RecolorToDefault()
        return
    else:
        print(*prufer_list)
        time.sleep(5)


# ---------- Kruskal UI ----------
def Kruskal_UI():
    mst = KruskalLogic()
    if not mst:
        print("MST not found")
        return

    RecolorToDefault()
    for u, w, v in mst:
        Colors[u] = "lime"
        Colors[v] = "lime"
        EdgeColors[(u, v)] = "lime"
        DrawGraph()
        time.sleep(1)
    RecolorToDefault()


# ---------- A* UI ----------
def AStar_UI(start, goal):
    path, visited_order, cost = AStar_logic(start, goal)
    
    if not path:
        print(f"No path found from {start} to {goal}")
        for n in visited_order:
            Colors[n] = "red"
        DrawGraph()
        time.sleep(1)
        RecolorToDefault()
        return
    
    RecolorToDefault()
    
    # Visualize nodes being explored (visited order)
    for node in visited_order:
        if node != start and node != goal:
            Colors[node] = "yellow"
        DrawGraph()
        time.sleep(0.5)
    
    # Highlight the final path
    for i, node in enumerate(path):
        Colors[node] = "lime"
        if i > 0:
            prev = path[i - 1]
            EdgeColors[(prev, node)] = "lime"
        DrawGraph()
        time.sleep(1)
    
    print(f"Path found: {' -> '.join(map(str, path))}")
    print(f"Total cost: {cost}")
    time.sleep(2)
    RecolorToDefault()