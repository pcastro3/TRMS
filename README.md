# TRMS
## Project Description
The Tuition Reimbursement System, TRMS, allows users to submit reimbursements for courses and training. The submitted reimbursement must be approved by that employee's supervisor, department head, and benefits coordinator. The benefits coordinator then reviews the grade received before finalizing the reimbursement.
## Technologies Used
- Python 3 (Version 3.10)
- PostgresSQL
- JavaScript, HTML, CSS
- Selenium
## Features
- Users can create and submit requests for reimbursement
- Designated approvers can approve or deny requests from users
- Upon approval, tuition amount is automatically calculated based on the type of course or training
## Getting Started
- Ensure Python 3 is installed
- Clone this repo "git clone https://github.com/pcastro3/TRMS.git"
- Set up a database connection with your AWS RDS
- Install Flask, Flask-cors, and Psycopg2
- Run the application and open login.html in a web browser
## Usage
Log in with credentials. If you are a standard user, you will only be able to create a request. Fill in the required fields and submit the request. If you are an approver (supervisor, department head, benefits coordinator), use the tools to find which employees have requests. Approve or deny their requests depending on whether they meet the requirements for tuition reimbursement.
