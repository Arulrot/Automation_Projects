# Registration System

This is a Python-based GUI Registration System built using Tkinter. It allows users to enter their details, verify their email via OTP, and store the registered data in a CSV file. The system is designed with an easy-to-use interface and includes email verification functionality.

## Features
- User registration with fields: Name, Email, Phone Number, and Department.
- OTP verification via email.
- Stores registered user details in a CSV file.
- Simple and intuitive GUI.
- LinkedIn contact button for the developer.

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.x
- Required Python libraries:
  ```bash
  pip install tk smtplib random csv
  ```

## How It Works
1. **User Registration**
   - Users enter their details and submit the form.
2. **OTP Generation & Email Verification**
   - A random 4-digit OTP is generated and sent to the user's email.
   - The user is required to enter the OTP to proceed.
3. **Data Storage**
   - Upon successful OTP verification, user details are saved in `Customer_data.csv`.
4. **Welcome Page**
   - After successful registration, a thank-you message is displayed.

## How to Run
1. Clone or download this repository.
2. Open the terminal or command prompt and navigate to the project directory.
3. Run the script:
   ```bash
   python script.py
   ```

## Configuration
- Update `sender_email` and `sender_password` in the `send_mail()` function with your valid SMTP credentials.
- Ensure **Less Secure Apps Access** is enabled in your email settings if using Gmail.

## Developer
- **ArulMohan**
- LinkedIn: [Visit Profile](https://www.linkedin.com/in/arulmohanp27/)

## License
This project is open-source and available under the MIT License.

