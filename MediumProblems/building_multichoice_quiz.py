class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


question_prompts = [
    "what colour are apples?\n(a) red/green\n(b) yellow\n(c) red\n",
    "what colour are banana?\n(a) red/green\n(b) yellow\n(c) red\n",
    "what colour are strawberry?\n(a) red/green\n(b) yellow\n(c) red\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "c")
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 4
        else:
            score += -1
    print("You got " + str(score) + "/" + str(len(questions) * 4) + " marks.")


run_test(questions)
