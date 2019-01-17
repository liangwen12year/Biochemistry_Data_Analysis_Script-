def combinationSum( candidates, target):
    res = []
    candidates.sort()
    dfs(candidates, target, 0, [], res)
    return res
    
def dfs( nums, target, index, path, res):
    if target < 0:
        return  # backtracking
    if target == 0:
        res.append(path)
        return 
    for i in range(index, len(nums)):
        dfs(nums, target-nums[i], i, path+[nums[i]], res)

def char_frequency(inputstr):
    """
    use a dictionary to store the frequency of all character in the string,
    and sort the dictionary in increasing order of character's frequency

    Args:
        input string

    Return:
        A dictionary holds the character in input string and their frequency.
        And the dictionary is sorted in increasing order of character's frequency
    """
    char_dict = {}
    for i in inputstr:
        keys = char_dict.keys()
        if i in keys:
            char_dict[i] += 1
        else:
            char_dict[i] = 1
    # sort in increasing order of each character's frequency
    char_dict = sorted(char_dict.items(), key=lambda x: x[1])
    return char_dict





if __name__ == '__main__':
    #candidates = [291.0954,162.0528,203.0794,162.0528,146.0579]
    candidates = [291,162,203,146]
    # target = 2479
    #target = 2625
    #target = 3119
    #target = 2557
    mz = 1251.9571
    mono = (mz - 1.008)*2

    target1 = int(mono - 18.0106 - 311.1746 - 237.040224)
    target2 = int(mono - 18.0106 - 311.1746 - 268.058613)
    target3 = int(mono - 18.0106 - 311.1746 - 298.069178)
    target4 = int(mono - 18.0106 - 311.1746 - 566.127791)
    target5 = int(mono - 18.0106 - 311.1746 - 596.138356)



# 566.127791
# 596.138356

    res = combinationSum( candidates, target4)
    j = 0
    for i in res:
        #print(i)
        flag = 0
        strs = ''
        formatres= char_frequency(i)
        for i in  formatres:
            if i[0] == 146 and i[1] > 3:
                flag = 1
        if flag == 1: continue
        for i  in formatres:
            if i[0] == 203:
                strs = 'HexNAc('+str(i[1])+')'
                #print(strs)
        for i  in formatres:
            if i[0] == 162:
                strs += 'Hex('+str(i[1])+')'
                #print(strs)
        for i  in formatres:
            if i[0] == 146:
                strs += 'Fuc('+str(i[1])+')'
                #print(strs)
        for i  in formatres:
            if i[0] == 291:
                strs += 'NeuAc('+str(i[1])+')'
         
        #  print(formatres)
        print(strs) 
    # print('***************')
    # strs = ''
    # print(formatres)
  