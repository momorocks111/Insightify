import axios from "axios";

const API_URL = "http://localhost:5000/api";

export const sendMessage = async (message) => {
  try {
    const response = await axios.post(`${API_URL}/analysis/process_message`, {
      message,
    });
    return response.data;
  } catch (error) {
    console.error("Error sending message:", error);
    throw error;
  }
};
