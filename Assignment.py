while True:
    dailylist = input("Select and Write One: Pray / Read / Exercise / Eat / Everything: ")
    if dailylist == "Pray":
        print("Masallah")
        break
    if dailylist == "Read":
        print("Great!!")
        break
    if dailylist == "Exercise":
        print("Very Good")
        break
    if dailylist == "Eat":
        print("Helthy")
        break
    if dailylist == "Everything":
        print("You are the Best...Hope you Will Shine In your Life...Best Wish For You.")
        break

Daily_list = ['Read', 'Add', 'Update', 'Delete']
while True:
    Dailylist = input("Write one:")
    if Dailylist == "Read":
        print("This is Your List:", Daily_list)
    elif Dailylist == "Add":
        Daily_list.append(input("Write what you want to Add:"))
        print("This is Your New List:", Daily_list)
    elif Dailylist == "Delete":
        Put_the_item = (input("Write what you want to Delete:"))
        if Put_the_item in Daily_list:
            Daily_list.remove(Put_the_item)
        else:
            print("Not Match Item")
        print("This is Your New List:", Daily_list)
    elif Dailylist == "Update":
        up_wrong = input("Write Your Wrong Text")
        up_right = input("write your right text")
        if up_wrong in Daily_list:
            wr = Daily_list.index(up_wrong)
            Daily_list[wr]= up_right
        else:
            print("Not Matched")
        print("This is your update list:" , Daily_list)

