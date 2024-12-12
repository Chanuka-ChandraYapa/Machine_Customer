// File: src/pages/Form.js
import React, { useState } from "react";
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

const Form = () => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    communication: "",
    category: "",
    productName: "",
    quantity: 1,
    minPrice: "",
    maxPrice: "",
    discounts: false,
    secondhand: "No",
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

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === "checkbox" ? checked : value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Form Data Submitted:", formData);
  };

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
            <MenuItem value="Electronics">Electronics</MenuItem>
            <MenuItem value="Clothing">Clothing</MenuItem>
            <MenuItem value="Home Appliances">Home Appliances</MenuItem>
            <MenuItem value="Books">Books</MenuItem>
            <MenuItem value="Beauty">Beauty</MenuItem>
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
        <FormControl margin="normal">
          <FormLabel>Consider Secondhand Products?</FormLabel>
          <RadioGroup
            name="secondhand"
            value={formData.secondhand}
            onChange={handleChange}
          >
            <FormControlLabel value="Yes" control={<Radio />} label="Yes" />
            <FormControlLabel value="No" control={<Radio />} label="No" />
          </RadioGroup>
        </FormControl>

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
