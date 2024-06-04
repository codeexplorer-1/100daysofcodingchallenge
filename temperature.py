def covert_temperature(temperature, input_scale, output_scale):
    
    valid_scales = ("C", "F", "K")
    if input_scale.upper() not in valid_scales or output_scale.upper() not in valid_scales:
        raise ValueError(f"Invalid temperature scale(s). Valid scales are: {', '.join(valid_scales)}")

    # Conversion formulas
    if input_scale.upper() == "C":
        if output_scale.upper() == "F":
            converted_temp = (temperature * 9/5) + 32
        elif output_scale.upper() == "K":
            converted_temp = temperature + 273.15
        else:
            converted_temp = temperature  
    elif input_scale.upper() == "F":
        if output_scale.upper() == "C":
            converted_temp = (temperature - 32) * 5/9
        elif output_scale.upper() == "K":
            converted_temp = (temperature - 32) * 5/9 + 273.15
        else:
            converted_temp = temperature  
    elif input_scale.upper() == "K":
        if output_scale.upper() == "C":
            converted_temp = temperature - 273.15
        elif output_scale.upper() == "F":
            converted_temp = (temperature - 273.15) * 9/5 + 32
        else:
            converted_temp = temperature  

    return converted_temp

# Example usage
while True:
    try:
        temperature = float(input("Enter temperature value: "))
        input_scale = input("Enter input scale (C, F, or K): ").upper()
        output_scale = input("Enter desired output scale (C, F, or K): ").upper()

        converted_temp = covert_temperature(temperature, input_scale, output_scale)
        print(f"{temperature}{input_scale} is equal to {converted_temp:.2f}{output_scale}")

        # Ask if the user wants to continue
        choice = input("Convert another temperature (y/n)? ").lower()
        if choice != 'y':
            break

    except ValueError as e:
        print(f"Error: {e}")
