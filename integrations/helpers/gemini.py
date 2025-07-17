import os

GEMINI_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent'
GEMINI_HEADERS = {'Content-Type': 'application/json',
                  'X-goog-api-key':  os.getenv("GEMINI_API_KEY"),
                  'response_mime_type': 'application/json'}


REQUEST_CONFIG = '{"contents":[{"parts":[{"inline_data":{"mime_type":"image/*","data":"{$REPLACE_BASE64}"}},{"text":"Crie subtarefas gamificadas de até 80 caracteres usando como base a imagem anexada ."}]}],"generationConfig":{"responseMimeType":"application/json","responseSchema":{"type":"ARRAY","items":{"type":"OBJECT","properties":{"Objective":{"type":"STRING"}}}}}}'