import axios from "axios";

const products = [
  {
    id: 1,
    title: "Essence Mascara Lash Princess",
    price: 9.99,
    rating: 4.94,
    availabilityStatus: "Low Stock",
    stock: 5,
    discountPercentage: 7.17,
    shippingInformation: "Ships in 1 month",
    reviews: [
      { rating: 2, comment: "Very unhappy with my purchase!" },
      { rating: 2, comment: "Not as described!" },
      { rating: 5, comment: "Very satisfied!" },
    ],
    tags: ["beauty", "mascara"],
  },
  {
    id: 2,
    title: "Apple AirPods Pro",
    price: 249.99,
    rating: 4.8,
    availabilityStatus: "In Stock",
    stock: 50,
    discountPercentage: 5.0,
    shippingInformation: "Ships in 3 days",
    reviews: [
      { rating: 5, comment: "Amazing sound quality!" },
      { rating: 4, comment: "Good, but overpriced." },
      { rating: 5, comment: "Best purchase I've made!" },
    ],
    tags: ["electronics", "audio", "apple"],
  },
  {
    id: 3,
    title: "Nike Running Shoes",
    price: 129.99,
    rating: 4.6,
    availabilityStatus: "Low Stock",
    stock: 8,
    discountPercentage: 10.0,
    shippingInformation: "Ships in 5 days",
    reviews: [
      { rating: 4, comment: "Comfortable and stylish!" },
      { rating: 3, comment: "Sizes run small." },
      { rating: 5, comment: "Great value for the price!" },
    ],
    tags: ["fashion", "footwear", "sports"],
  },
  {
    id: 4,
    title: "Adidas Running Shoes",
    price: 139.99,
    rating: 4.6,
    availabilityStatus: "Low Stock",
    stock: 8,
    discountPercentage: 10.0,
    shippingInformation: "Ships in 5 days",
    reviews: [
      { rating: 4, comment: "Comfortable and stylish!" },
      { rating: 3, comment: "Sizes run small." },
      { rating: 5, comment: "Great value for the price!" },
    ],
    tags: ["fashion", "footwear", "sports"],
  },
];

// Flask backend URL
const FLASK_BACKEND_URL = "http://127.0.0.1:5000";

// Function to send a list of products to Flask backend
export const sendProducts = async (products) => {
  try {
    const response = await axios.post(
      `${FLASK_BACKEND_URL}/process-products`,
      { products },
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    console.log("Processed Products Data from Flask Backend:", response.data);
    return response.data.processed_data;
  } catch (error) {
    console.error(
      "Error calling Flask backend:",
      error.response?.data || error.message
    );
  }
};

// Function to send user requirements to the backend
export const sendRequirements = async (requirements) => {
  try {
    const response = await axios.post(
      `${FLASK_BACKEND_URL}/requirements`,
      { requirements },
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    console.log(
      "Processed Requirements Data from Flask Backend:",
      response.data
    );
    return response.data;
  } catch (error) {
    console.error(
      "Error calling Flask backend:",
      error.response?.data || error.message
    );
  }
};

// Function to send updates of product quantities to the backend
export const sendProductUpdates = async (product) => {
  try {
    const response = await axios.post(
      `${FLASK_BACKEND_URL}/updateProductQuantity`,
      product, // Sending single product object
      {
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    console.log("Updated Product Data from Flask Backend:", response.data);
    return response.data;
  } catch (error) {
    console.error(
      "Error calling Flask backend:",
      error.response?.data || error.message
    );
  }
};
