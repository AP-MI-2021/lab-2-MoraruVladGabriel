def get_temp(temp , fr , to):
    '''
    Transforma o temperatura data dintr-o scara data intr-o alta scara data.
    :param temp: float.
    :param fr: str.
    :param to: str.
    :return: float.
    '''
    if fr =='C' and to =='K' :
        temp = temp + 273
    elif fr =='C' and to =='F' :
        temp = 9/5*temp+32
    elif fr =='K' and to =='C' :
        temp = temp - 273
    elif fr =='K' and to =='F' :
        temp = 9/5*(temp-273)+32
    elif fr =='F' and to =='C' :
        temp = 5/9*(temp-32)
    else :
        temp = 5/9*(temp-32)+273

    return temp


def test_get_temp():
    '''
    Verifica daca functia get_temp() returneaza date corecte.
    '''
    assert get_temp(273.0,'K','C') == 0.0
    assert get_temp(394.0,'F','C') == 201.11111111111111
    assert get_temp(123.0,'C','F') == 253.4


def get_cmmmc(numbers):
    '''
    Determina cmmmc-ul tuturor elementelor dintr-o lista.
    :param numbers: int list
    :return:int.
    '''
    cmmmc = numbers[0]
    for i in range(1,len(numbers)):
        copycmmmc=cmmmc
        copynumber=numbers[i]
        while copycmmmc!=copynumber:
            if copycmmmc>copynumber:
                copycmmmc=copycmmmc-copynumber
            elif copynumber>copycmmmc:
                copynumber=copynumber-copycmmmc
        cmmmc=cmmmc*numbers[i]//copynumber

    return int(cmmmc)


def test_get_cmmc():
    '''
        Verifica daca functia get_cmmmc() returneaza date corecte.
    '''
    assert get_cmmmc([6,5,10]) == 30
    assert get_cmmmc([20,12,59]) == 3540
    assert get_cmmmc([11,5,38,15]) == 6270


def isPrime(x):
    '''
    Veridica daca un numar este prim
    :param x: numarul dat, int
    :return: True, daca numarul este prim, False, daca numarul nu este prim.
    '''
    if x<2:
        return False
    if x==2:
        return True
    for i in range(2,x//2+1):
        if x%i==0:
            return False
    return True


def get_largest_prime_below(n):
    '''
    Determina ultimul numar prim mai mic decat un numar dat.
    :param n: numarul dat, int
    :return:  ultimul numar prim mai mic decat un numar dat, int
    '''
    for i in range(n-1,2,-1):
        if isPrime(i):
            return i
    return 0


def test_get_largest_prime_below():
    assert get_largest_prime_below(6)==5
    assert get_largest_prime_below(5)==3
    assert get_largest_prime_below(31)==29
    assert get_largest_prime_below(108)==107


if __name__ == "__main__":
    test_get_largest_prime_below()
    test_get_cmmc()
    test_get_temp()
    while True:
        print("1.Transforma o temperatura data dintr-o scara data intr-o alta scara data. ")
        print("2.Calculează CMMMC al n numere date.")
        print("3.Determina ultimul numar prim mai mic decat un numar dat: ")
        print("X.Iesire")
        optiune=input("Dati optiunea: ")
        if optiune=="1":
            temp=float(input("Temperatura"))
            fr=input("From(C,K,F): ")
            to=input("To(C,K,F): ")
            print(get_temp(temp,fr,to))
        elif optiune=="2":
            n=int(input("Numarul de elemnte din lista: "))
            numbers=[]
            if n<2:
                print("Date incorecte!")
            else:
                for i in range(n):
                    number=int(input("Dati element: "))
                    numbers.append(number)
                print(get_cmmmc(numbers))
        elif optiune=="3":
            nr=int(input("Dati numarul: "))
            prime=get_largest_prime_below(nr)
            print(f'ultimul numar prim mai mic decat {nr} este {prime}')
        elif optiune=="X":
            break
        else:
            print("Optiune gresita")

