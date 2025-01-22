continue_convert = True
print("==================================")
print("Welcome to temperature converter")
print("==================================")

while continue_convert:
    def get_temp_unit():
        print("Convert To What Unit? (Type C for celsius and F for fahrenheit)")
        unit = input("~ To Unit: ").lower()
        if unit == "f":
            print("Great! We will convert Celsius to get Fahrenheit")
        elif unit == "c":
            print("Great! We will convert Fahrenheit to get Celsius")
        else:
            print("Wrong Input (Type C for celsius and F for fahrenheit)")
            get_temp_unit()
        return unit

    convert_to = get_temp_unit()

    def get_temp():
        try:
            temp = float(input("~ Temperature value: "))
            return temp
        except:
            print("Write a valid number")
            get_temp()

    temp_value = get_temp()

    def convert(to, temp_value):
        converted_temp = 0
        if to == "c":
            converted_temp = (temp_value - 32.0) * 5.0/9.0
        elif to == "f":
            converted_temp = (temp_value * 9.0/5.0) + 32.0
        else:
            print("Something Went Wrong!")
        
        return converted_temp

    converted_value = convert(convert_to, temp_value)

    print("=====================")
    print("Conversion Completed")
    print("=====================")

    print(f"The Temperature {temp_value}° in {'Fahrenheit' if convert_to == 'c' else 'Celsius'} is equal to {converted_value}° in {'Celsius' if convert_to == 'c' else 'Fahrenheit'}\n\n")


    continue_convert = input("Again? (yes/no)").lower()

    if continue_convert == "yse" or continue_convert == "y":
        continue_convert = True
    else:
        continue_convert = False