// import { useState } from "react";
// import { Input } from "../components/ui/input";
// import { Button } from "../components/ui/button";

// export default function Chatbot() {
//   const [messages, setMessages] = useState([]);
//   const [input, setInput] = useState("");

//   const sendMessage = () => {
//     if (input.trim()) {
//       setMessages([...messages, { text: input, sender: "user" }]);
//       setInput("");
//     }
//   };

//   return (
//     <div className="flex flex-col h-full border rounded-lg p-4">
//       {/* Message Display */}
//       <div className="flex-1 overflow-auto p-2">
//         {messages.map((msg, index) => (
//           <div
//             key={index}
//             className={`p-2 ${
//               msg.sender === "user" ? "text-right" : "text-left"
//             }`}
//           >
//             {msg.text}
//           </div>
//         ))}
//       </div>

//       {/* Input & Send Button */}
//       <div className="flex gap-2 mt-2">
//         <Input
//           value={input}
//           onChange={(e) => setInput(e.target.value)}
//           placeholder="Type a message..."
//         />
//         <Button onClick={sendMessage}>Send</Button>
//       </div>
//     </div>
//   );
// }


import { useState, useRef, useEffect } from "react";
import { Send } from "lucide-react"; // Import an icon for better UI
import axios from "axios"

export default function Chat() {
  const [messages, setMessages] = useState([
    { text: "Hello! How can I assist you today?", sender: "bot" },
  ]);
  const [input, setInput] = useState("");
  const [isTyping, setIsTyping] = useState(false);
  const chatRef = useRef(null);

  useEffect(() => {
    chatRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const getBotResponse = (userMessage) => {
    const lowerCaseMsg = userMessage.toLowerCase();
    if (lowerCaseMsg.includes("hello")) return "Hi there! How can I help you?";
    if (lowerCaseMsg.includes("how are you"))
      return "I'm just a bot, but I'm doing great! 😊";
    if (lowerCaseMsg.includes("bye")) return "Goodbye! Have a great day! 👋";
    return "I'm not sure about that. Can you please rephrase?";
  };

  const sendMessage = async() => {
    if (input.trim() === "") return;
    const currentInput = input;

    const userMessage = { text: input, sender: "user" };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");

    setIsTyping(true);
    try {
      const response = await axios.post("http://localhost:5000/chatbot", {
        message: input,
      });

      // setMessages([...prev, { text: response.data.response, sender: "bot" }]);
      setMessages((prev) => [
        ...prev,
        { text: response.data.response, sender: "bot" },
      ]);
    } catch (error) {
      console.error("Error:", error);
    }

    setTimeout(() => {
      // const botReply = { text: getBotResponse(input), sender: "bot" };
      // setMessages((prev) => [...prev, botReply]);
      setIsTyping(false);
    }, 1000);
  };

  return (
    <div className="flex flex-col scrollbar-hide items-center rounded-2xl w-[80vw] justify-center h-[98vh] bg-gray-900 text-white p-4">
      <div className="flex-1 flex flex-col justify-between p-6">
        <div className="w-[67vw] bg-gray-800 p-6 rounded-lg shadow-xl">
          <h2 className="text-xl font-bold mb-3 text-center">MediChat 🤖</h2>

          {/* Chat Messages */}
          <div className="h-[70vh] w-[62vw] rounded-3xl overflow-y-auto border border-gray-700 p-3 rounded-lg space-y-3">
            {messages.map((msg, index) => (
              <div
                key={index}
                className={`flex ${
                  msg.sender === "user" ? "justify-end" : "justify-start"
                }`}
              >
                <div
                  className={`px-4 py-2 rounded-lg max-w-xs ${
                    msg.sender === "user"
                      ? "bg-blue-500 text-white"
                      : "bg-gray-600"
                  }`}
                >
                  {msg.text}
                </div>
              </div>
            ))}
            {isTyping && (
              <div className="text-gray-400 text-sm">Bot is typing...</div>
            )}
            <div ref={chatRef} />
          </div>

          {/* Input Box */}
          <div className="flex mt-4">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              className="flex-1 bg-gray-700 text-white border-none rounded-l-lg px-3 py-2 focus:outline-none"
              placeholder="Type a message..."
              onKeyDown={(e) => e.key === "Enter" && sendMessage()}
            />
            <button
              onClick={sendMessage}
              className="px-4 py-2 bg-blue-600 text-black rounded-r-lg hover:bg-blue-700 flex items-center"
            >
              <Send size={20} />
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
