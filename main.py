#!/usr/bin/python3

from langchain.llms import OpenAI
from dotenv import load_dotenv

print("Dotenv loaded ")

load_dotenv()


def generate_stock_names():
    llm = OpenAI(temperature=0.7)
    names = llm("Give me tha names of the stocks that were teh highest paying in 2018")
    return names

if __name__ == "__main__":
    print(generate_stock_names())

