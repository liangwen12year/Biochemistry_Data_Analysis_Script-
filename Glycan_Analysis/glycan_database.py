







if __name__ == '__main__':
    file=open("/home/wliang/Desktop/glycan/cases.txt", "r")

    mass1 =596.138356
    mass2 =298.069178
    mass3 =566.127791
    mass4 =268.058613

    mass5 = 864.196969
    mass6 =1162.266147
    mass7 =536.117226
    mass8 =1132.255582
    mass9 =1192.276712
    mass10 =894.207534
    mass11 =834.186404


    content = file.readline()
    content = file.readline()
    while (content!="2\n"):
        print(content)
        content = content.split(' ')
        #print(content)
        base_mass= content[2].split('\n')
        #print(base_mass[0])
        #print(round(float(base_mass[0])+mass1, 6))
        print(content[0]+ ' ' + str(mass1) + ' ' + content[1]+' ' + str(round(float(base_mass[0]) + mass1, 6 )) )
        print(content[0] + ' ' + str(mass2) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass2, 6)))
        print(content[0] + ' ' + str(mass3) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass3, 6)))
        print(content[0] + ' ' + str(mass4) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass4, 6)))
        print(content[0] + ' ' + str(mass5) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass5, 6)))
        print(content[0] + ' ' + str(mass6) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass6, 6)))
        print(content[0] + ' ' + str(mass7) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass7, 6)))
        print(content[0] + ' ' + str(mass8) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass8, 6)))
        print(content[0] + ' ' + str(mass9) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass9, 6)))
        print(content[0] + ' ' + str(mass10) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass10, 6)))
        print(content[0] + ' ' + str(mass11) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass11, 6)))
        content = file.readline()



    print("***************************************")

    mass1=864.196969
    mass2=1162.266147
    mass3=536.117226
    mass4=1132.255582
    mass5=1192.276712
    mass6=894.207534
    mass7=834.186404
    mass8=536.117226
    mass9=1430.32476
    mass10=804.175839
    mass11=1400.314195
    mass12=1460.335325
    mass13=1102.245017
    mass14=1728.393938
    mass15=1698.383373
    mass16=1758.404503
    mass17=1490.345890
    mass18=1788.415068
    mass19=596.138356
    mass20=298.069178
    mass21=566.127791
    mass22=268.058613

    content = file.readline()
    while (content != "3\n"):
         print(content)
         content = content.split(' ')
         # print(content)
         base_mass = content[2].split('\n')
         # print(base_mass[0])
         # print(round(float(base_mass[0])+mass1, 6))
         print(content[0] + ' ' + str(mass1) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass1, 6)))
         print(content[0] + ' ' + str(mass2) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass2, 6)))
         print(content[0] + ' ' + str(mass3) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass3, 6)))
         print(content[0] + ' ' + str(mass4) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass4, 6)))
         print(content[0] + ' ' + str(mass5) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass5, 6)))
         print(content[0] + ' ' + str(mass6) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass6, 6)))
         print(content[0] + ' ' + str(mass7) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass7, 6)))
         print(content[0] + ' ' + str(mass8) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass8, 6)))
         print(content[0] + ' ' + str(mass9) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass9, 6)))
         print(content[0] + ' ' + str(mass10) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass10, 6)))
         print(content[0] + ' ' + str(mass11) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass11, 6)))
         print(content[0] + ' ' + str(mass12) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass12, 6)))
         print(content[0] + ' ' + str(mass13) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass13, 6)))
         print(content[0] + ' ' + str(mass14) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass14, 6)))
         print(content[0] + ' ' + str(mass15) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass15, 6)))
         print(content[0] + ' ' + str(mass16) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass16, 6)))
         print(content[0] + ' ' + str(mass17) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass17, 6)))
         print(content[0] + ' ' + str(mass18) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass18, 6)))
         print(content[0] + ' ' + str(mass19) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass19, 6)))
         print(content[0] + ' ' + str(mass20) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass20, 6)))
         print(content[0] + ' ' + str(mass21) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass21, 6)))
         print(content[0] + ' ' + str(mass22) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass22, 6)))
         content = file.readline()





    print("***************************************")

    mass1=596.138356
    mass2=298.069178
    mass3=566.127791
    mass4=268.058613
    mass5=237.040224
    mass6=864.196969
    mass7=1162.266147
    mass8=536.117226
    mass9=1132.255582
    mass10=1192.276712
    mass11=894.207534
    mass12=834.186404
    mass13=505.098837
    mass14=803.168015
    mass15=535.109402
    mass16=833.178580
    mass17=1101.237193
    mass18=1399.306371
    mass19=773.157450
    mass20=1369.295806
    mass21=1429.316936
    mass22=1131.247758
    mass23=1071.226628


    content = file.readline()
    while (content != "4\n"):
         print(content)
         content = content.split(' ')
         # print(content)
         base_mass = content[2].split('\n')
         # print(base_mass[0])
         # print(round(float(base_mass[0])+mass1, 6))
         print(content[0] + ' ' + str(mass1) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass1, 6)))
         print(content[0] + ' ' + str(mass2) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass2, 6)))
         print(content[0] + ' ' + str(mass3) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass3, 6)))
         print(content[0] + ' ' + str(mass4) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass4, 6)))
         print(content[0] + ' ' + str(mass5) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass5, 6)))
         print(content[0] + ' ' + str(mass6) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass6, 6)))
         print(content[0] + ' ' + str(mass7) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass7, 6)))
         print(content[0] + ' ' + str(mass8) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass8, 6)))
         print(content[0] + ' ' + str(mass9) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass9, 6)))
         print(content[0] + ' ' + str(mass10) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass10, 6)))
         print(content[0] + ' ' + str(mass11) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass11, 6)))
         print(content[0] + ' ' + str(mass12) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass12, 6)))
         print(content[0] + ' ' + str(mass13) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass13, 6)))
         print(content[0] + ' ' + str(mass14) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass14, 6)))
         print(content[0] + ' ' + str(mass15) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass15, 6)))
         print(content[0] + ' ' + str(mass16) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass16, 6)))
         print(content[0] + ' ' + str(mass17) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass17, 6)))
         print(content[0] + ' ' + str(mass18) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass18, 6)))
         print(content[0] + ' ' + str(mass19) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass19, 6)))
         print(content[0] + ' ' + str(mass20) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass20, 6)))
         print(content[0] + ' ' + str(mass21) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass21, 6)))
         print(content[0] + ' ' + str(mass22) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass22, 6)))
         print(content[0] + ' ' + str(mass23) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass23, 6)))
         content = file.readline()


    print("***************************************")

    mass1 = 596.138356
    mass2 = 298.069178
    mass3 = 566.127791
    mass4 = 268.058613
    mass5 = 237.040224
    mass6 = 864.196969
    mass7 = 1162.266147
    mass8 = 536.117226
    mass9 = 1132.255582
    mass10 = 1192.276712
    mass11 = 894.207534
    mass12 = 834.186404
    mass13 = 536.117226
    mass14 = 1430.32476
    mass15 = 804.175839
    mass16 = 1400.314195
    mass17 = 1460.335325
    mass18 = 1102.245017
    mass19 = 1728.393938
    mass20 = 1698.383373
    mass21 = 1758.404503
    mass22 = 1490.345890
    mass23 = 1788.415068
    mass24 = 803.168015
    mass25 = 1101.237193
    mass26 = 1399.306371
    mass27 = 773.157450
    mass28 = 1369.295806
    mass29 = 833.178580
    mass30 = 1429.316936
    mass31 = 1131.247758
    mass32 = 1071.226628
    mass33 = 1667.364984
    mass34 = 1041.216063
    mass35 = 1637.354419
    mass36 = 1697.375549
    mass37 = 1339.285241
    mass38 = 1965.434162
    mass39 = 1935.423597
    mass40 = 1995.444727
    mass41 = 1727.386114
    mass42 = 1429.316936
    mass43 = 2025.455292

    content = file.readline()
    while (content != "5\n"):
        print(content)
        content = content.split(' ')
        # print(content)
        base_mass = content[2].split('\n')
        # print(base_mass[0])
        # print(round(float(base_mass[0])+mass1, 6))
        print(content[0] + ' ' + str(mass1) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass1, 6)))
        print(content[0] + ' ' + str(mass2) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass2, 6)))
        print(content[0] + ' ' + str(mass3) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass3, 6)))
        print(content[0] + ' ' + str(mass4) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass4, 6)))
        print(content[0] + ' ' + str(mass5) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass5, 6)))
        print(content[0] + ' ' + str(mass6) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass6, 6)))
        print(content[0] + ' ' + str(mass7) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass7, 6)))
        print(content[0] + ' ' + str(mass8) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass8, 6)))
        print(content[0] + ' ' + str(mass9) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass9, 6)))
        print(content[0] + ' ' + str(mass10) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass10, 6)))
        print(content[0] + ' ' + str(mass11) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass11, 6)))
        print(content[0] + ' ' + str(mass12) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass12, 6)))
        print(content[0] + ' ' + str(mass13) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass13, 6)))
        print(content[0] + ' ' + str(mass14) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass14, 6)))
        print(content[0] + ' ' + str(mass15) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass15, 6)))
        print(content[0] + ' ' + str(mass16) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass16, 6)))
        print(content[0] + ' ' + str(mass17) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass17, 6)))
        print(content[0] + ' ' + str(mass18) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass18, 6)))
        print(content[0] + ' ' + str(mass19) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass19, 6)))
        print(content[0] + ' ' + str(mass20) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass20, 6)))
        print(content[0] + ' ' + str(mass21) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass21, 6)))
        print(content[0] + ' ' + str(mass22) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass22, 6)))
        print(content[0] + ' ' + str(mass23) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass23, 6)))
        print(content[0] + ' ' + str(mass24) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass24, 6)))
        print(content[0] + ' ' + str(mass25) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass25, 6)))
        print(content[0] + ' ' + str(mass26) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass26, 6)))
        print(content[0] + ' ' + str(mass27) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass27, 6)))
        print(content[0] + ' ' + str(mass28) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass28, 6)))
        print(content[0] + ' ' + str(mass29) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass29, 6)))
        print(content[0] + ' ' + str(mass30) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass30, 6)))
        print(content[0] + ' ' + str(mass31) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass31, 6)))
        print(content[0] + ' ' + str(mass32) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass32, 6)))
        print(content[0] + ' ' + str(mass33) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass33, 6)))
        print(content[0] + ' ' + str(mass34) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass34, 6)))
        print(content[0] + ' ' + str(mass35) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass35, 6)))
        print(content[0] + ' ' + str(mass36) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass36, 6)))
        print(content[0] + ' ' + str(mass37) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass37, 6)))
        print(content[0] + ' ' + str(mass38) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass38, 6)))
        print(content[0] + ' ' + str(mass39) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass39, 6)))
        print(content[0] + ' ' + str(mass40) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass40, 6)))
        print(content[0] + ' ' + str(mass41) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass41, 6)))
        print(content[0] + ' ' + str(mass42) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass42, 6)))
        print(content[0] + ' ' + str(mass43) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass43, 6)))
        content = file.readline()

    print("***************************************")

    mass1 = 596.138356
    mass2 = 298.069178
    mass3 = 566.127791
    mass4 = 268.058613
    mass5 = 237.040224
    mass6 = 864.196969
    mass7 = 1162.266147
    mass8 = 536.117226
    mass9 = 1132.255582
    mass10 = 1192.276712
    mass11 = 894.207534
    mass12 = 834.186404
    mass13 = 803.168015
    mass14 = 1101.237193
    mass15 = 1399.306371
    mass16 = 773.157450
    mass17 = 1369.295806
    mass18 = 833.178580
    mass19 = 1429.316936
    mass20 = 1131.247758
    mass21 = 1071.226628
    mass22 = 1040.208239
    mass23 = 1338.277417
    mass24 = 1636.346595
    mass25 = 1010.197674
    mass26 = 1606.336030
    mass27 = 1070.218804
    mass28 = 1666.357160
    mass29 = 1368.287982
    mass30 = 1308.266852


    content = file.readline()
    while (content != "6\n"):
        print(content)
        content = content.split(' ')
        # print(content)
        base_mass = content[2].split('\n')
        # print(base_mass[0])
        # print(round(float(base_mass[0])+mass1, 6))
        print(content[0] + ' ' + str(mass1) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass1, 6)))
        print(content[0] + ' ' + str(mass2) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass2, 6)))
        print(content[0] + ' ' + str(mass3) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass3, 6)))
        print(content[0] + ' ' + str(mass4) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass4, 6)))
        print(content[0] + ' ' + str(mass5) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass5, 6)))
        print(content[0] + ' ' + str(mass6) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass6, 6)))
        print(content[0] + ' ' + str(mass7) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass7, 6)))
        print(content[0] + ' ' + str(mass8) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass8, 6)))
        print(content[0] + ' ' + str(mass9) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass9, 6)))
        print(content[0] + ' ' + str(mass10) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass10, 6)))
        print(content[0] + ' ' + str(mass11) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass11, 6)))
        print(content[0] + ' ' + str(mass12) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass12, 6)))
        print(content[0] + ' ' + str(mass13) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass13, 6)))
        print(content[0] + ' ' + str(mass14) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass14, 6)))
        print(content[0] + ' ' + str(mass15) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass15, 6)))
        print(content[0] + ' ' + str(mass16) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass16, 6)))
        print(content[0] + ' ' + str(mass17) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass17, 6)))
        print(content[0] + ' ' + str(mass18) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass18, 6)))
        print(content[0] + ' ' + str(mass19) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass19, 6)))
        print(content[0] + ' ' + str(mass20) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass20, 6)))
        print(content[0] + ' ' + str(mass21) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass21, 6)))
        print(content[0] + ' ' + str(mass22) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass22, 6)))
        print(content[0] + ' ' + str(mass23) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass23, 6)))
        print(content[0] + ' ' + str(mass24) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass24, 6)))
        print(content[0] + ' ' + str(mass25) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass25, 6)))
        print(content[0] + ' ' + str(mass26) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass26, 6)))
        print(content[0] + ' ' + str(mass27) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass27, 6)))
        print(content[0] + ' ' + str(mass28) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass28, 6)))
        print(content[0] + ' ' + str(mass29) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass29, 6)))
        print(content[0] + ' ' + str(mass30) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass30, 6)))

        content = file.readline()

    print("***************************************")

    mass1 = 596.138356
    mass2 = 298.069178
    mass3 = 566.127791
    mass4 = 268.058613
    mass5 = 237.040224
    mass6 = 864.196969
    mass7 = 1162.266147
    mass8 = 536.117226
    mass9 = 1132.255582
    mass10 = 1192.276712
    mass11 = 894.207534
    mass12 = 834.186404
    mass13 = 536.117226
    mass14 = 1430.32476
    mass15 = 804.175839
    mass16 = 1400.314195
    mass17 = 1460.335325
    mass18 = 1102.245017
    mass19 = 1728.393938
    mass20 = 1698.383373
    mass21 = 1758.404503
    mass22 = 1490.345890
    mass23 = 1788.415068
    mass24 = 803.168015
    mass25 = 1101.237193
    mass26 = 1399.306371
    mass27 = 773.157450
    mass28 = 1369.295806
    mass29 = 833.178580
    mass30 = 1429.316936
    mass31 = 1131.247758
    mass32 = 1071.226628
    mass33 = 1667.364984
    mass34 = 1041.216063
    mass35 = 1637.354419
    mass36 = 1697.375549
    mass37 = 1339.285241
    mass38 = 1965.434162
    mass39 = 1935.423597
    mass40 = 1995.444727
    mass41 = 1727.386114
    mass42 = 1429.316936
    mass43 = 2025.455292
    mass44 = 1040.208239
    mass45 = 1338.277417
    mass46 = 1636.346595
    mass47 = 1010.197674
    mass48 = 1606.336030
    mass49 = 1070.218804
    mass50 = 1666.357160
    mass51 = 1368.287982
    mass52 = 1308.266852
    mass53 = 1904.405208
    mass54 = 1278.256287
    mass55 = 1874.394643
    mass56 = 1934.415773
    mass57 = 1576.325465
    mass58 = 2202.474386
    mass59 = 2172.463821
    mass60 = 2232.484951
    mass61 = 1964.426338
    mass62 = 2262.495516

    content = file.readline()
    while (content != "\n"):
        print(content)
        content = content.split(' ')
        # print(content)
        base_mass = content[2].split('\n')
        # print(base_mass[0])
        # print(round(float(base_mass[0])+mass1, 6))
        print(content[0] + ' ' + str(mass1) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass1, 6)))
        print(content[0] + ' ' + str(mass2) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass2, 6)))
        print(content[0] + ' ' + str(mass3) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass3, 6)))
        print(content[0] + ' ' + str(mass4) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass4, 6)))
        print(content[0] + ' ' + str(mass5) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass5, 6)))
        print(content[0] + ' ' + str(mass6) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass6, 6)))
        print(content[0] + ' ' + str(mass7) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass7, 6)))
        print(content[0] + ' ' + str(mass8) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass8, 6)))
        print(content[0] + ' ' + str(mass9) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass9, 6)))
        print(content[0] + ' ' + str(mass10) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass10, 6)))
        print(content[0] + ' ' + str(mass11) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass11, 6)))
        print(content[0] + ' ' + str(mass12) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass12, 6)))
        print(content[0] + ' ' + str(mass13) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass13, 6)))
        print(content[0] + ' ' + str(mass14) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass14, 6)))
        print(content[0] + ' ' + str(mass15) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass15, 6)))
        print(content[0] + ' ' + str(mass16) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass16, 6)))
        print(content[0] + ' ' + str(mass17) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass17, 6)))
        print(content[0] + ' ' + str(mass18) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass18, 6)))
        print(content[0] + ' ' + str(mass19) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass19, 6)))
        print(content[0] + ' ' + str(mass20) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass20, 6)))
        print(content[0] + ' ' + str(mass21) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass21, 6)))
        print(content[0] + ' ' + str(mass22) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass22, 6)))
        print(content[0] + ' ' + str(mass23) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass23, 6)))
        print(content[0] + ' ' + str(mass24) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass24, 6)))
        print(content[0] + ' ' + str(mass25) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass25, 6)))
        print(content[0] + ' ' + str(mass26) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass26, 6)))
        print(content[0] + ' ' + str(mass27) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass27, 6)))
        print(content[0] + ' ' + str(mass28) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass28, 6)))
        print(content[0] + ' ' + str(mass29) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass29, 6)))
        print(content[0] + ' ' + str(mass30) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass30, 6)))
        print(content[0] + ' ' + str(mass31) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass31, 6)))
        print(content[0] + ' ' + str(mass32) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass32, 6)))
        print(content[0] + ' ' + str(mass33) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass33, 6)))
        print(content[0] + ' ' + str(mass34) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass34, 6)))
        print(content[0] + ' ' + str(mass35) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass35, 6)))
        print(content[0] + ' ' + str(mass36) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass36, 6)))
        print(content[0] + ' ' + str(mass37) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass37, 6)))
        print(content[0] + ' ' + str(mass38) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass38, 6)))
        print(content[0] + ' ' + str(mass39) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass39, 6)))
        print(content[0] + ' ' + str(mass40) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass40, 6)))
        print(content[0] + ' ' + str(mass41) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass41, 6)))
        print(content[0] + ' ' + str(mass42) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass42, 6)))
        print(content[0] + ' ' + str(mass43) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass43, 6)))
        print(content[0] + ' ' + str(mass44) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass44, 6)))
        print(content[0] + ' ' + str(mass45) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass45, 6)))
        print(content[0] + ' ' + str(mass46) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass46, 6)))
        print(content[0] + ' ' + str(mass47) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass47, 6)))
        print(content[0] + ' ' + str(mass48) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass48, 6)))
        print(content[0] + ' ' + str(mass49) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass49, 6)))
        print(content[0] + ' ' + str(mass50) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass50, 6)))
        print(content[0] + ' ' + str(mass51) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass51, 6)))
        print(content[0] + ' ' + str(mass52) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass52, 6)))
        print(content[0] + ' ' + str(mass53) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass53, 6)))
        print(content[0] + ' ' + str(mass54) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass54, 6)))
        print(content[0] + ' ' + str(mass55) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass55, 6)))
        print(content[0] + ' ' + str(mass56) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass56, 6)))
        print(content[0] + ' ' + str(mass57) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass57, 6)))
        print(content[0] + ' ' + str(mass58) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass58, 6)))
        print(content[0] + ' ' + str(mass59) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass59, 6)))
        print(content[0] + ' ' + str(mass60) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass60, 6)))
        print(content[0] + ' ' + str(mass61) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass61, 6)))
        print(content[0] + ' ' + str(mass62) + ' ' + content[1] + ' ' + str(round(float(base_mass[0]) + mass62, 6)))

        content = file.readline()

    print("***************************************")
    # while (content != "4\n"):
    #     print(content)
    #     content = file.readline()
    #
    #
    #
    #
    #
    # print("***************************************")
    #
    # content = file.readline()
    # while (content != "5\n"):
    #     print(content)
    #     content = file.readline()
    #
    #
    #
    #
    # print("***************************************")
    #
    # content = file.readline()
    # while (content != "6\n"):
    #     print(content)
    #     content = file.readline()
    #
    # print("***************************************")
    #
    # content = file.readline()
    # while (content != "\n"):
    #     print(content)
    #     content = file.readline()