import React, { useState } from "react";
import {
    Button,
    Box,
    Typography,
    TextField,
    Grid,
    Divider,
    CircularProgress,
    Paper,
} from "@mui/material";
import { getProductList } from "../services/apiService";
import { useNavigate } from "react-router-dom";
import { sendProducts, sendRequirements } from "../services/modelService";
import { searchProducts } from "../services/apiService";

const LLM = () => {
    const [description, setDescription] = useState("");
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();
    const [products, setProducts] = useState([]);
    const [formData, setFormData] = useState({
        name: "",
        email: "",
        phone: "",
        communication: "",
        category: "",
        brand: "",
        productName: "",
        quantity: 1,
        minPrice: 99,
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

    // Function to submit form
    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const data = await sendProducts(products);
            const filteredProducts = products.filter((product) =>
                data.some((p) => p.id === product.id)
            );

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
        } catch (error) {
            console.error(error.message);
        }
    };

    // Function to call LLM and get product details
    const handleLLMCall = async () => {
        setLoading(true);
        try {
            const response = await getProductList(description);
            const {
                category,
                brand,
                products,
                maximum_price,
                minimum_price,
                minimum_rating,
                product_name,
                quantity,
            } = response;

            setFormData((prevData) => ({
                ...prevData,
                category,
                brand,
                productName: product_name,
                quantity,
                minPrice: minimum_price,
                maxPrice: maximum_price,
                minRating: minimum_rating,
            }));

            if (product_name) {
                const fetchedProducts = await searchProducts(product_name);
                setProducts(fetchedProducts);
            }
        } catch (error) {
            console.error("Error fetching product details:", error.message);
        } finally {
            setLoading(false);
        }
    };

    return (
        <Box className="product-container" py={4}>
            <Paper elevation={3} sx={{ maxWidth: 600, margin: "0 auto", padding: 4 }}>
                <Typography variant="h4" align="center" gutterBottom>
                    Tell me what you need
                </Typography>
                <TextField
                    label="Enter product description"
                    multiline
                    rows={4}
                    value={description}
                    onChange={(e) => setDescription(e.target.value)}
                    fullWidth
                    variant="outlined"
                />
                <Box mt={3}>
                    <Button
                        variant="contained"
                        color="primary"
                        onClick={handleLLMCall}
                        disabled={loading || !description.trim()}
                        fullWidth
                    >
                        {loading ? <CircularProgress size={24} /> : "Get Product Details"}
                    </Button>
                </Box>

                {formData.productName && (
                    <Box mt={4}>
                        <Typography variant="h6" gutterBottom>
                            Extracted Product Details
                        </Typography>
                        <Grid container spacing={2}>
                            <Grid item xs={6}>
                                <Typography variant="body1">
                                    <strong>Category:</strong> {formData.category}
                                </Typography>
                            </Grid>
                            <Grid item xs={6}>
                                <Typography variant="body1">
                                    <strong>Brand:</strong> {formData.brand}
                                </Typography>
                            </Grid>
                            <Grid item xs={6}>
                                <Typography variant="body1">
                                    <strong>Product Name:</strong> {formData.productName}
                                </Typography>
                            </Grid>
                            <Grid item xs={6}>
                                <Typography variant="body1">
                                    <strong>Quantity:</strong> {formData.quantity}
                                </Typography>
                            </Grid>
                            <Grid item xs={6}>
                                <Typography variant="body1">
                                    <strong>Min Price:</strong> {formData.minPrice}
                                </Typography>
                            </Grid>
                            <Grid item xs={6}>
                                <Typography variant="body1">
                                    <strong>Max Price:</strong> {formData.maxPrice}
                                </Typography>
                            </Grid>
                            <Grid item xs={6}>
                                <Typography variant="body1">
                                    <strong>Min Rating:</strong> {formData.minRating}
                                </Typography>
                            </Grid>
                        </Grid>
                        <Divider sx={{ my: 3 }} />
                    </Box>
                )}

                <Box mt={3}>
                    <Button
                        variant="contained"
                        color="secondary"
                        onClick={handleSubmit}
                        disabled={loading || !products.length}
                        fullWidth
                    >
                        Submit Form
                    </Button>
                </Box>
            </Paper>
        </Box>
    );
};

export default LLM;
