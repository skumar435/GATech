## Query the data

import pandas as pd
import mysql.connector
import numpy as np

conn = mysql.connector.connect(host='localhost',
                            database='atlanta',
                            user='root',
                            password='password')

query = conn.cursor()
query.execute('select * from ( select  distinct name, price, rating, coordinates from atlanta.flight_view cross join atlanta.hotel_view cross join atlanta.restaurants_view where date_inbound = check_in and price_per_night *3  + min_price + price * 9 > 1200 and (price = 60 or price = 100) and date_outbound = check_out limit 20 ) as temp order by price, rating desc limit 10')
data = query.fetchall()
data = np.array(data)
data.shape
