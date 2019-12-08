import requests

def get(appid, language='brazilian', printProgress=False):
    '''Request reviews from the Steam Web API and return them as a list. This is a blocking call that may take some time, depending on how many reviews there are.\n
    **appid** -- The Steam App ID as a string obtained from the game's store page URL\n
    **progress** -- Set to true to print the progress of each request.
    '''
    assert type(appid) is str

    def _makeRequest(appid, params):
        '''Helper function that sends a request to the Steam Web API and returns the response object.\n
        **appid** -- The Steam App ID obtained from the game's Store page URL\n
        **params** -- An object used to build the Steam API query. (https://partner.steamgames.com/doc/store/getreviews)
        '''
        
        response = requests.get(url=ENDPOINT+appid, params=params) # get the data from the endpoint
        return response.json() # return data extracted from the json response

    ENDPOINT = 'https://store.steampowered.com/appreviews/' # https://partner.steamgames.com/doc/store/getreviews
    results = []
    params = {
        'json': 1,
        'filter': 'recent', # sort by: recent, update
        'language': language, # languages at https://partner.steamgames.com/doc/store/localization
        'cursor': '*',
        'review_type': 'all', # all, positive, negative
        'purchase_type': 'all', # all, non_steam_purchase, steam
        'num_per_page': '100',
    }

    data = _makeRequest(appid, params)
    done = False

    count = 0

    try:
        total = data['query_summary']['total_reviews']
    except:
        return None
    
    while not done:
        if 'success' in data and data['success'] == 1: # if the query was successful
            if 'reviews' in data and data['query_summary']['num_reviews'] > 0: # if we received reviews
                results += data['reviews'] # add the reviews in this query to our results
                params['cursor'] = data['cursor'] # increase the start offset by the number of reviews received in this response
                count += data['query_summary']['num_reviews']
                if printProgress:
                    print('[%d/%d] reviews found...' % (count, total))
                #print(data['query_summary']['total_reviews'])
                data = _makeRequest(appid, params) # get the next page of reviews
            else: # there are no more reviews
                done = True
        elif data is None: # Steam Web API returns null if rate limit is reached.
            done = True
            raise ConnectionRefusedError('Steam Web API returned null. Rate limit may be exceeded.')
        else: # unsuccessful API call raises an error
            done = True
            raise ConnectionError('Steam Web API appreviews request was unsuccessful.')
    
    if printProgress:
        if len(results) > 0:
            print("Found all reviews.")
        else:
            print("0 reviews found.")
    
    return results
