# Patrice Moracchini
# CSD-325
# city_functions.py
# this program returns three cities with different parameters and some are optional

def city_country (city, country, population=None, language=None):
    """Return a string formatted as one of
    -'City, Country'
    - 'City, Country - population 5000000'
    - 'City, Country - population 5000000, Language'
    """
    result = f"{city.title()}, {country.title()}"
              
    if population is not None:     
        result += f" - population: {population}"
    if language is not None:
        result += f", {language.title()}"
    
    return result

if __name__ == "__main__":
    # Example usage
    print(city_country("Santiago", "Chile"))
    print(city_country("Paris", "France",2148000,))
    print(city_country("Rome", "Italy",2873000, "Italian"))