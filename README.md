# Super-Market-Billing-System-Python-

## Project Overview

This project is a **Python-based Supermarket Billing System** designed to simulate a real-world retail checkout process. The system allows users to select multiple products, apply conditional discounts, calculate totals, and generate a detailed itemized bill for customers.

The application automates several billing operations that are typically performed manually in retail environments. By implementing Python programming concepts such as loops, conditional statements, functions, and dictionaries, the system improves transaction efficiency and reduces calculation errors.

The project demonstrates how basic programming logic can be used to build a **Point of Sale (POS)** style billing system.

---

## Problem Statement

Retail stores process numerous transactions daily, often involving multiple products, variable quantities, and promotional discounts. Manual billing can lead to calculation mistakes and inefficiencies.

The objective of this project is to build a **console-based billing system** that can:

* Accept multiple product purchases in a single transaction
* Apply promotional discounts automatically
* Calculate subtotals and final billing amounts
* Generate a formatted receipt for customers

The system handles real-time user input while ensuring accuracy and usability.

---

## Key Features

The Super Market Billing System includes the following functionalities:

* Customer information input (name and phone number)
* Product catalog display
* Item selection using product IDs
* Quantity input validation
* Multiple item purchases in one transaction
* Automatic discount application based on quantity conditions
* Subtotal and final bill calculation
* Generation of an itemized receipt

---

## Product Inventory

The system contains a predefined inventory of supermarket products including:

* Rice
* Wheat Flour
* Sugar
* Cooking Oil
* Milk
* Bread
* Eggs
* Soap
* Shampoo
* Biscuits

Each item contains the following attributes:

* Product ID
* Product Name
* Price
* Unit of measurement

The inventory data is stored using **Python dictionaries**, allowing efficient product lookup operations.

---

## Discount Rules

The system applies promotional discounts based on specific purchase conditions.

### Active Discounts

* Buy **5 kg or more** of Rice → Get **5% discount**
* Buy **3 litres or more** of Milk → Get **10% discount**
* Buy **2 packets or more** of Biscuits → Get **15% discount**

These discounts are automatically applied during the billing process.

---

## System Workflow

### 1. Customer Input
* The user enters their name
* The system validates a 10-digit phone number

### 2. Product Menu Display
* The system displays all available products along with prices and units

### 3. Shopping Cart Creation
* Users select product IDs
* Users enter quantities
* Selected items are stored in a temporary cart list

### 4. Billing and Discount Calculation

The system processes each item in the cart and performs:

* Line item total calculation
* Discount condition checks
* Discount application when criteria are met
* Subtotal and final total calculation

### 5. Bill Generation

The system prints a structured bill containing:

* Product name
* Quantity purchased
* Price per unit
* Discount applied
* Final price
* Subtotal and Grand Total

---

## Programming Concepts Used

This project demonstrates several core Python programming concepts.

### Data Structures
* Dictionaries for storing product inventory
* Lists for managing shopping cart items

### Control Flow
* Conditional statements (`if`, `elif`, `else`)
* Loops for continuous item input

### Functions

Custom functions were implemented for:

* Input validation
* Menu display
* Billing calculations
* System workflow control

### Exception Handling
* `try-except` blocks were used to handle invalid user inputs safely

---

## Code Structure

The system is organized into modular functions including:

* `user_input()` — collects customer details
* `show_header()` — displays store header
* `show_menu()` — prints product catalog
* `input_int()` — validates integer inputs
* `input_float()` — validates numeric inputs
* `discount_offers()` — displays active promotions
* `main()` — controls the entire billing workflow

This modular approach improves readability and maintainability of the program.

---

## Technologies Used

* **Language:** Python
* **Interface:** Console-based
* **Data Structures:** Lists and Dictionaries
* **Logic:** Conditional statements and loops

---

## Example Output

The system generates a structured receipt including:

* Customer details
* Purchased items
* Discounts applied
* Subtotal
* Final bill amount

---

## Conclusion

The Super Market Billing System successfully automates the retail checkout process using Python. The program handles multiple items, validates user inputs, applies promotional discounts accurately, and generates a detailed receipt.

This project demonstrates the practical application of Python programming for building simple transaction management systems.

---

## Future Enhancements

* Database integration for persistent inventory management
* Graphical User Interface using **Tkinter** or **PyQt**
* Inventory stock tracking
* Sales reporting and analytics
* Integration with barcode scanning systems
