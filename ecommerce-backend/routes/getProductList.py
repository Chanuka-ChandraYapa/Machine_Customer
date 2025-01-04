from flask import Blueprint, request, jsonify
from flask_cors import CORS
from groq import Groq
import json

getProductList_bp = Blueprint('getProductList', __name__)

# Initialize the Groq client with your API key
client = Groq(api_key="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")

@getProductList_bp.route('/getProductList', methods=['POST'])
def get_product_list():
    try:
        # Parse the incoming JSON request
        data = request.json
        prompt = data.get('prompt')  # A simple string prompt
        messages = data.get('messages')  # A structured list of messages

        if prompt:
            # Create a new prompt with the updated requirements
            new_prompt = f"""Extract the key details about the product described below and format them as a JSON object. 
            Include fields like category, brand, product name, quantity, minimum price, maximum price, minimum rating, and shipping time.
            If any information is missing, leave the corresponding field as null. Give only json outputs. Here's the product description:
            {prompt}

            Return the extracted details in this format:
            {{
                "category": null,
                "brand": null,
                "product_name": null,
                "quantity": null,
                "minimum_price": null,
                "maximum_price": null,
                "minimum_rating": null,
                "shipping_time": null
            }}
            """
            # Convert the simple prompt into a messages array
            messages = [{"role": "user", "content": new_prompt}]
        
        # Set other optional parameters
        model = data.get('model', 'llama-3.3-70b-versatile')
        temperature = data.get('temperature', 1)
        max_tokens = data.get('max_tokens', 1024)
        top_p = data.get('top_p', 1)
        
        # Call the Groq API
        completion = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=top_p,
            stream=True,
        )
        
        # Stream the response
        response_content = ""
        for chunk in completion:
            response_content += chunk.choices[0].delta.content or ""
        
        # Extract JSON from the response content
        try:
            # Remove code block markers if present
            clean_response = response_content.strip("```")
            # Parse the JSON string
            parsed_json = json.loads(clean_response)
        except Exception as e:
            # If parsing fails, return raw response
            parsed_json = {"error": "Failed to parse JSON", "raw_response": response_content}

        # Return the parsed JSON or raw response
        return jsonify(parsed_json)

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 500
