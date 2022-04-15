import React, { useEffect, useState } from "react";

import { v4 as uuidv4 } from "uuid";
import "react-chat-widget/lib/styles.css";
import { addResponseMessage, Widget } from "react-chat-widget";
import "./styles.css";
import { sendMessage, setSlots } from "./utils";

export default function App() {
  const [convId, setConvId] = useState("");

  useEffect(() => {
    setConvId(uuidv4());
    addResponseMessage(
      "Hey there 😁, your basket price is {placeholder}. What is your best offer?"
    );
  }, []);

  const handleNewUserMessage = async (newMessage) => {
    console.log(`New message incoming! ${newMessage}`);
    const botResponse = await sendMessage(newMessage, convId);
    botResponse.forEach((el) => {
      addResponseMessage(el.text);
    });
  };

  const handleToggle = async (status) => {
    console.log("widget status", status);
    if (status) await setSlots(convId, 1200, 1800);
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
