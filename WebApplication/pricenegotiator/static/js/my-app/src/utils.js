import axios from "axios";

export async function setSlots(convId, minPrice, maxPrice) {
  const url = `http://localhost:5005/conversations/${convId}/tracker/events`;
  console.log(typeof maxPrice);
  const response = await axios.post(url, [
    {
      event: "slot",
      name: "min_price",
      value: minPrice,
    },
    {
      event: "slot",
      name: "max_price",
      value: maxPrice,
    },
  ]);

  console.log(response.data.slots);
}

export async function sendMessage(message, convId) {
  const url = "http://localhost:5005/webhooks/rest/webhook";
  const response = await axios.post(url, {
    sender: convId,
    message,
  });

  console.log(response);

  return response.data;
}
