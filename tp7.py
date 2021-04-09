from random import *
"""
    modelisation a partir d'une liste

"""
#question n°1:

def init_ram_list(taille):
    return [0]*taille

#RAM=init_ram_list(16)
#print(RAM)
'''
    init_ram_list(16)
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

'''

#question n°2:

def fill_ram_random(ram,N):
    for n in range(N):
        index=randint(0,len(ram)-1)
        valeur=randint(1,255)
        ram[index]=valeur
    return ram

#RAM = fill_ram_random(RAM, 5)
#print(RAM)
'''
     fill_ram_random(init_ram_list(16), 5)
[0, 0, 0, 0, 74, 0, 0, 162, 166, 0, 0, 0, 0, 0, 192, 139]

'''

#question n°3:

def fill_ram_place(ram,N):
    for i in range(N):
        i=N
        ram[i]=randint(1,255)
    return ram

#RAM = fill_ram_place(RAM, 5)
#print(RAM)
'''
     fill_ram_place(init_ram_list(16), 5)
[0, 0, 0, 0, 0, 167, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

'''

#question n°4:
def fill_ram_random(ram,N):
    for n in range(N):
        index=randint(0,len(ram)-1)
        valeur=randint(1,255)
        ram[index]=valeur
    return ram
def get_value_liste(ram,adresse):
    return ram[adresse]

#print(get_value_list(RAM,3)
#print(get_value_list(RAM,4)
'''
    get_value_liste(fill_ram_random(init_ram_list(16),32),3)
180
'''

is_in(M, 0)
"""
    modelisation a partir d'un dictionnaire

"""

#question n°1:

def init_ram_dict(taille):
    return {"taille":taille}

#RAM = init_ram_dict(2)
#print(RAM)
'''
     init_ram_dict(2)
{'taille': 2}
'''

#question n°2:

def fill_ram_random_dict(ram, N):
    for n in range(N):
        index=randint(1,ram["taille"]-1)
        valeur=randint(1,255)
        ram[index]=valeur
    return ram

#RAM = fill_ram_random_dict(RAM, 5)
#print(RAM)
'''
    fill_ram_random_dict(init_ram_dict(16), 5)
{'taille': 16, 6: 195, 10: 185, 13: 59, 14: 65, 15: 237}

'''

#question n°3:

def fill_ram_place_dict(ram, N):
    for i in range(N):
        index=randint(1,ram["taille"]-1)
        ram[index]=index
    return ram

#RAM = fill_ram_place_dict(RAM, 5)
#print(RAM)
'''
fill_ram_place_dict(init_ram_dict(16), 5)
{'taille': 16, 6: 6, 11: 11, 12: 12, 13: 13, 14: 14}

'''

#question n°4:

def get_value_dict(ram,adresse):
    return ram.get(adresse,0)

#get_value_dict(RAM, 3)
#print(RAM)
'''
     get_value_dict(fill_ram_random_dict(init_ram_dict(16),32),3)
69
'''

"""
    cache full associative == La mémoire associative

"""

#question n°1:

def is_in(mem_asso, mot):
    taille = len(mem_asso)
    etat = "MISS"
    comparaisons = []
    index = None
    for i, m in enumerate(mem_asso):
        if not m == mot: comparaisons += [False]
        else:
            comparaisons += [True]
            index = i
            etat = "HIT"
    return (etat, comparaisons, index)

#M = [4, 1, 2, 0] 
#is_in(M, 3)/is_in(M, 1)/is_in(M, 0)
'''
is_in([4,1,2,0],3)
('MISS', [False, False, False, False], None)
is_in([4,1,2,0],1)
('HIT', [False, True, False, False], 1)
is_in([4,1,2,0],0)
('HIT', [False, False, False, True], 3) 
'''

"""
    cache full associative == La mémoire classique

"""
#question n°1:
def get_value(mem, idx):
    if idx > len(mem): return None

    value = mem[idx]
    if not value["ok"]:
        value["data"] = None
    return value
#M = [{'ok': True, 'data': 0x44}, {'ok': False, 'data': 0XFF},
#     {'ok': True, 'data': 0x22}, {'ok': True, 'data': 0x99}]

# print(3, get_value(M, 3))
# print(1, get_value(M, 1))
