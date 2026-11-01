import numpy as np

# 1. Generate one simple OFDM symbol using IFFT
N = 64  # Number of subcarriers (FFT size)

# Generate random QPSK symbols (frequency domain)
symbols = np.random.choice([1+1j, -1-1j, 1-1j, -1+1j], size=N)

# Apply IFFT to get the time-domain OFDM symbol
ofdm_base = np.fft.ifft(symbols)

# 2 & 3. Add CP lengths and calculate percentage overhead
cp_lengths = [0, 8, 16]

print(f"{'CP Length':<12} | {'Total Samples':<15} | {'Overhead (%)':<15}")
print("-" * 47)

for cp_len in cp_lengths:
    # Extract the last 'cp_len' samples and prepend them
    if cp_len > 0:
        cyclic_prefix = ofdm_base[-cp_len:]
        ofdm_with_cp = np.concatenate((cyclic_prefix, ofdm_base))
    else:
        ofdm_with_cp = ofdm_base
        
    # Calculate percentage overhead
    total_length = N + cp_len
    overhead_pct = (cp_len / total_length) * 100
    
    print(f"{cp_len:<12} | {total_length:<15} | {overhead_pct:.1f}%")