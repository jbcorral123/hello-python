Input= input ("Enter a comma separated list of numbers: ")
print (type(Input))
user_input = Input.split(",")
print (type(user_input))


index=0
sum=0  
for x in user_input:
    sum += float (user_input[index])**2
    index+=1
    print ("Sum of squares:" , sum )