def city(city_name, country_name, population=''):
    if population:
        city_country = f"{city_name.title()}, {country_name.title()} - population {population}"
    else:
        city_country = f"{city_name.title()}, {country_name.title()}"
    return city_country

