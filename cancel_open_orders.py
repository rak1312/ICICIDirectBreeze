
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
