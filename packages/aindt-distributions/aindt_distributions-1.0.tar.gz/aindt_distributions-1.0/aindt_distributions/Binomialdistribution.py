import math
import matplotlib.pyplot as plt
from .Generaldistribution import Distribution

class Binomial(Distribution):
    """ Class for Binomial distribution from parent class Distribution
    
    Attributes:
        mean (float): the mean value of the distribution
        stdev (float): the standard deviation of the distribution
        data_list (list of floats): list of floats to be extracted from a data file
        p (float):  the probability of an event occurring
        n (int): total number of trials
    
            
    """
    
    #       A binomial distribution is defined by two variables: 
    #           the probability of getting a positive outcome
    #           the number of trials
    
    #       If you know these two values, you can calculate the mean and the standard deviation
    #       
    #       For example, if you flip a fair coin 25 times, p = 0.5 and n = 25
    #       You can then calculate the mean and standard deviation with the following formula:
    #           mean = p * n
    #           standard deviation = sqrt(n * p * (1 - p))
    
    #       
    
    def __init__(self, prob=.5, size=20):
        
        self.p = prob
        self.n = size
        
        mean_val = self.calculate_mean()        
        std_val = self.calculate_stdev()
        
        Distribution.__init__(self, self.mean, self.stdev)
        
      
    
    def calculate_mean(self):
    
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        mean_val = self.p * self.n
        self.mean = mean_val

        return mean_val



    def calculate_stdev(self):

        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        
        std_val = math.sqrt(self.n * self.p * (1 - self.p))
        self.stdev = std_val

        return std_val
        
        
        
    def replace_stats_with_data(self):
    
        """Function to calculate p and n from the data set.
        Reading the data set is inherit from Distribution class
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """        
        
        self.n = len(self.data)
        self.p = sum(self.data) / self.n
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()        
        

        return self.p, self.n
        
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        
        x_values = ['0', '1']
        count = [sum(self.data), len(self.data) - sum(self.data)]
        plt.bar(x_values, count)
        plt.gca().set(title = 'Histogram of data', xlabel='Number values', ylabel='Counts')

            
        
    def pdf(self, k):
        """Probability mass function calculator for the Binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        # When having zeros and ones, the probability of having either of each is 0.5 
        multiplier = math.factorial(self.n) / (math.factorial(k) * math.factorial(self.n-k))
        pmf = multiplier  * self.p ** k * (1-self.p) **(self.n-k)
        
        return pmf
        
                

    def plot_bar_pdf(self):

        """Function to plot the probability mass function of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        x_values = list(range(0, self.n + 1))
        y_values = []
        for x in x_values:
            y_values.append(self.pdf(x))
            
        plt.bar(x_values, y_values)
        plt.gca().set(title = 'Probability mass function', xlabel='Number values (k)', ylabel='Probability')

        return x_values, y_values
                
    def __add__(self, other):
        
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
        
            
        result = Binomial()     # Create a new Binomial distribution which will be the added result
        result.n = self.n + other.n
        result.p = self.p
        result.mean = result.calculate_mean()
        result.stdev = result.calculate_stdev()
        
        return result
        
        
    def __repr__(self):
    
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Gaussian
        
        """

        return f'Mean: {self.mean}, Standard deviation: {self.stdev}, p: {self.p}, n: {self.n}'