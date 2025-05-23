import os
from google import genai
import openlit

openlit.init(
    environment="openlit-testing",
    application_name="openlit-python-test",
    otlp_endpoint=os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://collector:4318"),
    disable_batch=True  # For immediate dispatch in demo
)

def main():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set")
    
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents='Why is the sky blue?'
    )
    print(f"Response: {response.text}")

if __name__ == "__main__":
    main() 