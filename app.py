import random

# Sample database of documents from different departments
documents = {
    "IT": [
        "The IT department is responsible for maintaining the company's computer systems.",
        "Our cybersecurity team ensures the protection of data from external threats.",
        "IT supports employees with technical issues and hardware management."
    ],
    "HR": [
        "The HR department handles employee relations, benefits, and recruitment.",
        "We ensure compliance with labor laws and company policies.",
        "HR conducts regular training sessions on workplace ethics and diversity."
    ],
    "Professional Development": [
        "Professional development programs help employees enhance their skills.",
        "We offer courses in leadership, communication, and time management.",
        "Employees are encouraged to attend workshops and seminars to further their careers."
    ],
    "Finance": [
        "The finance department manages the company's budgets and financial planning.",
        "We oversee payroll, billing, and financial reporting.",
        "Our team provides insights on cost reduction and revenue generation."
    ],
    "Marketing": [
        "The marketing team is responsible for brand management and advertising.",
        "We conduct market research to understand consumer preferences.",
        "Our department manages social media campaigns and promotional events."
    ]
}

# Function to retrieve relevant document snippets
def retrieve_documents(query):
    keywords = query.lower().split()
    relevant_docs = []
    for dept, docs in documents.items():
        for doc in docs:
            if any(keyword in doc.lower() for keyword in keywords):
                relevant_docs.append(doc)
    return relevant_docs if relevant_docs else ["No relevant documents found."]

# Function to generate a response
def generate_response(query):
    relevant_docs = retrieve_documents(query)
    if relevant_docs[0] == "No relevant documents found.":
        return relevant_docs[0]
    else:
        return random.choice(relevant_docs)

# Chatbot function to simulate RAG
def chatbot():
    print("Welcome to the Company RAG Chatbot! Type 'exit' to end the conversation.")
    while True:
        query = input("\nYou: ")
        if query.lower() == 'exit':
            print("Goodbye!")
            break
        response = generate_response(query)
        print("Bot:", response)

# Main function to run the chatbot
def main():
    chatbot()

# Run the chatbot
if __name__ == "__main__":
    main()
