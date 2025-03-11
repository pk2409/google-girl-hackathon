import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import Home from "./pages/Home";
import Chat from "./pages/Chat";
import medichatlogo from "./assets/medichatai.png";


function App() {
  return (
    <Router>
      <div className="bg-black text-white p-4 flex rounded-xl justify-between items-center shadow-lg fixed w-full top-0 z-50 h-12">
        <img src={medichatlogo} alt="Logo" className="h-10 w-10 mr-3" />
        {/* <h1 className="text-l font-bold tracking-wide">MediChat AI</h1> */}

        <nav className="space-x-6 flex">
          <Link
            to="/"
            className="text-white transition-all duration-300  text-lg font-medium px-3 py-1 rounded-md"
          >
            Home
          </Link>
          <Link
            to="/chat"
            className="text-white transition-all duration-300 hover:text-gray-400 text-lg font-medium px-3 py-1 rounded-md"
          >
            Chat
          </Link>
          <Link
            to="/login"
            className="text-white transition-all duration-300 hover:text-gray-400 text-lg font-medium px-3 py-1 rounded-md"
          >
            Login
          </Link>
          <Link
            to="/signup"
            className="text-white transition-all duration-300 hover:text-gray-400 text-lg font-medium px-3 py-1 rounded-md"
          >
            Sign Up
          </Link>
        </nav>
      </div>
      <div classname="mt-100 pt-20">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/chat" element={<Chat />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
