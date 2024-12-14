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
import { useLocation } from "react-router-dom";

const Product = () => {
  const location = useLocation();
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState(""); // State for search input

  useEffect(() => {
    const queryParams = new URLSearchParams(location.search);
    const data = queryParams.get("data");

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

    if (data) {
      try {
        const parsedProducts = JSON.parse(decodeURIComponent(data));
        setProducts(parsedProducts);
        setLoading(false);
      } catch (error) {
        console.error("Error parsing product data:", error);
      }
    } else {
      getProducts();
    }
  }, [location.search]);

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
        prevProducts.sort((a, b) => {
          const rankA = data.find((p) => p.id === a.id)?.rank;
          const rankB = data.find((p) => p.id === b.id)?.rank;

          const validRankA = isNaN(rankA) ? Infinity : rankA;
          const validRankB = isNaN(rankB) ? Infinity : rankB;
          return validRankA - validRankB;
        })
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
