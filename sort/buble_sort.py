
input_array = [5,3,7,9,10,4,1,8,6,2]

print 'original input array : ', input_array, '\n'

# expected result after short [1,2,3,4,5,6]

# # find out the smallest number for input_array[0]
# for x in xrange(1,len(input_array)-1):
# 	if input_array[0] > input_array[x]:
# 		temp = input_array[0]
# 		input_array[0] = input_array[x]
# 		input_array[x] = temp

# print input_array

# # find out second smallest number for input_array[1]
# for x in xrange(2,len(input_array)-1):
# 	if input_array[1] > input_array[x]:
# 		temp = input_array[1]
# 		input_array[1] = input_array[x]
# 		input_array[x] = temp

# print input_array

# find out right position for all element

for y in xrange(0, len(input_array)):
	
	# important moment the range is from y+1 to end of array	
	for x in xrange(y+1, len(input_array)):

		if input_array[y] > input_array[x]:
			temp = input_array[y]
			input_array[y] = input_array[x]
			input_array[x] = temp

	print 'right number for position input_array[{0}]'.format(y)
	print input_array
	print "\n"

print 'number_of_compare_used: ', number_of_compare