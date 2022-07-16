dividendo = int(input("Dividendo: "));
divisor = int(input("Divisor: "));

cociente = 0;

while True:
    if (dividendo < divisor): break;
    
    dividendo -= divisor;
    cociente += 1;

print("Cociente:", cociente);
print("Resto: ", dividendo);

