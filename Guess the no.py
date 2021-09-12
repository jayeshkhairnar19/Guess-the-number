i=12
count=0
print('WELCOME TO THE GAME')
print('Note The number is in between 1 and 20')
print('You have only 9 chances to guess the number')
while True:

    n=int(input('Enter a number:'))
    count+=1
    print('NO OF ATTEMPTS',count)
    
    if(count==9):
        print('You have reached your limits')
        if(n==i):
            print('Your guess is right and YOU ARE THE WINNER!')
            
        break
    if(n==i):
        print('Your guess is right and YOU ARE THE WINNER!')
        break
        
    elif(n<i):
        print('Please increase your number')
    elif(n>i):
        print('Please decrease your number')
print('Thanks for playing our game!')        
        
    
