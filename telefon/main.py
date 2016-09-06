# your code goes here
slowa=[]
slowa_decode=[]
ciag=[]
lista=[]
 
ilosc_slow,ilosc_ciagow=map(int,raw_input().split())
 
for x in range (0, ilosc_slow):
    slowa.append(raw_input())
    slowa_decode.append(0)
    
    
    mnoznik=10**(len(slowa[x])-1)
    for i in range (len(slowa[x])):
        
        if slowa[x][i]=='a' or slowa[x][i]=='b' or slowa[x][i]=='c':
            slowa_decode[x]=slowa_decode[x] +2*mnoznik
        if slowa[x][i]=='d' or slowa[x][i]=='e' or slowa[x][i]=='f':
            slowa_decode[x]=slowa_decode[x] +3* mnoznik
        if slowa[x][i]=='g' or slowa[x][i]=='h' or slowa[x][i]=='i':
            slowa_decode[x]=slowa_decode[x]+ 4*mnoznik
        if slowa[x][i]=='j' or slowa[x][i]=='k' or slowa[x][i]=='l':
            slowa_decode[x]=slowa_decode[x] +5*mnoznik   
        if slowa[x][i]=='m' or slowa[x][i]=='n' or slowa[x][i]=='o':
            slowa_decode[x]=slowa_decode[x] + 6 * mnoznik
        if slowa[x][i]=='p' or slowa[x][i]=='q' or slowa[x][i]=='r' or slowa[x][i]=='s':
            slowa_decode[x]=slowa_decode[x] + 7 * mnoznik
        if slowa[x][i]=='t' or slowa[x][i]=='u' or slowa[x][i]=='v':
            slowa_decode[x]=slowa_decode[x] + 8 * mnoznik
        if slowa[x][i]=='w' or slowa[x][i]=='x' or slowa[x][i]=='y' or slowa[x][i]=='z':
            slowa_decode[x]=slowa_decode[x] + 9 * mnoznik
            
        mnoznik=mnoznik/10
    
   
for x in range (ilosc_ciagow):
    ciag.append(int(raw_input()))
    
for x in range (ilosc_ciagow):
    exit=""
    flaga=0
    for i in range(ilosc_slow):
        if ciag[x]==slowa_decode[i]:
            lista.append(slowa[i])
            flaga=1
            #if exit=="":
            #    exit=slowa[i]
            #else:    
            #    exit=exit+" "+slowa[i]
    
    #if exit=="":
    #    exit="BRAK"
    if flaga:
        lista.sort()
        print "lista: "+lista[0]+lista[1]
        for i in range(len(lista)):
            if i==1:
                exit=lista[i]
            else:
                exit=exit + " " + lista[i]
        
    else:
        exit="BRAK"
    print(exit) 
    del lista[:]
    