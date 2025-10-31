print("*******WELCOME TO THE KBC QUIZ*******\n")
questions=[
["What is the name of India's first president?","Chintu","Narendra Modi","Pratibha patel","Dr Rajendra Prasa",4],
["What is the name of India's national animal?","Hen","tiger","Dog","Lion",2],
["Where is India's biggest slum area?","Delhi","Kolkata","Uttar Pradesh","Mumbai",4],
["What is the colore of sky?","Pink","Green","Yellow","Blue",4],
["Who is the current Prime Minister of India?", "Narendra Singh","Jawaharlal Nehru","Indira Gandhi","Narendra Modi",4]
]

levels=[1000,3000,5000,7000,10000]
i=0
for i in range(len(questions)):
    question=questions[i]  #gets the current question and assigns it to the variable question. 
    print(f"Question for Rs {levels[i]}") #question for Rs 1000,3000,5000,etc
    print(question[0])
    print(f"a.{question[1]}    b.{question[2]})")
    print(f"c.{question[3]}    d.{question[4]})")
    reply=int(input("Enter Your Option\n"))
    if (reply==question[5]):
       print("Correct Answer!!!")
    else:
       print("Wrong Answer!!!")
       break
print("\n*******Quiz is Finished*******")
