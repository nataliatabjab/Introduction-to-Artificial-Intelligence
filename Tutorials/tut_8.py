import matplotlib.pyplot as plt

# Create a figure
fig, ax = plt.subplots(figsize=(8, 5))

# Draw nodes for B1, B2, B3
ax.plot([0, 1], [0, 1], 'k-')  # root to B1
ax.plot([0, 1], [0, 0], 'k-')  # root to B2
ax.plot([0, 1], [0, -1], 'k-') # root to B3

# Draw nodes for A given B1, B2, B3
ax.plot([1, 2], [1, 1.5], 'k-')
ax.plot([1, 2], [1, 0.5], 'k-')

ax.plot([1, 2], [0, 0.5], 'k-')
ax.plot([1, 2], [0, -0.5], 'k-')

ax.plot([1, 2], [-1, -0.5], 'k-')
ax.plot([1, 2], [-1, -1.5], 'k-')

# Labels
ax.text(0, 0, "Start", ha='center', va='center', fontsize=12, bbox=dict(boxstyle="round", fc="w"))
ax.text(1, 1, "B1", ha='center', va='center', fontsize=12, bbox=dict(boxstyle="round", fc="w"))
ax.text(1, 0, "B2", ha='center', va='center', fontsize=12, bbox=dict(boxstyle="round", fc="w"))
ax.text(1, -1, "B3", ha='center', va='center', fontsize=12, bbox=dict(boxstyle="round", fc="w"))

ax.text(2, 1.5, "A", ha='center', va='center', fontsize=12, bbox=dict(boxstyle="round", fc="w"))
ax.text(2, 0.5, "¬A", ha='center', va='center', fontsize=12, bbox=dict(boxstyle="round", fc="w"))
ax.text(2, 0.5, "¬A", ha='center', va='center', fontsize=12, bbox=dict(boxstyle="round", fc="w"))

ax.text(2, 0.5, "A", ha='center', va='center', fontsize=12, bbox=dict(boxstyle="round", fc="w"))
ax.text(2, -0.5, "¬A", ha='center', va='center', fontsize=12, bbox=dict(boxstyle="round", fc="w"))

ax.text(2, -0.5, "A", ha='center', va='center', fontsize=12, bbox=dict(boxstyle="round", fc="w"))
ax.text(2, -1.5, "¬A", ha='center', va='center', fontsize=12, bbox=dict(boxstyle="round", fc="w"))

# Edge labels (probabilities)
ax.text(0.5, 0.5, "P(B1)", fontsize=10, rotation=30)
ax.text(0.5, 0, "P(B2)", fontsize=10, rotation=0)
ax.text(0.5, -0.5, "P(B3)", fontsize=10, rotation=-30)

ax.text(1.5, 1.25, "P(A|B1)", fontsize=10)
ax.text(1.5, 0.75, "P(¬A|B1)", fontsize=10)

ax.text(1.5, 0.25, "P(A|B2)", fontsize=10)
ax.text(1.5, -0.25, "P(¬A|B2)", fontsize=10)

ax.text(1.5, -0.75, "P(A|B3)", fontsize=10)
ax.text(1.5, -1.25, "P(¬A|B3)", fontsize=10)

# Formatting
ax.axis('off')
ax.set_title("Mutually Disjoint Events B1, B2, B3 Partitioning the Sample Space", fontsize=14)
plt.show()
