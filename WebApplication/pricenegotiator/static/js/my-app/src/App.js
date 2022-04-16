import React, { useEffect, useState } from "react";
import "react-chat-widget/lib/styles.css";
import { addResponseMessage, Widget } from "react-chat-widget";
import "./styles.css";
import { sendMessage, setSlots } from "./utils";

export default function App() {
  const [convId, setConvId] = useState("");
  const [orderDetails, setOrderDetails] = useState();

  useEffect(() => {
    const store = JSON.parse(localStorage.getItem("orderDetails"));
    setOrderDetails(store);
    setConvId("anon");
    addResponseMessage(
      `Hey there 😁, your basket price is $${store.order.get_cart_total}. What is your best offer?`
    );
  }, []);

  const handleNewUserMessage = async (newMessage) => {
    const botResponse = await sendMessage(newMessage, convId);
    botResponse.forEach((el) => {
      addResponseMessage(el.text);
    });
  };

  const handleToggle = async (status) => {
    if (status)
      await setSlots(
        convId,
        orderDetails.min_price,
        orderDetails.order.get_cart_total
      );
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
