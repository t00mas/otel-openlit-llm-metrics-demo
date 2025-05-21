# LLM Metrics Demo

Demonstrates OpenTelemetry instrumentation for LLM API calls using Google's Gemini model.

## Setup

1. Copy `.env.example` to `.env` and add your Google API key:
```bash
GOOGLE_API_KEY=your_api_key_here
```

2. Start the services:
```bash
docker compose up --build
```

The collector will output trace data in DEBUG mode to the console. You can view:
- OTLP gRPC endpoint: localhost:4317
- OTLP HTTP endpoint: localhost:4318
- Metrics endpoint: localhost:8888
- Prometheus endpoint: localhost:8889

## Components

- Python app using Gemini API with OpenTelemetry instrumentation
- OpenTelemetry Collector in debug mode
- Trace data includes:
  - Model name
  - Prompt
  - Response length 