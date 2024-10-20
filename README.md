# Hospital Management System

## Objective
The Hospital Management System project aims to streamline the registration and management of patients in a hospital setting. It includes features for storing patient details, managing billing, and providing easy access to clinical information. The system generates a unique ID for each patient and automatically logs clinical details and hospital tests. 

## Features
- **Patient Registration**: Register new patients and store their details securely in the system.
- **Unique Patient ID**: Each patient is assigned a unique ID for easy identification and record-keeping.
- **Billing Management**: Generate and manage billing details for each patient.
- **Search Functionality**: Search for patient details using their unique ID to check current status and clinical history.
- **User Authentication**: Secure access through a user ID and password, available for administrators, receptionists, and patients.
- **Data Editing**: Staff can easily edit patient data to ensure accuracy and up-to-date information.
- **User-Friendly Interface**: Designed with a simple and intuitive interface using the Tkinter module for ease of use.
- **Data Protection**: Patient data is well-protected and processed efficiently to ensure privacy and security.
- **Email Notifications**: Upon patient admission, an email is sent to the provided email address containing important information and billing details.

## Technologies Used
- **Python**: Core programming language for development.
- **Tkinter**: GUI development module for creating the application interface.
- **MySQL**: Database management system for storing patient details and billing information.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/reddynalamari/hospital-management-system.git
   ```
2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   - `requirements.txt` includes:
     - `mysql-connector-python`
     - `tkinter` (may be included with Python)

3. Set up your MySQL database and read [Setup](setup.txt) file carefully

4. Run the application:
   ```bash
   python main.py
   ```

## How It Works

1. **User Login**: Users can log in using their credentials. Administrators and receptionists can manage patient data, while patients can view their information using their unique ID.
2. **Patient Registration**: Staff can register new patients, assigning them a unique ID and collecting necessary details.
3. **Billing Management**: Billing information is generated and stored for each patient, which can be accessed and modified by the staff.
4. **Email Notification**: After a patient is admitted, an email notification is sent to them with relevant information and billing details.

## Contributors
- [Shashidhar Reddy Nalamari](https://github.com/reddynalamari)
- N V Ramkishore
- M Aditi
- M Vijay

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
