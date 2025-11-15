from question import Question

question_prompts = [
    "1. Which data type is immutable in Python?\n(a) List\n(b) Dictionary\n(c) Tuple\n(d) Set\n\nYour answer: ",
    
    "2. What does the 'range(5)' function return?\n(a) [1,2,3,4,5]\n(b) [0,1,2,3,4]\n(c) [0,1,2,3,4,5]\n(d) None of the above\n\nYour answer: ",
    
    "3. Which keyword is used to handle exceptions?\n(a) catch\n(b) error\n(c) try\n(d) except\n\nYour answer: ",
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "d")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print(f"you got {str(score)}/{str(len(questions))} Correct")

run_test(questions)