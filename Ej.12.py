def majoredat(edat):
    if edat > 18: 
        print("és major d'edat")
    elif edat<18: 
        print("és menor d'edat")
    else:
        print("felicitats, ets major d'edat")

edat = int(input("escriu la seva edat: "))
majoredat(edat)
edat = int(input("escriu la seva edat: "))
majoredat(edat)