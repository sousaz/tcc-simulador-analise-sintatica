import axios from "axios";

const api = axios.create({
  baseURL: import.meta.env.API_SASC_URL ?? "http://localhost:8000",
});

export default api;
