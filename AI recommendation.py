def get_recommendations(category):
    recommendations = {
        "movies": [
            "Dark Knight Rises",
            "Tennent",
            "schindlers list",
            "oppenhiemer",
            "Dunkirk",
            "intersteller",
        ],
        "books": [
            "The Gone Girl - Gillian Flynn",
            "1984 - George Orwell",
            "Linchpin - Seth Godlin",
            "The Kite Runner - khaleed Housini",
        ],
        "places": [
            "Kolkata",
            "Mumbai",
            "Edinburgh",
            "Las vegas",
            "New york",
        ]
    }
    
    return recommendations.get(category.lower(), [])

def ai_recommendation_chatbot():
    print("AI Recommendation Chatbot: Hello! I'm your AI recommendation chatbot.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("AI Recommendation Chatbot: Bye!")
            break
        
        recommendations = get_recommendations(user_input)
        
        if recommendations:
            print("AI Recommendation Chatbot: Here are some recommendations for you:")
            for idx, recommendation in enumerate(recommendations, start=1):
                print(f"{idx}. {recommendation}")
        else:
            print("AI Recommendation Chatbot: I'm sorry, but I couldn't find any recommendations.")

ai_recommendation_chatbot()