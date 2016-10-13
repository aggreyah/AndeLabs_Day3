class BinarySearch(list):

	def __init__(self, a, b):
		super(BinarySearch, self).__init__(range(b, a*b + b,b))
		self.length = a

	def search(self, target):
		bool_find, elem_idx, count = bin_search(target, self)
		my_out = {}
		my_out['count'] = count
		my_out['index'] = elem_idx

		return my_out

def bin_search(tgt, alist):
	
	alist.sort()	
	
	sub_list = alist
	n = 0

	if tgt == sub_list[0] or tgt == sub_list[-1]:
		return True, alist.index(tgt), n

	while sub_list:
		stat = 0
		stop = len(sub_list) - 1
		mid = int(round((stat + stop)/2))
		n += 1
		
		if out_of_range(tgt, sub_list):
			if sub_list[0] > tgt or sub_list[-1] < tgt:
				n += 2
				return False, -1, n
		else:
			if tgt == sub_list[mid]:
				return True, alist.index(tgt), n
			elif tgt < sub_list[mid]:
				sub_list = sub_list[ : mid]				
			else:
				stat = mid + 1
				sub_list = sub_list[stat :]


def out_of_range(t, l):
	if l[0] > t or l[-1] < t :
		return True
	else:
		return False


# one_to_twenty = BinarySearch(20, 1)
# two_to_forty = BinarySearch(20, 2)
# ten_to_thousand = BinarySearch(100, 10)

# print one_to_twenty.search(16)