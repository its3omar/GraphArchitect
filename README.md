
# 🧠 Python Graph Architect

An interactive Python application for building, visualizing, and analyzing graph data structures using classic algorithms and real-time animations.

---

## 🚀 Overview

**Python Graph Architect** is a powerful educational and visualization tool designed to help students and developers understand graph theory عملياً.

The project combines:

* Graph data structure implementation
* Advanced algorithms
* Real-time visualization with animations

---

## ✨ Features

### 🏗️ Graph Management

* Add / Remove Nodes
* Add / Remove Edges
* Automatic random edge weights

---

### 🔍 Traversal Algorithms

* 🔸 Breadth-First Search (BFS)
* 🔸 Depth-First Search (DFS)

➡️ مع عرض تفاعلي خطوة بخطوة

---

### 📊 Graph Analysis

* ✔️ Check Connectivity
* ✔️ Detect Tree
* ✔️ Euler Path / Circuit detection

---

### 🌳 Tree Algorithms

* 🔹 Prüfer Code Encoding

---

### 🧮 Optimization Algorithms

* 🔹 Kruskal Minimum Spanning Tree (MST)
* 🔹 A* Search Algorithm

---

### 🎨 Visualization

* باستخدام:

  * `NetworkX`
  * `Matplotlib`

* مميزات:

  * تلوين العقد (Nodes)
  * تلوين الحواف (Edges)
  * Animation لكل خوارزمية
  * عرض الأوزان

---

## 🧠 Algorithms Implemented

| Algorithm   | Description                  |
| ----------- | ---------------------------- |
| BFS         | Level-order traversal        |
| DFS         | Depth traversal              |
| Kruskal     | Minimum Spanning Tree        |
| A*          | Shortest path with heuristic |
| Prüfer Code | Tree encoding                |
| Euler Check | Graph classification         |

---

## 📂 Project Structure

```
Python-Graph-Architect/
│
├── Logic.py        # Core Graph + Algorithms
├── Ui.py           # Visualization & Animation
├── main.py         # Interactive CLI Menu
└── README.md
```

---

## 🛠️ Technologies Used

* Python 🐍
* NetworkX
* Matplotlib

---

## ⚙️ Installation

```bash
git clone https://github.com/your-username/python-graph-architect.git
cd python-graph-architect
pip install networkx matplotlib
```

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🖥️ Usage

بعد تشغيل البرنامج، سيظهر لك Menu:

```
1) Add Node
2) Remove Node
3) Add Edge
4) Remove Edge
5) BFS
6) DFS
7) Check connectivity
8) Check Euler
9) Check tree
10) Prufer code
11) Kruskal MST
12) A* search
0) Exit
```

---

## 🎬 Example Workflow

1. Add nodes: A, B, C, D
2. Connect them with edges
3. Run BFS or DFS
4. شاهد الحركة مباشرة على الرسم 😍

---

## 📈 Sample Output

* العقد تتحول إلى:

  * 🟡 أثناء الزيارة
  * 🟢 في المسار النهائي
  * 🔴 في حالات الفشل

---

## 🔮 Future Improvements

* GUI بدل CLI (Tkinter / PyQt) 🎨
* دعم Directed Graphs
* إضافة Dijkstra Algorithm
* حفظ وتحميل Graph من ملف
* تحسين الـ A* بهيوريستك حقيقي

---

## 👨‍💻 Author

**Omar Ismail**

---

## ⭐ Why This Project?

هذا المشروع ممتاز لعرض:

* فهمك لهياكل البيانات
* تطبيقك للخوارزميات
* قدرتك على Visualization
* كتابة كود نظيف Modular

---

## 📄 License

MIT License

