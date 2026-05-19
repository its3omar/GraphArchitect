# main.py
import matplotlib.pyplot as plt

from Ui import (
    AddNode_UI, RemoveNode_UI, AddEdge_UI, RemoveEdge_UI,
    DFS_UI, BFS_UI, isConnected_UI, isEuler_UI,isTree_UI,TypePruferEncode_UI,Kruskal_UI,AStar_UI
)

plt.ion()

def main():
    while True:
        print("\n1) Add Node\n2) Remove Node\n3) Add Edge\n4) Remove Edge\n5) BFS\n6) DFS\n7) Check if connected\n8) Check Euler\n9) Check if Tree\n10) Type Prufer Encode\n11)Kruskal\n12)A*\n0) Exit")
        c = input("> ")
        if c == "1":    AddNode_UI(input("Node label: "))
        elif c == "2":  RemoveNode_UI(input("Node label: "))
        elif c == "3":  AddEdge_UI(input("Node A: "), input("Node B: "))
        elif c == "4":  RemoveEdge_UI(input("Node A: "), input("Node B: "))
        elif c == "5":  BFS_UI(input("Start node: "))
        elif c == "6":  DFS_UI(input("Start node: "))
        elif c == "7":  isConnected_UI()
        elif c == "8":  isEuler_UI()
        elif c == "9":  isTree_UI()
        elif c == "10": TypePruferEncode_UI()
        elif c == "11": Kruskal_UI()
        elif c == "12": AStar_UI(input("Start node: "), input("Goal node: "))
        elif c == "0":  break
        
if __name__ == "__main__":
    main()
