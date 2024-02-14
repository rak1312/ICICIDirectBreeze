
import datetime
import math
import copy

#get breeze connection
from cred import breeze



import json
# JSON file
f = open ('./order_details.json', "r")

# Reading from file
data = json.loads(f.read())

full_orders_list = []


for i in data['Orders']:
    #Get the Current Order
    stock_code = i['stock_code']
    total_quantity = int(i['total_quantity'])
    max_quantity = int(i['max_quantity_order'])
    action = i['action']
    strike_price = i['strike_price']

    option_type = i['option_type']
    price = i['order_price']
    expiry_date = i['expiry_date']
    order_type = i['order_type']
    
    print("---------- This is the order getting executed  ---------------------")
    print(json.dumps(i,indent=4))

    #Store order instance
    order_getting_exec = dict()
    order_getting_exec['orderitt'] = dict(i)
    
    #Current order will have multiple part orders based on max qty and split Qty
    order_part_order=[]
    dict_part_order1 = dict()
    dict_part_order1['part_order_itt'] = 1
    dict_part_order1['part_order'] = copy.deepcopy(dict(i))
    del dict_part_order1['part_order']['total_quantity']
    del dict_part_order1['part_order']['max_quantity_order']
    
    u = int(i['total_quantity'])
    order_itt = 1
    while u >0 :
        #current Order getting Executed
        dict_part_order = copy.deepcopy(dict_part_order1)
        dict_part_order['part_order_itt'] = order_itt
        dict_part_order ['part_order']['quantity'] = "" + str(min(u, max_quantity))

        response = breeze.place_order(stock_code=stock_code,
                        action=action,
                        strike_price=strike_price,
                        right=option_type,
                        price=price,
                        expiry_date=expiry_date+"T06:00:00.000Z",
                        validity="day",
                        order_type=order_type,
                        quantity=str(min(u, max_quantity)),
                        validity_date=str(datetime.date.today())+"T06:00:00.000Z",
                        stoploss="",
                        disclosed_quantity="0",
                        exchange_code="NFO",
                        product="options")
        
        u -= int(i['max_quantity_order'])
        
        order_itt +=1
        dict_part_order ['order_status'] = response
        
        order_part_order.append(dict(dict_part_order))
    order_getting_exec['orderitt'] = dict(i)
    order_getting_exec['part_orders'] = list(order_part_order)
    full_orders_list.append(order_getting_exec)

f.close()

#Print full order to Json file
ffull = open('./fullorder.json','w')

print('{ "Orders": [ ', file=ffull)
str_order_comma = ""
for i in full_orders_list:
    cd = dict(i)
    #print(cd['orderitt'])
    print(str_order_comma + '{"Fullorder": ' + json.dumps(cd['orderitt']) + ",", file=ffull)
    str_order_comma = ","
    str_part_order = '"part_orders": ['
    str_part_comma = ""
    for y in cd['part_orders']:
        str_part_order = str_part_order + str_part_comma + json.dumps(y, indent=4)  
        str_part_comma = ","
    str_part_order = str_part_order + "]}"
    print(str_part_order, file=ffull)
print(']}', file=ffull)
ffull.close()


