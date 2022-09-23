# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 00:49:08 2022

@author: Manos
"""

import requests


class Apisys():  
    
    def __init__(self):
        self.done = False
        self.API_KEY = input("Input your API KEY: ")
        #My API_KEY is 219436cba7dd53cb@m135035 
    
    def menu(self):    
        print("Press 1 to add Product")
        print("Press 2 to add Supplier/Client")
        print("Press 3 to add InventoryLocation")
        print("Press 4 to add Tax")
        print("Press 5 to add Discount")
        print("Press 6 to place an order")
        print("Press any key to exit")
        self.choice  = int(input())
        if (self.choice == 1):
                print("You selected Products")
                url_product = "https://api.megaventory.com/v2017a/Product/ProductUpdate"
                self.p_sku = input("Enter SKU: ")
                self.p_description = input("Enter description: ")
                self.p_sales_price = float(input("Enter Sales Price: "))
                self.p_purchase_price = float(input("Enter Purchace Price:"))                
                ProductUpdate = {
                    "APIKEY": self.API_KEY,  
                    "mvProduct": {
                    "ProductSKU": self.p_sku,
                    "ProductDescription": self.p_description,
                    "ProductSellingPrice": self.p_sales_price,
                    "ProductPurchasePrice": self.p_purchase_price
                  },
                  "mvRecordAction": "Insert"
                }  
                r_product = requests.post(url_product, json = ProductUpdate)
                print(r_product.text)
                print("Updated")

        elif (self.choice == 2):
                print("You selected Supplier/Client")
                url_client = "https://api.megaventory.com/v2017a/SupplierClient/SupplierClientUpdate"
                self.sc_name = input("Enter Supplier/Client name: ")
                self.sc_address = input("Enter shipping adress: ")
                self.sc_phone = int(input("Enter Phone number: "))
                self.sc_email = input("Enter contact email: ")                
                SupplierClientUpdate = {
                    "APIKEY": self.API_KEY,
                    "mvSupplierClient": {
                    "SupplierClientName": self.sc_name,
                    "SupplierClientShippingAddress1": self.sc_address,
                    "SupplierClientPhone1": self.sc_phone,
                    "SupplierClientIM": self.sc_email
                  },
                  "mvRecordAction": "Insert"
                }
                r_client = requests.post(url_client, json = SupplierClientUpdate)
                print(r_client.text)
                print("Updated")
    
        elif (self.choice == 3):
                print("You selected InventoryLocation")
                url_inventory = "https://api.megaventory.com/v2017a/InventoryLocation/InventoryLocationUpdate"
                self.i_abbrevation = input("Enter Abbrevation: ")
                self.i_name = input("Enter location name: ")
                self.i_address = input("Enter location address")
                InventoryLocationUpdate	= {
                    "APIKEY": self.API_KEY,
                    "mvInventoryLocation":{
                    "InventoryLocationAbbreviation": self.i_abbrevation,
                    "InventoryLocationName": self.i_name,
                    "InventoryLocationAddress": self.i_address,
                    },
                    "mvRecordAction": "Insert"
                }
                r_inventory = requests.post(url_inventory, json = InventoryLocationUpdate)
                print(r_inventory.text)
                print("Updated")
                
        elif (self.choice == 4):
                print("You selected Tax")
                url_tax = "https://api.megaventory.com/v2017a/Tax/TaxUpdate"
                self.tax_name = input("Enter Tax name: ")
                self.tax_description = input("Enter Tax description: ")
                self.tax_value = float(input("Enter Tax Value: "))
                TaxUpdate = {
                    "APIKEY": self.API_KEY,
                    "mvTax":{
                    "TaxName": self.tax_name,
                    "TaxDescription": self.tax_description,
                    "TaxValue": self.tax_value
                    },
                    "mvRecordAction": "Insert"
                }                
                r_tax = requests.post(url_tax, json = TaxUpdate)
                print(r_tax.text)
                print("Updated")
    
        elif (self.choice == 5):
                print("You selected Discount")
                url_discount = "https://api.megaventory.com/v2017a/Discount/DiscountUpdate"
                self.dis_name = input("Enter Discount name: ")
                self.dis_description = input("Enter Discount description: ")
                self.dis_value = float(input("Enter Discount value: "))
                DiscountUpdate = {
                    "APIKEY": self.API_KEY,
                    "mvDiscount":{
                    "DiscountName": self.dis_name,
                    "DiscountDescription": self.dis_description,
                    "DiscountValue": self.dis_value
                    },
                    "mvRecordAction": "Insert",    
                }                
                r_discount = requests.post(url_discount, json = DiscountUpdate)
                print(r_discount.text)
                print("Updated")
                
        elif(self.choice == 6):
            print("You selected a Sales order")
            url_sales = "https://api.megaventory.com/v2017a/SalesOrder/SalesOrderUpdate"
            self.order_status = input("Enter order status: ")
            self.inventoryID = input("Enter Inventory Location ID (enter 0 if it is unknown): ")
            self.row_quantity = int(input("Enter row Quantity: "))
            SalesOrderUpdate = {
                "APIKEY": self.API_KEY,
                "mvSalesOrder": {
                "SalesOrderStatus": self.order_status,     #error
                "SalesOrderClientName": self.sc_name,
                "SalesOrderShippingAddress": self.sc_address, 
                "SalesOrderInventoryLocationID": self.inventoryID,
                "SalesOrderDetails": [
                    {
                        "SalesOrderRowProductSKU ": self.p_sku,
                        "SalesOrderRowQuantity ": self.row_quantity,
                        "SalesOrderRowTotalDiscountAmount": self.dis_value,
                        "SalesOrderTotalTaxAmount ": self.tax_value
                    }
                ]
                },
                "mvRecordAction": "Insert" 
            }
            r_salesOrder = requests.post(url_sales, json = SalesOrderUpdate)
            print(r_salesOrder.text)

        else:
            print("GoodBuy")
            self.done = True
           
    def loop(self):
        while not self.done:
            self.menu()
        
new_entry = Apisys()
new_entry.loop()


    
    