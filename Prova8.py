
"""
Donada una llista, determinar quantes vegades es repeteixen els elements 

"""
a =[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 1, 2, 1, 3, 5] # Llista
b = set(a) # Conjunt/set
c = list() # Llista buida on guardarem elemnt i numero de repeticions
for e ib b:
    c append([e,a.count(e)])
print(c)