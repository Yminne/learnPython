def convertFtoC (temperatureF):
    temperatureC = (float(temperatureF) - 32) * (5.0/9.0)
    return temperatureC
freezing = convertFtoC('60')
print('freezing = ',freezing,'C')