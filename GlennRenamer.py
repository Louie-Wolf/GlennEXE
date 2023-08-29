import sys, os, datetime

#version
version = 1.2
vdate = '23-08-2023'

# get path name
pathname = os.path.dirname(sys.argv[0])
fullpathname = os.path.abspath(pathname)

# define pathnames
finalDirectory = fullpathname + '\\!_Final'
draftDirectory = fullpathname + '\\1_Draft'
rawFootageVideosDirectory = fullpathname + '\\2_Raw-Footage\Videos'
projectFilesDirectory = fullpathname + '\\3_Project-Files'
musicDirectory = fullpathname + '\\4_Music'
graphicsDirectory = fullpathname + '\\5_Graphics'

#!_final:         YYYY-MM-DD_Project-Title_FINAL-CUT
#1_draft:         YYYY-MM-DD_Project-Title_RAW-CUT-V1,V2,etc...
#2_raw:           YYYY-MM-DD_Sony-A7S-iii / YYYY-MM-DD_Sony-A7-iv / YYYY-MM-DD_Sony-A7-iii / YYYY-MM-DD_other / YYYY-MM-DD_Drohne / YYYY-MM-DD_Audio 
#3_project files: YYYY-MM-DD_Project-Title
#4_music:         YYYY-MM-DD_Project-Title_Songtitle
#5_graphics:      YYYY-MM-DD_Project-Title_Filecontent

# loops
unconfirmedAnswer = True
invalidTodaysDateAnswer = True
invalidConfirmedDataAnswer = True
invalidDateAnswer = True

# date
year = 'wrong input'
month = 'wrong input'
day = 'wrong input'

# nameexception
nameExceptionList = ['Adobe Premiere Pro Auto-Save']

print(f'Welcome!\nKeyframe Glenn Renamer | Version: {version} from {vdate}\n')
print("Setting up Project...")

while(unconfirmedAnswer):
    while (invalidTodaysDateAnswer):
        print("Do you want to use todays date? (y/n)")
        answer = str(input().lower())

        if answer == 'y' or answer == 'yes':
            invalidTodaysDateAnswer = False
            # get date from datetime
            current_time = datetime.datetime.today()
            year = current_time.year
            month = current_time.month
            day = current_time.day

        elif answer == 'n'or 'no':

            invalidTodaysDateAnswer = False

            while (invalidDateAnswer):
                # get year from input
                print("Insert the year in YYYY format: (Ex. 2023)")
                year = input()
                if not year.isnumeric() or int(year) < 2000:  # check if input is numeric
                    print("Wrong Input! Please use a positive interger as input...")
                    continue

                # get month from input
                print("Insert the month in MM format: (Ex. 09 for september)")
                month = input()
                if not month.isnumeric() or int(month) < 1:  # check if input is numeric
                    print("Wrong Input! Please use a positive interger as input...")
                    continue

                # get day from input
                print("Insert the day in DD format: (Ex. 11)")
                day = input()
                if not day.isnumeric() or int(day) < 1:  # check if input is numeric
                    print("Wrong Input! Please use a positive interger as input...")
                    continue

                # break out of while loop
                invalidDateAnswer = False

        else:
            print("Wrong Input! Please enter: \"y\" for yes, or \"n\" for no...")
            continue

        # make sure format is YYYY-MM-DD
        if int(month) < 10:
            month = '0' + str(int(month))

        if int(day) < 10:
            day = '0' + str(int(day))

    # get project name from input
    print("Insert project title: (Ex. Winter-Tech-Days)")
    projectTitle = input()

    print(f'\n Date: {year}-{month}-{day} \n Title: {projectTitle} \n')
    print("Do you want to rename the files with this data? (y/n)")

    while(invalidConfirmedDataAnswer):
        renameFilesAnswer = str(input()).lower()
        if renameFilesAnswer == 'y' or renameFilesAnswer == 'yes':
            invalidConfirmedDataAnswer = False
            unconfirmedAnswer = False
            print("Input Confirmed! Renaming data...")
        elif renameFilesAnswer == 'n' or renameFilesAnswer == 'no':
            unconfirmedAnswer = True
            invalidTodaysDateAnswer = True
            invalidConfirmedDataAnswer = True
            invalidDateAnswer = True
            print("Restarting programm...")
            break
        else:
            print("Wrong Input! Please enter: \"y\" for yes, or \"n\" for no...")


#rename method for date, project title counted
def renameFilesDateTitle(year, month, day, title):
    for count, file in enumerate(os.listdir()):
        #check if exception name
        if file in nameExceptionList:
            continue

        newName = f'{year}-{month}-{day}_{title}-{file}'
        os.rename(file, newName)


#rename method for date
def renameFilesDate(year, month, day):
    for count, file in enumerate(os.listdir()):
        #check if exception name
        if file in nameExceptionList:
            continue
        
        newName = f'{year}-{month}-{day}_{file}'
        os.rename(file, newName)

# Change to own dir
os.chdir(finalDirectory)
renameFilesDateTitle(year, month, day, projectTitle)

os.chdir(draftDirectory)
renameFilesDateTitle(year, month, day, projectTitle)

os.chdir(rawFootageVideosDirectory)
renameFilesDate(year, month, day)

os.chdir(projectFilesDirectory)
renameFilesDateTitle(year, month, day, projectTitle)

os.chdir(musicDirectory)
renameFilesDateTitle(year, month, day, projectTitle)

os.chdir(graphicsDirectory)
renameFilesDateTitle(year, month, day, projectTitle)

print("Success!")
print("Press enter to close the program...")
a = input()
