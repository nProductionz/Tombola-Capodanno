import random

def main():
    f = open('frasi.txt')
    frasi = f.read()
    righeTemp = frasi.split(',')
    righe = []
    for r in righeTemp:
        righe.append(r.strip())
    count = 1
    while(count <= 20):
        strName = "lista"+str(count)+".txt"
        e = open(strName, "w+")
        for i in range(10):    
            temp = random.choice(righe)
            e.write(temp+"\n")
        count+=1

main()

