


def decryptRailFence ( cipher , key ) :

    rail = [['\n' for i in range ( len ( cipher ) )]
            for j in range ( key )]


    dir_down = None
    row , col = 0 , 0

    for i in range ( len ( cipher ) ) :
        if row == 0 :
            dir_down = True
        if row == key - 1 :
            dir_down = False

        rail[row][col] = '*'
        col += 1


        if dir_down :
            row += 1
        else :
            row -= 1


    index = 0
    for i in range ( key ) :
        for j in range ( len ( cipher ) ) :
            if ((rail[i][j] == '*') and
                    (index < len ( cipher ))) :
                rail[i][j] = cipher[index]
                index += 1


    result = []
    row , col = 0 , 0
    for i in range ( len ( cipher ) ) :

        # check the direction of flow
        if row == 0 :
            dir_down = True
        if row == key - 1 :
            dir_down = False

        if (rail[row][col] != '*') :
            result.append ( rail[row][col] )
            col += 1

        if dir_down :
            row += 1
        else :
            row -= 1
    return ("".join ( result ))



#x=encryptRailFence("howareyou",7)
#print(x)
password=""
text="IALTR TAPOG ALYWS BWMER LEITB IIEFC LESVU HHSLT EEHHA GLEII UFIIR LLTNL RLELR SEOMT GIURT TEHOL NYLSR SKFEE AGBAL MIMAR REIOW REOAR RNIOL LTATD EHDHS OTIYW IPMHA NNINN SPEAE WTNRN EHNAT ETTLI WFITO ETNEE TTNES TETEH OENOF EIRSA HOAOI ERITA DDHPS HIETH FHRIG MITMI TTNAT NWAEI EENA"
for i in text:
    if i==" ":
        continue
    else:
        password=password+i

for i in range(3,100,1):
    print(decryptRailFence(password,i))
    h=input("please press any letter to continue")

