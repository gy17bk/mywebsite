# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 19:50:51 2019

@author: Brigi
"""
import random
import operator
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
#this connects the agent class and file with the model
import agentframework_brigi
import csv
import matplotlib.animation 
import tkinter
from tkinter import messagebox
#this is used to download data from the website and use those coordinates
import requests
import bs4

# wrote this function to request data from website using beautiful soup
def download_agents():
    
#this is a doc test.
    """
    >>> download_agents()[0].x  # Donwloads data from website, checks the first agent's position
    20
    """

    r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
    content = r.text
    soup = bs4.BeautifulSoup(content, 'html.parser')
    td_ys = soup.find_all(attrs={"class": "y"})
    td_xs = soup.find_all(attrs={"class": "x"})
    # print(td_ys)  # I commented out this line - this makes the doctest fail
    # print(td_xs)  # I commented out this line as well as makes the doctest fail

    website_data= [] # make a new list
    for i in range(len(td_ys)):
        #I did put a len function here to check how long the list is
        #make a new empty list
        y = int(td_ys[i].text)
        x = int(td_xs[i].text)
        
        #I changed the below to use the empty list that i created not the agents.append
        website_data.append(agentframework_brigi.Agent(environment, [], y, x ))
    return website_data  # challange: this was in the for loop, and exited from the 
    # function after 1 iteration (that's why i only got one agent in the animation).

# Challange: 
#Before, I could not run the code 2x in spyder, 
#(when changed graphics to tkinter) only if i closed and re-opened spyder
#(it did not run again, because the code was still running in the background)
# this method closes the window and stops the code running.
#the code below makes a pop-up window when click on the [X] exit button and
# asks if i really want to close the window.
    
# Note: it still has an issue as it asks two times and after that it crashes
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        # the original code used .destroy but it did not stop the code running.
        #I chose to use .quit
        root.quit()
# code source: 
#https://stackoverflow.com/questions/111155/how-do-i-handle-the-window-close-event-in-tkinter 
#also: https://stackoverflow.com/questions/2307464/what-is-the-difference-between-root-destroy-and-root-quit                   

environment = [] # make an empty list 
# this reads in the 'in.txt' file and puts it in a 2D list
f = open(r'in.txt', newline='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)

for row in reader: # A list of rows
    rowlist = [] # make a new list before each row is processed
    for value in row: # A list of value
        rowlist.append(value) # do something with the values
        #print(value) # Floats - do something with values
    
    environment.append(rowlist)  #when a row is finished 
                                # append the rowlist to the environment list
                                
#this calculates the distance in Pythagoras
#def distance_between(agents_row_a, agents_row_b):
    #return (((agents_row_a.x - agents_row_b.x)**2) +
    #((agents_row_a.y - agents_row_b.y)**2))**0.5
agents = download_agents() #i did put a function here which downloads the agent 
                            #coordinates from the website and makes a list
num_of_agents = len(agents) # calculates the length of the agents list on the website
num_of_iterations = 3
neighbourhood = 30

print ("Agents")


fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

#ax.set_autoscale_on(False)
# Make the agents.
#for i in range(num_of_agents):
#   agents.append(agentframework_brigi.Agent (i, environment, agents))
#  print(agents[i])
#I dont need this anymore as added the agents line 38

carry_on = True
	
def update(frame_number):
    
    fig.clear()   
    global carry_on
#this for loop moves the agents along the x and y axes by +- 1 randomly
    for i in range(num_of_agents):
        if random.random() < 0.5:
            agents[i].x  = (agents[i].x + 1) % 99 
        else:
            agents[i].x  = (agents[i].x - 1) % 99
        
        if random.random() < 0.5:
            agents[i].y  = (agents[i].y + 1) % 99 
        else:
            agents[i].y  = (agents[i].y - 1) % 99 
            
        agents[i].eat()

        
    if agents[0].store > 150 : #  this sets the stopping condition to random
        carry_on = False
        print("stopping condition")
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
        #print(agents[i][0],agents[i][1]) 

print ("Agents after shuffle")
#implemented random function to shuffle the list of agents
random.shuffle(agents)
#print(agents[i])
   

# Move the agents.
for j in range(num_of_iterations):
    print("Iteration", str(j))
    for i in range(num_of_agents):
        agents[i].move() #this calls the move method
        agents[i].eat() #this calls the eat function from
                        #the agentframework file
        #and this calls the share function from agentframework
        agents[i].share_with_neighbours(neighbourhood)

# TODO: these lines below is the reason why the window was not empty 
#when I start the program.
"""
#this displays the environment data, I commented this out as
#it started a new window

matplotlib.pyplot.xlim(0, 99)
matplotlib.pyplot.ylim(0, 99)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i].x, agents[i].y)
    print(agents[i].x,agents[i].y)
    animation = matplotlib.animation.FuncAnimation(fig, update,
                                                   interval=1)
"""

# this is a generator for the stopping condition
def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as not assigning
    while (a < 10) and (carry_on): # where the condition is set to true (while True) 
                                # it will generate infinite seq.
                                #if any of these not true it will end the while loop
        yield 	# Returns control and waits next call.
        a = a + 1
    
#animation = matplotlib.animation.FuncAnimation(fig, update, 
                                                #interval=1, repeat=False, frames=10)

animation = matplotlib.animation.FuncAnimation(fig, update,
                                               frames=gen_function,
                                               repeat=False)


#this builds the main window, creates the matplotlib canvas  
# and opens it in a new window                                         
#root = tkinter.Tk()
#root.wm_title("Model")


#this creates the menu and links it with the run function
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
    # needed to change to draw, as the original '.show' did not work
    # solution is from: https://github.com/jarvisteach/appJar/issues/551
    canvas.draw() 

#this adds a menu that a user can interact with
root = tkinter.Tk()
#I moved the below 2 lines here as links to the root
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)

# This is linked to the def_closing which is on the top. 
# and stops running the code
root.protocol("WM_DELETE_WINDOW", on_closing)

#the root.mainloop() is not necessary,as the tkinter.mainloop()
# below does the job. 
#Starting the mainloop() twice only forces to click twice on 'OK' 
#when it asks "Do you want to quit?" so i commented it out.
# root.mainloop()  

# this opens a new txt file and writes the environment out to the file
f= open ("thisisenvironment2.txt", "w")
for line in environment:
    f.write(str(line) + "\n")

f.close() # Don't close until done with the reader;
        # the data is read on request.
        
#this is important as sets the GUI and awaits for interaction
tkinter.mainloop()

#this is a test and links it to the top (line 24-27) to check the first
# agent's position - which i expect to be 20.
#it only runs after the main code run and after closing the windows.
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
