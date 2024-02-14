# **Using ICICIDirect Breeze APIs for options trading**

@Author: Rakesh Shinde

**DISCLAIMER:**

PLEASE USE AT YOUR OWN RISK.
This is my first attempt at python programming and I have literally coded these scripts only in a couple of hours. They have NOT been tested thoroughly. 
However, I have used successfully used them about 20+ times to place and cancel orders with several combinations.
You need to have a technical programming background to run this.
Also, if you are trying to take advantage of ICICIDirect's current scheme of zero brokerage for API orders then Remember to sign-up for 'Zero Brokerage API plan' before you use the scripts. Otherwise they charge brokerage even if you execute with APIs.

  
## setting up environment

Instructions to setup python environment are available here :
[Python Environment setup](https://pypi.org/project/breeze-connect/#virtualenv)
You need to install python, the virtual environment and also install modules as suggested in the documentation.

NOTE:
Site suggests using pip install breeze-connect==1.0.47
You may have to use an earlier version if you are receiving error with HTTPS SSL connection while executing scripts.

  ## Registering for breeze API usage
 - Go to ICICI API portal. [API Portal](https://api.icicidirect.com/apiuser/home)
 - Use the Login button and using your ICICIDirect credentials login to the portal
 -  Register your app
	 - Click on register an app
	 - For field 'App Name' enter MyApp (or any name you want)
	 - For field 'Redirect URL' enter http://127.0.0.1Hit Submit
	 - copy the Values of 'API Key' and 'Secret Key' in notepad
**DO NOT SHARE these values with anyone**

## Setting up scripts
 1. Create directory called 'breezepy' (or any other directory name)
 2. Copy all provided scripts and .json files to 'breezepy' directory

## Running the python scripts

 1. Open terminal window
 2. Activate virtual environment with the command
    source breeze_venv/bin/activate 
  3. Navigate to 'breezepy' directory (use cd command to navigate to your directory)

## Establishing a connection to breeze

	## STEP 1: Getting token from API Portal

 1. Go to ICICI API portal. [API Portal](https://api.icicidirect.com/apiuser/home)
 2. Use the Login button and using your ICICIDirect credentials login to the portal
 3. Click on 'View Apps'
	 Click the Login button in front of MyApp
	 Relogin using ICICIDirect credentials
	 on successful login the browser will navigate to page with URL:
	 
	

> http://127.0.0.1/?apisession=34539275  	(of course the value of
> apisession variable will be different for you)
> 
> 
> 
> Copy the value of apisession (in above example 34539275). This is your
> session token

	## STEP 2: Getting python script connection
	
 1. Navigate to 'breezepy' directory (use cd command to navigate to your directory)
 2. open file 'cred.json' in notepad (or any editor)
 3. copy the value of 'API Key', 'Secret Key' and apisession in the respective variables of cred.json file
	
	    {
	    		"session_token": "",
	    		"app_key": "",
	    		"secret_key": ""
	    	}
 4. Save the file

	    If not done already activate the breeze_venv by executing command 'source breeze_venv/bin/activate'

 5. Run command 'python cred.py'
 6. You should an output like

	    ====Breeze session Connected=======
	    https://api.icicidirect.com/apiuser/login?api_key=xxxxxxxxxxx

 7. You have been successful in connecting to breeze

## Placing order for 'OPTIONS' only

Placing order:

**PRE REQ :** Make sure you have been able to execute and connect to breeze API using instructions in section 'establishing a connection to breeze'

  	## STEP 1: Entering Order details

 1. Navigate to 'breezepy' directory. Open order_details.json
 2. The file contains the following details per order:

	    {
		    "stock_code" 		: "SCRIP Code"
		    "strike_price" 		: "Strike Price"
		    "expiry_date" 	: "Expiry Date"
		    "option_type" 	: "Option Type - Values are call or put"
		    "action" 				: "action - Values are buy or sell"
		    
		    "total_quantity" : "Total quantity you want to trade - remember to enter this in multiple of lot 				size for the scrip you are trading"
		    
		    "max_quantity_order" : "Max quantity you want to trade per order"  This has to be multiple of lot size and lower than equal to max quantity that ICICIDirect allows per order for the scrip you are trading. E.g. ICICIDirect allows max of 900 for CNXBAN per order"
		    
		    "order_type" : "order type - Values are limit or market"
		    "order_price" : "order_price - value is the trade price you want to trade at (only in case of limit order)"
	    }

 A Sample configuration is 

		{
			"Orders" : [
						{
							"stock_code" : "CNXBAN",
							"strike_price" : "54000",
							"expiry_date" : "2024-02-14",
							"option_type" : "call",
							"action" : "sell",
							"total_quantity" : "4500",
							"max_quantity_order" : "900",
							"order_type" : "limit",
							"order_price" : "0.40"
						}
					]
			}


 3. Save the file


		## STEP 2: Executing the order
		
1.  On command prompt navigate to 'breezepy' directory.
**activate the breeze_venv by executing command 'source breeze_venv/bin/activate' (This has to be done only once)**
2. Run command 'python loops.py'
3. If successfully executed the script will create a file called fullorder.json
4. Open the file using json editor (you can open online [Json Editor](https://jsoneditoronline.org/#left=local.natipe&right=local.cacoja)). You can look at the status of your execution.
5. Open ICICIDirect website and verify orders under F&O -> Order book. All successfully placed orders should be visible here.

  

	    Executing multiple orders in single run:

 1. Open order_details.json in editor
 2. Just enter comma separated order details like below:

	    {
	    "Orders" : [
			    {
			    "stock_code" : "CNXBAN",
			    "strike_price" : "54000",
			    "expiry_date" : "2024-02-14",
			    "option_type" : "call",
			    "action" : "sell",
			    "total_quantity" : "4500",
			    "max_quantity_order" : "900",
			    "order_type" : "limit",
			    "order_price" : "0.40"
			    },
			    {
			    "stock_code" : "CNXBAN",
			    "strike_price" : "53000",
			    "expiry_date" : "2024-02-14",
			    "option_type" : "call",
			    "action" : "sell",
			    "total_quantity" : "4500",
			    "max_quantity_order" : "900",
			    "order_type" : "limit",
			    "order_price" : "0.40"
			    }
		    ]
	    }

3. Save the file
4. Execute python loops.py

## Cancelling order for 'OPTIONS' only

		## STEP 1: Configure the orders to cancel

 1. Open 'ordercancel.json' in editor
 2. These are the possible values you can filter on :

	    {
		    "order_id": "202402132400013696",
		    "exchange_code": "NFO",
		    "stock_code": "CNXBAN",
		    "product_type": "Options",
		    "action": "Sell",
		    "order_type": "Limit",
		    "quantity": "900",
		    "price": "3.85",
		    "expiry_date": "21-Feb-2024",
		    "right": "Call",
		    "strike_price": 53000.0
	    }

3. Examples on how to configure the file

	EXAMPLE 1:
	To cancel an order for a specific scrip with a specific strike price you need to configure file like this:

	    {
		    "stock_code": "CNXBAN",
		    "strike_price": 53000.0,
		    "expiry_date": "21-Feb-2024"
	    }

	  EXAMPLE 2:
	  To cancel all open orders (no parameters are required hence only empty curly brackets)
	  
		{
		}

  4. Save the file

  


			## STEP 2: Executing the cancel order

 1.  On command prompt navigate to 'breezepy' directory.
**activate the breeze_venv by executing command 'source breeze_venv/bin/activate' (This has to be done only once)**
 2. Run command 'python cancel_open_orders.py'







