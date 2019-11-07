import sys
import re
import pandas as pd

def maskName(name):
    name = name.lower()
    return name[-2:] + '***' + name[0:2]

def maskEmail(email):
    first, last = email.split('@')[0], email.split('@')[1]

    first = first[0] + ('*' * 8) + first[-1]

    return first + '@' + last

def maskAddress(address):
    return ('*' * 3) + ' ' + ('*' * 6) 

def maskPhoneNumber(phoneNumber):
    # Remove any non-digits
    phoneNumber = re.sub("\D", "", phoneNumber)

    # Replace all digits except the last 4 with *
    return '*' * (len(phoneNumber) - 4) + str(phoneNumber[len(phoneNumber)-4:])

def main():

    customerDataFileName = 'tests/testOrders.csv'
    if (len(sys.argv) > 1):
        customerDataFileName = sys.argv[1]
    
    customerData = pd.read_csv(customerDataFileName)

    # names
    billingFirstName = customerData['First Name (Billing)']
    billingLastName = customerData['Last Name (Billing)']
    shippingFirstName = customerData['First Name (Shipping)']
    shippingLastName = customerData['Last Name (Shipping)']
    
    for i, billingFirst in enumerate(billingFirstName):
        customerData['First Name (Billing)'][i] = maskName(billingFirst)

    for i, billingLast in enumerate(billingLastName):
        customerData['Last Name (Billing)'][i] = maskName(billingLast)
    
    for i, shippingFirst in enumerate(shippingFirstName):
        customerData['First Name (Shipping)'][i] = maskName(shippingFirst)
    
    for i, shippingLast in enumerate(shippingLastName):
        customerData['Last Name (Shipping)'][i] = maskName(shippingLast)

    # phone numbers
    phoneNumbers = customerData['Phone (Billing)']  

    for i, phoneNumber in enumerate(phoneNumbers):
        customerData['Phone (Billing)'][i] = maskPhoneNumber(phoneNumber)

    # addresses
    addressBilling = customerData['Address 1&2 (Billing)']
    addressShipping = customerData['Address 1&2 (Shipping)']
    for i, billingAddress in enumerate(addressBilling):
        customerData['Address 1&2 (Billing)'][i] = maskAddress(billingAddress)
    
    for i, shippingAddress in enumerate(addressShipping):
        customerData['Address 1&2 (Shipping)'][i] = maskAddress(shippingAddress)
    
    for i, phoneNumber in enumerate(phoneNumbers):
        customerData['Phone (Billing)'][i] = maskPhoneNumber(phoneNumber)

    # emails
    emails = customerData['Email (Billing)']  
    
    for i, emails in enumerate(emails):
        customerData['Email (Billing)'][i] = maskEmail(emails)
    
    customerData.to_csv("orders_masked.csv", index=False, encoding='utf8')

if __name__ == '__main__': main()