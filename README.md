Download Data for Every Census Tract in the U.S.

I was tasked with downloading the median household income for every Census tract in the U.S. The Census API is limited in that it only allows users to access the data for every tract one state at a time. This code works around the limitation by downloading the data for each state and then combining them into one CSV file.

You will need to obtain your own API key to use this code. This example pulls data for median household income, ‘DP03_0062E’. You can pull multiple values building a string with the variable codes separated by a comma. 
