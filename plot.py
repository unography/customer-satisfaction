#ALL IMPORTS
import pandas as pd
from pandas import Series
from pandas import DataFrame
pd.options.display.mpl_style = 'default'

import matplotlib.pyplot as plt

#END IMPORTS

def calc(filename): #Calculates total pos and neg words and normalizes the data. Ignores neutral tweets.
	f = open(filename,"r")
	count = 0.0
	val = {"pos":0.0,"neg":0.0}
	for line in f:
		if(line[:-1] != 'neutral'):
			val[line[:-1]] = val[line[:-1]] + 1
	count = val["pos"] + val["neg"] 
	for key in val:
		val[key] = float((val[key] *100)/ count)	
	return val

def create(): #Prepares data for plotting and plots the data
    
    #Get dictionary of count of positive and negative tweets for each brand
    amazonin = calc("amazonin.txt")
    flipkart = calc("flipkart.txt")
    snapdeal = calc("snapdeal.txt")
    myntra = calc("myntra.txt")
    shopclues = calc("shopclues.txt")

    #Convert dictionary to Panda Series
    amazoninSeries = Series(amazonin)
    flipkartSeries = Series(flipkart)
    snapdealSeries = Series(snapdeal)
    myntraSeries = Series(myntra)
    shopcluesSeries = Series(shopclues)
    
    #For better color scheme using Tableau's color data set
    tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),  
             (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),  
             (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),  
             (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),  
             (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]  

    # Scale the RGB values to the [0, 1] range, which is the format matplotlib accepts.  
    for i in range(len(tableau20)):  
        r, g, b = tableau20[i]  
        tableau20[i] = (r / 255., g / 255., b / 255.) 
   
    data = pd.DataFrame({'Shopclues': shopcluesSeries, 'Myntra': myntraSeries, 'Flipkart': flipkartSeries, 'Amazon': amazoninSeries, 'Snapdeal': snapdealSeries})
    data.plot(title = "Percentage of positive and negative tweets of various e-commerce brands", kind='barh',figsize=(12, 8), subplots=True, color = tableau20[:6])

def main():
    create()

main()