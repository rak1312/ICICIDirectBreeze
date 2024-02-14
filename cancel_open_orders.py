
import datetime
import math
import json



def filter_custom(obj, *args):
    """
    Custom filter function that takes dynamic arguments.
    """
    # Perform filtering logic based on dynamic arguments
    #print("Filter obj" + str(obj))
    return all(obj.get(arg) == value for arg, value in args)


# Reading cancel order criteria from file ordercancel.json
'''
Possible Filter Values
{
        "order_id": "202402132400013696",
        "exchange_order_id": "1400000048534549",
        "exchange_code": "NFO",
        "stock_code": "CNXBAN",
        "product_type": "Options",
        "action": "Sell",
        "order_type": "Limit",
        "stoploss": "0",
        "quantity": "900",
        "price": "3.85",
        "validity": "Day",
        "disclosed_quantity": "0",
        "expiry_date": "21-Feb-2024",
        "right": "Call",
        "strike_price": 53000.0,
        "average_price": "0",
        "cancelled_quantity": "900",
        "pending_quantity": "900",
        "status": "Cancelled",
        "user_remark": null,
        "order_datetime": "13-Feb-2024 11:39:09",
        "parent_order_id": "",
        "modification_number": null,
        "exchange_acknowledgement_date": null,
        "SLTP_price": null,
        "exchange_acknowledge_number": null,
        "initial_limit": null,
        "intial_sltp": null,
        "LTP": null,
        "limit_offset": null,
        "mbc_flag": null,
        "cutoff_price": null,
        "validity_date": null
    }
'''
f = open ('./ordercancel.json', "r")
filter_cr = json.loads(f.read())
f.close()

#get breeze connection
from cred import breeze

response = breeze.get_order_list(exchange_code="NFO",
                        from_date=str(datetime.date.today())+"T06:00:00.000Z",
                        to_date=str(datetime.date.today())+"T06:00:00.000Z")

json_dict = dict(response)

f_c = filter_cr.items()

filtered_objects = list(filter(lambda obj: filter_custom(obj, *f_c), json_dict['Success']))

for i in filtered_objects:
    if i['status'] == 'Ordered':
        res2 = breeze.cancel_order(exchange_code="NFO",
                    order_id=i['order_id'])
        print ('Order Id [{}] : Cancellation Status [{}]'.format(i['order_id'],str(res2)))
    #else skip cancelling
    else:
        print ('Order cannot be cancelled. OrderId [{}] : Current Order Status [{}]'.format(i['order_id'],i['status']))
