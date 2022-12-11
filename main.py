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
        array = []
        frs = 0
        while frs < 10:  
            temp = random.choice(righe)
            if temp not in array:
                array.append(temp)
                e.write(temp+"\n")
                frs += 1
        count+=1

main()

