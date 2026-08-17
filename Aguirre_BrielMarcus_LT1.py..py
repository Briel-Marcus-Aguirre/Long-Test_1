#Aguirre_BrielMarcus_LT1.py.
Total_Books = int(input("What are the total No. of Books? "))
#Asks how many notebookes there are
Books_per_Box = int(input("How many books fit in 1 box? "))
#Asksn how many notebooks fit in one box
Total_Box = Total_Books // Books_per_Box 
#Finds Total Number of Filled boxs
Left_Over = Total_Books % Books_per_Box
#Finds how many left over notebooks go into loose packs
if Total_Box == 0:
    print(f"There will be 0 Full box but there is {Left_Over} books in a loose pack.")
#shows how many left over books go into loose pack if there is no filled box
else:
    print(f"There will be {Total_Box} filled boxes and {Left_Over} loose packs.")
    #shows how many filled boxes with loose packs