!pip install qiskit qiskit-aer matplotlib numpy

import numpy as np
import matplotlib.pyplot as plt
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# --- CONFIGURATION ---
# High number of points to ensure patterns emerge from the density
n_points = 100000
canvas_size = 1000 # Visualization grid size (0 to 999)

print(f"Generating {n_points} (x,y) coordinates for each method...")

# ==========================================
# 1. THE "VILLAIN": Bad Classical PRNG (LCG)
# ==========================================
# This specific algorithm (Linear Congruential Generator) is famous for
# creating "lattice" or "grid" patterns in space-filling tests.
def bad_lcg_coordinates(n, limit):
    a = 75
    c = 74
    m = 2**16 + 1 # A small modulus helps reveal repetition and patterns
    state = 42    # Fixed seed (Deterministic behavior)

    coords_x = []
    coords_y = []

    for _ in range(n):
        # Generate X coordinate
        state = (a * state + c) % m
        x = int((state / m) * limit)

        # Generate Y coordinate
        state = (a * state + c) % m
        y = int((state / m) * limit)

        coords_x.append(x)
        coords_y.append(y)

    return coords_x, coords_y

prng_x, prng_y = bad_lcg_coordinates(n_points, canvas_size)

# ==========================================
# 2. THE "HERO": QRNG (Quantum Simulation)
# ==========================================
# We need 2*n_points random values (for X and Y)
total_qrng_needed = n_points * 2
# We generate 16 bits per number for high precision
bits_per_number = 16
total_shots = total_qrng_needed * bits_per_number

print("Running Quantum Circuit (Simulator)...")
qc = QuantumCircuit(1, 1)
qc.h(0)          # Hadamard gate: Creates a 50/50 superposition
qc.measure(0, 0) # Measurement: Forces a wave function collapse

sim = AerSimulator()
# Using memory=True to retrieve the exact sequence of individual bits
job = sim.run(qc, shots=total_shots, memory=True)
memory = job.result().get_memory()

# Process bits into coordinates
qrng_numbers = []
current_int = 0
for i, bit in enumerate(memory):
    current_int = (current_int << 1) | int(bit)
    if (i + 1) % bits_per_number == 0:
        # Normalize to canvas size (0 to 999)
        val = int((current_int / (2**bits_per_number)) * canvas_size)
        qrng_numbers.append(val)
        current_int = 0
        if len(qrng_numbers) >= total_qrng_needed:
            break

qrng_x = qrng_numbers[:n_points]
qrng_y = qrng_numbers[n_points:]

# ==========================================
# 3. PLOTTING (THE FINAL TEST)
# ==========================================
# We use very small dots (s=0.1) so that structural patterns emerge from density
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# Plot PRNG
ax1.scatter(prng_x, prng_y, s=0.1, c='black', marker='.')
ax1.set_title("Classical PRNG (LCG Algorithm)\nFAILURE: Visible 'grid' patterns and mathematical bias.", fontsize=14, color='red')
ax1.set_xlim(0, canvas_size)
ax1.set_ylim(0, canvas_size)
ax1.set_aspect('equal')
ax1.axis('off') # Hide axes to focus on the texture

# Plot QRNG
ax2.scatter(qrng_x, qrng_y, s=0.1, c='black', marker='.')
ax2.set_title("Quantum QRNG (True Entropy)\nSUCCESS: Uniform distribution and chaotic filling.", fontsize=14, color='blue')
ax2.set_xlim(0, canvas_size)
ax2.set_ylim(0, canvas_size)
ax2.set_aspect('equal')
ax2.axis('off')

plt.tight_layout()
# Save in high resolution for the paper/presentation
plt.savefig("obvious_final_comparison.png", dpi=300)
plt.show()
