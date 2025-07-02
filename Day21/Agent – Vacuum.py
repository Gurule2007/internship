# Simple Reflex Agent – Vacuum Cleaner
# 🔹Objective:
# Simulate a simple reflex agent for a 1D or 2D vacuum cleaner world.

# 🔹Instructions:
# Create an environment as a list of rooms: e.g. ['Dirty', 'Clean', 'Dirty']

# Agent starts at position 0.

# If the current position is 'Dirty' → clean it.

# Move to the next room and repeat.

# Stop when all rooms are clean.
def vacuum_cleaner_world(environment):
    position = 0  
    steps = 0     

    print("Initial Environment:", environment)

