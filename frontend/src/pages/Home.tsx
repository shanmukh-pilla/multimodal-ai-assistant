import { useState } from "react";
import { sendMessage } from "../services/api";

function Home() {
  const [message, setMessage] = useState("");

  const [response, setResponse] = useState("");
  const [explanation, setExplanation] = useState("");

  const [topic, setTopic] = useState("");
  const [confidence, setConfidence] = useState<number>(0);
  const [keywords, setKeywords] = useState<string[]>([]);

  const [domain, setDomain] = useState("");
  const [riskLevel, setRiskLevel] = useState("");
  const [interactionType, setInteractionType] = useState("");
  const [recommendedSystem, setRecommendedSystem] = useState("");
  const [processingStage, setProcessingStage] = useState("");

  const [reasoningSteps, setReasoningSteps] = useState<string[]>([]);

  const handleSend = async () => {
    if (!message.trim()) return;

    try {
      const data = await sendMessage(message);

      setResponse(data.response);
      setExplanation(data.explanation);

      setTopic(data.topic);
      setConfidence(data.confidence);
      setKeywords(data.keywords);

      setDomain(data.domain);
      setRiskLevel(data.risk_level);
      setInteractionType(data.interaction_type);
      setRecommendedSystem(data.recommended_system);
      setProcessingStage(data.processing_stage);

      setReasoningSteps(data.reasoning_steps);
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div
      style={{
        display: "grid",
        gridTemplateColumns: "250px 1fr 360px",
        height: "100vh",
        fontFamily: "Arial, sans-serif",
      }}
    >
      {/* Sidebar */}

      <div
        style={{
          borderRight: "1px solid #ddd",
          padding: "20px",
          background: "#fafafa",
        }}
      >
        <h2>AI Assistant</h2>

        <p>New Chat</p>
        <p>History</p>

        <hr />

        <h4>Research Areas</h4>

        <p>Artificial Intelligence</p>
        <p>Human Computer Interaction</p>
        <p>AR / VR</p>
        <p>Wearables</p>
      </div>

      {/* Conversation */}

      <div
        style={{
          padding: "20px",
          display: "flex",
          flexDirection: "column",
        }}
      >
        <h2>Conversation</h2>

        <div
          style={{
            background: "#f3f4f6",
            padding: "12px",
            borderRadius: "8px",
            marginBottom: "12px",
          }}
        >
          {message || "User message"}
        </div>

        <div
          style={{
            background: "#dbeafe",
            padding: "12px",
            borderRadius: "8px",
          }}
        >
          {response || "Assistant response"}
        </div>

        <div
          style={{
            marginTop: "auto",
            display: "flex",
            gap: "10px",
          }}
        >
          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            placeholder="Ask something..."
            style={{
              flex: 1,
              padding: "12px",
            }}
          />

          <button onClick={handleSend}>
            Send
          </button>
        </div>
      </div>

      {/* Explainability Panel */}

      <div
        style={{
          borderLeft: "1px solid #ddd",
          padding: "20px",
          overflowY: "auto",
          background: "#fafafa",
        }}
      >
        <h2>Explainability Dashboard</h2>

        <hr />

        <p><strong>Topic</strong></p>
        <p>{topic || "-"}</p>

        <p><strong>Confidence</strong></p>
        <p>{confidence ? `${confidence}%` : "-"}</p>

        <p><strong>Domain</strong></p>
        <p>{domain || "-"}</p>

        <p><strong>Risk Level</strong></p>
        <p>{riskLevel || "-"}</p>

        <p><strong>Interaction Type</strong></p>
        <p>{interactionType || "-"}</p>

        <p><strong>Recommended System</strong></p>
        <p>{recommendedSystem || "-"}</p>

        <p><strong>Processing Status</strong></p>
        <p>{processingStage || "-"}</p>

        <hr />

        <h3>Keywords</h3>

        <div
          style={{
            display: "flex",
            flexWrap: "wrap",
            gap: "8px",
          }}
        >
          {keywords.map((keyword) => (
            <span
              key={keyword}
              style={{
                background: "#e5e7eb",
                padding: "6px 10px",
                borderRadius: "20px",
              }}
            >
              {keyword}
            </span>
          ))}
        </div>

        <hr />

        <h3>AI Reasoning Pipeline</h3>

        {reasoningSteps.map((step, index) => (
          <div
            key={index}
            style={{
              marginBottom: "10px",
              padding: "10px",
              background: "#f3f4f6",
              borderRadius: "8px",
            }}
          >
            ✓ {step}
          </div>
        ))}

        <hr />

        <h3>Explanation</h3>

        <p>
          {explanation ||
            "The model explanation will appear here."}
        </p>
      </div>
    </div>
  );
}

export default Home;