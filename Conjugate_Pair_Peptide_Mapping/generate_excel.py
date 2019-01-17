import re







if __name__ == '__main__':
    file=open("/home/wliang/Desktop/nba/glycan3/Find pairs/test", "r")
    content = file.readline()
    while content != '':
        content = content.replace('\n', '')
        if 'N' in content:
            content = content.split('\t')
            output1 = content[0]+'_'+content[1]+'\t'+'M+1\t'+content[2]+'\t'+'M+H'
            output2 = content[0]+''+content[1]+'\t'+'M+2\t'+content[2]+'\t'+'M+2H'
            output3 = content[0]+'_'+content[1]+'\t'+'M+3\t'+content[2]+'\t'+'M+3H'
            # print(output1)
            print(output2)
            # print(output3)
            content = file.readline()  
        else:
            #print(' ')
            content = file.readline()

    file.close()
    #file2.close()
    
 
