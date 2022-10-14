print("**********")
print("1-> Celcius to Fahrenheit")
print("2-> Fahrenheit to Celcius")
print("**********")

choice = int(input("Your choice:"))

if choice == 1:
    print("Celcius to Fahrenheit")
    celcius = float(input("Degree to convert:"))
    fahrenheit = (celcius * 1.8) + 32
    print(" {} degrees Celsius is equal to {} degrees Fahrenheit.".format(celcius,fahrenheit))

elif choice == 2:
    print("Fahrenheit to Celcius")
    fahrenheit = float(input("Degree to convert"))
    celcius = (fahrenheit - 32) / 1.8
    print(" {} degree Fahrenheit is equal to {} degree Celcius.".format(fahrenheit,celcius))

else:
    print("İnvalid choice")
    