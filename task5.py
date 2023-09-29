# (1) + (2)
name = input("Name:")
age = int(input("Age:"))
street = input("street:")
city = input("city:")
country = input("country:")
address = street + ", " + city + ", " + country
print(" \"Name:" + " " + name + "\" ")
print(" \"Age:" + " " + str(age) + " \" ")
print(" \"Address:" + " " + address + " \" ")

# (3)
txt1 = f"\"Hellow {name} your age is {age - 5} years old, Your address is {address} \""
print(txt1.title())

# (4)
print(type(name))
print(type(age))
print(type(street))
print(type(city))
print(type(country))
txt2 = (f"\"hellow {name}," + " how are you? \ \"\"\" " + f" your age is \"{age - 5}\"\" " + " + " + " and " + f"your country is: {country}")
print(txt2.title())
txt3 =(f"\"hellow \'{name}\', how are you? \ \n \"\"\"your age is \"{age -5}\"\"" + "+" + f" and \nyour city is:{city} ")
print(txt3.title())

# (7) and (8)
Name ='ITF Gsg Python'
print(Name[0])
print(Name[2])
print(Name[-1])
print(Name[11:14:1])
print(len(Name))
print(Name[:3:1])
print(Name[:8:2])
print(Name[:7:-1])

# (9)
Name2 = "$&$&Mohammed$&$&"
print(Name2.strip('$'+'&'))

# (10)
msg = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg.replace("%7", "love"))

# (11) and (12)
num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num5.zfill(5))
print(num6.zfill(5))

my_str = " i love python "
# (13)
# : title(): Make the first letter in each word uppercase
print(my_str.title())

# upper() : make every letter in each word capitale
print(my_str.upper())

# swapcase(): Swaps cases, lower case becomes upper case and vice versa
print(my_str.swapcase())

# (14)
first_name = "sarah"
print(f"***********{first_name} \n***********{first_name}***********\n{first_name}***********")

# (15)
name_one = "SaMER"
name_two = "Abed"
print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())

# (16)
print(name_one[0:5].isupper())
print(name_two[0:4].islower())

# (17)
print(name_one.startswith("S"))
print(name_one.endswith("HD"))

# (18)
msg2 = "I Love Python And Although I Love GSG with Zakaria"
value1 = msg2.count("Love")
value2 = msg2.count("t")
print(f"Number of <Love> is: {value1}")
print(f"Number of <t> is:{value2}")

# (19)
msg3 = "I %7 Python And Although I %7 GSG with Zakaria"
print(msg3.replace("%7", "Love", 1))

print("The End 0f Task5")















