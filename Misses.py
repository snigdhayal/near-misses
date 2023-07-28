'''Title- Looking for Fermat's Last Theorem Near Misses
Filename- NearMisses.py
Necessary files- None
Created external files- Misses.exe which is an executable for windows
Name- Snigdha Sri Yalamarthi, Ushaswini Renukunta
Email- SnigdhaSriYalamart@lewisu.edu, Ushaswinirenukunta@lewisu.com
Course and Sections- SU23-CPSC-60500-001
Date- July 27 2023
Explanation- This Program helps an interactive user search for near misses
              of the form (x, y, z, n, k) in the formula x^n + y^n = z^n, where x, y, z, n, k
              are positive integers, 2< n <12, 10 <= x <= k, and 10 <= y <= k
Resource- None
Language used- Python 3.10'''

def getMisses(n, k):
    '''Calculate near misses usoong of Fermat's Last Theorem formula
    
    Calculate x^n + y^n = z^n, and then look for the minimum miss for which
    z^n < (x^n + y^n) < (z+1)^n satisfies. Find out which one (either z^n or (z+1)^n) is
    closer to (x^n + y^n), and determine the miss as the smallest of these two 
    values: [(x^n + y^n) - z^n] or [(z+1)^n- (x^n + y^n)]. Then get the
    RELATIVE size of the miss divide that miss by (x^n + y^n) and print the values'''

    min_relative_miss = None
    # Outer loop for first variable x of function x^n + y^n = z^n
    for x in range(10, k):
        # loop for y variable
        for y in range(10, k):
            # calculate (x^n + y^n)
            xyp = pow(x, n) + pow(y, n)
            z = int(pow(xyp, 1/n))
            zp = pow(z, n)
            z1p = pow(z+1, n)
            miss = min( xyp - zp, z1p - xyp)
            # get relative miss
            relative_miss = miss / xyp
            if min_relative_miss is None:
                # get the relative miss for the forst time
                min_relative_miss = relative_miss
                print("\nx = {}      y = {}      z = {}       Miss = {}      Relative Miss = {}%".format(x, y, z, miss, round(min_relative_miss*100,2)))
            else:
                if relative_miss < min_relative_miss: 
                    # get the minimum relative miss
                    min_relative_miss = relative_miss
                    print("x = {}      y = {}      z = {}       Miss = {}      Relative Miss = {}%".format(x, y, z, miss, round(min_relative_miss*100,2)))
    # Final miss result
    print("\nFinal result for misses- \n") 
    print("x = {}      y = {}      z = {}       Miss = {}      Relative Miss = {}%".format(x, y, z, miss, round(min_relative_miss*100,2)))
    
def MissesCalculate():
    '''Get the input of power,n and limit,k for x and y from user then call the calculate function
    '''
    n = int(input("Exponent value(integer between 2 and 12)- "))
    while(n<3 or n>11):
        # check if n is bigger than 2
        n = int(input("Try again- "))
    i = int(input("Limit of x and y(greater than 10)- "))
    while(i<11):
        # check if k is bigger than 10
        i = int(input("Try again- "))
    getMisses(n,i)
        
if __name__ == "__main__":
    MissesCalculate()
    # continue the program until user wants to exit
    while(True):
        ch = input("\nExit[y/n]- ")
        if (ch == 'y' or ch == 'Y'):
            break
        else:
            MissesCalculate()
            