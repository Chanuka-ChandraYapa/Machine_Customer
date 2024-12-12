import axios from "axios";
import { sendProducts } from "./modelService";

// API Client
const apiClient = axios.create({
  baseURL: "https://dummyjson.com",
  timeout: 5000,
});

// Fetch products
export const fetchProducts = async () => {
  try {
    const response = await apiClient.get("/products");
    console.log("Products fetched successfully:", response.data);
    return response.data.products;
  } catch (error) {
    console.error("Error fetching products:", error.message);
    throw new Error("Failed to fetch products");
  }
};

// Search products
export const searchProducts = async (query) => {
  try {
    const response = await apiClient.get("/products/search", {
      params: { q: query }, // Pass the search query as a parameter
    });
    console.log(`Search results for "${query}":`, response.data);
    return response.data.products;
  } catch (error) {
    console.error(
      `Error searching for products with query "${query}":`,
      error.message
    );
    throw new Error("Failed to search products");
  }
};
