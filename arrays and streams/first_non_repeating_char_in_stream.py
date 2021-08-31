
MAX_CHAR = 256
 
def findFirstNonRepeating():

    inDLL = [] * MAX_CHAR
    repeated = [False] * MAX_CHAR
    stream = "geekforgeekandgeeksandquizfor"
    for i in range(len(stream)):
        x = stream[i]
        if not repeated[ord(x)]:
            if not x in inDLL:
                inDLL.append(x)
            else:
                inDLL.remove(x)
                repeated[ord(x)] = True
 
        if len(inDLL) != 0:
            print ("First non-repeating character so far is ")
            print (str(inDLL[0]))
 
# Driver program
findFirstNonRepeating()