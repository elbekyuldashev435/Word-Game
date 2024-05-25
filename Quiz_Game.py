from essential import choice_units
from irregular_verbs import choice_verbs
from human_body import body


def choice_func():
    text = "To stop Enter-> 0"
    x = text.center(50)
    print(x)
    print(f"--------------------\n"
          f"1.Essential\n"
          "--------------------\n"
          f"2.Irregular verbs\n"
          "--------------------\n"
          f"3.Human body\n"
          "--------------------\n"
          f"4.Destination\n"
          "--------------------\n"
          f"5.Common words\n"
          "--------------------")
    try:
        selection = int(input("--> "))
        while True:
            if selection < 6:
                if selection == 0:
                    return 6
                if selection == 1:
                    a = choice_units()
                    if a == 7:
                        return choice_func()
                if selection == 2:
                    b = choice_verbs()
                    if b == 7:
                        return choice_func()
                if selection == 3:
                    c = body()
                    if c == 7:
                        return choice_func()
                if selection == 4:
                    print("--------------------------------------------------------\n"
                          "Sorry, no information yet. You can choose another topic.\n"
                          "--------------------------------------------------------")
                    return choice_func()
                if selection == 5:
                    print("--------------------------------------------------------\n"
                          "Sorry, no information yet. You can choose another topic.\n"
                          "--------------------------------------------------------")
                    return choice_func()
            else:
                print("-------------------------------\n"
                      "Enter a number less than 6!\n"
                      "-------------------------------\n")
                return choice_func()
    except ValueError:
        print("Enter only a number!")
        return choice_func()


choice_func()