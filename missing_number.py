def find_missing(a, b):
	if not a and not b:
		return 0
	for item in b:
		if not bin_search(item, a):
			return item
		else:
			continue
	return 0



def bin_search(tgt, alist):
	
	alist.sort()	
	
	sub_list = alist
	
	while sub_list:
		stat = 0
		stop = len(sub_list) - 1
		mid = int(round((stat + stop)/2))
		
		if tgt == sub_list[mid]:
			return True, alist.index(tgt)
		elif tgt < sub_list[mid]:			
			sub_list = sub_list[ : mid]
		else:
			stat = mid + 1
			sub_list = sub_list[stat :]
	
	return False