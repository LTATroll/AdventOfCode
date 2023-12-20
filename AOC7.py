f = open("sample.txt", "r")
n = 0
nn = 0
flag = 0

class cFROH:
    scoreOfHand = -1
    endRank = 0
    firstCardRank = -1
    secondCardRank = -1
    thirdCardRank = -1
    fourthCardRank = -1
    fifthCardRank = -1
    cBets = "orca"

cardValue = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 1,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2
}

for x in f:
    n = n + 1

f.close()
f = open("sample.txt", "r")

hands = [""] * n
bets = [""] * n
TOC = [""] * 5
SOH = [0] * n
NTOC = [0] * 5
ROH = [0] * n
IOHC = [0] * n
nnn = n
ANOH = n
AOCT = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
FROH = [] * n
SortedHands = [""] * n

for x in range(n):
    FROH.append(cFROH())

for x in f:
    n = 0
    
    while n < 5:
        hands[nn] = hands[nn] + x[n]
        n = n + 1
    n = n + 1
    if nn == nnn - 1:
        while n < len(x):
            bets[nn] = bets[nn] + x[n]
            n = n + 1
        break
    while n < len(x) - 1:
        bets[nn] = bets[nn] + x[n]
        n = n + 1
    nn = nn + 1
nn = 0
for x in hands:
    AOWC = 0
    n = 0
    nnn = 0
    while n < 5:
        TOC[n] = ""
        NTOC[n] = 0
        n = n + 1
    n = 0
    for xx in hands[nn]:
        flag = 0
        if n == 0:
            TOC[0] = TOC[0] + xx
            NTOC[0] = 1
            nnn = nnn + 1
            n = n + 1
            continue
        nnnn = 0
        while nnnn < nnn:
            if xx == TOC[nnnn]:
                flag = 1
                NTOC[nnnn] = NTOC[nnnn] + 1
            nnnn = nnnn + 1
        if flag == 0: 
            TOC[nnn] = xx
            NTOC[nnn] = NTOC[nnn] + 1
            nnn = nnn + 1
        n = n + 1
    for xx in range(5):
        if TOC[xx] == "J":
            AOWC = NTOC[xx]
            NTOC[xx] = 0
    NTOC.sort(reverse=True)
    NTOC[0] = NTOC[0] + AOWC
    if NTOC[0] == 5:
        SOH[nn] = 6
    if NTOC[0] == 4:
        SOH[nn] = 5
    if NTOC[0] == 3 and NTOC[1] == 2:
        SOH[nn] = 4
    if NTOC[0] == 3 and NTOC[1] != 2:
        SOH[nn] = 3
    if NTOC[0] == 2 and NTOC[1] == 2:
        SOH[nn] = 2
    if NTOC[0] == 2 and NTOC[1] != 2:
        SOH[nn] = 1
    if NTOC[0] == 1:
        SOH[nn] = 0
    nn = nn + 1
rank = 1000

i = 0

for x in reversed(range(7)):                            
    for xx in AOCT:
         for xxx in range(ANOH):
            if SOH[xxx] == x and hands[xxx][0] == xx:
                FROH[i].scoreOfHand = x
                FROH[i].firstCardRank = xx
                FROH[i].endRank = rank
                FROH[i].cBets = bets[xxx]
                SortedHands[i] = hands[xxx]
                rank = rank - 1
                i = i + 1
i = 0
for xxx in range(ANOH):
    FROH[i].secondCardRank = cardValue[SortedHands[xxx][1]]
    i = i + 1
i = 0
for xxx in range(ANOH):
    FROH[i].thirdCardRank = cardValue[SortedHands[xxx][2]]
    i = i + 1
i = 0
for xxx in range(ANOH):
    FROH[i].fourthCardRank = cardValue[SortedHands[xxx][3]]
    i = i + 1
i = 0
for xxx in range(ANOH):
    FROH[i].fifthCardRank = cardValue[SortedHands[xxx][4]]
    i = i + 1

for xxx in range(ANOH):
    for xx in range(999):
        if cardValue[SortedHands[xx][1]] > cardValue[SortedHands[xx + 1][1]] and FROH[xx].scoreOfHand == FROH[xx + 1].scoreOfHand and SortedHands[xx][0] == SortedHands[xx + 1][0]:
            continue
        elif cardValue[SortedHands[xx + 1][1]] > cardValue[SortedHands[xx][1]] and FROH[xx].scoreOfHand == FROH[xx + 1].scoreOfHand and SortedHands[xx][0] == SortedHands[xx + 1][0]:
            FROH[xx], FROH[xx + 1] = FROH[xx + 1], FROH[xx]
            SortedHands[xx], SortedHands[xx + 1] = SortedHands[xx + 1], SortedHands[xx]

for xxx in range(ANOH):
    for xx in range(999):
        if cardValue[SortedHands[xx][2]] > cardValue[SortedHands[xx + 1][2]] and FROH[xx].scoreOfHand == FROH[xx + 1].scoreOfHand and SortedHands[xx][0] == SortedHands[xx + 1][0] and SortedHands[xx][1] == SortedHands[xx + 1][1]:
            continue
        elif cardValue[SortedHands[xx + 1][2]] > cardValue[SortedHands[xx][2]] and FROH[xx].scoreOfHand == FROH[xx + 1].scoreOfHand and SortedHands[xx][0] == SortedHands[xx + 1][0] and SortedHands[xx][1] == SortedHands[xx + 1][1]:
            FROH[xx], FROH[xx + 1] = FROH[xx + 1], FROH[xx]
            SortedHands[xx], SortedHands[xx + 1] = SortedHands[xx + 1], SortedHands[xx]

for xxx in range(ANOH):
    for xx in range(999):
        if cardValue[SortedHands[xx][3]] > cardValue[SortedHands[xx + 1][3]] and FROH[xx].scoreOfHand == FROH[xx + 1].scoreOfHand and SortedHands[xx][0] == SortedHands[xx + 1][0] and SortedHands[xx][1] == SortedHands[xx + 1][1] and SortedHands[xx][2] == SortedHands[xx + 1][2]:
            continue
        elif cardValue[SortedHands[xx + 1][3]] > cardValue[SortedHands[xx][3]] and FROH[xx].scoreOfHand == FROH[xx + 1].scoreOfHand and SortedHands[xx][0] == SortedHands[xx + 1][0] and SortedHands[xx][1] == SortedHands[xx + 1][1] and SortedHands[xx][2] == SortedHands[xx + 1][2]:
            FROH[xx], FROH[xx + 1] = FROH[xx + 1], FROH[xx]
            SortedHands[xx], SortedHands[xx + 1] = SortedHands[xx + 1], SortedHands[xx]

for xxx in range(ANOH):
    for xx in range(999):
        if cardValue[SortedHands[xx][4]] > cardValue[SortedHands[xx + 1][4]] and FROH[xx].scoreOfHand == FROH[xx + 1].scoreOfHand and SortedHands[xx][0] == SortedHands[xx + 1][0] and SortedHands[xx][1] == SortedHands[xx + 1][1] and SortedHands[xx][2] == SortedHands[xx + 1][2] and SortedHands[xx][3] == SortedHands[xx + 1][3]:
            continue
        elif cardValue[SortedHands[xx + 1][4]] > cardValue[SortedHands[xx][4]] and FROH[xx].scoreOfHand == FROH[xx + 1].scoreOfHand and SortedHands[xx][0] == SortedHands[xx + 1][0] and SortedHands[xx][1] == SortedHands[xx + 1][1] and SortedHands[xx][2] == SortedHands[xx + 1][2] and SortedHands[xx][3] == SortedHands[xx + 1][3]:
            FROH[xx], FROH[xx + 1] = FROH[xx + 1], FROH[xx]
            SortedHands[xx], SortedHands[xx + 1] = SortedHands[xx + 1], SortedHands[xx]

total = 0
rank = 1000

for x in range(ANOH):
    total = (int(FROH[x].cBets) * rank) + total
    rank = rank - 1
print(total)
f.close()