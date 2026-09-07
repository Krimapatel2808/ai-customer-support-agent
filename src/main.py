from services.knowledge_base import load_knowledge_base


def main():
    knowledge = load_knowledge_base("data/faq.txt")

    print("AI Customer Support Agent is starting...")
    print("\nKnowledge base loaded successfully.")
    print(f"Knowledge base size: {len(knowledge)} characters")


if __name__ == "__main__":
    main()