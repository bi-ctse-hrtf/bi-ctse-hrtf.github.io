import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(12, 0.1))  # Wide and short

ax.text(0.5, 0.5, 'Mixture',
        fontsize=18,
        ha='center',
        va='center')

# Remove all axes
ax.axis('off')

# Tight layout, no padding
plt.tight_layout(pad=0)

# Save or show
plt.savefig('mixture_label.png', bbox_inches='tight')
# plt.show()

fig, ax = plt.subplots(figsize=(12, 0.1))  # Wide and short

ax.text(0.5, 0.5, 'Speaker 1',
        fontsize=18,
        ha='center',
        va='center')

# Remove all axes
ax.axis('off')

# Tight layout, no padding
plt.tight_layout(pad=0)

# Save or show
plt.savefig('speaker1_label.png', bbox_inches='tight')
# plt.show()

fig, ax = plt.subplots(figsize=(12, 0.1))  # Wide and short

ax.text(0.5, 0.5, 'Speaker 2',
        fontsize=18,
        ha='center',
        va='center')

# Remove all axes
ax.axis('off')

# Tight layout, no padding
plt.tight_layout(pad=0)

# Save or show
plt.savefig('speaker2_label.png', bbox_inches='tight')
# plt.show()
