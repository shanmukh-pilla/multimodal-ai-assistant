from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Request Model
# --------------------------------------------------

class ChatRequest(BaseModel):
    message: str


# --------------------------------------------------
# Health Check
# --------------------------------------------------

@app.get("/")
def health_check():
    return {
        "status": "running",
        "project": "Multimodal Explainable AI Assistant"
    }


# --------------------------------------------------
# Topic Rules
# --------------------------------------------------

TOPIC_RULES = {
    "Artificial Intelligence": {
        "keywords": [
            "ai",
            "machine learning",
            "deep learning",
            "llm",
            "chatgpt",
            "neural network"
        ],
        "tags": ["AI", "Reasoning", "Learning"],
        "confidence": 92,
        "domain": "AI Research"
    },

    "Human Computer Interaction": {
        "keywords": [
            "hci",
            "ux",
            "usability",
            "interaction",
            "user experience"
        ],
        "tags": ["HCI", "UX", "Interaction"],
        "confidence": 90,
        "domain": "Human Factors"
    },

    "AR/VR": {
        "keywords": [
            "ar",
            "vr",
            "augmented reality",
            "virtual reality",
            "unity"
        ],
        "tags": ["Immersive", "3D", "Interaction"],
        "confidence": 88,
        "domain": "Extended Reality"
    },

    "Wearable Technology": {
        "keywords": [
            "wearable",
            "watch",
            "sensor",
            "smartwatch",
            "fitness tracker"
        ],
        "tags": ["Sensors", "Wearables", "Health"],
        "confidence": 89,
        "domain": "Wearable Computing"
    },

    "IoT Systems": {
        "keywords": [
            "iot",
            "smart home",
            "connected device",
            "device"
        ],
        "tags": ["IoT", "Devices", "Connectivity"],
        "confidence": 87,
        "domain": "Internet of Things"
    },

    "Computer Vision": {
        "keywords": [
            "image",
            "camera",
            "vision",
            "object detection",
            "recognition"
        ],
        "tags": ["Vision", "Images", "Detection"],
        "confidence": 91,
        "domain": "Computer Vision"
    },

    "Natural Language Processing": {
        "keywords": [
            "nlp",
            "language",
            "text",
            "translation"
        ],
        "tags": ["NLP", "Language", "Text"],
        "confidence": 90,
        "domain": "Language AI"
    },

    "Sports Analytics": {
        "keywords": [
            "sports",
            "athlete",
            "fitness",
            "training",
            "performance"
        ],
        "tags": ["Athlete", "Performance", "Analytics"],
        "confidence": 87,
        "domain": "Sports Science"
    },

    "Robotics": {
        "keywords": [
            "robot",
            "robotics",
            "automation"
        ],
        "tags": ["Robotics", "Automation"],
        "confidence": 88,
        "domain": "Intelligent Systems"
    },

    "Data Analytics": {
        "keywords": [
            "dashboard",
            "analytics",
            "data",
            "visualization"
        ],
        "tags": ["Data", "Insights", "Visualization"],
        "confidence": 86,
        "domain": "Data Science"
    }
}


# --------------------------------------------------
# Explainability Engine
# --------------------------------------------------

def analyze_message(message: str):

    text = message.lower()

    for topic, info in TOPIC_RULES.items():

        for keyword in info["keywords"]:

            if keyword in text:

                return {
                    "topic": topic,
                    "keywords": info["tags"],
                    "confidence": info["confidence"],
                    "domain": info["domain"],
                    "risk_level": "Low",
                    "interaction_type": "Text Input",
                    "recommended_system": "Explainable Assistant",
                    "processing_stage": "Completed",
                    "reasoning_steps": [
                        "Received user query",
                        "Detected topic",
                        "Extracted relevant keywords",
                        "Estimated confidence score",
                        "Generated explanation",
                        "Returned response"
                    ]
                }

    return {
        "topic": "General",
        "keywords": ["General Query"],
        "confidence": 75,
        "domain": "General Knowledge",
        "risk_level": "Unknown",
        "interaction_type": "Text Input",
        "recommended_system": "General Assistant",
        "processing_stage": "Completed",
        "reasoning_steps": [
            "Received user query",
            "Unable to classify domain",
            "Used fallback classification",
            "Generated generic response"
        ]
    }


# --------------------------------------------------
# Chat Endpoint
# --------------------------------------------------

@app.post("/chat")
def chat(request: ChatRequest):

    analysis = analyze_message(request.message)

    response = (
        f"This query appears related to "
        f"{analysis['topic']}."
    )

    explanation = (
        f"The system classified this query under "
        f"{analysis['topic']} with a confidence score "
        f"of {analysis['confidence']}%."
    )

    return {
        "response": response,
        "explanation": explanation,
        "topic": analysis["topic"],
        "keywords": analysis["keywords"],
        "confidence": analysis["confidence"],
        "domain": analysis["domain"],
        "risk_level": analysis["risk_level"],
        "interaction_type": analysis["interaction_type"],
        "recommended_system": analysis["recommended_system"],
        "processing_stage": analysis["processing_stage"],
        "reasoning_steps": analysis["reasoning_steps"]
    }