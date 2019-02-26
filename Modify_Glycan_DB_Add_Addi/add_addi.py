import re

if __name__ == '__main__':
    file=open("/home/wliang/Desktop/nba/glycan4/final_glycan", "r")

    originalcontent = file.readline()
    while originalcontent != '':
        content = originalcontent.replace('\n', '')
        content_split = content.split(' ')
        #print(content_split[0])
        content_split[0] = content_split[0].replace('(', '')
        content_split[0] = content_split[0].replace(')', '')
        #print(content_split[0])
        substr = re.sub('[0-9]', ' ', content_split[0])
        #substr = substr.replace('', ' ')
        substr = substr.split(' ')
        #print(substr)

        chemcount = re.sub('[^0-9]', '', content_split[0])
        #print(chemcount)
        chemdict = {}
        
        for i in range(len(substr)-1):
            chemdict[substr[i]] = int(chemcount[i])
        #print(chemdict)
        Neucount = 0
        
        if 'NeuAc' in content_split[0]:
                Neucount += chemdict['NeuAc']
        
        if 'NeuGc' in content_split[0]:
                Neucount += chemdict['NeuGc']
        #print(Neucount)


        mass1 = 268.058613
        mass2 = 298.069178
        mass3 = round(mass1+mass1,6)
        mass4 = round(mass1+mass2,6)
        mass5 = round(mass2+mass2,6)
        mass6 = round(mass1+mass1+mass1,6)
        mass7 = round(mass2+mass2+mass2,6)
        mass8 = round(mass1+mass2+mass2,6)
        mass9 = round(mass1+mass1+mass2,6)
        
        Hex_Fuc = [0,mass1,mass2,mass3,mass4,mass5,mass6,mass7,mass8,mass9]
        #print(Hex_Fuc)
        

        print(originalcontent, end='')
        for i in range(Neucount+1):
            finaladdi = round(237.040224*i, 6)
            
            for j in range(len(Hex_Fuc)):
                finaladdi_2 =round( Hex_Fuc[j]+finaladdi, 6)
                outcontent = originalcontent.split(' ')
                base_mass= outcontent[2].split('\n')
                if finaladdi_2 != 0.0:
                    print(outcontent[0]+ ' ' + str(finaladdi_2) + ' ' + outcontent[1]+' ' + str(round(float(base_mass[0]) + finaladdi_2, 6 )) )


 
                    
        originalcontent= file.readline()
    


    #print(store)
    file.close()