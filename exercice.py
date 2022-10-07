    #!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    if number < 0:
        number *= -1
    return number

def use_prefixes() -> List[str]:
    prefixes, suffixe, a = 'JKLMNOPQ', 'ack', " "
    for i in prefixes:
        a += f"{i}{suffixe} "
    return a

def prime_integer_summation() -> int:
    x=2
    i=0
    S=0
    while i<100:
        for a in range(2,x+1):
            if x == a:
                i+=1
                S+=x
            elif x%a == 0:
                break
        x += 1
    return S

def factorial(number: int) -> int:
    i=1
    F=1
    while i<number:
        i+=1
        F*=i
    return F

def use_continue() -> None:
    a=""
    for i in range(1,11):
        if i == 5:
            continue
        a+= f"{i} "
    return print(a)

def verify_ages(groups: List[List[int]]) -> List[bool]:
    return []


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
