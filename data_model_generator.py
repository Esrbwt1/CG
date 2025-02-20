# data_model_generator.py

from nlp_parser import parse_input

def generate_model_code(intermediate_representation):
    """
    Generates Django model code based on the intermediate representation from the NLP parser.
    This is a naive mapping for our MVP demonstration.
    """
    # Retrieve the original text (converted to lowercase for simple matching)
    text = intermediate_representation.get("original_text", "").lower()
    model_code = ""
    
    # If the description mentions "product" or "product listing", generate a Product model.
    if "product" in text:
        model_code += '''
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.URLField()

    def __str__(self):
        return self.name
'''
    # If the description mentions "user registration" or "user", suggest using Django's built-in User model.
    if "user registration" in text or "user" in text:
        model_code += '''
# For user registration, Django's built-in User model can be utilized:
# from django.contrib.auth.models import User
'''
    return model_code

if __name__ == "__main__":
    # Sample natural language input
    sample_text = "Create an e-commerce site with product listing, shopping cart, and user registration."
    
    # Generate the intermediate representation using our NLP parser
    intermediate = parse_input(sample_text)
    
    # Generate the Django model code from the intermediate representation
    model_code = generate_model_code(intermediate)
    
    print("Generated Django Model Code:")
    print(model_code)