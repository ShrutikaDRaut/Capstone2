import React, { useEffect, useState } from "react";
import "react-chat-widget/lib/styles.css";
import { addResponseMessage, Widget } from "react-chat-widget";
import "./styles.css";
import { sendMessage, setSlots } from "./utils";

export default function App() {
  const [convId, setConvId] = useState("");
  const [orderDetails, setOrderDetails] = useState();
  const [offer, setOffer] = useState();

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
    const regex = /\$([0-9.]+)\./;
    const match = botResponse[0].text.match(regex);
    match?.length === 2 && setOffer(match[1]);
    if (botResponse[0].text.match("Congratulations!")) {
      localStorage.setItem("finalOffer", offer);
      setTimeout(() => {
        window.location = "checkout";
      }, 3000);
    }
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
        title="GadgetBot"
        subtitle="Let's deal"
      />
    </div>
  );
}
