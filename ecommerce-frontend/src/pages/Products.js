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
  Paper,
} from "@mui/material";
import { useLocation } from "react-router-dom";
import ProductModal from "../components/productModal";

const Product = () => {
  const location = useLocation();
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [searchQuery, setSearchQuery] = useState(""); // State for search input
  const [selectedProduct, setSelectedProduct] = useState(null);
  const [isModalOpen, setModalOpen] = useState(false);

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

  const handleOpenModal = (product) => {
    setSelectedProduct(product);
    setModalOpen(true);
  };

  const handleCloseModal = () => {
    setModalOpen(false);
    setSelectedProduct(null);
  };

  return (
    <>
      <Box sx={{ p: 4, backgroundColor: "#f5f5f5", borderRadius: 2 }}>
        <Typography variant="h4" textAlign="center" gutterBottom sx={{ fontWeight: 'bold' }}>
          Product List
        </Typography>

        {/* Search Bar */}
        <Box
          sx={{
            display: "flex",
            justifyContent: "center",
            mb: 4,
            gap: 2,
          }}
        >
          <TextField
            label="Search Products"
            variant="outlined"
            value={searchQuery}
            onChange={handleSearchChange}
            sx={{
              width: "300px",
              borderRadius: 1,
              backgroundColor: "white",
              "& .MuiOutlinedInput-root": {
                borderRadius: 2,
              },
            }}
          />
          <Button
            variant="contained"
            onClick={handleSearch}
            sx={{
              backgroundColor: "#1976d2",
              color: "white",
              "&:hover": { backgroundColor: "#1565c0" },
              paddingX: 4,
            }}
          >
            Search
          </Button>
          <Button
            variant="contained"
            onClick={handleRank}
            sx={{
              backgroundColor: "#388e3c",
              color: "white",
              "&:hover": { backgroundColor: "#2c6f32" },
              paddingX: 4,
            }}
          >
            Rank
          </Button>
        </Box>

        <Grid container justifyContent="center" spacing={3}>
          {products.map((product) => (
            <Grid item xs={10} sm={5} md={3} key={product.id}>
              <Paper elevation={3} sx={{ padding: 2, borderRadius: 5 }}>
                <div onClick={() => handleOpenModal(product)}>
                  <ProductCard product={product} />
                </div>
              </Paper>
            </Grid>
          ))}
        </Grid>
      </Box>
      {selectedProduct && (
        <ProductModal
          open={isModalOpen}
          handleClose={handleCloseModal}
          product={selectedProduct}
        />
      )}
    </>
  );
};

export default Product;
