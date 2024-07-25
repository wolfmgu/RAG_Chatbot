import random

# Sample database of documents from different HR topics
documents = {
    "Insurance": [
        "Our company offers comprehensive health insurance plans including medical, dental, and vision coverage.",
        "Employees can choose from a variety of insurance plans that best suit their needs.",
        "Life insurance and disability insurance are also available to ensure financial security."
    ],
    "Paid Time Off": [
        "Employees are entitled to paid time off (PTO) which includes vacation days, sick leave, and personal days.",
        "Our PTO policy allows for flexible scheduling to accommodate work-life balance.",
        "Unused PTO can be carried over to the next year, subject to company policy."
    ],
    "Professional Development": [
        "We offer a range of professional development opportunities, including training sessions, workshops, and online courses.",
        "Employees are encouraged to pursue certifications and advanced degrees to further their careers.",
        "Mentorship programs are available to help employees develop leadership skills."
    ],
    "Retirement Benefits": [
        "The company offers a 401(k) retirement savings plan with employer matching contributions.",
        "Employees can choose from a variety of investment options to suit their retirement goals.",
        "We provide financial planning resources to help employees prepare for retirement."
    ]
}

# Function to retrieve relevant document snippets
def retrieve_documents(query):
    keywords = query.lower().split()
    relevant_docs = []
    
    # First, check for an explicit mention of a department/topic
    for topic in documents:
        if topic.lower() in query.lower():
            relevant_docs.extend(documents[topic])
            return relevant_docs
    
    # If no specific topic is mentioned, search across all topics
    for topic, docs in documents.items():
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
    print("Welcome to the Human Resources RAG Chatbot! Type 'exit' to end the conversation.")
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
