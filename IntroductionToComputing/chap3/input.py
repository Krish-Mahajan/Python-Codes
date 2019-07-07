

def f():
    
    fahr = eval(input('Enter the temperature in degrees Fahrenheit: '))
    print(type(fahr))
    cels = (fahr - 32)*(5/9)
    print('The temperature in degrees celcius is', cels) 
    return cels  


s = 'it will be a sunny day today'

print(s.count('day'))
print(s.find('sunny'))
print(s.replace('sunny', 'cloudy'))
