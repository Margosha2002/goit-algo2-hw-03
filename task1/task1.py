import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


G = nx.DiGraph()


edges = [
    ("Terminal 1", "Warehouse 1", 25),
    ("Terminal 1", "Warehouse 2", 20),
    ("Terminal 1", "Warehouse 3", 15),
    ("Terminal 2", "Warehouse 3", 15),
    ("Terminal 2", "Warehouse 4", 30),
    ("Terminal 2", "Warehouse 2", 10),
    ("Warehouse 1", "Shop 1", 15),
    ("Warehouse 1", "Shop 2", 10),
    ("Warehouse 1", "Shop 3", 20),
    ("Warehouse 2", "Shop 4", 15),
    ("Warehouse 2", "Shop 5", 10),
    ("Warehouse 2", "Shop 6", 25),
    ("Warehouse 3", "Shop 7", 20),
    ("Warehouse 3", "Shop 8", 15),
    ("Warehouse 3", "Shop 9", 10),
    ("Warehouse 4", "Shop 10", 20),
    ("Warehouse 4", "Shop 11", 10),
    ("Warehouse 4", "Shop 12", 15),
    ("Warehouse 4", "Shop 13", 5),
    ("Warehouse 4", "Shop 14", 10),
]

for u, v, capacity in edges:
    G.add_edge(u, v, capacity=capacity)


source = "SuperSource"
sink = "SuperSink"

for terminal in ["Terminal 1", "Terminal 2"]:
    G.add_edge(source, terminal, capacity=float("inf"))

for shop in [
    "Shop 1",
    "Shop 2",
    "Shop 3",
    "Shop 4",
    "Shop 5",
    "Shop 6",
    "Shop 7",
    "Shop 8",
    "Shop 9",
    "Shop 10",
    "Shop 11",
    "Shop 12",
    "Shop 13",
    "Shop 14",
]:
    G.add_edge(shop, sink, capacity=float("inf"))


flow_value, flow_dict = nx.maximum_flow(G, source, sink)


results = []
for terminal in ["Terminal 1", "Terminal 2"]:
    for warehouse, flow_to_warehouse in flow_dict[terminal].items():
        if flow_to_warehouse > 0:  # Потік від терміналу до складу
            for shop, flow_to_shop in flow_dict[warehouse].items():
                if flow_to_shop > 0:  # Потік від складу до магазину
                    results.append(
                        (terminal, shop, min(flow_to_warehouse, flow_to_shop))
                    )


df = pd.DataFrame(results, columns=["Terminal", "Shop", "Actual Flow (units)"])


print("Max Flow Value:", flow_value)
print("\nFlow Table:")
print(df)


df.to_csv("logistics_flow_results.csv", index=False)


pos = {
    "SuperSource": (0, 5),
    "Terminal 1": (1, 4),
    "Terminal 2": (1, 6),
    "Warehouse 1": (2, 3),
    "Warehouse 2": (2, 5),
    "Warehouse 3": (2, 7),
    "Warehouse 4": (2, 9),
    "Shop 1": (3, 2),
    "Shop 2": (3, 3),
    "Shop 3": (3, 4),
    "Shop 4": (3, 5),
    "Shop 5": (3, 6),
    "Shop 6": (3, 7),
    "Shop 7": (3, 8),
    "Shop 8": (3, 9),
    "Shop 9": (3, 10),
    "Shop 10": (3, 11),
    "Shop 11": (3, 12),
    "Shop 12": (3, 13),
    "Shop 13": (3, 14),
    "Shop 14": (3, 15),
    "SuperSink": (4, 8),
}

nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=8)
labels = nx.get_edge_attributes(G, "capacity")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)
plt.title("Logistics Network")
plt.show()
