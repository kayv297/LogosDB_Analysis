import string
import random
from datetime import datetime, timedelta
import pandas as pd

# Define some base questions, answers, keywords, and topics with more variations
base_questions = [
    "What is the capital of {country}?", "How does {process} work?", "Explain the theory of {concept}.",
    "Who wrote '{book}'?", "What is {tech}?"
]
base_answers = [
    "The capital of {country} is {city}.", "{process} is a process involving {details}.",
    "The theory of {concept} was developed by {scientist} and describes {description}.",
    "{author} wrote '{book}'.", "{tech} is a technology that involves {details}."
]
countries = ["France", "Germany", "Italy", "Spain", "Portugal"]
cities = ["Paris", "Berlin", "Rome", "Madrid", "Lisbon"]
processes = ["photosynthesis", "respiration", "digestion", "circulation", "reproduction"]
concepts = ["relativity", "quantum mechanics", "evolution", "thermodynamics", "plate tectonics"]
scientists = ["Einstein", "Newton", "Darwin", "Boltzmann", "Wegener"]
books = ["1984", "Moby Dick", "The Great Gatsby", "War and Peace", "Hamlet"]
authors = ["George Orwell", "Herman Melville", "F. Scott Fitzgerald", "Leo Tolstoy", "William Shakespeare"]
techs = ["quantum computing", "blockchain", "artificial intelligence", "machine learning", "virtual reality"]
details_list = [
    "converting light energy into chemical energy", "the use of blocks in a chain", "the simulation of human intelligence",
    "algorithms that improve through experience", "a computer-generated simulation"
]
topics_list = ["Geography", "Biology", "Physics", "Literature", "Computer Science"]

# Function to generate random keywords
def generate_keywords(words):
    return ', '.join(random.sample(words, 3))

# Function to generate a unique ID
def generate_unique_id(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

# Generate more diverse mock data with 1,000,000 rows
data = []
for i in range(1, 1000001):
    country = random.choice(countries)
    city = cities[countries.index(country)]
    process = random.choice(processes)
    concept = random.choice(concepts)
    scientist = scientists[concepts.index(concept)]
    book = random.choice(books)
    author = authors[books.index(book)]
    tech = random.choice(techs)
    details = random.choice(details_list)
    topic = random.choice(topics_list)
    
    question_template = random.choice(base_questions)
    answer_template = random.choice(base_answers)
    
    question = question_template.format(country=country, process=process, concept=concept, book=book, tech=tech)
    answer = answer_template.format(country=country, city=city, process=process, details=details, concept=concept, scientist=scientist, description=details, author=author, book=book, tech=tech)
    
    keywords = generate_keywords([country, city, process, concept, scientist, book, author, tech, details])
    updated_time = datetime.now() - timedelta(days=random.randint(0, 365))
    
    data.append([generate_unique_id(), question, answer, keywords, updated_time.strftime('%Y-%m-%d %H:%M:%S'), topic])

# Create a DataFrame
df_unique = pd.DataFrame(data, columns=["id", "question", "answer", "keywords", "updated_time", "topic"])

# Save to CSV
csv_path_unique = "/mnt/data/mock_data_unique.csv"
df_unique.to_csv(csv_path_unique, index=False)

csv_path_unique
