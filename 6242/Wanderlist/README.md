# Wanderlist - A travel itinerary predictor

Wanderlist is a travel itinerary predictor capable of providing meaningful travel itinerary\
suggestions to users based on minimal input from users - primarily their budget and\
dates, and not provide every detail of their planned travel\

# Approaches
● Input dates and budget are taken and
returned are a combination of possible hotels,
restaurants and flights that a traveller could
take with a specific budget and clustered
according to ratings and price.\
● Seasonality analysis was carried out where we
plotted cost of different listing vs price, to
suggest the optimal time for vacation
optimised for a minimal budget.\
● Our tool is the first to provide a recommender
for planning a tour that combines flights,
hotels and restaurants data to provide an
itinerary thats optimised to be within a budget specified by the user.\

# Data and Tools used
● We downloaded the data corresponding to hotels and restaurant using API for popular websites like
Tripadvisor and Yelp.\
● We get flight information using API called skyscanner which gives the minimum prices and carrier Ids\
● Currently we collected data for 5 major cities of US (Atlanta, Miami, New York, LA , Philadelphia)\
● Since we are making predictions for future dates, we got temporal data by iterating predetermined start and
end dates of travel for next 6 months for our trial version\
