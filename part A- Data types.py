#1.integers
age = 28
current_year = 2026
birth_year = current_year - age
print("type of age: ",type(age))
print("type of current_year: ",type(current_year))
print("type of birth_year: ",type(birth_year))
age_in_2050 = 2050-birth_year
print("age in 2050 =",age_in_2050)

#output: type of age:  <class 'int'>
#type of current_year:  <class 'int'>
#type of birth_year:  <class 'int'>
#age in 2050 = 52



#2.strings
first_name ="sanvi"
last_name = "vemuru"
full_name = first_name + " "+ last_name
print(full_name.upper())
print(full_name.lower())
print(full_name.title())
print(len(full_name))
print(full_name[0],full_name[-1])


#output: SANVI VEMURU
#sanvi vemuru
#Sanvi Vemuru
#12
#s u

#3.booleans
is_raining = True
has_umbrella = False
print(type(is_raining))
print(type(has_umbrella))
print(is_raining and has_umbrella)
print(is_raining or has_umbrella)
print(not is_raining)


#output:<class 'bool'>
#<class 'bool'>
#False
#True
#False
