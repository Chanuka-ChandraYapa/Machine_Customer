import React from "react";
import {
  Box,
  Modal,
  Typography,
  Button,
  CardMedia,
  Divider,
  Chip,
  Grid,
  Stack,
} from "@mui/material";

// Modal style
const modalStyle = {
  position: "absolute",
  top: "50%",
  left: "50%",
  transform: "translate(-50%, -50%)",
  width: "80%",
  maxHeight: "90vh",
  bgcolor: "background.paper",
  boxShadow: 24,
  p: 4,
  overflowY: "auto",
  borderRadius: 2,
};

const ProductModal = ({ open, handleClose, product }) => {
  return (
    <Modal open={open} onClose={handleClose} aria-labelledby="product-modal">
      <Box sx={modalStyle}>
        {/* Header Section */}
        <Stack
          direction="row"
          justifyContent="space-between"
          alignItems="center"
          mb={2}
        >
          <Typography id="product-modal" variant="h5" fontWeight="bold">
            {product.title}
          </Typography>
          <Button variant="contained" color="error" onClick={handleClose}>
            Close
          </Button>
        </Stack>

        <Divider />

        {/* Content Section */}
        <Grid container spacing={4} mt={2}>
          {/* Product Image */}
          <Grid item xs={12} sm={6}>
            <CardMedia
              component="img"
              image={product.thumbnail}
              alt={product.title}
              sx={{
                borderRadius: 2,
                height: 300,
                objectFit: "contain",
              }}
            />
            <Stack direction="row" spacing={1} mt={2}>
              {product.images.map((img, idx) => (
                <CardMedia
                  key={idx}
                  component="img"
                  image={img}
                  alt={`Image ${idx + 1}`}
                  sx={{
                    width: 60,
                    height: 60,
                    objectFit: "contain",
                    borderRadius: 1,
                    border: "1px solid #ddd",
                  }}
                />
              ))}
            </Stack>
          </Grid>

          {/* Product Details */}
          <Grid item xs={12} sm={6}>
            <Typography variant="body1" color="text.secondary" mb={1}>
              {product.description}
            </Typography>

            <Typography variant="h6" color="primary" mt={2}>
              Price: ${product.price}{" "}
              <Typography variant="caption" color="text.secondary">
                ({product.discountPercentage}% off)
              </Typography>
            </Typography>

            <Typography variant="body2" color="text.secondary" mt={1}>
              Availability: {product.availabilityStatus} ({product.stock} in
              stock)
            </Typography>

            <Typography variant="body2" mt={1}>
              Category:{" "}
              <Chip label={product.category} color="primary" size="small" />
            </Typography>

            <Stack direction="row" spacing={1} mt={1}>
              {product.tags.map((tag, idx) => (
                <Chip key={idx} label={tag} variant="outlined" />
              ))}
            </Stack>

            <Divider sx={{ my: 2 }} />

            <Typography variant="body2" color="text.secondary">
              Minimum Order Quantity: {product.minimumOrderQuantity}
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Shipping: {product.shippingInformation}
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Warranty: {product.warrantyInformation}
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Return Policy: {product.returnPolicy}
            </Typography>
          </Grid>
        </Grid>

        <Divider sx={{ my: 2 }} />

        {/* Additional Information */}
        <Typography variant="h6" mt={2}>
          Additional Information
        </Typography>
        <Stack direction="row" justifyContent="space-between" mt={1}>
          <Typography variant="body2">SKU: {product.sku}</Typography>
          <Typography variant="body2">
            Barcode: {product.meta.barcode}
          </Typography>
          <Typography variant="body2">Weight: {product.weight}g</Typography>
          <Typography variant="body2">
            Dimensions:{" "}
            {`${product.dimensions.width} x ${product.dimensions.height} x ${product.dimensions.depth}`}{" "}
            cm
          </Typography>
        </Stack>

        <Divider sx={{ my: 2 }} />

        {/* Footer Section */}
        <Stack direction="row" justifyContent="space-between" mt={3}>
          <Typography variant="subtitle1" fontWeight="bold">
            Rating: {product.rating} / 5
          </Typography>
          <Button variant="contained" color="primary">
            Buy Now
          </Button>
        </Stack>
      </Box>
    </Modal>
  );
};

export default ProductModal;
