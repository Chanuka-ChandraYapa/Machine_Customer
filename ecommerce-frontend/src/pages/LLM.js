import React, { useState } from "react";
import "./LLM.css";
import { getProductList } from "../services/apiService";

const LLM = () => {
    const [description, setDescription] = useState("");
    const [responseText, setResponseText] = useState("");
    const [loading, setLoading] = useState(false);

    const handleLLMCall = async () => {
        setLoading(true);
        try {
            const response = await getProductList(description);
            setResponseText(JSON.stringify(response, null, 2));
        } catch (error) {
            setResponseText(`Error: ${error.message}`);
        } finally {
            setLoading(false);
        };
    }

    return (
        <div className="product-container">
            <h1>LLM Product Inquiry</h1>
            <textarea
                className="description-input"
                placeholder="Enter product description..."
                value={description}
                onChange={(e) => setDescription(e.target.value)}
            />
            <button onClick={handleLLMCall} disabled={loading || !description.trim()}>
                {loading ? "Processing..." : "Get Product Details"}
            </button>
            <div className="response-output">
                <h3>Response:</h3>
                <pre>{responseText}</pre>
            </div>
        </div>
    );
};

export default LLM;
