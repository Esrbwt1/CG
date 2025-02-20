import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

def parse_input(text):
    """
    Parses the input text and extracts entities, tokens, and a basic structure.
    Returns an intermediate representation as a dictionary.
    """
    doc = nlp(text)
    
    # Extract entities (e.g., PRODUCT, ACTIONS, etc.)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    
    # For now, we'll simply collect tokens to illustrate the structure.
    tokens = [token.text for token in doc]
    
    # Build an intermediate representation
    intermediate_representation = {
        "original_text": text,
        "entities": entities,
        "tokens": tokens,
        # Future enhancements: map actions, relationships, data models, etc.
    }
    return intermediate_representation

if __name__ == "__main__":
    # Sample input for testing
    sample_text = "Create an e-commerce site with product listing and a shopping cart for user registration."
    result = parse_input(sample_text)
    print("Intermediate Representation:")
    print(result)