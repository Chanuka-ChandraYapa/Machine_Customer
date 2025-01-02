import requests
from services.clustering import cluster
from services.ranking import rank
from services.feature_extraction import preprocess_products
from services.requirements import user_criteria

def SearchProduct(name):
    # URL for searching products
    # search_url = "https://dummyjson.com/products/search"
    search_url = "http://localhost:5001/products/search"
    
    try:
        # Send GET request to search for the product
        response = requests.get(search_url, params={"q": name})
        response.raise_for_status()  # Raise an error for HTTP failures
        data = response.json()
        print("Data************************",data)
        products = data["products"]
        return products

    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def ProcessProduct(name, quantity):
    # Step 1: Check if the product should be bought
    if (name == "Milk" and quantity < 500) or (name == "Butter" and quantity < 250) or (name == "Eggs" and quantity < 15):  
        print(f"Quantity of {name} is low. Deciding whether to buy...")
        
        # Step 2: Search for the product
        products = SearchProduct(name)
        print("Found: ", products)
        
        # If products are found, process them
        if products:
            # Step 3: Preprocess and extract features
            processed_products = [preprocess_products(product) for product in products]
            
            # Step 4: Apply clustering to the products
            clustered_products = cluster(processed_products)
            
            # Step 5: Rank products based on user criteria
            ranked_products = rank(clustered_products)
            
            # Step 6: Select the best product based on ranking
            best_product = ranked_products[0]  # Select the top-ranked product
            print(f"Best product to buy: {best_product}")
            
            # replace best_product with the actual product by searching the product in the products by 'id'.
            for product in products:
                if product["id"] == best_product["id"]:
                    best_product = product
                    break
            return best_product  # Return the best product to the frontend
        else:
            print(f"No products found for {name}.")
            return None
    else:
        print(f"Quantity of {name} is sufficient. No purchase needed.")
        return None
