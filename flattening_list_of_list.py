##INPUT
#list1=[["a","b"],["c","d"],["e","f]"]
##OUTPUT
#flat_list=["a","b","c","d","e","f"]
def flattening_list_of_list():
	list1=[["a","b"],["c","d"],["e","f"]]
	flat_list = [item for sublist in list1 for item in sublist]
	print(flat_list)
flattening_list_of_list()
