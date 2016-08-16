def manipulate_data(dstr,set_data):
	if (dstr == "list"):
		set_data.reverse()
		return set_data
		
	elif (dstr == "set"):
		set_data.update(["ANDELA", "TIA","AFRICA"])
		return set_data
	
	elif (dstr == "dictionary"):
		arr = []
		for key in set_data:
			arr.append(key)
		return arr
	
