import psycopg2


connection = psycopg2.connect(
    dbname="game",
    user="postgres",
    password="Qwerty2109",
    host="localhost",
    port="5432"
)
cursor = connection.cursor()

cursor.execute("SELECT v1, v2 FROM irregular_verbs;")
rows = cursor.fetchall()


cursor.close()
connection.close()


def verbs1():
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
        run = int(input("1. 10 tests\n"
                        "---------------\n"
                        "2. 20 tests\n"
                        "---------------\n"
                        "--> "))
        try:
            if run <= 2:
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
                print(f"{grade} ball\n"
                      f"------------------------------")
                if mistakes:
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
                print("Enter a number less than 3")
        except ValueError:
            print("Enter only a number!")
            return verbs1()