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




def cal_chemformula_case1(originalcontent):
    content = originalcontent.replace('\n', '')
    content_split = content.split(' ')
    #print(content_split[0])
    content_split[0] = content_split[0].replace('(', '')
    content_split[0] = content_split[0].replace(')', '')
    # print(content_split[0])
    substr = re.sub('[0-9]', ' ', content_split[0])
    # substr = substr.replace('', ' ')
    substr = substr.split(' ')
    # print(substr)

    chemcount = re.sub('[^0-9]', '', content_split[0])
    # print(chemcount)
    chemdict = {}

    for i in range(len(substr) - 1):
        chemdict[substr[i]] = int(chemcount[i])
    #print(chemdict)
    res = ''
    if 'HexNAc' in content_split[0]:
        for i in range(chemdict['HexNAc']):
            res = combine(res, 'C8O5NH13')

    if 'Hex' in content_split[0]:
        for i in range(chemdict['Hex']):
            res = combine(res, 'C6O5H10')

    if 'Fuc' in content_split[0]:
        for i in range(chemdict['Fuc']):
            res = combine(res, 'C6O4H10')

    if 'NeuAc' in content_split[0]:
        for i in range(chemdict['NeuAc']):
            res = combine(res, 'C11O8NH17')

    if 'NeuGc' in content_split[0]:
        for i in range(chemdict['NeuGc']):
            res = combine(res, 'C11O9NH17')

    print(res)





def cal_chemformula_case2(originalcontent):
    content = originalcontent.replace('\n', '')
    content_split = content.split(' ')
    #print(content_split[0])
    content_split[0] = content_split[0].replace('(', '')
    content_split[0] = content_split[0].replace(')', '')
    # print(content_split[0])
    substr = re.sub('[0-9]', ' ', content_split[0])
    # substr = substr.replace('', ' ')
    substr = substr.split(' ')
    # print(substr)

    chemcount = re.sub('[^0-9]', '', content_split[0])
    # print(chemcount)
    chemdict = {}

    for i in range(len(substr) - 1):
        chemdict[substr[i]] = int(chemcount[i])
    #print(chemdict)

    #print('**********************************')
    res = ''
    if 'HexNAc' in content_split[0]:
        for i in range(chemdict['HexNAc']):
            res = combine(res, 'C8O5NH13')

    if 'Hex' in content_split[0]:
        for i in range(chemdict['Hex']):
            res = combine(res, 'C6O5H10')

    if 'Fuc' in content_split[0]:
        for i in range(chemdict['Fuc']):
            res = combine(res, 'C6O4H10')

    if 'NeuAc' in content_split[0]:
        for i in range(chemdict['NeuAc']):
            res = combine(res, 'C11O8NH17')

    if 'NeuGc' in content_split[0]:
        for i in range(chemdict['NeuGc']):
            res = combine(res, 'C11O9NH17')



    addi = int(float(content_split[1]))
    res = combine_final_and_addi(res, addi)

    print(res)


def cal_chemformula_case3(originalcontent):
    content = originalcontent.replace('\n', '')
    content_split = content.split(' ')
   # print(content_split[0])
    content_split[0] = content_split[0].replace('(', '')
    content_split[0] = content_split[0].replace(')', '')
    # print(content_split[0])
    substr = re.sub('[0-9]', ' ', content_split[0])
    # substr = substr.replace('', ' ')
    substr = substr.split(' ')
    # print(substr)

    chemcount = re.sub('[^0-9]', '', content_split[0])
    # print(chemcount)
    chemdict = {}

    for i in range(len(substr) - 1):
        chemdict[substr[i]] = int(chemcount[i])
    #print(chemdict)
    res = ''
    if 'HexNAc' in content_split[0]:
        for i in range(chemdict['HexNAc']):
            res = combine(res, 'C8O5NH13')

    if 'Hex' in content_split[0]:
        for i in range(chemdict['Hex']-1):
            res = combine(res, 'C6O5H10')

    if 'Fuc' in content_split[0]:
        for i in range(chemdict['Fuc']):
            res = combine(res, 'C6O4H10')

    if 'NeuAc' in content_split[0]:
        for i in range(chemdict['NeuAc']):
            res = combine(res, 'C11O8NH17')

    if 'NeuGc' in content_split[0]:
        for i in range(chemdict['NeuGc']):
            res = combine(res, 'C11O9NH17')

    if 'M6P' in content_split[0]:
        res = combine(res, 'C6H11O8P')

    print(res)



def cal_chemformula_case4(originalcontent):
    content = originalcontent.replace('\n', '')
    content_split = content.split(' ')
    #print(content_split[0])
    content_split[0] = content_split[0].replace('(', '')
    content_split[0] = content_split[0].replace(')', '')
    # print(content_split[0])
    substr = re.sub('[0-9]', ' ', content_split[0])
    # substr = substr.replace('', ' ')
    substr = substr.split(' ')
    # print(substr)

    chemcount = re.sub('[^0-9]', '', content_split[0])
    # print(chemcount)
    chemdict = {}

    for i in range(len(substr) - 1):
        chemdict[substr[i]] = int(chemcount[i])
    #print(chemdict)
    res = ''
    if 'HexNAc' in content_split[0]:
        for i in range(chemdict['HexNAc']):
            res = combine(res, 'C8O5NH13')

    if 'Hex' in content_split[0]:
        for i in range(chemdict['Hex']-1):
            res = combine(res, 'C6O5H10')

    if 'Fuc' in content_split[0]:
        for i in range(chemdict['Fuc']):
            res = combine(res, 'C6O4H10')

    if 'NeuAc' in content_split[0]:
        for i in range(chemdict['NeuAc']):
            res = combine(res, 'C11O8NH17')

    if 'NeuGc' in content_split[0]:
        for i in range(chemdict['NeuGc']):
            res = combine(res, 'C11O9NH17')

    if 'M6P' in content_split[0]:
        res = combine(res, 'C6H11O8P')


    addi = int(float(content_split[1]))
    res = combine_final_and_addi(res, addi)
    print(res)


def combine_final_and_addi(finalres,addi):
    dict = [237, 267, 297, 566, 596]

    if dict[0] == addi:
        addistr = 'C7H12NO6P'
        return combine(finalres, addistr)


    if dict[1] == addi:
        addistr = 'C8H14NO7P'

        return combine(finalres, addistr)


    if dict[2] == addi:
        addistr = 'C9H16NO8P'

        return combine(finalres, addistr)



    if dict[3] == addi:
        addistr = 'C17H32N2O15P2'

        return combine(finalres, addistr)

    if dict[4] == addi:
        addistr = 'C18H34N2O16P2'

        return combine(finalres, addistr)




    if addi == 504:
        addistr1 = 'C7H12NO6P'
        addistr2 = 'C8H14NO7P'
        finalres1 = combine(finalres, addistr1)
        return combine(finalres1, addistr2)



    if addi == 534:
        addistr1 = 'C7H12NO6P'
        addistr2 = 'C9H16NO8P'
        finalres1 = combine(finalres, addistr1)
        return combine(finalres1, addistr2)


    if addi == 564:
        addistr1 = 'C8H14NO7P'
        addistr2 = 'C9H16NO8P'
        finalres1 = combine(finalres, addistr1)
        return combine(finalres1, addistr2)


    if addi == 474:
        addistr1 = 'C7H12NO6P'
        addistr2 = 'C7H12NO6P'
        finalres1 = combine(finalres, addistr1)
        return combine(finalres1, addistr2)

    if addi == 534:
        addistr1 = 'C8H14NO7P'
        addistr2 = 'C8H14NO7P'
        finalres1 = combine(finalres, addistr1)
        return combine(finalres1, addistr2)


    if addi == 594:
        addistr1 = 'C9H16NO8P'
        addistr2 = 'C9H16NO8P'
        finalres1 = combine(finalres, addistr1)
        return combine(finalres1, addistr2)





if __name__ == '__main__':
    file=open("C:/Users/liang/OneDrive/Desktop/nba/convert_glycan_to_chem_formula/glycan_input.txt", "r")

    originalcontent = file.readline()
    while originalcontent != '':
        if 'c' in originalcontent:
            if ('.' not in originalcontent)and ('M6P' not in originalcontent):
                cal_chemformula_case1(originalcontent)
                #Neucount = 0

            if ('.' in originalcontent) and ('M6P' not in originalcontent):
                cal_chemformula_case2(originalcontent)

            if ('.' not in originalcontent) and ('M6P' in originalcontent):
                cal_chemformula_case3(originalcontent)

            if ('.' in originalcontent) and ('M6P' in originalcontent):
                cal_chemformula_case4(originalcontent)
        else:
            print(' ')
        originalcontent = file.readline()

    file.close()