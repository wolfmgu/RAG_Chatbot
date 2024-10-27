import random
import difflib

# Sample database of documents from different HR topics
documents = {
    "Insurance": [
        "Our company offers comprehensive health insurance plans including medical, dental, and vision coverage.",
        "Employees are eligible for insurance after the first 30 days of service.",
        "Life insurance and disability insurance are also available."
    ],
    "Paid Time Off": [
        "Employees are entitled to 120 hours of paid time off (PTO) which includes vacation days, sick leave, and personal days.",
        "PTO should be arranged with your manager at least 30 days ahead of time.",
        "Unused PTO can be carried over to the next year, subject to company policy."
    ],
    "Professional Development": [
        "We offer a range of professional development opportunities, including training sessions, workshops, and online courses.",
        "Employees must complete 20 hours of professional development education each year.",
        "Mentorship programs are available to help employees develop leadership skills."
    ],
    "Retirement Benefits": [
        "The company offers a 401(k) retirement savings plan with employer matching contributions.",
        "Employees can choose from a variety of investment options after their first year of employment.",
        "We provide financial planning resources to help employees prepare for retirement."
    ],
    "Salary": [
        "Our company offers competitive salaries and performance-based bonuses.",
        "Employees are eligible for annual salary reviews and potential increases based on performance.",
        "Bonuses are awarded based on individual and company performance metrics."
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

# Function to find the best matching response based on user input
def find_best_match(query, documents):
    best_match = None
    highest_similarity = 0

    for doc in documents:
        similarity = difflib.SequenceMatcher(None, query, doc).ratio()
        if similarity > highest_similarity:
            highest_similarity = similarity
            best_match = doc

    return best_match

# Function to generate a response
def generate_response(query):
    relevant_docs = retrieve_documents(query)
    if relevant_docs[0] == "No relevant documents found.":
        return relevant_docs[0]
    else:
        return find_best_match(query, relevant_docs)

# Chatbot function to simulate RAG
def chatbot():
    print("Welcome to your Human Resources Portal. Please ask a question about your insurance, paid time off, professional development, or retirement benefits. Type 'exit' to end the conversation.")
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
