# Run Time Analysis:

### Worst Case O(n) Efficiency Report:

##### Task0:
  Calculation of O(n), for the texts.csv file, is 1. My assumption is that
  n = 1 because there is only one pass through 
  of the for loop with the texts.csv file.

  Calculation of O(n), for the calls.csv file, is 1. My assumption is that 
  n = 1 because there is only one pass through 
  of the for loop with the calls.csv file.

  Therefore, the total of n would be 1 + 1 = 2. My guess is that the
  efficiency is O(2n) for the texts.csv file and calls.csv file
  combined.

##### Task1:
  Calculation of O(n), for the uniqueNumbers = [] array is 1 because there 
  will be 1 call through the array to check if a "new number" is unique 
  in the list. 

  Calculation of O(n), for the texts.csv file, is 2. My assumption is that
  n = 2 because there is one(1) pass through for the uniqueNumbers array, 
  one pass through with the for loop for row[0], and one pass through  
  for row[1] on the texts.csv file.

  Calculation of O(n), for the calls.csv file, is 2. My assumption is that
  n = 2 because there is  one pass through for the row[0] array and 
  one pass through with the row[1] array on the calls.csv file.

  Therefore, the total of n would be 1 + 2 + 2 = 5. My guess is that O(n) equals 5
  for the texts.csv file and calls.csv file combined.

##### Task2:

  My for loop, "for call in calls:" will take O(nlogn). Then, when comparing the total
  time spent on the phone, it would be another pass through of the dictionary, therefore
  making the total time complexity something like 0(n+nlogn+1) or O(nlogn(n)). 

##### Task3:

  For part A, calculation of O(n), for Bangalore_codes(), would be 0(n*logn) due to my sorting. 
  For part B, calculation of O(n) would be O(n) because it's just one pass through the data.

##### Task4:

  Creating a list of phone numbers, from the text.csv file, has an efficiency of O(n). Every 
  call  will check for duplicates in receiver list - this efficiency is O(n).
  Sorting in lexicographic order has an efficiency of 0(nlog(n))
