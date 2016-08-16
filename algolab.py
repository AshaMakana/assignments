def get_algorithim_result(get_list):
	largest = get_list[0]
	for num in get_list:
		if largest < num:
			largest = num
	return largest

def prime_number(no_int):
	if (no_int == 1):
		return False
	elif (no_int == 2):
		return True
	else:
		for x in range(2, no_int):
			if (no_int % x ==0):
				return False
			return True


