import io

binaryfile=open("binary.txt","wb+")

binaryfile.write(b"hello my name is ghanshyam\ni am going into market")

binaryfile.seek(0)

textfile=io.TextIOWrapper(binaryfile,encoding="utf-8")

data=textfile.read()

print(data)


print(type(binaryfile))

print(type(textfile))

textfile.close()
binaryfile.close()