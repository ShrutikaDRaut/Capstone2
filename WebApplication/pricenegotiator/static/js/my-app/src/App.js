import { addResponseMessage, Widget } from "react-chat-widget";
import "./styles.css";
import "react-chat-widget/lib/styles.css";
import React, { useEffect, useState } from "react";

import { v4 as uuidv4 } from "uuid";

export default function App() {
  const [convId, setConvId] = useState("");

  useEffect(() => {
    setConvId(uuidv4());
    addResponseMessage(
      "Hey there 😁, your basket price is {placeholder}. What is your best offer?"
    );
  }, []);

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
        title="GagdetBot"
        subtitle="Let's deal"
      />
    </div>
  );
}
