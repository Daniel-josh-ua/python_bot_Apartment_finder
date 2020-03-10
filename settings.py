import os
#Price preference
MIN_PRICE = 500
MAX_PRICE = 2000

## Location preferences

# The Craigslist site you want to search on.
CRAIGSLIST_SITE = 'essen'

# A list of neighborhoods and coordinates that you want to look for apartments in.This has been found using boundingbox.
# attached will be checked to see which area it is in.  If there's a match, it will be annotated with the area
# name.  If no match, the neighborhood field, which is a string, will be checked to see if it matches
# anything in NEIGHBORHOODS.
BOXES = {
    "kettwig": [
        [6.905093,51.347571],
        [6.986504,51.389321],
    ],
    "werden": [
        [7.001633107,51.3877813484],
        [7.0041087113,51.3891389602],
    ],
    "fischlaken": [
        [7.018624,51.384961],
        [7.045231,51.399207],
    ],
    "bredeney": [
        [6.982429,51.407561],
        [7.005432,51.417304],
    ],
    "heidhausen": [
        [7.01053,51.370003],
        [7.021688,51.377611],
    ],
}

# A list of neighborhood names to look for in the Craigslist neighborhood name field. If a listing doesn't fall into
# one of the boxes you defined, it will be checked to see if the neighborhood name it was listed under matches one
# of these.  This is less accurate than the boxes, because it relies on the owner to set the right neighborhood,
# but it also catches listings that don't have coordinates (many listings are missing this info).
NEIGHBORHOODS = ["kettwig", "werden", "fischlaken", "bredeney", "heidhausen"]

## Transit preferences

# The farthest you want to live from a transit stop.
MAX_TRANSIT_DIST = 2 # kilometers

# Transit stations you want to check against.  Every coordinate here will be checked against each listing,
# and the closest station name will be added to the result and posted into Slack.
TRANSIT_STATIONS = {
    "kettwig_stausee_station": [51.356507,6.938670],
    "essen_alte_Landstr": [51.528360,7.008000],
    "essen_werden_station": [51.388470,7.005360],
    "essen_hügel_station": [51.407270,7.010290],
    "essen_grenze_heidhausen": [51.375020,7.015640]
}

## Search type preferences

# The Craigslist section underneath housing that you want to search in.
# For instance, https://sfbay.craigslist.org/search/apa find apartments for rent.
# https://sfbay.craigslist.org/search/sub finds sublets.
# You only need the last 3 letters of the URLs.
CRAIGSLIST_HOUSING_SECTION = 'apa'

## System settings

# How long we should sleep between scrapes of Craigslist.
# Too fast may get rate limited.
# Too slow may miss listings.
SLEEP_INTERVAL = 20 * 60 # 20 minutes

# Which slack channel to post the listings into.
SLACK_CHANNEL = "#information-on-the-apartments-for-students"

# The token that allows us to connect to slack.
# Should be put in private.py, or set as an environment variable.
SLACK_TOKEN = os.getenv('SLACK_TOKEN', "xoxp-981803832497-991888701216-991915682245-3e659c608bd2823473a2e293493357f6")

# Any private settings are imported here.
try:
    from private import *
except Exception:
    pass

# Any external private settings are imported from here.
try:
    from config.private import *
except Exception:
    pass
