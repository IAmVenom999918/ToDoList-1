from tkinter import * 
import csv
from playsound import playsound # pip install playsound

databasePath = 'ToDoList-1/required files/databasecsv.csv'
# file = open('ToDoList-1/databasecsv.csv', 'a+')
# csvFileReader = csv.reader(file)
# csvFileWriter = csv.writer(file)
# file.close()

# BACK END

class Task:
    def __init__(self, taskId, title, description, due_date):
        self.taskId = taskId
        self.title = title
        self.description = description
        self.due_date = due_date

def button_click_sound():
    playsound('ToDoList-1/required files/Instant Sound Buttons 180.mp3')

def addTask(title, description, due_date):
    taskId = 1
    with open(databasePath, 'r') as file:
        try:
            taskId = int(((file.readlines())[-1].split(','))[0]) + 1 # get last task id in databasecsv.csv then add 1 to it
        except:
            taskId = 1
    a = Task(taskId, title, description, due_date) # making a new task

    with open(databasePath, 'a') as file: # adding new task to the database file
        csvFileWriter = csv.writer(file)
        csvFileWriter.writerow([a.taskId,a.title,a.description,a.due_date])
    
    print(f'Successfully Added {a.title}')





# FRONT END

windowGeometery = '400x600'
windowsResizeable = True

def ViewScreen():
    v = Tk()
    v.title('View Tasks')
    v.geometry(windowGeometery)
    v.resizable(windowsResizeable, windowsResizeable)
    backToMainScreenButton = Button(v, text="Back",width=10, command=lambda:[button_click_sound(),v.destroy(), mainScreen()])
    backToMainScreenButton.pack()
    v.mainloop()

def AddScreen():
    a = Tk()
    a.title('Add Tasks')
    a.geometry(windowGeometery)
    a.resizable(windowsResizeable, windowsResizeable)

    Label(a, text='Task Name').grid(row=0)
    e1 = Entry(a)
    e1.grid(row=0, column=1)
    Label(a, text='Task Description').grid(row=1)
    e2 = Entry(a)
    e2.grid(row=1, column=1)
    Label(a, text='Task Due Date').grid(row=2)
    e3 = Entry(a)
    e3.grid(row=2, column=1)


    # "Add" Button
    Button(a, text="Add",width=10, command=lambda:[
        button_click_sound(),
        addTask( e1.get(),e2.get(),e3.get() ), 
        print('added'), 
        e1.delete(0, END),
        e2.delete(0, END),
        e3.delete(0, END)
         ] if e1.get() != '' else'').grid(row=3, column=1)
    
    # Back to Main Screen Button
    Button(a, text="Back",width=10, command=lambda:[ button_click_sound(),a.destroy(), mainScreen()]).grid(row=4, column=1)



    a.mainloop()

def RemoveScreen():

    r = Tk()
    r.title('Remove Tasks')
    r.geometry(windowGeometery)
    r.resizable(windowsResizeable, windowsResizeable)
    backToMainScreenButton = Button(r, text="Back",width=10, command=lambda:[button_click_sound(),r.destroy(), mainScreen()])
    backToMainScreenButton.pack()
    r.mainloop()

def mainScreen():
    m = Tk()
    m.title('TO DO LIST')
    m.geometry(windowGeometery)
    m.resizable(windowsResizeable, windowsResizeable)

    w = Label(m, text = "Options : ")
    w.pack()

    viewScreenButton = Button(m, text='View Tasks',width='20', command=lambda:[ button_click_sound(),m.destroy(),ViewScreen()])
    viewScreenButton.pack()

    addScreenButton = Button(m, text='Add Task',width='20', command=lambda:[ button_click_sound(),m.destroy(),AddScreen()])
    addScreenButton.pack()

    removeScreenButton = Button(m, text='Remove Task',width='20', command=lambda:[ button_click_sound(),m.destroy(),RemoveScreen()])
    removeScreenButton.pack()
    
    quitButton = Button(m, text='Quit',width='20', command=lambda:[ button_click_sound(),m.destroy()])
    quitButton.pack()
    

    m.mainloop()

mainScreen()

