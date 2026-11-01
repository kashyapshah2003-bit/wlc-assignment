
import matplotlib.pyplot as plt
import numpy as np

E_val = 10
c_val = 15

def erlang_b(E, c):
    """
    Calculate the Erlang-B blocking probability.
    
    Parameters:
    E (float): Total offered traffic in Erlangs
    c (int): Number of servers/channels
    
    Returns:
    float: Blocking probability (0.0 to 1.0)
    """
    if E == 0:
        return 0.0
        
    inv_b = 1.0
    for i in range(1, c + 1):
        inv_b = 1.0 + (i / E) * inv_b
        
    return 1.0 / inv_b

#Part 1: Single Calculation Example
blocking_prob = erlang_b(E_val, c_val)
print(f"Example - Traffic: {E_val} Erlangs, Channels: {c_val}")
print(f"Blocking Probability: {blocking_prob:.4f}\n")

#Part 2: Plotting for 10, 20, and 30 channels
print("Generating plot for 10, 20, and 30 channels...")

traffic_values = [i * 40 / 99 for i in range(100)]
channel_capacities = [10, 20, 30]

plt.figure(figsize=(10, 6))

for channels in channel_capacities:
    
    # Calculate probabilities for the current channel capacity across all traffic values
    blocking_probs = [erlang_b(t, channels) for t in traffic_values]
    plt.plot(traffic_values, blocking_probs, label=f'{channels} Channels', linewidth=2)

# Format and display the plot
plt.title('Erlang-B Blocking Probability vs. Offered Traffic', fontsize=14, pad=15)
plt.xlabel('Offered Traffic (Erlangs)', fontsize=12)
plt.ylabel('Blocking Probability (Grade of Service)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(fontsize=12)

# Lock axes limits for standard probability visualization
plt.xlim(0, 40)
plt.ylim(0, 1.0)

plt.show()