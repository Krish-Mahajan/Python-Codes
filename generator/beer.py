


def beerDataGenerator():
    file = "recipeData.csv"
    for row in open(file, encoding="ISO-8859-1"):
        yield row



if __name__ == '__main__':  
    
    beer_data = "recipeData.csv"
    lines = (line for line in open(beer_data,encoding="ISO-8859-1")) 
    lists = (l.split(",") for l in lines)
    columns = next(lists)    
    beerdicts = (dict(zip(columns,data)) for data in lists )
    '''
    beer_counts = {}
    for bd in beerdicts:
        if bd["Style"] not in beer_counts:
            beer_counts[bd["Style"]] = 1
        else:
            beer_counts[bd["Style"]] +=1 
            
    most_popular = 0 
    most_popular_type = None
    for beer , count in beer_counts.items():
        if count > most_popular :
            most_popular = count 
            most_popular_type = beer 
            
    print("{} is the most popular beer with {} count".format(most_popular_type,most_popular))
    '''
    abv = (float(bd["ABV"]) for bd in beerdicts if bd["Style"] == "American IPA")
    print(sum(abv))

        