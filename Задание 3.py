try:
    n=int(input("Введите количество строк: "))
    country_city = [input() for _ in range(n)]
    if n>0:
        def f(n, country_city):
            dict = {}
            for line in country_city:
                parts = line.split()
                country = parts[0]
                cities = ''.join(parts[1:]).split(',')
                dict[country] = [city.strip() for city in cities]
            return dict

        def g(dict, city):
            for country, cities in dict.items():
                if city in cities:
                    return(country)
            return ""

        dict = f(n,country_city)
        city_search = input("Введите город, который необходимо найти: ")
        country = g(dict, city_search)
        if country:
            print(f"Город {city_search} находится в стране: {country}")
        else:
            print("")
    else:
        print("Введите натуральное значение для количества строк")
except:
    print("Неверно введено значение для количества строк")







