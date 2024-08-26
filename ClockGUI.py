#Skylar Brown
#INF 308
#Assignment 7





#imporing the tkinter module as tk 
import tkinter as tk
#importing Clock class
from Clock import Clock

#instantiating the Clock object 
clock_obj = Clock()

#defining a display time method that will display the clock object as a string when called in label2
def display_time():
    
    label2.config(text= f"{clock_obj}")

#definition for the set time button
def set_time_button_pressed():

 
    #setting the selection of the monthbox to the variable month and the same thing
    #for day, year, hour, minute, and second 
    month  = monthbox.curselection() 

    day = days_listbox.curselection() 

    year = year_listbox.curselection()

    hour = hour_listbox.curselection()

    minute = min_listbox.curselection()

    second = sec_listbox.curselection()
    
    #calling the setClock method from the clock class and taking the 0th index of the selection since curselection
    #will return as a tuple
    #adding 1 to day and month and adding 1900 to year since they start at 0 and need to be adjusted
    #so the numbers will display properly 
    clock_obj.setClock(hour[0], minute[0], second[0], month[0]+1, day[0]+1, year[0]+1900)

    #calling the display time method to display the clock object as a string in the second label
    display_time()

    

    

#definiton for the increase day button      
def increase_day_button_pressed():

    #calling the increase day function from the Clock class 
    clock_obj.increaseDay()

    #calling the display time method 
    display_time()
    
    
    




#defining a decrease day button
def decrease_day_button_pressed():

    #calling the decrease day function from the Clock class
    clock_obj.decreaseDay()

    #calling display time to print the object's contents to the GUI
    display_time()




#definition for the increase day button
def increase_day_button_pressed():

    #calling the increase day function to increase the day when the button is pressed 
    clock_obj.increaseDay()

    #calling display time function to change the time in the second label
    display_time()


#defintion of the increase second button 
def increase_second_button_pressed():

    
    #increasing the seconds from the clock class
    clock_obj.increaseSecond()

    #displaying the time in the second label
    display_time()

#definition for decreasing the seconds of the button 
def decrease_second_button_pressed():

    #calling the decrease second method from the Clock class
    clock_obj.decreaseSecond()

    #displaying the clock object's contents in the second label 
    display_time()

#initiating the root widget 
screen = tk.Tk()
#setting the background color of the main window 
screen.configure(bg ="lavender")
#adding a title to the screen 
screen.title("Clock")
#adding a size to the screen of 550 x 700
screen.geometry = ("550 x 700")





#creating a top frame and giving it a width, height, and color
screen.top_frame = tk.Frame(screen, width=800, height = 85, bg= "mediumpurple1")

#placing the top frame with tk's place method 
screen.top_frame.place(relx= .24, rely= .1)


#initializing the first and second labels and giving them text, color, and borders    
label1 = tk.Label(screen, bg="plum1",  text = "Current Time", borderwidth=3, relief = "ridge" )
label2 = tk.Label(screen, bg="plum1", text= "01/01/1980 12:00:00 AM", borderwidth=3, relief = "ridge")


#placing both labels with the place method 
label1.place(relx = .48, rely = .12)
label2.place(relx =.463, rely = .145)



#creating a middle frame and giving it a width, height, and background color
screen.mid_frame = tk.Frame(screen, width = 1500, height = 300, bg = "mediumpurple1")

#placing the frame using the place method
screen.mid_frame.place(relx= .01, rely=.23)


#initializing the 3rd label which will be above the listbox
label3 = tk.Label(screen, bg = "plum1", text = "Month", borderwidth=3, relief = "ridge")
label3.place(relx= .2, rely = .24)

#Day label that is above the day listbox 
label4 = tk.Label(screen, bg = "plum1", text = "Day", borderwidth=3, relief = "ridge")
label4.place(relx = .32, rely =.24)


#Year label above year listbox 
label5 = tk.Label(screen, bg = "plum1" , text = "Year", borderwidth=3, relief = "ridge")
label5.place(relx = .43, rely = .24)

#Hour label above hour listbox 
label6 = tk.Label(screen, bg= "plum1" , text = "Hour", borderwidth=3, relief = "ridge")
label6.place(relx =.53, rely = .24)


#Minute label above minute listbox
label7 = tk.Label(screen, bg = "plum1" , text = "Minute", borderwidth=3, relief = "ridge")
label7.place(relx =.65, rely =.24)


#Second label above the second listbox 
label8 = tk.Label(screen, bg = "plum1" , text = "Second", borderwidth=3, relief = "ridge")
label8.place(relx =.75, rely = .24)



#creating a months list containing all the months in a year 
months = ["January", "February" , "March", "April" , "May", "June" , "July" , "August", "September", "October", "November", "December"]


#creating a scroll bar with a vertical orient 
scroll_bar = tk.Scrollbar(screen, orient = "vertical")

#initializing a month listbox 
monthbox = tk.Listbox(screen, width = 14, exportselection = 0, selectmode = "single", yscrollcommand = scroll_bar.set)






#using a for loop to put all of the months inside the months listbox 
for x in range(len(months)):
    monthbox.insert("end", months[x])

    #setting the select set to 0, so if nothing is selected the first element January will be selected if Set Time is presed,
    #so it will not produce an error 
monthbox.select_set(0)


    #configuring a scroll bar and associating it with the month listbox
scroll_bar.config(command = monthbox.yview)

    #placing the month list box 
monthbox.place(relx = .185, rely = .27)

    #placing the scroll bar 
scroll_bar.place(relx = .24, rely = .3)




#creating a scroll bay for the days list box 
scroll_bar_days = tk.Scrollbar(screen, orient = "vertical")


#creating a days listbox 
days_listbox = tk.Listbox(screen, width = 14, exportselection =0, selectmode = "single", yscrollcommand= scroll_bar_days.set)



#for loop that has a range of 31, so it will add days 1-30 in the days listbox
for x in range(31):
    
    #typecasting so the integers convert into strings and adding one so the days list box goes to 31 
    days_listbox.insert("end", str(x+1))

    #setting the select set to 0 
days_listbox.select_set(0)
    
    #associating the scroll bar with the days list box 
scroll_bar_days.config(command = days_listbox.yview)


    #placing the listbox with the scroll bar 
days_listbox.place(relx= .3, rely= .27)
scroll_bar_days.place(relx = .357, rely= .3)




#creating a year scroll bar 
scroll_bar_year = tk.Scrollbar(screen, orient = "vertical")

#creating a year listbox 
year_listbox = tk.Listbox(screen, width = 14, exportselection = 0, selectmode = "single", yscrollcommand = scroll_bar_year.set)


#putting the range 1900-2101 inside the range funciton so it will interate through the years 1900-2100 and display in the listbox 
for x in range(1900, 2101):

    year_listbox.insert("end", str(x))

#setting the select set of the year list box to 0 
year_listbox.select_set(0)


#associating the year scroll bar with the year list box 
scroll_bar_year.config(command = year_listbox.yview)

#placing the year list box and year scroll bar 
year_listbox.place(relx =.41, rely =.272)

scroll_bar_year.place(relx = .467, rely =.3)


#creating a scroll bar for hour 
scroll_bar_hour = tk.Scrollbar(screen, orient = "vertical")

#creating a listbox for hour 
hour_listbox = tk.Listbox(screen, width = 14, exportselection = 0, selectmode = "single", yscrollcommand = scroll_bar_year.set)


#filling the hour list box with hours 0-24
for x in range(0, 24):

    #converting the integers to string
    
    hour_listbox.insert("end", str(x))

#setting the hour listbox to select set 0 
hour_listbox.select_set(0)

#associating the hour listbox with the hour scroll bar 
scroll_bar_hour.config(command = hour_listbox.yview)


#placing the hour list box and scroll bar 
hour_listbox.place(relx = .514, rely = .272)

scroll_bar_hour.place(relx = .57, rely = .3)



#creaing a scroll bar for the minute listbox 
scroll_bar_min = tk.Scrollbar(screen, orient = "vertical")


#creating a minute list box
min_listbox = tk.Listbox(screen, width = 14, exportselection = 0,selectmode = "single", yscrollcommand = scroll_bar_min.set)


#filling the minute listbox with the integers 0-59
for x in range(0, 60):

    #inserting the listbox and typecasting it to a string
     min_listbox.insert("end", str(x))

#setting the select set to 0
min_listbox.select_set(0)

#associating the minute scroll bar with the minute listbox
scroll_bar_min.config(command = min_listbox.yview)

#placing the minute listbox and minute scroll bar
min_listbox.place(relx = .63748, rely =.2749)

scroll_bar_min.place(relx = .694, rely =.3)


#creating a scroll bar for the seconds listbox
scroll_bar_sec = tk.Scrollbar(screen, orient="vertical")


#creating a seconds listbox
sec_listbox = tk.Listbox(screen, width = 14, exportselection = 0, selectmode = "single", yscrollcommand = scroll_bar_sec.set)


#fillin the listbox with the integers 0-59
for x in range(0, 60):

    sec_listbox.insert("end", x)

#setting the select set to 0
sec_listbox.select_set(0)

#associating the scroll bar with the listbox
scroll_bar_sec.config(command = sec_listbox.yview)

#placing the seonds listbox with the second scroll bar
sec_listbox.place(relx = .738, rely = .275)

scroll_bar_sec.place(relx= .795, rely=.3)


#creating a bottom frame and giving it a width, height, and color
screen.bottom_frame = tk.Frame(screen, width=900, height = 300, bg= "mediumpurple1")

#placing the bottom frame
screen.bottom_frame.place(relx= .195, rely= .6)


#creating a quit button that uses tk's destroy method that will get rid of the GUI when pressed 
quitbutton = tk.Button(screen, text = "Quit", command = screen.destroy)

#placing the quit button
quitbutton.place(relx = .485, rely =.69)

#creaing a set time button and setting it's command to the set_time_button_pressed method that is defined at the top of the program
set_time_button = tk.Button(screen, text = "Set Time", command = set_time_button_pressed)

#placing the set time button
set_time_button.place(relx = .315, rely =.65)    

#creating an increase day button that is associated with the increase day button pressed method defined above
increase_day_button = tk.Button(screen, text = "Increase Day", command=increase_day_button_pressed)


#placing the increase day button 
increase_day_button.place(relx =.39, rely = .65)

#creating a decrease day button with the command of the decrease_day_button_pressed method 
decrease_day_button = tk.Button(screen, text = "Decrease Day", command = decrease_day_button_pressed)


#placing the decrease day button
decrease_day_button.place(relx =.47, rely =.65)

#creating an increase second button that goes to the increase_second_button_pressed method when pressed 
increase_second_button = tk.Button(screen, text = "Increase Second", command = increase_second_button_pressed)

#plaicng the increase second button
increase_second_button.place(relx = .55, rely =.65)


#creating a decrease second button that will execute the decrease second button pressed method when pressed
decrease_second_button = tk.Button(screen, text = "Decrease Second", command = decrease_second_button_pressed)

#placing the decrease second button
decrease_second_button.place(relx = .64, rely = .65)

#calling the tk's mainloop funciton so that the main window will keep appearing until the user does otherwise 
screen.mainloop()













    

  
