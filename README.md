# inventory-management

This is car parts inventory management system. User can add details of car parts and perform actions like updating/deleting parts from the database table.

## Requirements
1. Python 3
2. Sqlite Python 
3. Flask 
4. Bootstrap 4 
5. urllib
6. json 
---
### Install instructions 
open command prompt and type the following commands
#### Clone this repository and install the required files using requirements.txt file
`git clone https://github.com/dreambakers/inventory-management.git`

`cd inventory-management`

`pip install -r requirements.txt`

### How to run the app
1. Make sure you are in `inventory-management` directory 
2. open command prompt and type
 `python FlaskCarPartsInventory.py`
3. The website starts running on this address:
 `http://127.0.0.1:5000/`
Copy this address and paste it in browser to run the site 

### Issues 
Make sure you are connected with internet, otherwise UI will break due to no internet connection css files will not be downloaded

### Latest Changes
1. In AddProduct.html, added `step="any"` for allowing floating number
2. In `index` function, removed the check for mininmum 1 product