from verbs import first_condition, second_condition


def choice_verbs():
    text = "Return to Main Menu enter-> 0"
    x = text.center(50)
    print(x)
    print("--------------------\n"
          "1.Past Simple\n"
          "--------------------\n"
          "2.Past Participle\n"
          "--------------------")
    try:
        selection = int(input("--> "))
        print("------------------------------")
        if selection < 3:
            if selection == 0:
                return 7
            if selection == 1:
                first_condition.verbs1()
            if selection == 2:
                second_condition.verbs2()
        else:
            print("------------------------------\n"
                  "Enter a number less than 3!\n"
                  "------------------------------\n")
            return choice_verbs()
    except ValueError:
        print("------------------------------\n"
              "Enter only a number!\n"
              "------------------------------\n")
        return choice_verbs()