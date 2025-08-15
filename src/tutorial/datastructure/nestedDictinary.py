students={

    "student":{
        "name":"raheem",
        "age":1200,
        "marks":{"math":90,"physics":100}
    },
    "student2":{
        "name": "roshan",
        "age": 1100,
        "marks": {"math": 900, "physics": 100}
    }
}


print(students)

print(students["student"]["age"])

#adding value in nested dictinary

students["student3"]={
    "name": "rakesh",
    "age": 1400,
    "pin": {"city": "delhi", "pin": "110027"}
}


print(students["student3"]["age"])