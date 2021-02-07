def average(x):

	runningSum = 0.0;
	numElements = 0.0;

	test = True;

	for a in x:
		for b in str(a):
                	if b.isdigit() == False and b != '.' and b != '-':
				test = False;
		
		if(test == True):
			runningSum = runningSum + a;
			numElements = numElements + 1;


	if len(x) == 0:
		return ("You entered an empty list.")

	if test == False:
		return("At least one of the list elements was invalid.")

	return(round((runningSum / numElements), 5))

