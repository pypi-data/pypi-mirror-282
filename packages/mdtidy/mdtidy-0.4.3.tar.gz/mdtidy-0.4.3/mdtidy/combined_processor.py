from mdtidy.gemini_processor import process_gemini_conversation
from mdtidy.gpt_processor import process_gpt_conversation
import re

def process_conversation() -> None:
    print("Welcome to the mdtidy!")
    print("This tool processes GPT and Gemini conversation data into structured Jupyter notebooks.")
    print("Please enter the conversation URL to begin.")

    url = input("Enter the conversation URL: ").strip()
    
    if re.match(r'^https://chatgpt\.com/c/[0-9a-fA-F-]{36}$', url):
        print("Processing GPT conversation...")
        process_gpt_conversation(url)
    elif re.match(r'^https://g.co/gemini/share/[a-zA-Z0-9]+$', url):
        print("Processing Gemini conversation...")
        process_gemini_conversation(url)
    else:
        print("Invalid URL format. Please enter a valid GPT or Gemini conversation URL.")

if __name__ == "__main__":
    process_conversation()
