def erlang_b(C, A):
    """
    Calculates the Erlang-B blocking probability.
    
    Parameters:
    C (int): Number of available channels
    A (float): Offered traffic in Erlangs
    
    Returns:
    float: Blocking probability (Grade of Service)
    """
    if A == 0:
        return 0.0
        
    E = 1.0  # Base case: 100% blocking when there are 0 channels
    
    for k in range(1, C + 1):
        # Recursive calculation for each channel up to C
        E = (A * E) / (k + A * E)
        
    return E

# --- Example Usage ---
channels = 10
traffic = 5.084

gos = erlang_b(channels, traffic)
print(f"Channels: {channels}")
print(f"Offered Traffic: {traffic} Erlangs")
print(f"Blocking Probability (GoS): {gos:.4f} ({gos * 100:.2f}%)")