import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import { AppBar, Toolbar, Button, Box } from "@mui/material";
import Home from "./pages/Home";
import Product from "./pages/Products";
import Form from "./pages/Form";
// import About from "./pages/About";
// import Contact from "./pages/Contact";

const App = () => {
  return (
    <Router>
      <AppBar position="static">
        <Toolbar>
          <Button color="inherit" component={Link} to="/">
            Home
          </Button>
          <Button color="inherit" component={Link} to="/products">
            Products
          </Button>
          <Button color="inherit" component={Link} to="/about">
            About
          </Button>
          <Button color="inherit" component={Link} to="/contact">
            Contact
          </Button>
          <Button color="inherit" component={Link} to="/form">
            Requirements
          </Button>
        </Toolbar>
      </AppBar>
      <Box sx={{ mt: 4 }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/products" element={<Product />} />
          {/* <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} /> */}
          <Route path="/form" element={<Form />} />
          <Route path="/products/:products" element={<Product />} />
        </Routes>
      </Box>
    </Router>
  );
};

export default App;
