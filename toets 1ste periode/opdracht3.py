n = int(input("Vul een getal in: \n"))

def prime(n):
    state = True
    for i in range(2, n):
        if n % i == 0:
            state = False
    return state
print(prime(n))

priem = prime(n)

if priem == False:
    print("Invoer is geen Priem getal")
else:
    print("Invoer is een Priem getal")
