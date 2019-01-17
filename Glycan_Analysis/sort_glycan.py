







if __name__ == '__main__':
    file=open("/home/wliang/Desktop/nba/glycan2/format", "r")
    file2=open("/home/wliang/Desktop/nba/glycan2/newformat", "r")
    file3=open("/home/wliang/Desktop/nba/glycan2/newnewformat", "r")


    # content = file.readline()
    # print(len(content))
    # if content[8] == "\t":
    #     print(content)
    # #print(content[8])
    # print('*********************')


    # content = file.readline()
    # print(len(content))
    # print(content)
    # print('*********************')


    # content = file.readline()
    # print(len(content))
    # print(content)
    # print('*********************')

    # content = file.readline()
    # print(len(content))
    # print(content)
    # print('*********************')

    # content = file.readline()
    # print(len(content))
    # print(content)
    # print('*********************')

    # content = file.readline()
    # print(content)
    # print(len(content))

    # content = file.readline()
    # print(content)
    # print(len(content))

    # content = file.readline()
    # print(content)
    # print(len(content))

    # content = file.readline()
    # print(content)
    # print(len(content))
    # print("*********")
    # print("*********")
    content = file.readline()
    content2 = file2.readline()
    while (content != ""):
        if content2[0] == "0":
            content3 = file3.readline()
            print(content3, end ='')
        else:
            print(' ')
        content = file.readline()
        content2 = file2.readline()
        #  print("******")
        # content = content.split(' ')
        # #print(content)
        # base_mass= content[2].split('\n')
        # #print(base_mass[0])
        #print(round(float(base_mass[0])+mass1, 6))

    file.close()
    file2.close()
    file3.close()    
    #content = file.readline()





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