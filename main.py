from dotenv import load_dotenv
load_dotenv()
import os

missing = []
if not os.environ.get('OPENAI_API_KEY'):
    missing.append('OPENAI_API_KEY')
if not os.environ.get('FRED_API_KEY'):
    missing.append('FRED_API_KEY')

if missing:
    print(f"❌ Missing environment variable(s): {', '.join(missing)}. Please set them in your .env file.")
    exit(1)
else:
    print("✅ All required API keys are set.")
