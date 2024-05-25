import psycopg2


connection = psycopg2.connect(
    dbname="game",
    user="postgres",
    password="Qwerty2109",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()

cursor.execute("SELECT uzb, eng FROM unit6_10;")
rows = cursor.fetchall()


cursor.close()
connection.close()


def func2():
    from random import sample
    words = dict(rows)

    count = 1
    grade = 0
    mistake = 0
    mistakes = {}

    while True:
        text = "Return to Units enter-> 0"
        x = text.center(50)
        print(x)
        try:
            run = int(input("1. 10 tests\n"
                            "---------------\n"
                            "2. 20 tests\n"
                            "---------------\n"
                            "3. 30 tests\n"
                            "---------------\n"
                            "-> "))
            result = sample(list(words.items()), k=run*10)
            if run == 0:
                return 0

            for i in result:
                respond = input(f"{count}.{i[0].capitalize()} - ").lower()
                if respond == '0':
                    break
                if respond == i[1]:
                    grade += 1
                    count += 1
                elif respond != i[1]:
                    if respond == "":
                        mistake += 1
                        respond = 'Null'
                        mistakes.update({f"{count}.Yours-{respond.capitalize()}": f"Correct-{i[1].capitalize()}"})
                        count += 1
                    else:
                        mistake += 1
                        mistakes.update({f"{count}.Yours-{respond.capitalize()}": f"Correct-{i[1].capitalize()}"})
                        count += 1
                if mistake > 4:
                    break

            print("------------------------------")
            print(f"Dear Gamer your grade: {grade} ball\n"
                  f"------------------------------")

            if mistakes:
                text = "MISTAKES"
                x = text.center(25)
                print(x)
                for k, v in mistakes.items():
                    print(f"{k} : {v}")
                print("------------------------------")
            play = int(input("Will you continue?\nYes=1|No=0: "))
            print("------------------------------")
            if play == 0:
                break
            elif play == 1:
                grade = 0
                mistake = 0
                count = 1
                mistakes.clear()
            else:
                print("------------------------------\n"
                      "Enter a number less than 4!\n"
                      "------------------------------\n")
                return func2()
        except ValueError:
            print("------------------------------\n"
                  "Enter only a number!\n"
                  "------------------------------\n")
            return func2()