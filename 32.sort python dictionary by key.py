def dictionairy():
    # Declare hash function
    key_value ={}

    # Initializing value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print ("Task 1:-\n")
    print ("Keys are")

    # iterkeys() returns an iterator over the
    # dictionary’s keys.
    for i in sorted (key_value.keys()) :
        print(i, end = " ")

def main():
    # function calling
    dictionairy()

# Main function calling
if __name__=="__main__":
    main()
print("\n")
# function calling
def dictionairy():

    # Declaring the hash function
    key_value ={}

    # Initialize value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323

    print ("Task 2:-\nKeys and Values sorted in",
           "alphabetical order by the key  ")

    # sorted(key_value) returns an iterator over the
    # Dictionary’s value sorted in keys.
    for i in sorted (key_value) :
        print ((i, key_value[i]), end =" ")

def main():
    # function calling
    dictionairy()

# main function calling
if __name__=="__main__":
    main()

print("\n")
# Function calling
def dictionairy():

    # Declaring hash function
    key_value ={}

    # Initializing the value
    key_value[2] = 56
    key_value[1] = 2
    key_value[5] = 12
    key_value[4] = 24
    key_value[6] = 18
    key_value[3] = 323


    print ("Task 3:-\nKeys and Values sorted",
           "in alphabetical order by the value")

    # Note that it will sort in lexicographical order
    # For mathematical way, change it to float
    print(sorted(key_value.items(), key =
    lambda kv:(kv[1], kv[0])))

def main():
    # function calling
    dictionairy()

# main function calling
if __name__=="__main__":
    main()
