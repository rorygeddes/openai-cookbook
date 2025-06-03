import os
import datetime
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI()

# Check for required API keys
missing = []
if not os.environ.get('OPENAI_API_KEY'):
    missing.append('OPENAI_API_KEY')
if not os.environ.get('FRED_API_KEY'):
    missing.append('FRED_API_KEY')

if missing:
    raise ValueError(f"Missing required API keys: {', '.join(missing)}")


# Main callable workflow function
async def run_workflow(custom_question=None):
    today_str = datetime.date.today().strftime("%B %d, %Y")
    question = (
        f"Today is {today_str}. "
        + (custom_question or "How would a planned interest rate cut affect my holdings in GOOGL?")
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4-turbo-preview",
            messages=[
                {"role": "system", "content": "You are a helpful assistant with expertise in finance and investment analysis."},
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message.content
        print(f"\nAnswer: {answer}")
        return answer
    except Exception as e:
        print(f"\nError: {e}")
        return f"Error: {e}"


# Optional interactive CLI
def main():
    import asyncio

    print("Finance and Investment Analysis Assistant")
    print("---------------------------------------")
    while True:
        user_input = input("\nEnter your question (or 'quit' to exit): ")
        if user_input.lower() == 'quit':
            break
        answer = asyncio.run(run_workflow(user_input))
        print(f"\nAnswer: {answer}")
    print("\nGoodbye!")


if __name__ == "__main__":
    main()
