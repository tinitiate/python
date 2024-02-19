import random
import time
import datetime
import json

def getBillID():
    format1 = "%Y%m%d%H%M%S"
    return datetime.datetime.today().strftime(format1)
    
def getBillDate():
    start = "01/01/2008 00:00:00"
    end = "01/01/2009 23:59:59"
    time_format = "%m/%d/%Y %H:%M:%S"
    prop = random.random()
    stime = time.mktime(time.strptime(start, time_format))
    etime = time.mktime(time.strptime(end, time_format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(time_format, time.localtime(ptime))

def getProductID():
    return random.randint(1,25)

def getStoreID():
    return random.randint(1,4)

def getQty():
    return random.randint(1,20)

#
l_bills_path = "D:/training/PythonFeb2024/code/python-assignments/billing\\bills\\"

while True:
    l_bill_id = getBillID()

    l_bill_json = { "BillID":l_bill_id
                   ,"BillDate":getBillDate()
                   ,"StoreID":getStoreID()
                   }
    l_bill_details  = []
    l_curr_products = []
    for c1 in range(random.randint(1,25)):
        l_prod_id = getProductID()
        if l_prod_id in l_curr_products:
            pass
        else:
            l_curr_products.append(l_prod_id)
            l_bill_line_item = {}
            
            l_bill_line_item["ProductID"]=l_prod_id
            l_bill_line_item["Quantity"]=getQty()
            l_bill_details.append(l_bill_line_item)

    l_bill_json["BillDetails"]=l_bill_details

    print(l_bill_json)

    new_file = open(l_bills_path+l_bill_id+".json", "w")
    new_file.write(json.dumps(l_bill_json))
    new_file.close()
    
    time.sleep(2)