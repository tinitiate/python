class ShoppingCart:

    # Class Variables
    products = ( {"product_name":"Apple","Price":2}
                ,{"product_name":"Banana","Price":0.5}
                ,{"product_name":"Pear","Price":2}
                ,{"product_name":"Watermelon","Price":5}
                ,{"product_name":"Grapes","Price":6}
                ,{"product_name":"Orange","Price":3})

    cust_name = None
    cart = [] # [ {product_name:"Apple",Qty:100,Line_Item_Price:1000},{product_name:?,Qty:?,Line_Item_Price:?}
              #  ,{product_name:B,Qty:?,Line_Item_Price:?},{product_name:?,Qty:?,Line_Item_Price:?}]
    total_price = 0

    def check_product_in_cart(self,p_prod_name):
        product_not_incart_flg = True
        for item in self.cart:
            if item["product_name"] == p_prod_name:
                return True
        if product_not_incart_flg:
            return False

    # Return True if valid product or False for invalid product
    def is_product_valid(self,p_prod_name):
        # This variable will used to check if the input product is valid or not
        product_not_found_flg = True
        for p in self.products:
            if p["product_name"] == p_prod_name:
                return True
        if product_not_found_flg:
            print("Product",p_prod_name,"is invalid")
            return False

    def get_product_price(self,p_prod_name):
        # This variable will used to check if the input product is valid or not
        product_not_found_flg = True
        for p in self.products:
            if p["product_name"] == p_prod_name:
                product_not_found_flg = False
                return p["Price"]
            
        if product_not_found_flg:
            print("get_product_price: Input product",p_prod_name,"is invalid")


    # Class Functions
    def add_to_cart(self,p_prod_name,p_qty):
        if self.is_product_valid(p_prod_name):
            # if product exists in cart, Update QTY and Line Item Price
            if self.check_product_in_cart(p_prod_name):
                for item in self.cart:
                    if item["product_name"] == p_prod_name:
                        l_price = p_qty*self.get_product_price(p_prod_name)
                        item["Qty"] = item["Qty"]+p_qty
                        item["Line_Item_Price"] = item["Line_Item_Price"]+l_price
            # if product Doesnt exists in cart, Add ProductName, QTY and Line Item Price
            else:
                l_price = p_qty*self.get_product_price(p_prod_name)
                self.cart.append({"product_name":p_prod_name,"Qty":p_qty,"Line_Item_Price":l_price})


    def show_cart(self):
        print(self.cart)

    def remove_from_cart(self,p_prod_name,p_qty):
        for p in self.products:
            # 1. Validate the Product Name
            if p["product_name"] == p_prod_name:
                # 2. Check the cart for the product
                for c in self.cart:
                    if c["product_name"] == p_prod_name and p_qty >= c["Qty"]:
                        self.cart.remove({"product_name":c["product_name"]
                                          ,"Qty":c["Qty"]
                                          ,"Line_Item_Price":c["Line_Item_Price"]})
                    elif  c["product_name"] == p_prod_name and p_qty < c["Qty"]:
                       # IF qty to remove is < the Qty in cart
                       # 1. Remove qty
                       # 2. Update new price
                       c["Qty"] = c["Qty"]-p_qty
                       c["Line_Item_Price"] = c["Line_Item_Price"]-(p["Price"]*p_qty)

    def get_bill_total(self):
        for item in self.cart:
            self.total_price = self.total_price + item["Line_Item_Price"]
        print("Bill Total",self.total_price)
        # print("Bill Total "+str(self.total_price)) NOT [CONVERT self.total_price to STRING] print("Bill Total "+self.total_price)

cust1 = ShoppingCart()
cust1.cust_name="AAA"
cust1.add_to_cart("Onion",4)     # Error Scenario, COMPLETED
cust1.show_cart()
cust1.add_to_cart("Apple",2000)  # 
cust1.add_to_cart("Apple",2)     # FIX to include this scenario, adding to an existing product in cart
cust1.show_cart()
cust1.add_to_cart("Banana",3)
cust1.add_to_cart("Grapes",4)
cust1.show_cart()
cust1.remove_from_cart("Apple",100)
cust1.show_cart()
cust1.get_bill_total()


# cust2 = ShoppingCart()
# cust3 = ShoppingCart()
