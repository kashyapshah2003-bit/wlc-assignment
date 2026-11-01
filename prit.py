import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------
# ASSIGNMENT 7: OFDM AND CYCLIC PREFIX
# -----------------------------------------------------

# Simulation parameters
N = 64
cp_lengths = [0, 8, 16]

# Fixed random seed for reproducibility
np.random.seed(7)

# -----------------------------------------------------
# 1. Generate QPSK symbols
# -----------------------------------------------------

# Two random bits per QPSK symbol
bits_I = np.random.randint(0, 2, N)
bits_Q = np.random.randint(0, 2, N)

# QPSK mapping: values = (+/-1 +/- j)/sqrt(2)
X = ((2 * bits_I - 1) +
     1j * (2 * bits_Q - 1)) / np.sqrt(2)

# -----------------------------------------------------
# 2. Generate OFDM symbol using IFFT
# -----------------------------------------------------

x = np.fft.ifft(X, N)

print("Number of subcarriers =", N)
print("Number of useful OFDM samples =", len(x))

# -----------------------------------------------------
# 3. Function for adding cyclic prefix
# -----------------------------------------------------

def add_cp(ofdm_symbol, cp_length):

    if cp_length == 0:
        return ofdm_symbol.copy()

    cp = ofdm_symbol[-cp_length:]

    return np.concatenate((cp, ofdm_symbol))

# -----------------------------------------------------
# 4. Add CP = 0, 8 and 16
# -----------------------------------------------------

signals = {}

for cp in cp_lengths:

    signals[cp] = add_cp(x, cp)

# -----------------------------------------------------
# 5. Calculate efficiency and overhead
# -----------------------------------------------------

print("\nCP Comparison")
print("-" * 70)
print("CP\tTotal Samples\tEfficiency (%)\tOverhead (%)")
print("-" * 70)

efficiencies = []
overheads = []

for cp in cp_lengths:

    total_samples = N + cp

    efficiency = N / total_samples * 100

    # CP fraction of complete transmitted symbol
    overhead = cp / total_samples * 100

    efficiencies.append(efficiency)
    overheads.append(overhead)

    print(f"{cp}\t{total_samples}\t\t"
          f"{efficiency:.2f}\t\t{overhead:.2f}")

# -----------------------------------------------------
# 6. Plot original OFDM symbol
# -----------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(np.arange(N),
         np.real(x),
         marker='o',
         markersize=3)

plt.title("Real Part of One 64-Subcarrier OFDM Symbol")
plt.xlabel("Sample Index")
plt.ylabel("Amplitude")
plt.grid(True)

plt.tight_layout()
plt.show()

# -----------------------------------------------------
# 7. Plot OFDM signals with different CP lengths
# -----------------------------------------------------

plt.figure(figsize=(11, 6))

for cp in cp_lengths:

    signal = signals[cp]

    # Negative sample numbers indicate CP samples
    index = np.arange(-cp, N)

    plt.plot(index,
             np.real(signal),
             marker='.',
             label=f"CP = {cp}")

plt.axvline(x=0,
            linestyle='--',
            label="Start of Useful OFDM Symbol")

plt.title("OFDM Symbol with Different Cyclic Prefix Lengths")
plt.xlabel("Sample Index")
plt.ylabel("Real Part of Amplitude")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

# -----------------------------------------------------
# 8. Plot CP percentage overhead
# -----------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar([str(cp) for cp in cp_lengths], overheads)

plt.title("Cyclic Prefix Overhead")
plt.xlabel("CP Length (samples)")
plt.ylabel("Overhead (% of Transmitted Symbol)")
plt.grid(axis='y')

plt.tight_layout()
plt.show()

# -----------------------------------------------------
# 9. Plot OFDM efficiency
# -----------------------------------------------------

plt.figure(figsize=(8, 5))

plt.bar([str(cp) for cp in cp_lengths], efficiencies)

plt.title("OFDM Efficiency for Different CP Lengths")
plt.xlabel("CP Length (samples)")
plt.ylabel("Efficiency (%)")
plt.ylim(0, 110)
plt.grid(axis='y')

plt.tight_layout()
plt.show()

# -----------------------------------------------------
# 10. Verify that CP is copied from end of symbol
# -----------------------------------------------------

for cp in [8, 16]:

    copied_prefix = signals[cp][:cp]
    original_tail = x[-cp:]

    check = np.allclose(copied_prefix, original_tail)

    print(f"\nCP = {cp}: "
          f"Prefix equals last {cp} OFDM samples: {check}")
