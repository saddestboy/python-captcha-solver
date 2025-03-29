import os
from dotenv import load_dotenv
from DrissionPage import ChromiumOptions

# Load environment variables from .env file
load_dotenv()

# Get Chrome path from environment variables, with a fallback path
chrome_path = os.getenv('CHROME_PATH', r'D:\Chrome\Chrome.exe')
ChromiumOptions().set_browser_path(chrome_path).incognito().save()

print(f"Path set to {chrome_path}")