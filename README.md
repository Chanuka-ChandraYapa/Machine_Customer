# Smart Cart: Next-Generation E-Commerce with Machine Customers

**Smart Cart** is a groundbreaking platform designed to redefine the e-commerce experience with the power of AI. By introducing the concept of "machine customers," this project aims to enable automated AI agents to shop on behalf of users. These intelligent agents autonomously evaluate products, compare deals, and make data-driven purchasing decisions, mimicking human shopping behavior efficiently and intelligently.  

---

## ✨ Features
- **Machine Customers**: AI-powered agents that shop on behalf of users based on predefined preferences.
- **Product Evaluation**: Automated analysis and comparison of products across platforms.
- **Generative AI Integration**: Advanced decision-making using state-of-the-art AI technologies.
- **Enhanced Shopping Experience**: Personalized, efficient, and user-centric automation.

---


## Table of Contents  
1. [Prerequisites](#prerequisites)  
2. [Setup Instructions](#setup-instructions)  
   - [React Frontend](#react-frontend)  
   - [Flask Backend 1](#flask-backend-1)  
   - [Flask Backend 2](#flask-backend-2)  
3. [Usage](#usage)  

---

### Prerequisites  
Ensure you have the following installed on your system:  
- **Node.js** (v16.x or later)  
- **Python** (v3.8 or later)  
- **pip** (Python package installer)  
- **Virtualenv** (for creating isolated Python environments)  

---

## Setup Instructions  

### React Frontend  
1. Navigate to the `ecommerce-frontend` directory:  
   ```bash
   cd ecommerce-frontend

2. Install dependencies:  
   ```bash
   npm install

3. Run the frontend using below command:
   ```bash
   npm start

### Flask Backend 1
1. Navigate to the `ecommerce-backend` directory:
   ```bash
   cd ecommerce-backend

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt

4. Update the GROQ_API key in below path in line 9.
   ```bash
   ecommerce-backend/routes/getProductList.py
   
4. Run the Flask server:
   ```bash
   python app.py

### Flask Backend 2
1. Navigate to the `mock-api` directory:
   ```bash
   cd mock-api

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the Flask server:
   ```bash
   python products.py

### Usage
Access the application in your web browser at:
  ```bash
  http://localhost:3000```
