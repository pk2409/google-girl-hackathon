import { useNavigate } from "react-router-dom";
import { Button } from "../components/ui/button";
import chatImage from "../assets/medichatai2.png";


export default function Home() {
  const navigate = useNavigate();
  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      {/* Hero Section */}
      <div className="flex flex-col lg:flex-row items-center justify-between px-2 py-16 bg-white shadow-md">
        <div className="lg:w-1/2 text-center lg:text-left">
          <h1 className="text-4xl font-bold text-gray-900 mb-4">
            Get your Diagnosis with AI-Powered Chatbots
          </h1>
          <p className="text-gray-600 mb-6">
            An AI-powered medical diagnostic assistant designed to enhance
            patient interaction, automate preliminary assessments, and support
            faster healthcare decisions.
          </p>
          <Button
            className="px-6 py-3 bg-gray-200 border-gray-300 text-gray-700 text-lg"
            onClick={() => navigate("/chat")}
          >
            GET DIAGNOSED
          </Button>
        </div>
        <div className="lg:w-1/2 flex justify-center">
          <img src={chatImage} className="max-w-full h-auto" />
        </div>
      </div>

      {/* Features Section */}
      <div className="py-16 px-10 bg-gray-50 text-center">
        <h2 className="text-3xl font-semibold text-gray-800 mb-8">
          Why Choose Our Chatbot ?
        </h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 ">
          <FeatureBox
            // imgSrc =
            title="AI-Powered Medical Diagnosis"
            desc="Accurately analyze symptoms and provide instant preliminary assessments."
          />
          <FeatureBox
            // imgSrc =
            title="Smart Healthcare Connectivity"
            desc="Seamlessly integrate with hospital systems and electronic health records (EHR)."
          />
          <FeatureBox
            // imgSrc =
            title="Multilingual Support"
            desc="Ensure accessibility for diverse populations with multiple language options."
          />
          <FeatureBox
            // imgSrc =
            title="Expert-Backed Insights"
            desc="Utilize AI-driven recommendations supported by medical professionals."
          />
        </div>
      </div>
    </div>
  );
}

function FeatureBox({ title, desc }) {
  return (
    <div className="p-6 bg-white shadow-lg rounded-lg">
      {/* <img src={imgSrc} alt={title} className="w-12 h-12 mb-4" /> */}
      <h3 className="text-xl font-semibold text-gray-800 mb-2">{title}</h3>
      <p className="text-gray-600">{desc}</p>
    </div>
  );
}
