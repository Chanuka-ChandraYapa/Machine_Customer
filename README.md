# SmartCart: Automated Grocery Management System

This project is a smart, automated solution to manage household groceries efficiently using a React frontend and two Flask backends. Below are the instructions to set up and run the project.

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


   
