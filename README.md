# Inventory Management System

This is a Django-based inventory management system that helps businesses track and manage their products.

## Description

The Inventory Management System is a web application built with Django that provides a user-friendly interface for managing inventory. It allows users to register, log in, and manage products, orders, and customers. The system is designed to be simple and intuitive, making it easy for businesses to keep track of their inventory and streamline their operations.

## Features

*   **User Authentication**: Users can register, log in, and log out of the system.
*   **Dashboard**: A central dashboard to view key inventory metrics.
*   **Product Management**: Add, edit, and delete products from the inventory.
*   **Order Management**: Create and manage customer orders.
*   **Customer Management**: Keep track of customer information.
*   **Profile Management**: Users can update their profiles.

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/inventory-management-system.git
    ```
2.  **Create a virtual environment:**
    ```bash
    pip install --upgrade virtualenv
    virtualenv env
    source env/bin/activate
    ```
3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5.  **Create a superuser:**
    ```bash
    python manage.py createsuperuser
    ```

## Usage

1.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```
2.  **Open your web browser and navigate to `http://127.0.0.1:8000/`**
3.  **Log in with the superuser credentials you created during the installation.**

## Dependencies

The project's dependencies are listed in the `requirements.txt` file. You can install them using the following command:
```bash
pip install -r requirements.txt
```
The main dependencies are:
- Django
- django-crispy-forms
- Pillow

## Screenshots
![client dashboard](https://user-images.githubusercontent.com/70535612/160160094-27578254-1fc3-4ed7-91b5-fd68b6048bf3.png)
![client profile](https://user-images.githubusercontent.com/70535612/160160098-5f6fe351-ef8e-4ec3-b439-0390688daeca.png)
![members](https://user-images.githubusercontent.com/70535612/160160101-746f39f9-1df4-40e2-b0f9-36497723ded3.png)
![orders](https://user-images.githubusercontent.com/70535612/160160107-fb65da98-bf70-4994-8e50-5033dc853b52.png)
![products](https://user-images.githubusercontent.com/70535612/160160109-ec495281-394d-4cc2-80c7-87c1d7fcb2a0.png)
![profile ](https://user-images.githubusercontent.com/70535612/160160113-fbb3ea12-ce99-40cc-9363-2e3477c9efaa.png)
![register](https://user-images.githubusercontent.com/70535612/160160116-45d1deba-4b9b-4d31-b533-6addcd47a769.png)
![Screenshot 2021-09-26 131503](https://user-images.githubusercontent.com/70535612/160160118-404284ee-6f1f-4d7a-82b1-0935e98d7889.png)
![total members](https://user-images.githubusercontent.com/70535612/160160120-85923e3d-ee80-4112-823c-38ee3a2881d7.png)
