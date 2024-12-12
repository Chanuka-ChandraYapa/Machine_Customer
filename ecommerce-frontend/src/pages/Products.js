// src/pages/Product.js
import React, { useState, useEffect } from "react";
import { fetchProducts, searchProducts } from "../services/apiService";
import { sendProducts } from "../services/modelService";
import ProductCard from "../components/productCard";
import {
  Grid,
  Typography,
  CircularProgress,
  Box,
  TextField,
  Button,
} from "@mui/material";

const Product = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState(""); // State for search input

  useEffect(() => {
    const getProducts = async () => {
      try {
        const data = await fetchProducts();
        setProducts(data);
        setLoading(false);
      } catch (error) {
        console.error(error.message);
        setLoading(false);
      }
    };
    getProducts();
  }, []);

  const handleSearch = async () => {
    if (searchQuery.trim()) {
      setLoading(true);
      try {
        const data = await searchProducts(searchQuery);
        setProducts(data);
        setLoading(false);
      } catch (error) {
        console.error(error.message);
        setLoading(false);
      }
    }
  };

  const handleRank = async () => {
    setLoading(true);
    try {
      const data = await sendProducts(products);
      //remove the products not in data by checking their ids
      setProducts((prevProducts) =>
        prevProducts.filter((product) =>
          data.map((p) => p.id).includes(product.id)
        )
      );
      //sort the products based on the rank of data
      setProducts((prevProducts) =>
        prevProducts.sort(
          (a, b) =>
            data.find((p) => p.id === a.id).rank -
            data.find((p) => p.id === b.id).rank
        )
      );
      setLoading(false);
    } catch (error) {
      console.error(error.message);
      setLoading(false);
    }
  };

  const handleSearchChange = (event) => {
    setSearchQuery(event.target.value);
  };

  if (loading) {
    return (
      <Box
        sx={{
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
          height: "100vh",
        }}
      >
        <CircularProgress />
      </Box>
    );
  }

  return (
    <Box sx={{ p: 4 }}>
      <Typography variant="h4" textAlign="center" gutterBottom>
        Product List
      </Typography>

      {/* Search Bar */}
      <Box sx={{ display: "flex", justifyContent: "center", mb: 4 }}>
        <TextField
          label="Search Products"
          variant="outlined"
          value={searchQuery}
          onChange={handleSearchChange}
          sx={{ mr: 2 }}
        />
        <Button variant="contained" onClick={handleSearch} sx={{ mr: 2 }}>
          Search
        </Button>
        <Button variant="contained" onClick={handleRank}>
          Rank
        </Button>
      </Box>

      <Grid container justifyContent="center">
        {products.map((product) => (
          <Grid item key={product.id}>
            <ProductCard product={product} />
          </Grid>
        ))}
      </Grid>
    </Box>
  );
};

export default Product;
