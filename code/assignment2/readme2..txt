
							Assignment 2. - Black Death
 
	List of contents: 

·       Assignment2_Finished.ipynb - which is a Jupyter notebook file containing the code 

·       Death.rats.txt - which contains the data of the average rats caught per week; 

·       Death_parishes.txt - which is the average population density; 

·       When the program finishes, a new text file is written out called absolut_death.txt 

The model as suggested on the project description page, does the followings: 

·       Reads in data using the death.rats.txt and Death_parishes.txt files, 

·       Uses historical data and the given equation to calculate figures and places the map of average deaths per 100x100 m square area, 

·       Displays the average population map, the average rats caught per week map, on the screen, 

·       At the end of the program, it writes out the results to a new txt file, called  absolut_death.txt, 

·       Has a GUI which allows the user to change the values using a scroll bar and the equation.  

o   Variables (min., max.,step, description and values) can be found in detail in the code comments as well, but for both the population and rats scroll bar, the step value is set up to change 0.01 at the time which gives the user the ability to refine the variable from 0 to 10 and initial value on the scroll bar is set to 1.30, and 0.8 as given in the equation. 

	Project description and challenges 

First, I started writing the code in Jupyter Notebooks and when I missed out a line/made the first mistake I realised that it is quite difficult to amend or insert lines between already existing lines. As the line numbers in Jupyter indicates in which order the program will it run, inserting or deleting a line made the code not executed in a right order. Even after re-starting the kernel, I could not get it properly working.  This is the reason why I decided to write my code in Spyder, and after I got it working, I uploaded/saved it as a Jupyter notebook. 
The below paragraphs details the challenges I encountered while writing the code in Python: 

·       As the txt file is containing strings as values, I needed to convert them to floats to be able to do mathematical operations. 

·       Initially I used this code twice for reading in the two different datasets: 

f = open('death.rats.txt', newline='') 
  
rats = [] 
     
reader = csv.reader(f) 
  
for row in reader: # A list of rows 
    rowlist = [] # make a new list before each row is processed 
    
    for value in row: # A list of value 
         
         rowlist.append(float(value)) # do something with the values 
         # converted values (string) to float  
         
        #print(value) # Floats - do something with values 
     
    rats.append(rowlist) 
#print (rats) 

·       When reading the death.rats.txt csv file in, I could have used the  
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)  
which “Instructs writer objects to quote all non-numeric fields and instructs the reader to convert all non-quoted fields to type float.” (https://docs.python.org/2/library/csv.html) 

·       I did use the above method for reading in the death_parishes.txt file 

·       After writing the above two codes, I wanted to shrink it, as it would be easier to read and for that, I created a function called read_txt which has a parameter (passz) 

·       I imported matplotlib.pyplot  at the top of the code, and used it to show the parishes 

·       The challenge here was to figure out how to show both maps in the same time, because first I wrote the code in a wrong order. 

pyplot.imshow(parishes) 
pyplot.imshow(rats) 
pyplot.show(parishes) 
pyplot.show(rats) 

·       The above only showed the rats values on a plot. 
I separated them and both plots are now showing correctly.

pyplot.imshow(rats) 
pyplot.show() 
 
pyplot.imshow(parishes) 
pyplot.show() 

Also, the second sets of parentheses are empty, (parishes/rats) are not needed. 
 
·       For the scrollbar I decided to use an algorithm called ipywidgets for creating a GUI and to show scrollbars in my program effectively and easy. Although it is not available for spyder, it can be used very efficiently in Jupyter notebooks. 

·       When changing the parameters on the scrollbar (from 1.3 for population and 0.8 for rats) we need to run the program again to be able to see the changes in the array. 

·       Also, the written out txt file (absolut_death.txt) will change every time the user changes the parameters and run the program again. 

·       However, the plotted maps of London won’t change as the proportion  between the avg rats and avg death do not change. 
 
·       Why Numpy? 
Importing numpy at the top of the code allows to put the data in 2D arrays, and in contrast of python lists, numpy uses less memory, which is beneficial in regards to the code’s efficiency. 
 
·       Testing:  
Since the absolute deaths file changes every time as the user changes the values on the scroll-bar, doctest can’t be effectively used in this case. 
I used the doctest module to check the first position of the Death_parishes.txt file what the program expects to be 0.0. This is tested at the bottom of the code, in block 13th. 
 
·       When developing the model, the main idea was to create an easily useable model with a GUI where the user can decide and change the parameter weights for the equation upon request. 

·       The software development process followed the well-known iterative and incremental development model, but in this case there were no “test users” involved as the iterative design process suggests. With my model, I broke down the project into small parts after studying the Assignment requirements, and each time I added a small part/function to my code, and ran it in Python.  When an issue occurred, such as error message in the iPython console of mistyping the code, or wrong indentation or else, I went back to the code and tried to fix the issue, also used the testing module, as described above to make sure the program read the data in correctly.
 

·       References: 

[Online].[Accessed 6 December 2019]. Available from: 
Display array as raster: 
https://stackoverflow.com/questions/3886281/display-array-as-raster-image-in-python 

Numpy 
[Online]. [Accessed 18 December 2019]. Available from:
https://towardsdatascience.com/a-hitchhiker-guide-to-python-numpy-arrays-9358de570121 
 
Numeric widget
[Online]. [Accessed 14 December 2019]. Available from:
https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html#Numeric-widgets 

Slider: 
[Online].[Accessed 14 December 2019]. Available from:
https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html

Software development
[Online]. [Accessed 19 December 2019]. Available from:
https://en.wikipedia.org/wiki/Iterative_and_incremental_development 

[Online]. [Accessed 20 December 2019]. Available from:
https://en.wikipedia.org/wiki/Software_development_process

[Online]. [Accessed 20 December 2019]. Available from:
https://en.wikipedia.org/wiki/Iterative_design
