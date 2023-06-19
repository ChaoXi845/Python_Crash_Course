class AnonymousSurvey:

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, new_respones):
        self.responses.append(new_respones)

    def show_results(self):
        print("Survey results: ")
        for response in self.responses:
            print(f"- {response}")