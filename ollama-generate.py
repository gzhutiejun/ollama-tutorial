import ollama
import os

model = "llama3.2"
input_file = "./data/grocery_list.txt"
output_file = "./data/catagorized_grocery_list.txt"

if not os.path.exists(input_file):
    print(f"Input file '{input_file}' does not exist.")
    exit(1)

with open(input_file, 'r') as f:
    items = f.read().strip()

print(items)
prompt = f"""
    You are a grocery list categorizer.

    Here is a list of grocery items:
    {items} 

    Please :
    1. Categorize the items into the following categories:
        - Produce
        - Dairy
        - Meat
        - Frozen Foods
        - Canned Goods
        - Baking
        - Snacks
        - Beverages
        - Household
        - Personal Care
        - Pet Supplies
        - Other
    2. Return the categorized items in a single line, separated by commas.
    3. Do not include any additional text or explanations.
    """

try:
    response = ollama.generate(
        model=model,
        prompt=prompt,
    )

    generated_text = response.get(["response"],"")  
    with open(output_file, 'w') as f:
        f.write(generated_text)
    print(f"Generated text has been written to '{output_file}'.")
except Exception as e:
    print(f"Error: {e}")