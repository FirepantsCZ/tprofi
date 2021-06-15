import os
import sys

f = open(os.devnull, "w")
s = sys.stdout
sys.stdout = f
import czfakeid as c
sys.stdout = s

dictableSmall = list(u"ěščřžýáíéúůóťďňü")
nedictableSmall = list("escrzyaieuuotdnu")

dictableBig = list(u"ĚŠČŘŽÝÁÍÉÚŮŤĎŇÜ")
nedictableBig = list("ESCRZYAIEUUTDNU")

def get_email():
    vyslednyZnaky = ""
    pohlavi = c.get_pohlavi()
    email = c.get_email(c.get_jmeno(pohlavi), c.get_prijmeni(pohlavi), c.get_rok_narozeni())

    for znak in email:
        if znak in dictableSmall:
            vyslednyZnaky += nedictableSmall[dictableSmall.index(znak)]
        elif znak in dictableBig:
            vyslednyZnaky += nedictableBig[dictableBig.index(znak)]
        else:
            vyslednyZnaky += znak

    return vyslednyZnaky

for _ in range(100):
    print(get_email())