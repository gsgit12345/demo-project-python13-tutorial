s = "  python programming  "

print(s.lower())           # '  python programming  '
print(s.upper())           # '  PYTHON PROGRAMMING  '
print(s.strip())           # 'python programming'
print(s.replace("python", "java"))  # '  java programming  '
print(s.split())           # ['python', 'programming']
print(s.count('p'))        # 2
print(s.startswith('py'))  # False (leading space)
print(s.endswith('ing'))   # True
