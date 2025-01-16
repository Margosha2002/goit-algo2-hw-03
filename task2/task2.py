import timeit
from BTrees.OOBTree import OOBTree
import pandas as pd

# Load data
data = pd.read_csv("generated_items_data.csv")


# Functions for adding items to OOBTree and dict
def add_item_to_tree(tree, item):
    tree[item["ID"]] = {
        "Name": item["Name"],
        "Category": item["Category"],
        "Price": item["Price"],
    }


def add_item_to_dict(d, item):
    d[item["ID"]] = {
        "Name": item["Name"],
        "Category": item["Category"],
        "Price": item["Price"],
    }


# Functions for range queries
def range_query_tree(tree, min_price, max_price):
    return list(tree.items(min=min_price, max=max_price))


def range_query_dict(d, min_price, max_price):
    return [(k, v) for k, v in d.items() if min_price <= v["Price"] <= max_price]


tree = OOBTree()
d = {}

# Add data to structures
for _, row in data.iterrows():
    item = row.to_dict()
    add_item_to_tree(tree, item)
    add_item_to_dict(d, item)


min_price = 100
max_price = 200

# Measure execution time for OOBTree
range_tree_time = timeit.timeit(
    lambda: range_query_tree(tree, min_price, max_price), number=100
)

# Measure execution time for dict
range_dict_time = timeit.timeit(
    lambda: range_query_dict(d, min_price, max_price), number=100
)

# Results
print(f"Total range_query time for OOBTree: {range_tree_time:.6f} seconds")
print(f"Total range_query time for Dict: {range_dict_time:.6f} seconds")
