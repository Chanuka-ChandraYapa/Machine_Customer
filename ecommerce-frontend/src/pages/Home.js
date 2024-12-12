import React from "react";
import { Typography, Box } from "@mui/material";

const Home = () => (
  <Box sx={{ p: 4, textAlign: "center" }}>
    <Typography variant="h4">Welcome to the E-Commerce Platform</Typography>
    <Typography variant="body1" sx={{ mt: 2 }}>
      Explore our products and enjoy seamless shopping.
    </Typography>
  </Box>
);

export default Home;
