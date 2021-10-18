

print ("Referendum stemmen met (v)oor of (t)egen:")

uw_stem_1 = input("Geef uw stem:  ")

uw_stem_2 = input("Geef uw stem:  ")

uw_stem_3 = input("Geef uw stem:  ")

uw_stem_4 = input("Geef uw stem:  ")

uw_stem_5 = input("Geef uw stem:  ")

if uw_stem_1 == "v":
    stem_v1 = 1
else:
    stem_v1 = 0

if uw_stem_1 == "t":
    stem_t1 = 1
else:
    stem_t1 = 0

if uw_stem_2 == "v":
    stem_v2 = 1
else: stem_v2 = 0

if uw_stem_2 == "t":
    stem_t2 = 1
else: stem_t2 = 0

if uw_stem_3 == "v":
    stem_v3 = 1
else: stem_v3 = 0

if uw_stem_3 == "t":
    stem_t3 = 1
else: stem_t3 = 0

if uw_stem_4 == "v":
    stem_v4 = 1
else: stem_v4 = 0

if uw_stem_4 == "t":
    stem_t4 = 1
else: stem_t4 = 0

if uw_stem_5 == "v":
    stem_v5 = 1
else: stem_v5 = 0

if uw_stem_5 == "t":
    stem_t5 = 1
else: stem_t5 = 0

totaal_v = (stem_v1 + stem_v2 + stem_v3 + stem_v4 + stem_v5)
totaal_t = (stem_t1 + stem_t2 + stem_t3 + stem_t4 + stem_t5)
print (" %.0f voor | %.0f tegen" % (totaal_v, totaal_t))

while totaal_v > totaal_t:
    print("Het referendum is aangenomen")
    exit("")
while totaal_v < totaal_t:
    print("Het referendum is verworpen")
    exit("")
