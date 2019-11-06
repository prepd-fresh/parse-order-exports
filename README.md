# Parse Weekly Order Exports

This tool is used to parse the order exports from Woocommerce to be used for further processing and order fulfillment.

## Build
In order to run this tool, Python 3.6 or greater is required.

1. Install the required python packages by running:
`python -m pip install -r requirements.txt`

2. Download or acquire the order.csv file which consists of the weekly order data and move it to the user_data folder.

3. Run the following command to start the program:
`python parse_order_exports.py`

4. The resulting WeeklyOrders.csv file will contain the results needed. Forward this information to the appropriate party.

## Development

Coming soon...
