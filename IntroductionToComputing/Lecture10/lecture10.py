


# Demonstrates escaping quotes 

print("Escaping gives us control over quotes:") 

print("This is a double quote: \" ")

print('This is a single quote: \' ') 


# String methods give us many more options !

message = " I like Python." 

print(message.upper())
print(message.lower()) 

message.replace("Python", "pizza") 
print(message) 

message = message.replace("Python" , "pizza")
print(message) 


seuss = "one fish , Two fish,\nRed fish, Blue fish" 


# we can limit how many times the replace happens. 

print(seuss.replace("fish","car",2)) 

message = "i like python."
string = "\t\n Test! \n\t"

print(message.title() , "\n") 

print(string.strip()) 


message = "I like Python" 

#split on spaces 
print(message.split(" "))
      
#split on commas 
names = "Alan ,Beth,Cody,Danielle, Ethan, Fiona"

print(names.split(","))


seuss = "One fish , Two fish, \nRed fish, Blue fish" 

# Count finds the number of occurences of a string 

print("There are", seuss.count("fish") , "fish.") 

print(seuss.find("Red"))
print(seuss.find("Purple")) 


message = "I like Python." 

print(message[7:13])
print(message[-7:-1])