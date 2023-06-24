scores=[["Harvey","ron",56],
        ["Jones","alan",85],
        ["Lansbury","christine",68],
        ["Mills","David",72]]
typeOfSort= input ("do you want to sort by last name, first name or score?  ")
if typeOfSort == "last name":
    typeOfSortNumber=(0)
elif typeOfSort == "first name":
    typeOfSortNumber=(1)
elif typeOfSort == "score":
    typeOfSortNumber=(2)
ascendingOrDescending = input ("do you want to give the results ascending or descending? ")
scoresAscending=sorted(scores, key=lambda x:x [typeOfSortNumber])
scoresDecending = sorted(scores, key=lambda x:x[typeOfSortNumber],reverse = True)
if ascendingOrDescending == ("ascending"):
    
    for  n in range (len (scores)):
        print(scoresAscending[n])
elif  ascendingOrDescending == ("descending"):
    
    for  n in range (len (scores)):
        print(scoresDecending[n])
