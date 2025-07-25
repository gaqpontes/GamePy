import os
from pathlib import Path

file=open(os.path.join(Path(__file__).resolve().parent, 'prompt.json'), 'r',  encoding='utf-8')
file_content = file.read()
file.close()

GEMINI_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent'
GEMINI_HEADERS = {'Content-Type': 'application/json',
                  'charset': 'utf-8',
                  'X-goog-api-key':  os.getenv("GEMINI_API_KEY"),
                  'response_mime_type': 'application/json'}


REQUEST_CONFIG = file_content