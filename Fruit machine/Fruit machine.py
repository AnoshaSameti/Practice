def fruit(reels, spins):
    rolled=[]
    fruits = {"Wild": 10, "Star": 9, "Bell": 8, "Shell": 7, "Seven": 6, "Cherry": 5, "Bar": 4, "King": 3, "Queen": 2, "Jack": 1}
    for i in range(3):
        rolled.append(reels[i][spins[i]])
    matched= len(set(sorted(rolled)))
    rol=sorted(rolled)
    if matched == 1:
        return(fruits[rolled[0]] *10)
    elif matched==2:
        if 'Wild' in rolled and rolled.count('Wild')==1:
            return(fruits[rolled[i]]*2)
        elif 'Wild' in rolled and rolled.count('Wild')==2:
            return(10)
        elif 'Wild' not in rolled:
            return(fruits[rol[1]])
    elif matched ==3:
        return(0)
    else:
        return('error')  