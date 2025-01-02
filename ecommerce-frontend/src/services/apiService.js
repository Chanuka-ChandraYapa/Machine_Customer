import axios from "axios";
import { sendProducts } from "./modelService";

// API Client
const apiClient = axios.create({
  // baseURL: "https://dummyjson.com"
  baseURL:"http://localhost:5001",
  timeout: 5000,
});

// Fetch products
export const fetchProducts = async () => {
  try {
    const response = await apiClient.get("/products");
    console.log("Products:", response.data.products);
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
    return response.data.products;
  } catch (error) {
    console.error(
      `Error searching for products with query "${query}":`,
      error.message
    );
    throw new Error("Failed to search products");
  }
};

// Fetch all categories
export const fetchCategories = async () => {
  try {
    const response = await apiClient.get("/products/category-list");
    return response.data; // Assuming the API returns a "categories" field
  } catch (error) {
    console.error("Error fetching categories:", error.message);
    throw new Error("Failed to fetch categories");
  }
};

// Fetch products by category
export const fetchProductsByCategory = async (category) => {
  try {
    const response = await apiClient.get(`/products/category/${category}`);
    return response.data.products;
  } catch (error) {
    console.error(
      `Error fetching products in category "${category}":`,
      error.message
    );
    throw new Error(`Failed to fetch products in category "${category}"`);
  }
};

// Get all brands from a list of products
export const extractBrands = (products) => {
  try {
    const brands = Array.from(
      new Set(products.map((product) => product.brand))
    );
    return brands;
  } catch (error) {
    console.error("Error extracting brands:", error.message);
    throw new Error("Failed to extract brands");
  }
};
