

list=[3,4,5,6,7,8,9]

print(list[0::2])

nums = [0, 1, 2, 3, 4, 5, 6]

print(nums[::2])   # [0, 2, 4, 6]  → every 2nd element
print(nums[1::2])  # [1, 3, 5]     → start at index 1, every 2nd element
print(nums[::-1])  # [6, 5, 4, 3, 2, 1, 0] → reverse list

#  some operation using the extended slicing notation

num=[1,2,3,4,5,6,7,8,9]

# reversing list

print(num[::-1][::-1]) # it will give the original list


#negative step

print(num[5:2:-1])  # start ,skip and end


#check palindrom

p="word";

p="madam";

print("is palinddrom:",p[::-1]==p)