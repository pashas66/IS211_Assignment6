#IS211_Assignment6

#There is a total of 6 functions, each one having a test case which confirms it is properly converting.

def convertCelsiusToKelvin(num):
    #A conversion function used to convert celsius to kelvin using this formula:  °C + 273.15 = K
    kel = num + 273.15
    
    return kel

def convertCelsiusToFahrenheit(num):
    #A conversion function used to convert celsius to fahrenheit using this formula: (°C × 9/5) + 32 = °F
    far = (num*(9/5)) + 32
    
    return far
    
def convertFahrenheitToCelsius(num):
    #A conversion function used to convert fahrenheit to celsius using this formula: (°F − 32) × 5/9 = °C
    cel = (num-32) * (5/9)
    
    return cel

def convertFahrenheitToKelvin(num):
    #A conversion function that converts fahrenheit to kelvin using this formula: (°F − 459.67) × 5/9 = K
    kel = (num+459.67) * (5/9)
    
    return kel

def convertKelvinToFahrenheit(num):
    #A conversion function that converts kelvin to fahrenheit using this formula: (K × (9/5)) - 459.67 = °F
    far = (num*(9/5))-459.67
    
    return far

def convertKelvinToCelsius(num):
    #A conversion function that converts kelvin to celsius using this formula: K − 273.15 = °C
    cel = num - 273.15
    
    return cel