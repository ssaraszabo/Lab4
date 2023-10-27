l = [14, 34, 93, 22, 21, 13, 34, 39, 67]
l_string = ["14", "34", "93", "22", "21", "13", "34", "39", "67"]
new_list = []
new_nr = 0
print(l)
#1
def enf_wiederholen(lista):
    for i in range(0, len(l)):
        if l[i] not in new_list:
            new_list.append(l[i])
    print(new_list)

#2
def simetric(lista):
    nr_simetric = 0
    for i in range(0, len(l)):             #mache ich eine neue Liste mit inversen
        new_nr = l[i] // 10 + l[i] % 10 * 10
        # x = l[i]
        # while x > 0:
        #     new_nr = new_nr * 10 + x % 10
        #     x = x / 10                    #am generalizat sa functioneze algoritmul si cu numere cu mai mult de doua cifre
        new_list.append(new_nr)             #adaugam inversa elementului listei noi
    for j in range(0, len(l)):              #wenn ein Zahl in beide List ist, dann ist auch die inverse in l
        if l[j] in new_list:
            nr_simetric += 1
    print(nr_simetric // 2)                  #schauen wir halb der gefundene Zahlen, weil wir die Zahl der Paaren finden wollen

#3
def nr_max_conc(lista):
    new_list = l
    new_list.sort(reverse=True)             #
    nr_conc = 0
    for i in range(0, len(l)):
        nr_conc = nr_conc * 100 + new_list[i]
    print(nr_conc)

#4
def encrypt_plus(lista):
    key = l[0]
    for i in range(0, len(l)):
        l[i] = l[i] + key
    print(l)

def encrypt_multiplication(lista):
    key = l[0]
    for i in range(0, len(l)):
        l[i] = l[i] * key
    print(l)

def nr_binar(numar):
    if numar >= 1:
        nr_binar(numar // 2)            #calculam forma binara a elementelor
    print(numar % 2, end = '')

def encrypt_xor(lista):
    l_binar = 0                            #Element der Liste bevor xor (local)
    key = int(bin(l[0])[2:])               #die binare Forme
    e_nr = 0                               #die neue Zahl (nach xor)
    for i in range(0, len(l)):
        l_binar = int(bin(l[i])[2:])
        e_nr = l_binar ^ key
        new_list.append(e_nr)
    print(new_list)

def filter(string):
    l_int = []                                  # xy formaju szamok
    f_list = []
    for i in range(0, len(l)):
        l_int.append(int(l_string[i]))          #convert string list to int list
    for j in range(0, len(l)):
        if (l_int[j] % 10) % (l_int[j] // 10) == 0:         #y*Zahl=x
            f_list += "y*" + str((l_int[j] % 10) // (l_int[j] // 10)) + "=x"
        elif l_int[j] // 10 % l_int[j] % 10 == 0:           #x*Zahl=y
            f_list += "x*", str((l_int[j] // 10) // (l_int[j] % 10)), "=y"
        elif (l_int[j] // 10) % (l_int[j] % 10) == 0:       #x/y=Zahl
            f_list += "x/y=", str((l_int[j] // 10) // (l_int[j] % 10))
        elif (l_int[j] % 10) % (l_int[j] // 10) == 0:       #y/x=Zahl
            f_list += "y/x=", str((l_int[j] % 10) // (l_int[j] // 10))
        else:
            f_list += "no rule"             #NEM MEGY AHOGY KELL
    print(f_list)

#6:
def domino(lista):
    d_max = 1
    max = 1
    for i in range(1, len(l)):
        if l[i - 1] % 10 == l[i] // 10:
            max += 1
            if max > d_max:
                d_max = max
        else:
            max = 0
    print(d_max)

#7
def lnko(a, b):         #cel mai mare multiplicativ comun
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

print("a")

def lkkt(a, b):         #kleinsten gemeinsamen Vielfachen fur a,b
    o = lnko(a, b)
    return a * b // o

def lkkt_list(lista, ifrom, ito):       #i(ndex)from/to
    for i in range(ifrom, ito):
        pass

#1:
#enf_wiederholen(l)
#2:
#simetric(l)
#3:
#nr_max_conc(l)
#4:
#encrypt_plus(l)
#encrypt_multiplication(l)
print(bin(7)[2:])
#encrypt_xor(l)
#5
#filter(l_string)
#6:
domino(l)
#7:
# f = int(input(f))
# t = int(input(t))
# lkkt_list(l, f, t)