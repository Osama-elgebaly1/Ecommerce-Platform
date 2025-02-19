# **E-commerce Platform**

## **Description**  
E-commerce Platform is a fully functional online shopping system built with Django. It consists of three main apps:  

- **Ecommerce App** – Manages products, categories, and user authentication.  
- **Cart App** – Handles shopping cart functionality.  
- **Payment App** – Manages the checkout process and payment integration.  

This platform provides a seamless shopping experience, allowing users to browse products, add items to their cart, and complete purchases securely.  

---

## **Features**  

- **Product Browsing** – Users can explore available products with detailed descriptions and images.  
- **User Authentication** – Secure login, logout, registration, and password reset functionality.  
- **Product Search** – A dedicated search page allows users to search for products by title and description.  
- **Shopping Cart** – Users can add, update, and remove products from their cart before proceeding to checkout.  
- **Order Tracking** – Users can track their orders after making a purchase.  
- **Product Management** – New products can only be added from the **Django Admin Panel**.  

---

## **Tech Stack**  

- **Backend:** Django (Python)  
- **Database:** SQLite3 (Default Django database)  
- **Frontend:** HTML, Bootstrap, and some JavaScript  

This stack ensures a robust backend with Django while providing a responsive and user-friendly interface using Bootstrap and JavaScript.  

---

## **Installation & Setup**  

Follow these steps to set up and run the project locally:  

### **1. Set Up a Virtual Environment**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### **2. Clone the Repository**  
```bash
git clone https://github.com/Osama-elgebaly1/Ecommerce-Platform.git
cd Ecommerce-Platform/project
```

### **3. Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **4. Apply Migrations**  
```bash
python manage.py migrate
```

### **5. Run the Development Server**  
```bash
python manage.py runserver
```

Now, the project should be running at **http://127.0.0.1:8000/**.  

---

## **Usage**  

Once the project is up and running, users can:  

- **Register & Log In** – Create an account or log in to access full platform features.  
- **Browse & Search Products** – Explore available products or use the search feature to find specific items.  
- **Manage Cart** – Add, update, or remove products from the shopping cart.  
- **Checkout & Payment** – Proceed to checkout and complete the payment process.  
- **Track Orders** – View order history and track the status of placed orders.  
- **Product Management** – New products can only be added from the **Django Admin Panel**.  

### **Accessing the Admin Panel**  
To add products, log in to the Django admin panel:  
- Visit: **http://127.0.0.1:8000/admin/**  
- Use the provided admin credentials or create a superuser with:  
  ```bash
  python manage.py createsuperuser
  ```  

---

## **Demo Video**  
*Upload your demo video and add a link here:*  
```markdown
[Click here to watch the demo]()
```

---

## **Contributing**  
Contributions are welcome! If you'd like to improve this project, feel free to fork the repository, make your changes, and submit a pull request.  

---



