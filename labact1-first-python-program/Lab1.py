print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("Pounds to Kilograms Converter")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

weight_pounds = float(input("Enter weight in pounds: "))
print("Weight in Pounds: ", weight_pounds, "lbs")
weight_converter = 2.205

weight_kilograms = (weight_pounds) / (weight_converter)
print("Weight in Kilograms: ", round(weight_kilograms,2), "kg")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
print("Miles to Kilometers Converter")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
length_miles = float(input("Enter length in miles: "))
print("Length in Miles: ", length_miles, "mi")
length_converter = 1.609

length_kilometers = (length_miles) * (length_converter)
print("Length in Kilometers: ", round(length_kilometers,2), "km")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

print("Fahrenheit to Celsius Converter")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
temp_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
print("Temperature in Fahrenheit: ", temp_fahrenheit, "°F")
temp_celsius = (temp_fahrenheit - 32)* 5 / 9
print("Temperature in Celsius: ", round(temp_celsius, 2), "°C")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

print("Calculate the Average Age of 10 Students")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
S1 = int(input("Age of Student 1: "))
S2 = int(input("Age of Student 2: "))
S3 = int(input("Age of Student 3: "))
S4 = int(input("Age of Student 4: "))
S5 = int(input("Age of Student 5: "))
S6 = int(input("Age of Student 6: "))
S7 = int(input("Age of Student 7: "))
S8 = int(input("Age of Student 8: "))
S9 = int(input("Age of Student 9: "))
S10 = int(input("Age of Student 10: "))
sum = S1 + S2 + S3 + S4 + S5 + S6 + S7 + S8 + S9 + S10
average = sum/10
print("The average age of the students is: ", average)
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")

print("Urban Fantasy Story about Devils")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
#characters
characterOne = '<The Control Devil>'
characterTwo = '<Gun Devil>'
characterThree = '<Blood Devil>'
characterFour = '<Hell Devil>'
characterFive ='<The Chainsaw Devil>'
#abilities
gunAbility = ' <Worldwide Shot Ability>'
contractName = '<Tactless Contract>'
transformation = ' <ChainsawMan Transformation>'
makimaAbility = '<One Shot, One Kill>'
hellAbility = '<Cast Into Hell>'
pleading = '"Save me, Chainsaw Devil."'
chainsawAbility = "<Five-Chainsaw Attack> "
mostPowerfulAbility = "<Eat Existence Ability>"

print('As Makima, ' + characterOne + ' prepares for ability activation, she was shot on the head by the ' + characterTwo + "'s" + gunAbility + ".")
print("It was Makima's 29th recorded death. Makima's " + contractName + " with the Prime Minister helped her to survive this fatal shot.")
print("In exchange for Makima's death, it would be passed to a random citizen.")
print("Controlled by Makima, Denji's" + transformation + " had appeared, executing the Gun Devil.")
print("Due to Makima's anger, she unleashed her " + makimaAbility + " ability causing " + characterThree + ", who just appeared from the door get killed.")
print("The Anti-Makima Squad tried to beat Makima by the ability, " + hellAbility + " getting help through " + characterFour + ".")
print("But before they could win, " + characterOne + " whispered under her breath, " + pleading)
print("Then and there, with the engine's roaring noise, the superhero of Hell appeared, " + characterFive + ".")
print("Call him once, and he will come. Using his " + chainsawAbility + characterFour + " was cut into pieces within a nanosecond.")
print("But unbeknowst to Makima, the devils who called for help are cut up and killed too.")
print("Then so, " + mostPowerfulAbility + " kicked off, erasing " + characterOne + " from existence.")
print("END OF STORY")
print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
