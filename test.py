import google.generativeai as genai

# List available models
models = genai.models.list_models()
for model in models:
    print(f"Model Name: {model.name}, Supported Methods: {model.supported_methods}")
