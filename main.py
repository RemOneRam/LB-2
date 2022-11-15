import requests
s_city ="Moscow,RU"
appid ="453937f3592fba4b07cd292212495270"
lat = "55.752304"
lon = "37.372393"
coord ="55.752304, 37.372393"
dt = "1668543495"

#res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                   #params={'q': s_city,'units':'metric','lang':'ru','APPID': appid})
#data = res.json()

#print("Город:", s_city)
#print("Погодные условия:", data['weather'][0]['description'])
#print("Температура:", data['main']['temp'])
#print("Минимальная температура:", data['main']['temp_min'])
#print("Максимальная температура", data['main']['temp_max'])

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': s_city,'units':'metric','lang':'ru','APPID': appid})
data = res.json()
print("Прогноз погоды на неделю:")
for i in data['list']:
        print("Дата <", i['dt_txt'], "> \r\nТемпература<",
            '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодныеусловия <",
            i['weather'][0]['description'], "> \r\n Скорость ветра<",
            i['wind']['speed'], "> \r\n Видимость<",
             i['visibility'], "> ")
        print("____________________________")


#res = requests.get("https://api.openweathermap.org/data/2.5/roadrisk",
 #                   params={'q': coord, 'dt':dt, 'weather.wind_speed':'weather.visibility','lang':'ru','APPID': appid})
#data = res.json()

#for i in data['list1']:
    #print("Скорость ветра:",data['main']['weather.wind_speed'])
    #print("Видимость:", data['main']['weather.visibility'])