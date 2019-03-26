class Marriage:

    def __init__(self, dulhan_name="", dulha_name="", marrige_budget="", marrige_of_address="", sound_system=""):
        self.dulhan_name = dulhan_name
        self.dulha_name = dulha_name
        self.marrige_budget = marrige_budget
        self.marrige_of_address = marrige_of_address
        self.sound_system = sound_system

        s = open("marriage.txt", "a+")

        s.write("\nDulhan name: {0}\nDulha name: {1}\nMarrige_budget : {2}\n"
                "Address : {3}\nSound_System : {4}".
                format(self.dulhan_name, self.dulha_name, self.marrige_budget, self.marrige_of_address,
                       self.sound_system))
        s.close()

class Angegement:
    def __init__(self, Dulhan_Name = " ", Dulha_Name=" ", Angegement_Budget = " ", address_of_Angegement=" "):
        self.Dulhan_Name = Dulhan_Name
        self.Dulha_Name = Dulha_Name
        self.Angegement_Budget = Angegement_Budget
        self.address_of_Angegement = address_of_Angegement

        s = open("Angagement.txt", "a+")

        s.write("\nDulhan name: {0}\nDulha name: {1}\nAngegement_badget : {2}\n"
                "Address : {3}".
                format(self.Dulhan_Name, self.Dulha_Name, self.Angegement_Budget, self.address_of_Angegement,
                       ))
        s.close()

class Party:
    def __init__(self,NameOfOrganiser = " " ,cotsume = " ", AddressOfParty = " " ,  ListOfGuest = " ",Budgets = " "):
        self.NameOfOrganiser = NameOfOrganiser
        self.cotsume = cotsume
        self.AddressOfParty = AddressOfParty
        self.ListOfGuest = ListOfGuest
        self.Budgets = Budgets

        party = open("partys.txt","a+")
        party.write("\nNameOfOrganiser : {0}\ncotsume : {1}\nAddress : {2}\nListOfGuest : {3}\nBudgets : {4} "
                    .format(self.NameOfOrganiser , self.cotsume ,self.AddressOfParty, self.ListOfGuest ,self.Budgets   ))
        party.close()

def Display():
    f = open("marriage.txt", "r")
    print(f.read())
    f.close()

    angegement = open("Angagement.txt", "r")
    print(angegement.read())
    angegement.close()

    parties = open("partys.txt" ,"r")
    print(parties.read())
    parties.close()

while True:
    print("1.Marrige_management\n2.Angagement_management\n3.Partys\n4.Exit")
    login = int(input("Enter your choice : "))

    if login == 1:
        print("\n1.Add_record\n2.Search_record\n3.Food_Item\n4.Display_Record")
        choice = int(input("ENTER YOUR CHOICE : "))

        if choice == 1:
            Dulhan_name = input("Enter your Dulhan`s name : ")
            Dulha_name = input("Enter your Dulha`s name : ")
            Budget = int(input("Enter budget : "))
            Address = input("Enter address : ")
            sound_system = input("Enter name of sound system : ")
            mrg1 = Marriage(Dulhan_name, Dulha_name, str(Budget), Address, sound_system)

        if choice == 2:

            SE = input("please enter to search : ")
            search_file = open("marriage.txt", "r")
            check_file = search_file.readlines()
            search_file.close()

            for line in check_file:
                try:
                    if line.split()[2] == SE:
                        print(" Found ")
                    else:
                        continue
                except IndexError:
                    pass

        if choice == 3:
            print("\n1.gujrati food\n2.panjabi food\n3.chinese food\n4.japaneas food")
            CHOICE = int(input("Enter your choice : "))

            if CHOICE == 1:
                Gujratifood = input("Enter gujrati item :")
                A = open("marriage.txt", "a")
                A.write("\nGujrati Food : " + Gujratifood)
                A.close()

            elif CHOICE == 2:
                Panjabifood = input("Enter panjabi item :")
                B = open("marriage.txt", "a")
                B.write("\nPanjabi Food : " + Panjabifood)
                B.close()

            elif CHOICE == 3:
                Chinesefood = input("Enter Chinese item :")
                C = open("marriage.txt", "a")
                C.write("\nChinese Food : " + Chinesefood)
                C.close()

            elif CHOICE == 4:
                Japanesefood = input("Enter Japanese item :")
                D = open("marriage.txt", "a")
                D.write("\nJapanese Food : " + Japanesefood)
                D.close()

        if choice == 4:
            Display()

    if login == 2:
        print("\n1.Add_record\n2.Search_record\n3.Food_Item\n4.Display_Record")
        Ang = int(input("ENTER YOUR CHOICE : "))

        if Ang == 1:
            Dulhan = input("Enter your Dulhan`s name : ")
            Dulha = input("Enter your Dulha`s name : ")
            Angage_Budgets = int(input("Enter budget : "))
            Address = input("Enter address : ")
            Angege = Angegement(Dulhan, Dulha, str(Angage_Budgets), Address)

        if Ang == 2:

            SEARCH = input("please enter to search : ")
            search_file = open("Angagement.txt", "r")
            check_file = search_file.readlines()
            search_file.close()

            for line in check_file:
                try:
                    if line.split()[2] == SEARCH:
                        print(" Found ")
                    else:
                        continue
                except IndexError:
                    pass

        if Ang == 3:
            print("\n1.gujrati food\n2.panjabi food\n3.chinese food\n4.japaneas food")
            check = int(input("Enter your choice : "))

            if check == 1:
                GujratiFood = input("Enter gujrati item :")
                A = open("Angagement.txt", "a")
                A.write("\nGujrati Food : " + GujratiFood)
                A.close()

            elif check == 2:
                PanjabiFood = input("Enter panjabi item :")
                B = open("Angagement.txt", "a")
                B.write("\nPanjabi Food : " + PanjabiFood)
                B.close()

            elif check == 3:
                ChineseFood = input("Enter Chinese item :")
                C = open("Angagement.txt", "a")
                C.write("\nChinese Food : " + ChineseFood)
                C.close()

            elif check == 4:
                JapaneseFood = input("Enter Japanese item :")
                D = open("Angagement.txt", "a")
                D.write("\nJapanese Food : " + JapaneseFood)
                D.close()

        if Ang == 4:
            Display()


    if login == 3:
        print("\n1.TypesOfParty\n2.FoodService")
        p = int(input("Enter your choice : "))

        if  p == 1 :
            print("\n1.Culture party\n2.College party\n3.Birthday party")
            pa = int(input("Enter Your choice : "))

            if pa  == 1:
                name_Of_Organiser = input("Enter name Of the Organiser : ")
                Costume  = input("Enter types of Costume : ")
                Address = input("Enter the address of the party : ")
                List_Of_Guest = input("Enter number of guest in party :")
                Party_Budget = int(input("Enter party budget : "))
                par1 = Party(name_Of_Organiser,Costume,Address,List_Of_Guest,Party_Budget)

            if pa == 2:
                Name_of_Organiser = input("Enter name Of the Organiser : ")
                CostumeOfStudent = input("Enter types of Costume : ")
                AddressOfParty = input("Enter the address of the party : ")
                List_Of_Student = input("Enter number of guest in party :")
                Party_budget = int(input("Enter party budget : "))
                par2 = Party(Name_of_Organiser, CostumeOfStudent , AddressOfParty, List_Of_Student, Party_budget)

            if pa == 3 :
                Name_Of_organiser = input("Enter name Of the Organiser : ")
                Costumes = input("Enter types of Costume : ")
                Addrese = input("Enter the address of the party : ")
                ListGuests = input("Enter number of guest in party :")
                Party_Budgets = int(input("Enter party budget : "))
                par3 = Party(Name_Of_organiser, Costumes,  Addrese,ListGuests, Party_Budgets)


        if p == 2:
            print("\n1.gujrati food\n2.panjabi food\n3.chinese food\n4.japaneas food")
            food = int(input("Enter your choice : "))

            if food == 1:
                Gujrati_Food = input("Enter gujrati item :")
                guj= open("partys.txt", "a")
                guj.write("\nGujrati Food : " + Gujrati_Food)
                guj.close()

            elif food == 2:
                Panjabi_Food = input("Enter panjabi item :")
                pan = open("partys.txt", "a")
                pan.write("\nPanjabi Food : " + Panjabi_Food)
                pan.close()

            elif check == 3:
                Chinese_Food = input("Enter Chinese item :")
                Chin = open("partys.txt", "a")
                Chin.write("\nChinese Food : " + Chinese_Food)
                Chin.close()

            elif food == 4:
                Japanese_Food = input("Enter Japanese item :")
                japa = open("partys.txt", "a")
                japa.write("\nJapanese Food : " + Japanese_Food)
                japa.close()

    if login == 4:
        exit()





