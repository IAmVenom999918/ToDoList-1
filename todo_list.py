from tkinter import * 
import csv
from playsound import playsound # pip install playsound

databasePath = 'ToDoList-1/required files/databasecsv.csv'
buttonSoundPath = 'ToDoList-1/required files/Instant Sound Buttons 180.mp3'
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
    playsound(buttonSoundPath)

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

def removeTask(taskId):
    with open(databasePath, 'r', newline='') as file:
        csvFileReader = csv.reader(file)
        data = list(csvFileReader)
        for i in range(len(data)):
            if data[i][0] == taskId:
                data.pop(i)
                break
    # Write the modified data back to the CSV file
    with open(databasePath, 'w', newline='') as file:
        csvFileWriter = csv.writer(file)
        csvFileWriter.writerows(data)


# FRONT END

windowGeometery = '400x400'
windowsResizeable = True

def ViewScreen():
    file = open(databasePath, 'r')
    csvFileReader = csv.reader(file)
    v = Tk()
    v.title('View Tasks')
    v.geometry('600x600')
    v.resizable(windowsResizeable, windowsResizeable)

    scrollbar = Scrollbar(v)
    scrollbar.pack( side = RIGHT, fill = Y )
    mylist = Listbox(v, yscrollcommand = scrollbar.set,width=100)

    for line in csvFileReader:
        mylist.insert(END, f"Task Id. {line[0]} : {line[3]} : {line[1]} : {line[2]}")
    mylist.pack()
    scrollbar.config( command = mylist.yview )

    # Back Button
    Button(v, text="Back",width=10, command=lambda:[button_click_sound(),v.destroy(), mainScreen()]).pack()


    v.mainloop()
    file.close()

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
    
    Label(r, text="Task Id to Remove : ").grid(row=0,column=0)
    e1 = Entry(r)
    e1.grid(row=0,column=1)

    Button(r, text="Remove",width=10, command=lambda:[
        button_click_sound(),
        removeTask(e1.get()),
        e1.delete(0,END)
        ]).grid(row=1,column=1)

    Button(r, text="Back",width=10, command=lambda:[button_click_sound(),r.destroy(), mainScreen()]).grid(row=2,column=1)

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

