import React from "react";
import { BrowserRouter as Router, Routes, Route, Link, NavLink } from "react-router-dom";
import { AppBar, Toolbar, Button, Box, Container } from "@mui/material";
import Home from "./pages/Home";
import Product from "./pages/Products";
import Form from "./pages/Form";
import Simulation from "./pages/simulation";
import LLM from "./pages/LLM";
// import About from "./pages/About";
// import Contact from "./pages/Contact";

const App = () => {
  return (
    <Router>
      {/* AppBar with background color */}
      <AppBar position="sticky" sx={{ backgroundColor: "#0d1b32", boxShadow: 3 }}>
        <Container maxWidth="lg">
          <Toolbar sx={{ justifyContent: "space-between" }}>
            {/* Left section: Logo or Brand name */}
            <Button color="inherit" component={Link} to="/" sx={{ fontSize: "1.5rem", fontWeight: "bold" }}>
              E-Shop
            </Button>

            {/* Right section: Navigation links */}
            <Box sx={{ display: "flex", gap: 2 }}>
              {/* Using NavLink for active link styles */}
              <NavLink
                to="/"
                style={({ isActive }) => ({
                  textDecoration: "none",
                  color: isActive ? "#ff9800" : "inherit", // Highlight active link
                })}
              >
                <Button color="inherit" sx={{ "&:hover": { backgroundColor: "#333" } }}>
                  Home
                </Button>
              </NavLink>

              <NavLink
                to="/products"
                style={({ isActive }) => ({
                  textDecoration: "none",
                  color: isActive ? "#ff9800" : "inherit", // Highlight active link
                })}
              >
                <Button color="inherit" sx={{ "&:hover": { backgroundColor: "#333" } }}>
                  Products
                </Button>
              </NavLink>

              <NavLink
                to="/form"
                style={({ isActive }) => ({
                  textDecoration: "none",
                  color: isActive ? "#ff9800" : "inherit", // Highlight active link
                })}
              >
                <Button color="inherit" sx={{ "&:hover": { backgroundColor: "#333" } }}>
                  Requirements
                </Button>
              </NavLink>

              <NavLink
                to="/simulation"
                style={({ isActive }) => ({
                  textDecoration: "none",
                  color: isActive ? "#ff9800" : "inherit", // Highlight active link
                })}
              >
                <Button color="inherit" sx={{ "&:hover": { backgroundColor: "#333" } }}>
                  Simulation
                </Button>
              </NavLink>

              <NavLink
                to="/llm"
                style={({ isActive }) => ({
                  textDecoration: "none",
                  color: isActive ? "#ff9800" : "inherit", // Highlight active link
                })}
              >
                <Button color="inherit" sx={{ "&:hover": { backgroundColor: "#333" } }}>
                  LLM
                </Button>
              </NavLink>

              {/* Uncomment when pages are available */}
              {/* <NavLink to="/about" style={({ isActive }) => ({
                  textDecoration: "none",
                  color: isActive ? "#ff9800" : "inherit", // Highlight active link
                })}>
                  <Button color="inherit" sx={{ "&:hover": { backgroundColor: "#333" } }}>
                    About
                  </Button>
                </NavLink>

                <NavLink to="/contact" style={({ isActive }) => ({
                  textDecoration: "none",
                  color: isActive ? "#ff9800" : "inherit", // Highlight active link
                })}>
                  <Button color="inherit" sx={{ "&:hover": { backgroundColor: "#333" } }}>
                    Contact
                  </Button>
                </NavLink> */}
            </Box>
          </Toolbar>
        </Container>
      </AppBar>

      {/* Main content container with elevation */}
      <Box sx={{ mt: 0 }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/products" element={<Product />} />
          <Route path="/form" element={<Form />} />
          <Route path="/simulation" element={<Simulation />} />
          <Route path="/llm" element={<LLM />} />
          {/* <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} /> */}
        </Routes>
      </Box>
    </Router>
  );
};

export default App;
