
nested_tuple = (("apple", "banana"), ("cat", "dog")) # two level tuple

for inner in nested_tuple:
    for item in inner:
       print(",".join(item))



print(",".join(item for inner in nested_tuple for item in inner))


nested_tuple1 = (("apple", ("banana", "cherry")), ("cat", ("dog", "elephant")))


def iterate_tuple(t, result=None):
    if result is None:
        result = []
    for item in t:
        if isinstance(item, tuple):
            iterate_tuple(item, result)  # recursive call
        else:
            result.append(str(item))
    return result

# Get all items in a flat list
items = iterate_tuple(nested_tuple1)

# Print them in one line
print(" ".join(items))
