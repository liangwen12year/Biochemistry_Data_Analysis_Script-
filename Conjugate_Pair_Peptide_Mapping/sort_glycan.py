import re



def combine(formula1, formula2):
    p1 = find_chem_dict(formula1)
    p2 = find_chem_dict(formula2)    
    #print(find_chem_dict(finalres))

    #print(find_chem_dict(addistr))
    for k, v in p2.items():
        if k in p1.keys():
            p1[k] += v
        else:
            p1[k] = v
    #X,Y=,Counter(p2)
    # z=dict(Counter(p1)+Counter(p2))
    list1 = sorted(p1.items())
    #print(list1)

    temp = ''
    res = ''
    for i in list1:
        temp = i[0]+ str(i[1])
        res = res + temp

    return res




def find_chem_dict(inputstr):
    chem_dict = {}
    j = -1 
    for i in inputstr:
        j += 1
        if i.isalpha():
            p = j+1
            chem_dict[i] = 1
            flag2 = 0
            strrr = ''
            while  p < len(inputstr) and inputstr[p].isdigit():
                strrr += inputstr[p]  
                p += 1 
                #print(strrr)
                flag2 = 1
            if flag2 == 1:
                chem_dict[i] = int(strrr)
    # chem_dict = sorted(che_dict.items(), key=lambda x: x[1])
    return chem_dict
    # return sorted(chem_dict.items())



def combine_final_and_addi(finalres,addistr):
    dict = [237, 268, 566, 298]

    if dict[0] == addi:
        addistr = 'C7H12NO6P'
        return combine(finalres, addistr)


    if dict[1] == addi:
        addistr = 'C8H15NO7P'
        return combine(finalres, addistr)


    if dict[2] == addi:
        addistr = 'C17H32N2O15P2'
        return combine(finalres, addistr)



    if dict[3] == addi:
        addistr = 'C9H17NO8P'
        return combine(finalres, addistr)


    if addi == 535:
        addistr1 = 'C7H12NO6P'   
        addistr2 = 'C9H17NO8P'
        finalres1 = combine(finalres, addistr1)
        return combine(finalres1, addistr2)  



    if addi == 536:
        addistr1 = 'C8H15NO7P'   
        addistr2 = 'C8H15NO7P'
        finalres1 = combine(finalres, addistr1)
        return combine(finalres1, addistr2)


    if addi == 596:
        addistr1 = 'C9H17NO8P'   
        addistr2 = 'C9H17NO8P'
        finalres1 = combine(finalres, addistr1)
        return combine(finalres1, addistr2)


    if addi == 804:
        addistr1 = 'C8H15NO7P'   
        addistr2 = 'C8H15NO7P'
        addistr3 = 'C8H15NO7P'
        finalres1 = combine(finalres, addistr1)
        finalres2 = combine(finalres1, addistr2)
        return combine(finalres2, addistr3)    


    if addi == 833:
        addistr1 = 'C9H17NO8P'   
        addistr2 = 'C9H17NO8P'
        addistr3 = 'C7H12NO6P'
        finalres1 = combine(finalres, addistr1)
        finalres2 = combine(finalres1, addistr2)
        return combine(finalres2, addistr3)



    if addi == 834:
        addistr1 = 'C8H15NO7P'   
        addistr2 = 'C17H32N2O15P2'
        finalres1 = combine(finalres, addistr1)
        return combine(finalres1, addistr2)



    if addi == 864:
        addistr1 = 'C8H15NO7P'   
        addistr2 = 'C18H34N2O16P2'
        finalres1 = combine(finalres, addistr1)
        return combine(finalres1, addistr2)



    if addi == 894:
        addistr1 = 'C9H17NO8P'   
        addistr2 = 'C18H34N2O16P2'
        finalres1 = combine(finalres, addistr1)
        return combine(finalres1, addistr2)
        

    if addi == 1071:
        addistr1 = 'C7H12NO6P'   
        addistr2 = 'C8H15NO7P'
        addistr3 = 'C17H32N2O15P2'
        finalres1 = combine(finalres, addistr1)
        finalres2 = combine(finalres1, addistr2)
        return combine(finalres2, addistr3)


    if addi == 1132:
        addistr1 = 'C17H32N2O15P2'   
        addistr2 = 'C17H32N2O15P2'
        finalres1 = combine(finalres, addistr1)
        return combine(finalres1, addistr2)


    if addi == 1162:
        addistr1 = 'C17H32N2O15P2'   
        addistr2 = 'C18H34N2O16P2'
        finalres1 = combine(finalres, addistr1)
        return combine(finalres1, addistr2)


    if addi == 1727:
        addistr1 = 'C7H12NO6P'   
        addistr2 = 'C9H17NO8P'
        addistr3 = 'C18H34N2O16P2'
        addistr4 = 'C18H34N2O16P2'
        finalres1 = combine(finalres, addistr1)
        finalres2 = combine(finalres1, addistr2)
        finalres3 = combine(finalres2, addistr3)
        return combine(finalres3, addistr4)




if __name__ == '__main__':
    file=open("/home/wliang/Desktop/nba/glycan3/Find pairs/test", "r")
    content = file.readline()
    while content != '':
        if content != '\n':
            content = content.replace('\n', '')
            if '.' not in content:
                file2=open("/home/wliang/Desktop/nba/glycan3/Find pairs/compounds.xml", "r") 
                list = 'name=\''+content+'\'>'
                #print(list)
                flag = 0
                content2=file2.readline()
                while content2 != '':
                    if list in content2:
                         file2.readline()
                         ele = file2.readline()
                         finalres = '' 
                         while '</molecular_formula>' not in ele:
                            #print(ele)
                            final = ele.strip()
                            str1 = re.sub('[^CHNO]', '', final)
                            str2 = re.sub('[^0-9]', '', final)
                            result = str1+str2
                            finalres += result 
                            ele = file2.readline()
                            flag = 1

                         finalres = combine(finalres, 'C13H17N3')
                         print(finalres)
                         if flag == 1: break
                    content2 = file2.readline()
                file2.close()
                if(flag == 0):
                    print(' ') 
                content = file.readline()

            else:
                #print(1)
                file2=open("/home/wliang/Desktop/nba/glycan3/Find pairs/compounds.xml", "r") 
                content = content.split(' ') 
                list = 'name=\''+content[0]+'\'>'
                #print(list)
                content2=file2.readline()
                #print(4)
                flag = 0
                while content2 != '':
                    #print(6)
                    if list in content2:
                         #print(5)
                         flag = 0
                         file2.readline()
                         ele = file2.readline()
                         finalres = ''
                         #print(2) 
                         while '</molecular_formula>' not in ele:
                            #print(ele)
                            final = ele.strip()
                            str1 = re.sub('[^CHNO]', '', final)
                            str2 = re.sub('[^0-9]', '', final)
                            result = str1+str2
                            finalres += result 
                            ele = file2.readline()
                            flag = 1
                         addi = int(float(content[1]))
                         #print(3)
                         finalres = combine_final_and_addi(finalres, addi)
                         finalres = combine(finalres, 'C13H17N3')
                         print(finalres)
                         #print("***************")
                         if(flag == 1): break
                    content2 = file2.readline()
                if(flag == 0):
                    print(' ')       
                file2.close()
                content = file.readline()
        else:
            print(' ')
            content = file.readline()

    file.close()
    file2.close()
    
 
