Auxiliary documentation

-Contents of files:
* in.txt - contains raster data where each value is a pixel in an image
* agentframework_brigi.py - includes the class of 'Agent' and instructs them to 'eat', 'move' and 'share with neighbours'
* model2.0_brigi.py - code of the model

-Outline what the software is
The software is an agent-based model which creates Agents, moves them, get them interact with their neighbours and shows them on a "map".
It is an iterative model, which means the 'Agents' do things ( move, eat, share with neighbours) until some kind of "stopping condition" is reached ( this can be either random or set up, in my model I left it on random.)
Basically the code includes an Agent code where I created the agents, they can communicate with each other(by having a list of other agents), and they can move around the 'Environment' canvas.
The code also sets up the Environment where the Agents can do things (eat and move). In this code the Environment is a raster image, the 'in.txt' file contains the data. In the code I 'invited' the raster image file by making a new empty list (environment) and I used f = open method to read in and display the image.
After that, I set up a function where I called and downloaded agent coordinates from a website (this is from last practical unit)
I also wrote code for moving the agents around, shuffling them and they stop with a random condition.

I also created a GUI based menu where the model is waiting for the user to interact (press the run button on the menu) Then the animation runs showing the agents  moving and eating (with starting coordinates from the website) .

As the outcome of the model a txt file is saved containing the environment data. (File called "thisisenvironment2.txt")

-How can it be run and what is expected when it is run

The model can be run by pressing the 'run' button in Spyder, than the user can expect two windows to appear, and an empty 'canvas'. After that, we have the 'tk' window, where we can find the menu. By pressing the 'Model' button on the left hand side top corner we have the 'run model' button, which is for actually running the model.

To exit, press the red X in the right-hand side, top corner. A window will appear to ask  'Do you really want to quit?' and press 'yes'. It should close the windows and should stop the program running in the background. Instead, it crashes the program and need to manually “force close” the two windows and may need to re-start the IPython console as well.
This is a known issue.
The model best run in Spyder.

-Testing

The code is tested using doctest module. I set up this test to check whether downloading the data from the website is successful and correct. The test downloads the first position of X from the website , and expects 20 as the answer.(https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html)

The test runs, when the user presses the model menu/run model button and the initial model finishes.

-Licence:
https://gy17bk.github.io/mywebsite/code/licence1.pdf

References:
Also included in the code's comments

[Online].[Accessed 10 December 2019]. Available from: https://stackoverflow.com/questions/2307464/what-is-the-difference-between-root-destroy-and-root-quit

Used code from the comments to find out how to exit and stop the code running in the background
[Online].[Accessed 11 December 2019]. Available from:   https://stackoverflow.com/questions/110923/how-do-i-close-a-tkinter-window

[Online].[Accessed 02 December 2019]. Available from: 
https://docs.python.org/3/library/doctest.html

Canvas 
[Online].[Accessed 15 December 2019]. Available from: 
https://github.com/jarvisteach/appJar/issues/551


