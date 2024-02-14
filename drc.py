import os

def mainmenu():
    while True:
        os.system('cls')
        print("Welcome to Tyler's Driver Rating Calculator")
        print("Python Version 0.1")
        print()
        print(f"Current data pool: {rostername}") #formatted string literals, Python 3.6 or later
        print("To begin calculations, enter 'Calc'")
        print("To load a data pool, type 'Load'")
        print("To save the current data pool, type 'Save'")
        print("To save all current data, type 'Full save'")
        print("To enter a new data pool, type 'Edit'")
        print("To edit calculation settings, type 'Settings'")
        print("To view all current data, type 'View'")
        print("To view the changelog, type 'Log'")
        print("To quit, type 'Exit'")
        userinput=input(">").lower()
        
        if userinput=='exit':
            break
        elif userinput=='log':
            changelog()
        elif userinput=='view':
            viewdata()
        else:
            print("Invalid choice.")
            input()

def viewdata():
    os.system('cls')
    print(f"Roster name: {rostername}")
    print(f"Best championship finish: {champfinbest}")
    print(f"Worst championship finish: {champfinworst}")
    print(f"Max races: {maxrace}")
    print(f"Min races: {minrace}")
    print(f"Max wins: {maxwin}")
    print(f"Min wins: {minwin}")
    print(f"Max top fives: {maxtopfive}")
    print(f"Min top fives: {mintopfive}")
    print(f"Max top tens: {maxtopten}")
    print(f"Min top tens: {mintopten}")
    print(f"Max poles: {maxpole}")
    print(f"Min poles: {minpole}")
    print(f"Max laps ran: {maxlap}")
    print(f"Min laps ran: {minlap}")
    print(f"Max laps led: {maxled}")
    print(f"Min laps led: {minled}")
    print(f"Best average start: {beststart}")
    print(f"Worst average start: {worststart}")
    print(f"Best average finish: {bestfin}")
    print(f"Worst average finish: {worstfin}")
    print(f"Max RAF: {maxraf}")
    print(f"Min RAF: {minraf}")
    print(f"Max LLF: {maxllf}")
    print(f"Min LLF: {minllf}")
    print(f"Win weight: {winweight*100}%")
    print(f"Top five weight: {topfiveweight*100}%")
    print(f"Top ten weight: {toptenweight*100}%")
    print(f"Pole weight: {poleweight*100}%")
    print(f"Laps ran weight: {lapweight*100}%")
    print(f"Laps led weight: {ledweight*100}%")
    print(f"Average start weight: {startweight*100}%")
    print(f"Average finish weight: {finweight*100}%")
    print(f"RAF weight: {rafweight*100}%")
    print(f"LLF weight: {llfweight*100}%")
    print(f"Normalization minimum: {normmin}%")
    print(f"Normalization maximum: {normmax}%")
    input()

def changelog():
    os.system('cls')
    print("v0.1 02/xx/2024")
    print("-initial python build, port from basic to make a version i might eventually be willing to share")
    input()
    #mainmenu() is not needed, because this is not in a while true loop
    #use break to exit a while true loop to return to main menu

if __name__=="__main__":
    rostername="2009 NASCAR Cup Series"
    champfinbest,champfinworst=1,67
    maxrace,minrace=36,1
    maxwin,minwin=7,0
    maxtopfive,mintopfive=16,0
    maxtopten,mintopten=25,0
    maxpole,minpole=7,0
    maxlap,minlap=10468,8
    maxled,minled=2238,0
    beststart,worststart=8.3,43
    bestfin,worstfin=10.2,43
    maxraf,minraf=36,0
    maxllf,minllf=31,0
    winweight,topfiveweight,toptenweight,poleweight,lapweight,ledweight,startweight,finweight,rafweight,llfweight=.25,.16,.11,.06,.04,.09,.05,.12,.04,.08
    normmin,normmax=60,100
    mainmenu()
