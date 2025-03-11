import Sidebar from "../components/Sidebar";
import Chatbot from "../components/Chatbot";

export default function Chat() {
  return (
    <div className="flex h-screen w-full scrollbar-hide">
      <Sidebar />
      <div className="flex-1 p-4">
        <Chatbot />
      </div>
    </div>
  );
}
