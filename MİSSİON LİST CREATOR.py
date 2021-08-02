#---------------Modules, List and Title---------------# 
import os
import time
print ("Welcome to the mission list creating program.")
print("-"*70)
missions= []

#--------------------Misssion List----------------------# 	 
while True:
    print("Your Mission List: ")
    if len( missions)== 0:
	    print("At this moment,  your mission list is empty. İf you want you can add missions to this list.")
	    print("•"*70)
	    
    else:
	    counter=1
	    for i  in missions:
	        print(counter, ")", i)
	        counter+=1
	    print("•"*70)
	
#-----------------Mission List Choices----------------#    
    choice= input("For add a new mission to mission list, type 'A'. For remove a misson from mission list, type 'R'. For clear all missions from list, type 'C'. İf you want leave from app,  write anything : ")
    if choice== "A" or choice== "a":
        print("-"*70)
        addMission= input("Please type here mission you want add: ")
        missions.append(addMission)
        print("-"*70)
        print("The task you typed has been added to the list.")
        time.sleep(3)
        os.system("clear")
	
		  
    elif choice== "R" and len(missions)== 0:		
       print("-"*70)
       print("The mission list already empty. So you can't remove a mission from empty list.")
       print("-"*70)
       time.sleep(3)
       os.system("clear")
       
       
    elif choice== "R" or choice== "r":
      while True:
          try:
              removeMission=int( input("Please type here mission's number you want removed:  "))
              missions.pop(removeMission-1)  
              break
          except ValueError:
              print("-"*70)
              print("You can only write numbers to here. Please don't write anything else to here. Try again")
              print("-"*70)
          except IndexError:    
              print("-"*70)          
              print("Do not write any numbers other than those in the list.Try again.")
              print("-"*70)      
      print("-"*70)
      print("The task on the number you write has been removed.")
      time.sleep(3)
      os.system("clear")
      
    elif  choice== "C" or "c":
           missions.clear()
           print("-"*70)
           print("All missions cleared from list.")
           time.sleep(3)
           os.system("clear")
		  
		  
    else:
          print ("-"*70)
          print("You left from app.")
          exit()
          
#----------------------------------------------------------# 