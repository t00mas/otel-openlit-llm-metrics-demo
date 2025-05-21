import os
import google.generativeai as genai
import openlit
from opentelemetry import metrics
from opentelemetry.metrics import Counter, Histogram

# Initialize openlit
openlit.init(
    environment="openlit-testing",
    application_name="openlit-python-test",
    otlp_endpoint=os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://collector:4318"),
    disable_batch=True  # For immediate dispatch in demo
)

# Get meter
meter = metrics.get_meter("llm.metrics")
llm_requests = meter.create_counter(
    "llm.requests",
    description="Number of LLM requests",
    unit="1"
)
llm_latency = meter.create_histogram(
    "llm.latency",
    description="Latency of LLM requests",
    unit="ms"
)

def main():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY environment variable not set")
    
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    llm_requests.add(1, {"model": "gemini-1.5-flash"})
    
    import time
    start = time.time()
    response = model.generate_content("Explain the difference between a cat and a dog")
    latency = (time.time() - start) * 1000  # Convert to ms
    llm_latency.record(latency, {"model": "gemini-1.5-flash"})
    
    print(f"Response: {response.text}")

if __name__ == "__main__":
    main() 