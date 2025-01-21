from groq import Groq
from flask import request, jsonify
import json


client = Groq(
    api_key="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")


def generate_negotiation_email(product):
    product_name = product.get('product_name', 'product')
    quantity = product.get('quantity', '100')
    price = product.get('price', '100')
    double_quantity = str(int(quantity) * 2)

    try:

        new_prompt = f"""Write a professional email to negotiate with a supplier about purchasing {product_name}. Specify that the intended quantity is {quantity}, and the quoted price is {price} per unit. Mention the currently offered discount and ask for details on how much the discount could be increased if double the quantity ({double_quantity}) is purchased.
                        Additionally, inquire about:
                        Payment terms (e.g., discounts for early payment or extended payment schedules).
                        Lead time for delivery and whether there are options for expedited shipping.
                        Bulk purchase incentives or other benefits for a long-term partnership.
                        The email should maintain a respectful and professional tone, express an interest in establishing a collaborative business relationship, and request a detailed response regarding the updated terms and conditions.
        """
        # Convert the simple prompt into a messages array
        messages = [{"role": "user", "content": new_prompt}]

        # Set other optional parameters
        model = 'llama-3.3-70b-versatile'
        temperature = 1
        max_tokens = 1024
        top_p = 1

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
            # print(clean_response)
            # Parse the JSON string
            # parsed_json = json.loads(clean_response)
        except Exception as e:
            # If parsing fails, return raw response
            parsed_json = {"error": "Failed to parse JSON",
                           "raw_response": response_content}

        # Return the parsed JSON or raw response
        return clean_response

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 500


def extract_response_email(email):
    try:

        new_prompt = f"""Analyze the response email from the supplier regarding the product negotiation. Extract the following relevant details and structure them into a JSON file:
                        product_name: Name of the product.
                        quoted_price_per_unit: Price per unit quoted by the supplier.
                        quantity: Quantity discussed in the email.
                        current_discount: Discount currently offered.
                        discount_for_double_quantity: New discount percentage or amount offered for purchasing double the quantity.
                        payment_terms: Details about payment terms, including any early payment discounts or extended payment options.
                        lead_time: Lead time for delivery of the product.
                        expedited_shipping: Availability and terms of expedited shipping (if mentioned).
                        bulk_incentives: Any additional benefits or incentives offered for bulk purchase or long-term collaboration.
                        If any of these fields are missing or unclear in the email, include them in the JSON file with a value of null or undefined. Ensure the extracted details are accurate and correctly formatted.

                        The below is the email:
                        {email}
        """
        # Convert the simple prompt into a messages array
        messages = [{"role": "user", "content": new_prompt}]

        # Set other optional parameters
        model = 'llama-3.3-70b-versatile'
        temperature = 1
        max_tokens = 1024
        top_p = 1

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
            # print(clean_response)
            # Parse the JSON string
            # parsed_json = json.loads(clean_response)
        except Exception as e:
            # If parsing fails, return raw response
            clean_response = {"error": "Failed to parse JSON",
                           "raw_response": response_content}

        # Return the parsed JSON or raw response
        return clean_response

    except Exception as e:
        print("Error:", e)
        return jsonify({'error': str(e)}), 500