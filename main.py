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

if __name__ == "__main__":
    while True:
        print("1.Transforma o temperatura data dintr-o scara data intr-o alta scara data. ")
        print("2.Calculează CMMMC al n numere date.")
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
            for i in range(n):
                number=int(input("Dati element: "))
                numbers.append(number)
            print(get_cmmmc(numbers))
        elif optiune=="X":
            break
        else:
            print("Optiune gresita")

