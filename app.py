import random

# Sample database of documents
documents = [
    "The capital of France is Paris.",
    "The Great Wall of China is one of the Seven Wonders of the World.",
    "The Pacific Ocean is the largest ocean on Earth.",
    "Python is a popular programming language for data science and machine learning.",
    "The human body has 206 bones."
]

# Function to retrieve relevant document snippets
def retrieve_documents(query):
    # A very simple retrieval mechanism: return all documents containing any word from the query
    keywords = query.lower().split()
    relevant_docs = [doc for doc in documents if any(keyword in doc.lower() for keyword in keywords)]
    return relevant_docs if relevant_docs else ["No relevant documents found."]

# Function to generate a response
def generate_response(query):
    # Retrieve documents
    relevant_docs = retrieve_documents(query)
    
    # Generate a response based on retrieved documents
    if relevant_docs[0] == "No relevant documents found.":
        return relevant_docs[0]
    else:
        # For demonstration, return a random relevant document
        return random.choice(relevant_docs)

# Chatbot function to simulate RAG
def chatbot():
    print("Welcome to the RAG Chatbot! Type 'exit' to end the conversation.")
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
