import pickle as pick

data = {
    "int": 42,
    "float": 3.14,
    "bool": True,
    "str": "Hello Pickle",
    "bytes": b"byte data",
    "list": [1, 2, 3],
    "tuple": (4, 5, 6),
    "dict": {"a": 1, "b": 2},
    "set": {7, 8, 9},
    "frozenset": frozenset([10, 11, 12]),
    "complex": 2 + 3j,
    "range": range(5),
    "bytearray": bytearray(b"abc")
}


with open("data.pkl","wb") as file:
  pick.dump(data,file)

with open("data.pkl","rb") as file2:

 datal=   pick.load(file2)

 print("loaded data ::::::::::::",datal)
