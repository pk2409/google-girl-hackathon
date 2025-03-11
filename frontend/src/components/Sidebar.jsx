import { Button } from "../components/ui/button";
import { useNavigate } from "react-router-dom";

export default function Sidebar() {
  const navigate = useNavigate();

  return (
    <div className="w-64 p-4 bg-gray-100 h-full">
      <Button className="w-full mb-2 h-[5vh]" onClick={() => navigate("/")}>
        Home
      </Button>
      <Button className="w-full text-black mb-2">Chat History</Button>
      <Button className="w-full text-black mb-2">Quick Actions</Button>

      <div className="w-[16vw] h-[75vh] bg-gray-800 p-4 border-r rounded-lg border-gray-700 ">
        <h2 className="text-xl text-white font-bold mb-4">Medical Tips 🏥</h2>

        {/* Tip Box 1 */}
        <div className="bg-gray-500 text-white w-[13vw] h-[20vh] p-3 rounded-lg mb-3">
          <h3 className="font-semibold">🩺 Stay Hydrated</h3>
          <p className="text-sm">
            Drink at least 8 glasses of water daily to stay healthy.
          </p>
        </div>

        {/* Tip Box 2 */}
        <div className="bg-gray-500 text-white w-[13vw] h-[20vh] p-3 rounded-lg mb-3">
          <h3 className="font-semibold">💊 Regular Check-ups</h3>
          <p className="text-sm">
            Visit a doctor regularly for preventive care.
          </p>
        </div>

        {/* Tip Box 3 */}
        <div className="bg-gray-500 text-white w-[13vw] h-[20vh] p-3 rounded-lg">
          <h3 className="font-semibold">🍏 Healthy Diet</h3>
          <p className="text-sm">
            Eat fruits and vegetables for a balanced diet.
          </p>
        </div>
      </div>
    </div>
  );
}


