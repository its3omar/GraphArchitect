# logic.py
import random
Nodes = []
Edges = []
# -----------------------
#        PURE LOGIC
# -----------------------

def AddNode_logic(nodeName):
    if nodeName not in Nodes:
        Nodes.append(nodeName)
        return True
    return False

def RemoveNode_logic(nodeName):
    if nodeName in Nodes:
        Nodes.remove(nodeName)
        global Edges
        Edges = [e for e in Edges if nodeName not in e]
        return True
    return False

def AddEdge_logic(a, b):
    if not(a in Nodes and b in Nodes):
      return False
    else:
      for e in Edges:
        if a==e[0] and b==e[2] or a==e[2] and b==e[0]:
            return False
    r=random.randint(1,8)
    Edges.append([a,r,b])
    return True

def RemoveEdge_logic(a, b):
    for e in Edges:
     if e[0]==a and e[2]==b or e[2]==a and e[0]==b:
        Edges.remove(e)
        return True
    return False


def BuildAdjList():
    adj = {n: [] for n in Nodes}
    for e in Edges:
        adj[e[0]].append(e[2])
        adj[e[2]].append(e[0])
    return adj


# ----- DFS Logic -----
def DFS_logic(start):
    if start not in Nodes:
        return []

    adj = BuildAdjList()
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            for neigh in adj[node]:
                if neigh not in visited:
                    stack.append(neigh)

    return list(visited)


# ----- BFS Logic -----
def BFS_logic(start):
    if start not in Nodes:
        return []

    adj = BuildAdjList()
    visited = set()
    queue = [start]
    order = []

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.add(node)
            order.append(node)
            for neigh in adj[node]:
                if neigh not in visited:
                    queue.append(neigh)

    return order


# ----- Connectivity -----
def isConnectedLogic():
    if not Nodes:
        return True
    visited = DFS_logic(Nodes[0])
    return len(visited) == len(Nodes)


# ----- Euler Logic -----
def isEulerLogic():
    if not isConnectedLogic():
        return 0
    adj = BuildAdjList()
    odd = 0
    for n in Nodes:
         if len(adj[n]) % 2 == 1:
             odd += 1
             
    if odd == 0:
        return 1
    elif odd == 2:
        return 2
def isTreeLogic():
    return len(Nodes)==len(Edges)+1 and isConnectedLogic()
def TypePruferEncodeLogic():
    # تحقق أن الرسم متصل وشجرة
    if not isTreeLogic():
        return -1

    adj = BuildAdjList()

    prufer = []

    # نحافظ على قائمة الأوراق (العقد ذات الدرجة 1)
    leaves = []

    for node in adj:
        if len(adj[node]) == 1:
            leaves.append(node)

    # نخلي الأوراق مرتبة دائماً
    leaves.sort()

    # نكرر لغاية ما يبقى عقدتان فقط
    while len(adj) > 2:

        # نأخذ أصغر ورقة
        leaf = leaves.pop(0)

        # جارتها الوحيدة
        neighbor = adj[leaf][0]

        # نضيف الجار لترميز بروفِر
        prufer.append(neighbor)

        # نحذف الورقة من الرسم
        adj[neighbor].remove(leaf)
        del adj[leaf]

        # إذا أصبحت درجة الجار 1 → صار ورقة جديدة
        if len(adj[neighbor]) == 1:
            # أضفه للأوراق والمحافظة على الترتيب
            leaves.append(neighbor)
            leaves.sort()

    return prufer
# دالة مساعدة: Union-Find
parent = {}
def find(u):
    if not parent[u] == u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    pu, pv = find(u), find(v)
    if pu != pv:
        parent[pu] = pv
        return True
    return False

# خوارزمية Kruskal
def KruskalLogic():
    if not Nodes or not Edges:
        return []

    # تهيئة Union-Find
    for node in Nodes:
        parent[node] = node

    # ترتيب الحواف حسب الوزن تصاعديًا
    sorted_edges = sorted(Edges, key=lambda e: e[1])

    mst = []  # قائمة MST النهائية

    for edge in sorted_edges:
        u, w, v = edge
        if union(u, v):  # إذا لم تكوّن دورة
            mst.append(edge)

        # توقف إذا اكتمل MST
        if len(mst) == len(Nodes) - 1:
            break

    return mst


# ----- A* Algorithm -----
def AStar_logic(start, goal, heuristic=None):
    """
    A* pathfinding algorithm.
    Returns a tuple: (path, visited_order, cost)
    If no path exists, returns ([], [], float('inf'))
    
    heuristic: function that takes a node and returns estimated cost to goal
    If None, uses a default heuristic (all nodes have equal distance)
    """
    if start not in Nodes or goal not in Nodes:
        return [], [], float('inf')
    
    if start == goal:
        return [start], [start], 0
    
    # Default heuristic: all nodes are equally distant
    if heuristic is None:
        heuristic = lambda node: 0
    
    adj = BuildAdjList()
    
    # open_set: list of (f_score, counter, node)
    import heapq
    open_set = [(heuristic(start), 0, start)]
    counter = 1
    
    # Track visited nodes for visualization
    visited_order = []
    
    # g_score: cost from start to node
    g_score = {node: float('inf') for node in Nodes}
    g_score[start] = 0
    
    # f_score: g_score + heuristic
    f_score = {node: float('inf') for node in Nodes}
    f_score[start] = heuristic(start)
    
    # came_from: track the path
    came_from = {}
    
    # closed_set: nodes already evaluated
    closed_set = set()
    
    while open_set:
        _, _, current = heapq.heappop(open_set)
        
        if current in closed_set:
            continue
        
        visited_order.append(current)
        closed_set.add(current)
        
        if current == goal:
            # Reconstruct path
            path = []
            node = goal
            while node in came_from:
                path.append(node)
                node = came_from[node]
            path.append(start)
            path.reverse()
            return path, visited_order, g_score[goal]
        
        # Check all neighbors
        for neighbor in adj[current]:
            if neighbor in closed_set:
                continue
            
            # Find edge weight between current and neighbor
            edge_weight = 1
            for e in Edges:
                if (e[0] == current and e[2] == neighbor) or (e[2] == current and e[0] == neighbor):
                    edge_weight = e[1]
                    break
            
            tentative_g = g_score[current] + edge_weight
            
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor)
                
                if neighbor not in [node for _, _, node in open_set]:
                    heapq.heappush(open_set, (f_score[neighbor], counter, neighbor))
                    counter += 1
    
    # No path found
    return [], visited_order, float('inf')

