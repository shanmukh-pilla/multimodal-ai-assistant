function ChatWindow() {
  return (
    <div className="chat-window">
      <h3>Conversation</h3>

      <div className="message user">
        User message will appear here
      </div>

      <div className="message assistant">
        Assistant response will appear here
      </div>
    </div>
  );
}

export default ChatWindow;