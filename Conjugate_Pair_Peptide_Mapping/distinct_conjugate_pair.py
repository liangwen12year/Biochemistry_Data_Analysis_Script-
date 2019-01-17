if __name__ == '__main__':
    file=open("/home/wliang/Desktop/nba/glycan3/Find pairs/temp", "r")
    content = file.readline()
    content += file.readline()
    store =''
    while content != '':
        if content not in store:
            store += content
        content = file.readline()
        content += file.readline()
    


    print(store)
    file.close()