import random
import spacy
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
nlp = spacy.load("en_core_web_sm")
analyzer = SentimentIntensityAnalyzer()
greetings = ["Hello!", "Hi there!", "Hey!", "Hi! How can I help you today?"]
questions = ["How's your day going?", "What's on your mind?", "Anything interesting happening?", "Tell me more about it", "What's your take on this?"]
import bleach
class Character:
    
    def __init__(self, name, personality_traits):
        self.name = name
        self.personality_traits = personality_traits
        self.responses = []
        self.personality_changed = False

    def add_response(self, response):
        self.responses.append(response)

    def get_personality(self):
        if not self.responses:
            return self.personality_traits
        if not self.personality_changed:
            notify_user = self.detect_possible_personality_change()
            if notify_user:
                user_input = input("Notice: Your character is exhibiting a possible change in personality. Would you like to allow that? (yes/no): ")
                if user_input.lower() == "yes":
                    self.personality_changed = True
                else:
                    return self.personality_traits
        personality_counts = {trait: 0 for trait, _ in self.personality_traits}
        total_responses = len(self.responses)
        for response in self.responses:
            for trait, percentage in self.personality_traits:
                if random.randint(1, 100) <= percentage:
                    personality_counts[trait] += 1
        updated_personality_traits = [(trait, count / total_responses * 100) for trait, count in personality_counts.items()]
        return updated_personality_traits

    def detect_possible_personality_change(self):
        current_personality = dict(self.get_personality())
        if not self.responses or not current_personality:
            return False
        response_personality = dict(self.calculate_average_personality())
        for trait, percentage in current_personality.items():
            if abs(percentage - response_personality.get(trait, 0)) > 10:
                return True
        return False

    def calculate_average_personality(self):
        if not self.responses:
            return {}
        personality_counts = {trait: 0 for trait, _ in self.personality_traits}
        total_responses = len(self.responses)
        for response in self.responses:
            for trait, percentage in self.personality_traits:
                if random.randint(1, 100) <= percentage:
                    personality_counts[trait] += 1
        updated_personality_traits = [(trait, count / total_responses * 100) for trait, count in personality_counts.items()]
        return dict(updated_personality_traits)

    def get_response(self, user_input):
        doc = nlp(user_input)
        named_entities = [ent.text for ent in doc.ents]
        if named_entities:
            response = self.generate_complex_response(named_entities)
        elif "hello" in user_input.lower():
            response = random.choice(greetings)
        elif "?" in user_input:
            response = random.choice(questions)
        else:
            sentiment_response = self.analyze_sentiment(user_input)
            response = sentiment_response
        if self.detect_possible_personality_change():
            user_input = input("Notice: Your character is exhibiting a possible change in personality. Would you like to allow that? (yes/no): ")
            if user_input.lower() == "yes":
                self.personality_changed = True
            else:
                return "I'll stay true to my usual self."
        self.add_response(response)
        return response

    def generate_complex_response(self, named_entities):
        if not named_entities:
            return "I'm here to chat with you! What's on your mind?"
        response_templates = {
            'PERSON': "I see you mentioned {name}. Tell me more about {name}.",
            'GPE': "You mentioned {location}. What's your connection to {location}?",
            'ORG': "I noticed {organization} in your input. Are you affiliated with {organization}?",
            'TRAUMA': "I'm here to listen. Can you share more about your experiences with {trauma}?",
            'MENTAL_HEALTH': "Mental health is important. How has your journey with {mental_health} been?"
        }
        entity = named_entities[0] if named_entities else ""
        entity_type = nlp(entity).ents[0].label_ if named_entities else None
        template = response_templates.get(entity_type, "I'm here to chat with you! What's on your mind?")
        populated_response = template.format(
            name=entity,
            location=entity if len(named_entities) > 1 else "",
            organization=entity if len(named_entities) > 2 else "",
            trauma=entity if len(named_entities) > 3 else "",
            mental_health=entity if len(named_entities) > 4 else ""
        )
        return populated_response
    
    def analyze_sentiment(self, user_input):
        sentiment = analyzer.polarity_scores(user_input)
        compound_score = sentiment["compound"]
        if compound_score > 0.1:
            return "I'm glad to hear that!"
        elif compound_score < -0.1:
            return "I'm sorry to hear that."
        else:
            return "That's interesting."

"""
        
def friend_simulator(user_input, character):
    doc = nlp(user_input)
    named_entities = [ent.text for ent in doc.ents]
    user_input = bleach.clean(user_input)
    if "hello" in user_input.lower():
        return random.choice(greetings)
    elif "?" in user_input:
        return random.choice(questions)
    elif named_entities:
        return character.generate_complex_response(doc.ents)
    else:
        return character.analyze_sentiment(user_input)

"""

def choose_characteristics(category_name, characteristics_list):
    while True:
        print(f"Choose one {category_name} characteristic:")
        for i, characteristic in enumerate(characteristics_list, start=1):
            print(f"{i}: {characteristic}")
        choice = input("Enter the number of your choice: ")
        if choice.isnumeric():
            choice = int(choice)
            if 1 <= choice <= len(characteristics_list):
                return characteristics_list[choice - 1]
        print("Invalid choice. Using a random characteristic.")

def choose_personality_traits():
    personality_traits = [
        "friendly", "shy", "outgoing", "introverted", "optimistic", "pessimistic",
        "confident", "insecure", "empathetic", "self-centered", "funny", "serious",
        "loyal", "adventurous", "cautious", "creative", "analytical", "impulsive",
        "patient", "impatient", "kind", "rude", "generous", "stingy", "ambitious",
        "lazy", "honest", "dishonest", "compassionate", "competitive"
    ]
    chosen_traits = []
    remaining_percentage = 100
    while len(chosen_traits) < 5 and remaining_percentage > 0:
        print(f"Choose a personality trait and assign a percentage (multiple of 5):")
        for i, trait in enumerate(personality_traits, start=1):
            print(f"{i}: {trait}")
        choice = input("Enter the number and percentage (e.g., '1 20' for the first trait with 20%): ").split()
        try:
            if len(choice) == 2:
                trait_index, percentage = map(int, choice)
                if 1 <= trait_index <= len(personality_traits) and percentage % 5 == 0 and 0 <= percentage <= remaining_percentage:
                    chosen_trait = personality_traits.pop(trait_index - 1)
                    chosen_traits.append((chosen_trait, percentage))
                    remaining_percentage -= percentage
                    print(f"You chose '{chosen_trait}' with {percentage}%.")
                else:
                    print("Invalid input. Please provide a valid trait number and percentage.")
            else:
                print("Invalid input format. Please provide both a trait number and a percentage.")
        except ValueError:
            print("Invalid input. Please provide a valid trait number and percentage.")
    return chosen_traits

def sanitize_input(user_input):
    sanitized_input = bleach.clean(user_input)
    return sanitized_input

def main():
    print("Welcome to AllFriends!")
    print("Choose a character to interact with:")
    print("1: BestFriend")
    print("2: BoyFriend")
    print("3: GirlFriend")
    character_choice = input("Enter the number of your choice: ")
    character_choice = sanitize_input(character_choice)
    if character_choice == "1":
        character = Character("BestFriend", [])
    elif character_choice == "2":
        character = Character("BoyFriend", [])
    elif character_choice == "3":
        character = Character("GirlFriend", [])
    else:
        print("Invalid choice. Please enter a valid number (1, 2, or 3).")
        return
    custom_name = input(f"Enter a custom name for your {character.name} (or press Enter to keep the default): ")
    custom_name = sanitize_input(custom_name)
    if custom_name:
        character.name = custom_name
    form_characteristics = ["tall", "short", "thin", "muscular", "curvy"]
    face_characteristics = ["freckled", "dimpled", "bearded", "mustached", "bald", "tattooed", "scarred", "birthmarked"]
    accessories_characteristics = ["bespectacled", "pierced", "hatted", "suited", "booted"]
    hair_characteristics = ["long-haired", "curly-haired", "red-haired", "blonde-haired", "brunette-haired", "gray-haired"]
    eyes_characteristics = ["green-eyed", "blue-eyed", "brown-eyed", "hazel-eyed", "black-eyed"]
    skin_characteristics = ["very fair-skinned", "fair-skinned", "medium-skinned", "olive-skinned", "brown-skinned", "black-skinned"]
    form = choose_characteristics("form", form_characteristics)
    face = choose_characteristics("face", face_characteristics)
    accessories = choose_characteristics("accessories", accessories_characteristics)
    hair = choose_characteristics("hair", hair_characteristics)
    eyes = choose_characteristics("eyes", eyes_characteristics)
    skin = choose_characteristics("skin", skin_characteristics)
    character.personality_traits = choose_personality_traits()
    character.get_personality()
    if custom_name:
        character_description = f"{form}, {face}, {accessories}, {hair}, {eyes}, {skin} {custom_name}"
    else:
        character_description = f"{form}, {face}, {accessories}, {hair}, {eyes}, {skin} {character.name}"
    print(f"You are now talking to your {character_description}. Type 'exit' to end the conversation.")
    character_instance = character
    in_custom_response_mode = True
    while True:
        if in_custom_response_mode:
            user_input = input("Enter a custom response for your character (or press Enter to skip): ")
            if user_input == "":
                in_custom_response_mode = False
                continue
            else:
                user_input2 = input("You: ")
                print(f"{character_instance.name}: {user_input}")
        else:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print(f"{character_instance.name}: Goodbye!")
                break
            else:
                response = character_instance.get_response(user_input)
                print(f"{character_instance.name}: {response}")
                
if __name__ == "__main__":
    main()
