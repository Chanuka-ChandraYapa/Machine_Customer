import React from "react";
import { Typography, Box, Button, Grid, Paper } from "@mui/material";

const Home = () => (
  <Box
    sx={{
      minHeight: "100vh",
      background: "linear-gradient(to bottom, #0d1b2a, #1b263b, #415a77)",
      color: "#ffffff",
      display: "flex",
      flexDirection: "column",
      justifyContent: "center",
      alignItems: "center",
      textAlign: "center",
      padding: 0, // Ensures no padding from Box
      margin: 0, // Ensures no margin from Box
    }}
  >
    {/* Hero Section */}
    <Box
      sx={{
        maxWidth: 900,
        p: 4,
        boxShadow: "0 4px 15px rgba(0, 0, 0, 0.3)",
        backgroundColor: "rgba(255, 255, 255, 0.1)",
        borderRadius: "15px",
        width: "100%", // Ensure full width
        marginBottom: 4, // Space for separation
      }}
    >
      <Typography variant="h2" gutterBottom sx={{ fontWeight: "bold" }}>
        Discover Amazing Products
      </Typography>
      <Typography variant="h5" sx={{ mb: 3 }}>
        Your one-stop shop for quality, affordability, and convenience.
      </Typography>
      <Button
        variant="contained"
        size="large"
        sx={{
          backgroundColor: "#0077b6",
          color: "#ffffff",
          padding: "12px 30px",
          fontSize: "1.2rem",
          borderRadius: "30px",
          "&:hover": {
            backgroundColor: "#023e8a",
          },
        }}
      >
        Start Shopping
      </Button>
    </Box>

    {/* Features Section */}
    <Box sx={{ mt: 8, width: "100%", maxWidth: "1200px", px: 2 }}>
      <Grid container spacing={4}>
        <Grid item xs={12} sm={6} md={4}>
          <Paper
            elevation={3}
            sx={{
              p: 3,
              textAlign: "center",
              backgroundColor: "#1e3a56",
              color: "#ffffff",
              borderRadius: "10px",
            }}
          >
            <Typography variant="h6" gutterBottom>
              Wide Range of Products
            </Typography>
            <Typography variant="body1">
              From electronics to fashion, find everything you need.
            </Typography>
          </Paper>
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <Paper
            elevation={3}
            sx={{
              p: 3,
              textAlign: "center",
              backgroundColor: "#1e3a56",
              color: "#ffffff",
              borderRadius: "10px",
            }}
          >
            <Typography variant="h6" gutterBottom>
              Affordable Prices
            </Typography>
            <Typography variant="body1">
              Get the best deals and discounts across all categories.
            </Typography>
          </Paper>
        </Grid>
        <Grid item xs={12} sm={6} md={4}>
          <Paper
            elevation={3}
            sx={{
              p: 3,
              textAlign: "center",
              backgroundColor: "#1e3a56",
              color: "#ffffff",
              borderRadius: "10px",
            }}
          >
            <Typography variant="h6" gutterBottom>
              Seamless Shopping Experience
            </Typography>
            <Typography variant="body1">
              Enjoy fast delivery, secure payments, and easy returns.
            </Typography>
          </Paper>
        </Grid>
      </Grid>
    </Box>
  </Box>
);

export default Home;
