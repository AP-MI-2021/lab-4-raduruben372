import copy


def print_menu():
    '''
    Afiseaza meniul
    :return: meniul
    '''
    print('''
1.  Citire lista numere intregi.
2.  Afișarea tuturor numerelor negative nenule din listă
3.  Afișarea celui mai mic număr care are ultima cifră egală cu o cifră citită de la tastatură.
4.  Afișarea tuturor numerelor din listă care sunt superprime. Un număr este superprim dacă este
    strict pozitiv și toate prefixele sale sunt prime. De exemplu, 173 nu este superprim deoarece 1 nu
    este prim, iar 239 este superprim deoarece 2, 23 și 239 sunt toate prime.
5.  Afișarea listei obținute din lista inițială în care numerele pozitive și nenule au fost înlocuite cu
    CMMDC-ul lor și numerele negative au cifrele în ordine inversă.
x.  Iesire
    ''')


#P1
def citire_lista():
    lst = []
    stringCitit = input("Dati lista(separata prin ,): ")
    numere = stringCitit.split(",")
    for x in numere:
        lst.append(int(x))
    return lst


#P2
def numere_negative_din_lista(lst):
    '''
    Afiseaza toate numerele negative nenule din lista
    :param lst: lista cu numere intregi
    :return:numerele negative nenule
    '''
    lista_numer_neg = []
    for numar in lst:
        if numar < 0 and numar not in lista_numer_neg:
            lista_numer_neg.append(numar)
    return lista_numer_neg


def  test_numere_negative_din_lista():
    assert numere_negative_din_lista([2, 3, 4 ,10 , -1 , -2 , 0]) == [-1, -2]
    assert numere_negative_din_lista([2, -3, -5, -3, 6]) == [-3, -5]


#P3
def min_cu_ult_cifra(lst, cifra):
    '''
    Afiseaza cel mai mic numar care are ultima cifra egala cu o cifra citita de la tastatura
    :return: Cel mai mic numar cu ultima cifra egala cu cea citita la tastatura
    '''
    min_cu_cif = None
    for numar in lst:
        if numar % 10 == cifra and min_cu_cif == None:
            min_cu_cif = numar
        elif numar % 10 == cifra and numar < min_cu_cif:
            min_cu_cif = numar
    return min_cu_cif


def test_min_cu_ult_cifra():
    assert min_cu_ult_cifra([1, 6, 34, 68, 40, 48, 20], 8) == 48
    assert min_cu_ult_cifra([2,3005,40,55,51,101,21], 1) == 21


#P4
def este_prim(n):
    '''
    Verifica daca n este prim
    :param n: numar intreg
    :return: True, daca n este prim, False in caz contrar
    '''
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def test_este_prim():
    assert este_prim(5) is True
    assert este_prim(10) is False
    assert este_prim(2) is True
    assert este_prim(1) is False


def numere_superprime_lista(lst):
    '''
    Determina toate numerele super prime din lista
    :param lst: lista cu numere intregi
    :return: Toate numerele super prime din lista
    '''
    lst_super_prim = []
    for numar in lst:
        cop_numar = numar
        superprim = True
        while cop_numar > 0:
            if este_prim(cop_numar) is False:
                superprim = False
            cop_numar //= 10
        if superprim is True and numar not in lst_super_prim:
            lst_super_prim.append(numar)
    return lst_super_prim


def test_numere_superprime_lista():
    assert numere_superprime_lista([100, 239, 11]) == [239]
    assert numere_superprime_lista([231, 239, 239, 400]) == [239]
    assert numere_superprime_lista([200, 400, 5022]) == []


#P5
def lista_cmmdc_neg_inv(lst):
    '''
    Inlocuieste numerele pozitive cu cmmdc-ul lor, cele negative fiind puse invers
    :param lst: lista numere intregi
    :return: lista in care numere pozitive sunt inlocuite cu cmmdc-ul lor, iar cele negative sunt puse invers
    '''
    lista_poz = []
    lista_finala = []
    for numar in lst:
        if numar > 0:
            lista_poz.append(numar)
    cmmdc = lista_poz[0]
    for numar in range(1,len(lista_poz)):
        cop = copy.copy(lista_poz[numar])
        while cop != cmmdc:
            if cop > cmmdc:
                cop = cop - cmmdc
            elif cop < cmmdc:
                cmmdc = cmmdc - cop
    for numar in lst:
        if numar > 0:
            lista_finala.append(cmmdc)
        else:
            numar_str = str(numar)
            numar_str = numar_str.split("-")[1]
            numar_str = numar_str[::-1]
            lista_finala.append(-int(numar_str))
    return lista_finala


def test_lista_cmmdc_neg_inv():
    assert lista_cmmdc_neg_inv([-76, 12, 24, -13, 144]) == [-67, 12, 12, -31, 12]
    assert lista_cmmdc_neg_inv([-23, 12, 24, -15, 144]) == [-32, 12, 12, -51, 12]


def toate_testele():
    '''
    contine toate testele
    '''
    test_numere_negative_din_lista()
    test_min_cu_ult_cifra()
    test_este_prim()
    test_numere_superprime_lista()
    test_lista_cmmdc_neg_inv()


def main():
    toate_testele()
    lst = []
    while True:
        print_menu()
        numar = input("Introducere numar : ")
        if numar == '1':
            lst = citire_lista()
        elif numar == '2':
            print('Numerele negative nenule din lista sunt:', numere_negative_din_lista(lst))
        elif numar == '3':
            cifra_citita = int(input('Dati cifra : '))
            print('Cel mai mic numar este: ', min_cu_ult_cifra(lst,cifra_citita))
        elif numar == '4':
            print('Numerele super prime sunt: ', numere_superprime_lista(lst))
        elif numar == '5':
            print('Lista este: ', lista_cmmdc_neg_inv(lst))
        elif numar =='x':
            break
        else:
            print('Introdu alt numar!!!')


if __name__ == '__main__':
    main()
