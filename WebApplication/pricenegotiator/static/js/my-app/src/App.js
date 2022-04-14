import { Widget } from "react-chat-widget";
import "./styles.css";
import "react-chat-widget/lib/styles.css";

export default function App() {
  const handleNewUserMessage = (newMessage) => {
    console.log(`New message incoming! ${newMessage}`);
  };

  const handleToggle = (status) => {
    console.log("widget status", status);
  };
  return (
    <div className="App">
      <Widget
        handleNewUserMessage={handleNewUserMessage}
        handleToggle={handleToggle}
      />
    </div>
  );
}
