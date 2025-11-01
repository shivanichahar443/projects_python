print("*******WELCOME TO THE KBC QUIZ*******\n")
questions=[
["What is the name of India's first president?","Chintu","Narendra Modi","Pratibha patel","Dr Rajendra Prasa",4],
["What is the name of India's national animal?","Hen","tiger","Dog","Lion",2],
["Where is India's biggest slum area?","Delhi","Kolkata","Uttar Pradesh","Mumbai",4],
["What is the colore of sky?","Pink","Green","Yellow","Blue",4],
["Who is the current Prime Minister of India?", "Narendra Singh","Jawaharlal Nehru","Indira Gandhi","Narendra Modi",4]
]     # multiple lists in a single list(questions) also added the correct answer's option in the end of each list 

levels=[1000,3000,5000,7000,10000] #prize money for each question
i=0#not really needed
for i in range(len(questions)):#loops in the list named questions
    question=questions[i]  #gets the current question and assigns it to the variable question. 
    print(f"Question for Rs {levels[i]}") #question for Rs 1000,3000,5000,etc
    print(question[0])
    print(f"a.{question[1]}    b.{question[2]})")#{question[1]}gives option 1 {question[2]}gives option 2 and same for 3 and 4 
    print(f"c.{question[3]}    d.{question[4]})")#basically 1,2,3,4 are the indexs of the options 
    reply=int(input("Enter Your Option\n"))#will take the user input  for the answer
    if (reply==question[5]): #question[5] basically he 5th index element stores the correct option number (1,2,3 or 4).
       print("Correct Answer!!!") #if both match then correct answer 
    else:
       print("Wrong Answer!!!")# did't match wrong answer 
       break#if wrong answer stop the game
print("\n*******Quiz is Finished*******")
