import axios from "axios";

const api = axios.create({
  baseURL: "https://api-sasc.onrender.com",
});

export default api;
