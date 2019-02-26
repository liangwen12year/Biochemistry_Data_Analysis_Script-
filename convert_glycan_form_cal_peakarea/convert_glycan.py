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


	file=open("/home/wliang/Desktop/nba/convert_glycan_form_cal_peakarea/test", "r")
	content = file.readline()
	# print(content)
	# print(content[0])
	# print(content[3])
	while content != '':
		resstr= ''
		resstr += 'HexNAc('+str(content[3])+')'
		resstr += 'Hex('+str(int(content[2])+int(content[4]))+')'
		if content[5] != '0':
			resstr += 'Fuc('+str(content[5])+')'
		if content[1] != '0':
			resstr += 'NeuAc('+str(content[1])+')'
		print(resstr)
		content = file.readline()
