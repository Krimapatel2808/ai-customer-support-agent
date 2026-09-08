from src.services.agent import answer_question


def main():
    question = input("Customer: ")

    answer = answer_question(question)

    print("\nAssistant:", answer)


if __name__ == "__main__":
    main()