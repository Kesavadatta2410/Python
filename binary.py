def binary_function(x):
    if x > 0:
        return 1
    else:
        return 0

def nand_gate(a1, a2):
    weight = -1  
    theta_1 = -1  
    theta_2 = 0 
    s1 = binary_function(weight * a1 + theta_1)
    s2 = binary_function(weight * a2 + theta_1)
    final_sum = s1 + s2  
    output = binary_function(final_sum - theta_2)
    return output
print("NAND Gate Truth Table:")
print(f"NAND(0, 0) = {nand_gate(0, 0)}")
print(f"NAND(0, 1) = {nand_gate(0, 1)}")
print(f"NAND(1, 0) = {nand_gate(1, 0)}")
print(f"NAND(1, 1) = {nand_gate(1, 1)}")