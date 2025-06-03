def total_chocolates_A(jars, N):
    total = 0
    for chocolates in jars:
        total += (chocolates + 2) // 3
    return total

# Example usage:
input_jars = [10, 20, 30]
N = 3
print(total_chocolates_A(input_jars, N))  # Output should be 21