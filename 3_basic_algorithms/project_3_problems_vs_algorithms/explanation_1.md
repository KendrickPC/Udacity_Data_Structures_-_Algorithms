# Finding the Square Root of an Integer

##### Explanation

	I first check for negative values and raise a ValueError message if
	the user input tries to obtain a square root value of a negative value.
	
	Next, we check for base cases of a square root - this takes into 
	consideration an input number of 0 and 1s. If those base case inputs
	are received, the output is just a return of the input.

	Next, we create a start variable and assign it a value of 0
	The end value is assigned as the input number.

	Next, I run a while loop when the the start number is less than the
	end number (which is the input value). 

	I use integer division and half the value of the input; I store this
	value in a variable called average. 

	Then I check if the average squared equals the input number. If
	so, I will return the number - the square root is found. 

	The second check in my while loop considers if the square of the 
	average is less than the number. If so, I will add a value of 1
	to the average value and start my while loop over again with a 
	new average value.

	If the average squared is more than the input number, I run the 
	else equation which subtracts 1 from the average; then I run my while loop again. My while loop will end once the average squared == number.


##### Time Complexity
	O(log(n)) 

##### Space Efficiency
	O(1) because it takes constant time and does not depend on the 
	data set.


