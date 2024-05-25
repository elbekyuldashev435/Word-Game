from units import unit1_5, unit6_10, unit11_15, unit16_20, unit21_25, unit26_30


def choice_units():
    text = "Return to Main Menu enter-> 0"
    x = text.center(50)
    print(x)
    print("--------------------\n"
          "1.Unit 1-5\n"
          "--------------------\n"
          "2.Unit 6-10\n"
          "--------------------\n"
          "3.Unit 11-15\n"
          "--------------------\n"
          "4.Unit 16-20\n"
          "--------------------\n"
          "5.Unit 21-25\n"
          "--------------------\n"
          "6.Unit 26-30\n"
          "--------------------")
    try:
        selection = int(input("--> "))
        if selection < 7:
            if selection == 0:
                return 7
            if selection == 1:
                unit1_5.func1()
            if selection == 2:
                unit6_10.func2()
            if selection == 3:
                unit11_15.func3()
            if selection == 4:
                unit16_20.func4()
            if selection == 5:
                unit21_25.func5()
            if selection == 6:
                unit26_30.func6()
        else:
            print("------------------------------\n"
                  "Enter a number less than 7!\n"
                  "------------------------------\n")
            return choice_units()
    except ValueError:
        print("------------------------------\n"
              "Enter only a number!\n"
              "------------------------------\n")
        return choice_units()