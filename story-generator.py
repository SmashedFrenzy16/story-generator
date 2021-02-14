loop = 1

while (loop < 10):

    # All the questions that the program asks the user
    noun = input("Choose your noun: ")
    p_noun = input("Choose your plural noun: ")
    noun2 = input("Choose your noun: ")
    place = input("Name your place: ")
    adjective = input("Choose your adjective (Describing word): ")
    noun3 = input("Choose your noun: ")

    # Displays the story based on the users input
    print ("------------------------------------------")
    print ("Once you met a",noun,"- headed", noun)
    print ("Which ate a", noun2,",")
    print ("You gave him to",p_noun,"in",place)
    print ("Because the weather was always",adjective,".")
    print ()
    print ("You may think that is this the place for a",noun3,",")
    print ("Well it really is.")
    print ("------------------------------------------")

    # Loop back to "loop = 1"
    loop = loop + 1
