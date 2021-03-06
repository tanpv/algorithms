
# problem 1
# using recursion to print n number

def print_n_number(n):
	if(n == 0):
		return 0
	else:
		print "{0}\n".format(n)
		return print_n_number(n-1)


# problem 2
# using recursion to implement factorial function

def factorial(n):
	if(n == 1):
		return 1
	else:
		return n*factorial(n-1)

# problem 3
# use recursion to create fibonaci series

def fibonaci(n):
	if (n==1 or n==2):
		#print "{0} ".format(1)
		return 1;
	else:
		#print "{0} ".format(fibonaci(n-1) + fibonaci(n-2))
		return fibonaci(n-1) + fibonaci(n-2)

def print_first_n_fibonaci_number(n):
	for x in xrange(1,n+1):
		print fibonaci(x)

# problem 4
# use recursion to revert a string
# example "abcd" --> "dcba"
# base case : len(str) == 1

def string_revert(input_string):
	if len(input_string) == 1:
		return input_string
	else:
		return input_string[len(input_string)-1] + string_revert(input_string[:-1])



# problem 5
# find all permutation of string
# permutation of abc are ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']

def permutation(input_string):	
	
	result = []
	
	if len(input_string) == 1:
		# show in case input string contain only one char
		# print input_string
		result.append(input_string)
		return result
	
	sub_permutation = permutation(input_string[1:len(input_string)])

	for one_permutation in sub_permutation:
		
		for pos in range(len(one_permutation) + 1):

			new_permutation = one_permutation[:pos] + input_string[0] + one_permutation[pos:]

			# print permutation before add
			# print new_permutation

			result.append(new_permutation)

	return result

# print_n_number(100)
# print factorial(4)
# fibonaci(10)
# print_first_n_fibonaci_number(30)
# print string_revert("0123456789")
# print len(permutation('abcdefgh'))
