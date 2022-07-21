N = int(input()) # number of operations that you have to perform

lis = [] # list to store the numbers

for num in range(N):
    changes = input().split() # input the number
    match changes[0]:
        case 'append':
            for i in range(1, len(changes)): 
                lis.append(int(changes[i])) # append the numbers to the list
        case 'pop':
            try:
                lis.pop((changes[1])) # pop the number from the list
            except IndexError:
                print("You can't pop from an empty list!")  # if the list is empty
        case 'insert':
            lis.insert(int(changes[1]), int(changes[2])) # insert the number at the specified index
        case 'remove':
            try:
                lis.remove(int(changes[1])) # remove the number from the list
            except ValueError:
                print("This member is not in the list.") # if the number is not in the list
        case 'reverse':
            lis.reverse() # reverse the list
        case 'sort':
            lis.sort() # sort the list
        case 'print':
            print(lis) # print the list
