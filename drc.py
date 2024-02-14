import os

def main_menu():
    while True:
        os.system('cls')
        print("Welcome to Tyler's Driver Rating Calculator")
        print("Python Version 0.1")
        print()
        print(f"Current data pool: {roster_name}") #formatted string literals, Python 3.6 or later
        print("To begin calculations, enter 'Calc'")
        print("To load a data pool, type 'Load'")
        print("To save the current data pool, type 'Save'")
        print("To save all current data, type 'Full save'")
        print("To enter a new data pool, type 'Edit'")
        print("To edit calculation settings, type 'Settings'")
        print("To view all current data, type 'View'")
        print("To view the changelog, type 'Log'")
        print("To quit, type 'Exit'")
        user_input=input(">").lower()
        
        if user_input=='exit':
            break
        elif user_input=='log':
            changelog()
        else:
            print("Invalid choice.")
            input()

def changelog():
    os.system('cls')
    print("v0.1 02/xx/2024")
    print("-initial python build, port from basic to make a version i might eventually be willing to share")
    input()
    #main_menu() is not needed, because this is not in a while true loop
    #use break to exit a while true loop to return to main menu

if __name__=="__main__":
    roster_name="2009 NASCAR Cup Series"
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
    main_menu()
