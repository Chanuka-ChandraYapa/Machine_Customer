// File: src/pages/Form.js
import React, { useState, useEffect } from "react";
import {
  TextField,
  Button,
  Checkbox,
  Radio,
  RadioGroup,
  FormControl,
  FormControlLabel,
  FormLabel,
  Select,
  MenuItem,
  Typography,
  Slider,
  Box,
  InputLabel,
} from "@mui/material";
import {
  extractBrands,
  fetchCategories,
  fetchProductsByCategory,
} from "../services/apiService";
import { sendProducts, sendRequirements } from "../services/modelService";
import { useNavigate } from "react-router-dom";

const Form = () => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    communication: "",
    category: "",
    brand: "",
    productName: "",
    quantity: 1,
    minPrice: 1,
    maxPrice: 999,
    discounts: false,
    secondhand: false,
    preferredBrands: "",
    avoidBrands: "",
    quality: "",
    minRating: 3,
    minReviews: 10,
    deliveryLocation: "",
    urgency: "",
    expressShipping: "No",
    requiredFeatures: "",
    optionalFeatures: "",
    colorSize: "",
    rankAttributes: [],
    purchaseAuthority: "Yes",
    approvalRequired: "No",
    maxSpend: "",
    ecoFriendly: "No",
    avoidRegions: "",
    localBusiness: false,
    additionalNotes: "",
  });

  const [categories, setCategories] = useState([]);
  const [brands, setBrands] = useState([]);
  const [isBrandFieldActive, setIsBrandFieldActive] = useState(false);
  const [products, setProducts] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    const findCategories = async () => {
      try {
        const response = await fetchCategories(); // Replace `apiClient` with your configured axios instance
        setCategories(response);
      } catch (error) {
        console.error("Error fetching categories:", error.message);
      }
    };

    findCategories();
  }, []);

  const fetchProducts = async (category) => {
    try {
      const response = await fetchProductsByCategory(category);
      //print products in console
      setProducts(response);
      const productBrands = extractBrands(response);
      setBrands(productBrands);
      setIsBrandFieldActive(true);
    } catch (error) {
      console.error(
        `Error fetching products in category "${category}":`,
        error.message
      );
    }
  };

  const filterProductByName = async (productName) => {
    try {
      // Filter products based on whether their title includes the entered product name (case insensitive)
      const filteredProducts = products.filter((product) =>
        product.title.toLowerCase().includes(productName.toLowerCase())
      );
      setProducts(filteredProducts);
    } catch (error) {
      console.error("Error filtering products by name:", error.message);
    }
  };

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === "checkbox" ? checked : value,
    });

    if (name === "category") {
      fetchProducts(value);
      setFormData((prevData) => ({ ...prevData, brand: "" })); // Reset brand selection
      setIsBrandFieldActive(false);
    }

    if (name === "productName"){
      filterProductByName(value);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("Form Data Submitted:", formData);
    try {
      const req = await sendRequirements(formData);
      const data = await sendProducts(products);
      //remove the products not in data by checking their ids
      // Filter the products to include only those in the data array
      const filteredProducts = products.filter((product) =>
        data.some((p) => p.id === product.id)
      );

      // Sort the filtered products based on the rank in the data array
      const sortedProducts = filteredProducts.sort((a, b) => {
        const rankA = data.find((p) => p.id === a.id)?.rank;
        const rankB = data.find((p) => p.id === b.id)?.rank;

        const validRankA = isNaN(rankA) ? Infinity : rankA;
        const validRankB = isNaN(rankB) ? Infinity : rankB;
        return validRankA - validRankB;
      });
      const encodedProducts = encodeURIComponent(
        JSON.stringify(sortedProducts)
      );
      navigate(`/products?data=${encodedProducts}`);
      console.log("Processed Products:", sortedProducts);
    } catch (error) {
      console.error(error.message);
    }
  };

  const handleRank = async () => {};

  return (
    <Box
      sx={{
        maxWidth: 600,
        margin: "0 auto",
        padding: 4,
        boxShadow: 3,
        borderRadius: 2,
      }}
    >
      <Typography variant="h4" gutterBottom>
        AI Shopping Agent - User Requirement Form
      </Typography>
      <form onSubmit={handleSubmit}>
        {/* 2. Product Details */}
        <Typography variant="h6" mt={3}>
          Product Details
        </Typography>
        <FormControl fullWidth margin="normal">
          <InputLabel>Category</InputLabel>
          <Select
            name="category"
            value={formData.category}
            onChange={handleChange}
          >
            {categories.map((category) => (
              <MenuItem key={category} value={category}>
                {category}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
        <FormControl fullWidth margin="normal" disabled={!isBrandFieldActive}>
          <InputLabel>Brand</InputLabel>
          <Select name="brand" value={formData.brand} onChange={handleChange}>
            {brands.map((brand) => (
              <MenuItem key={brand} value={brand}>
                {brand}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
        <TextField
          label="Product Name or Keywords"
          name="productName"
          value={formData.productName}
          onChange={handleChange}
          fullWidth
          margin="normal"
        />
        <TextField
          label="Quantity"
          name="quantity"
          type="number"
          value={formData.quantity}
          onChange={handleChange}
          fullWidth
          margin="normal"
        />

        {/* 3. Budget & Pricing Preferences */}
        <Typography variant="h6" mt={3}>
          Budget & Pricing Preferences
        </Typography>
        <TextField
          label="Minimum Price"
          name="minPrice"
          type="number"
          value={formData.minPrice}
          onChange={handleChange}
          fullWidth
          margin="normal"
        />
        <TextField
          label="Maximum Price"
          name="maxPrice"
          type="number"
          value={formData.maxPrice}
          onChange={handleChange}
          fullWidth
          margin="normal"
        />
        <FormControlLabel
          control={
            <Checkbox
              name="discounts"
              checked={formData.discounts}
              onChange={handleChange}
            />
          }
          label="Consider Discounts or Deals?"
        />
        <FormControlLabel
          control={
            <Checkbox
              name="secondhand"
              checked={formData.secondhand}
              onChange={handleChange}
            />
          }
          label="Consider Second hand products?"
        />

        {/* Submit Button */}
        <Box mt={3}>
          <Button variant="contained" color="primary" type="submit" fullWidth>
            Submit Preferences
          </Button>
        </Box>
      </form>
    </Box>
  );
};

export default Form;
