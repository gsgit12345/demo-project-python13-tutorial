import io


write=open("buff.txt","w")

write.write("hello how are ypu \n i am fine")

write.close()

read=open("buff.txt","r")

data=    read.read();

print(data)

print(type(write))
print(type(read))
read.close()