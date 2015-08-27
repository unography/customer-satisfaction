
##Project page: http://eldor4do.github.io/customer-satisfaction

###Customer Satisfaction Analysis

The aim of the project is to analyze tweets of/to various e-commerce companies in India in order to gauge their customer satisfaction level.

We initially collect the data.
Running the file, "getData.py" will do this. Change various parameters inside the code to get data of different companies.
It collects streaming tweets, and uses text-processing.com's API to perform sentiment analysis for each of those tweets.
It gives to output text files, one containing the tweets, and the other containing the sentiment of each of those tweets in the form of pos (positive), neg(negative) or neutral.

We then plot the data using "plot.py".

The sample data for this plot is given in the "tweets" directory.

INSTALLATION REQUIREMENTS

- Python 2.7
- Requests, Pandas, Matplotlib

PREFERRED INSTALLATION

- Anaconda Python distribution

The current plot is given in the "results" directory.

TODO: Add further analysis
TODO: Use own sentiment analysis algorithm
