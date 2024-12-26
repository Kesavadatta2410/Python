def union(a, b):
    result = {}
    for key in a: 
        if key in b:
            result[key] = max(a[key], b[key])
        else:   
            result[key] = a[key]
    for key in b:
        if key not in a:
            result[key] = b[key]
    return result
def intersection(a, b):
    result = {}
    for key in a:
        if key in b:
            result[key] = min(a[key], b[key])
        else:
            result[key] = a[key]
    for key in b:
        if key not in a:
            result[key] = b[key]
    return result
a = {'1': 0.2, '3': 0.5, '5': 0.3}
b = {'1': 0.3, '3': 0.2, '5': 0.8}
union = union(a, b)
print("Union of sets a and b:", union) 
intersection = intersection(a, b)
print("intersection of sets a and b:", intersection)