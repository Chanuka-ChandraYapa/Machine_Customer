import React from "react";
import {
  Card,
  CardMedia,
  CardContent,
  Typography,
  Rating,
  Box,
} from "@mui/material";

const ProductCard = ({ product }) => {
  return (
    <Card sx={{ maxWidth: 300, m: 2, boxShadow: 3 }}>
      <CardMedia
        component="img"
        height="200"
        image={product.thumbnail}
        alt={product.title}
      />
      <CardContent>
        <Typography variant="h6" gutterBottom noWrap>
          {product.title}
        </Typography>
        <Box
          sx={{
            position: "relative",
            overflow: "hidden",
            display: "inline-block",
            width: "100%",
          }}
        >
          <Typography
            variant="body2"
            color="text.secondary"
            noWrap
            sx={{
              display: "inline-block",
              whiteSpace: "nowrap",
              transition: "transform 0s",
              ":hover": {
                transition: "transform 20s linear",
                transform: "translateX(-100%)",
              },
            }}
          >
            {product.description}
          </Typography>
        </Box>
        <Typography variant="h6" sx={{ mt: 1 }}>
          ${product.price}
        </Typography>
        <Box sx={{ display: "flex", alignItems: "center", mt: 1 }}>
          <Rating value={product.rating} precision={0.1} readOnly />
          {/* <Typography variant="body2" sx={{ ml: 1 }}>
            ({product.rating.count})
          </Typography> */}
        </Box>
      </CardContent>
    </Card>
  );
};

export default ProductCard;
