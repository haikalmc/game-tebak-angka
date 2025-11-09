import random 

angka_rahasia = random.randint(1, 100)
ronde = 0
max_ronde = 10 
print("====== TEBAK ANGKA ======")
print("tebak angka nya y dari 1 - 100")
print("kamu punya " + str(max_ronde) + " kesempatan")

while(ronde < max_ronde):
    tebakan = int(input("tebakan mu: "))
    ronde += 1

    if (tebakan < angka_rahasia):
        print("kekecilan woi coba lagi")
    elif (tebakan > angka_rahasia):
        print("kebesaran kecilin lagi")
    else:
        print("betul loh ya, curang kah manizz??")
        exit(0)
    print("kesempatan sisa " + str(max_ronde - ronde))
    print("_________________________________________")

print("ya kalahh wkkwwkwkkw")
print("angka nya ini =>" + str(angka_rahasia))