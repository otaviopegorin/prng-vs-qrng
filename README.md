# 🎲 Visual Comparative Analysis: PRNG vs. QRNG

This project provides a visual and statistical demonstration of the fundamental difference between **Pseudo-Random Number Generators (PRNG)**, based on classical deterministic algorithms, and **Quantum Random Number Generators (QRNG)**, based on quantum mechanics simulation.

Through the **Space-Filling Test**, this experiment highlights how flawed deterministic algorithms create hidden geometric patterns, whereas quantum entropy results in true uniformity.

## 📋 About the Project

The script generates two high-resolution scatter plots containing thousands of coordinate points $(x, y)$ to compare:

1.  **The "Villain" (PRNG - Pseudo-Random Number Generator):**
    * **Algorithm:** Manual implementation of a **LCG (Linear Congruential Generator)**.
    * **Parameters:** Uses parameters known to be flawed (based on IBM's infamous **RANDU** algorithm).
    * **Visual Result:** The formation of "stripes", lattices, or grids (The Marsaglia Effect), proving the generator is predictable.

2.  **The "Hero" (QRNG - Quantum Random Number Generator):**
    * **Method:** Uses **Qiskit** (IBM's Quantum SDK) to simulate a quantum circuit.
    * **Logic:** Applies a **Hadamard Gate** to create superposition and measures the wave function collapse.
    * **Visual Result:** A uniform, chaotic cloud of points with no discernible geometric patterns.

## 🚀 Technologies Used

* **Python 3.x**
* **Qiskit & Qiskit Aer:** For quantum circuit simulation.
* **Matplotlib:** For high-resolution data visualization (Scatter Plots).
* **NumPy:** For numerical array manipulation.

## 📦 Installation

To run this project, you need to install the required Python libraries. Run the following command in your terminal or Jupyter Notebook:

```bash
pip install qiskit qiskit-aer matplotlib numpy
