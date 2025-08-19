import json
import random
import os

file_path = "package.json"

global Times_Answered_questions
Times_Answered_questions = 1
global Number_Of_Failed_Times
Number_Of_Failed_Times = 0


# Otwieramy i wczytujemy plik
with open(file_path, "r", encoding="utf-8") as f: #otwierany pliku z odpowiednimi przywilejami i formacie
    questions = json.load(f)



#Okresl jaka chcesz powtarzalnosc pytania
print("Would you like to continue previous session? (y/n)")
answer = input()
if answer == "n":
    print("How many times would you like each question to be repeated?")
    NumberOfTimes = int(input())
    with open("package.json", "r", encoding="utf-8") as f:
        questions = json.load(f)
    for q in questions:
        q["occurrences"] = NumberOfTimes  # Adding occurrences field
    with open("package.json", "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=0)
    print("Added value 'occurences' i the json file:", NumberOfTimes)
    NumberOfTimes = int(NumberOfTimes)

elif answer == "y":
    print("You're continuing previous session now. Value occurrences are the same")

else:
    print("unknown, please try again - y or n")
    exit()


#function to determine how many questions are in the json file
global Total_NumberOfQuestions
Total_NumberOfQuestions = len(questions)
print("Number of questions:", Total_NumberOfQuestions)

#Funkcja pokaz progres bar
def Show_progress_bar():
    Total_NumberOfQuestions
    Mastered_Questions = sum(1 for question in questions if question["occurrences"] == 0)
    percent = int((Mastered_Questions / Total_NumberOfQuestions) * 100)
    bar_length = 50  # Długość paska w znakach
    filled_length = int(bar_length * Mastered_Questions // Total_NumberOfQuestions)
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    print(f"\nProgress: |{bar}| {percent}% ({Mastered_Questions}/{Total_NumberOfQuestions} mastered)")

#Funkkcja Win to lose ratio
def win_lose_ratio():
    global NumberOfCurrentTry
    percent = int(abs(((Number_Of_Failed_Times / Times_Answered_questions) * 100)-100))
    #print("Win to lose ratio: {percent}%".format(percent=percent))
    Bar_Length = 50
    filled_length = int(Bar_Length * percent // 100)
    bar = '█' * filled_length + '-' * (Bar_Length - filled_length)
    print("Win to lose ratio:", f"|{bar}| {percent}%")
    if NumberOfCurrentTry < 1:
        {
            percent == 0
        }








#funkcja random number generator
def Generate_Random_Number():
    #global Random_number
    #Random_number= random.randint(0, Total_NumberOfQuestions)
    #print("\n\n""------------------------------------------------------------------------------------------------","\n", "So for now Random Quesion is number :",Random_number,)
    #return Random_number
    global Random_number
    available_indices = [i for i, q in enumerate(questions) if q["occurrences"] > 0]

    if not available_indices:
        print("Brak pytań z occurrences > 0. Koniec quizu.")
        exit()  # lub break, jeśli używasz pętli w funkcji

    Random_number = random.choice(available_indices)
    print("\n\n" + "-" * 100)
    return Random_number

#funckja wprowadz poprawna odpowiedz
def Enter_Correct_Answer():
    global UserAnswer
    UserAnswer = input("Enter your answer:""\n").upper()
    print("You've selected:", UserAnswer)# Wprowadz poprawna odpowiedz
    return UserAnswer

#Funkcja przelec po wszystkich pytaniach w petli:
def Iterate_Through_Questions():
    print(questions[Random_number]["question"])
    for key, value in questions[Random_number]["options"].items():
        print(f" {key}. {value}")

#Funkcja wyprowadz dobra odpowiedz
def Return_Correct_Answer():
    global CorrectAnswer
    global Times_Answered_questions
    global Number_Of_Failed_Times
    CorrectAnswer = questions[Random_number]["answer"]
    if questions[Random_number]["occurrences"] > 0:
        if CorrectAnswer == UserAnswer:
            print("You selected Correct Answer!")
            questions[Random_number]["occurrences"] -=1
            Times_Answered_questions += 1 #This is needed for win/losse ratio
            print("So this question will appear times:", questions[Random_number]["occurrences"])
            return CorrectAnswer
        else:
            print("\n","You've selected incorrect Answer -", " Correct Answer is:", CorrectAnswer)
            questions[Random_number]["occurrences"] += 1
            Times_Answered_questions += 1 #This is needed for win/losse ratio
            Number_Of_Failed_Times += 1 #This is needed for win/losse ratio
            print("So this question will appear times:",questions[Random_number]["occurrences"])
            #Zapisz zmiany do pliku json
            with open("package.json", "w", encoding="utf-8") as f:
                json.dump(questions, f, ensure_ascii=False, indent=2)
            return CorrectAnswer
    else:
        pass

#Funkcja enter aby kontynuować
def press_enter_to_continue():
    input("\nPress enter to continue...")

#funkcja wyczysc terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 30)

#Funkcja zapisz pytania do osobnej bazy
def save_question_to_separate_file(question):
    separate_file = "difficult_questions.json"

    # Sprawdź, czy plik istnieje
    if os.path.exists(separate_file):
        with open(separate_file, "r", encoding="utf-8") as f:
            saved_questions = json.load(f)
    else:
        saved_questions = []

    # Dodaj pytanie tylko jeśli go tam jeszcze nie ma
    if question not in saved_questions:
        saved_questions.append(question)
        with open(separate_file, "w", encoding="utf-8") as f:
            json.dump(saved_questions, f, ensure_ascii=False, indent=2)
        print("✅ Pytanie zapisane do osobnej bazy.")
    else:
        print("ℹ️ To pytanie już znajduje się w osobnej bazie.")

#Funkcja zmieniaj wartosc wystapienia danego pytania
#Funckja zlicz ilosc wystapien danego pytania
#Funkcja sprawdz czy odpowiedz jest dobra
#funkcja wyrzucanie poprawnej odpowiedzi z pytania
#funkcja sprawdzanie poprawnej odpowiedzi



#Funkcja printujaca pytania randomowo - z petla do x wystapienia
NumberOfTries = 3000
global NumberOfCurrentTry
NumberOfCurrentTry = 0
QuestionOcurrence = 2
while NumberOfCurrentTry < NumberOfTries:
    NumberOfCurrentTry = NumberOfCurrentTry + 1
    Random_number = Generate_Random_Number() #I have to do that because the variable is within the function and variable is local
    print("Question number:", Random_number)
    Show_progress_bar()
    win_lose_ratio()
    #print(questions[Random_number]["question"], "\n A. ",questions[Random_number]["options"]["A"], "\n B. ",questions[Random_number]["options"]["B"], "\n C. ",questions[Random_number]["options"]["C"], "\n D. ",questions[Random_number]["options"]["D"])
    Iterate_Through_Questions()
    Enter_Correct_Answer()
    print("Correct answer is:", Return_Correct_Answer())
    print("Press 's' to save the question into a separate file or press 'Enter' to continue...")
    user_input = input().lower()
    if user_input == "s":
        save_question_to_separate_file(questions[Random_number])
    clear_screen()



