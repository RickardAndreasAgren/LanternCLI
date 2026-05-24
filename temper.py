
from Space.weather import Weather
from Hours.principles import Hour

def testweather() -> bool:
  test = Weather()
  test.from_seasonandorvector()
  return True
  
def testhour() -> bool:
  ht1 = Hour.HEART
  ht2 = Hour.KNOCK
  ht3 = Hour.MOTH
  test = ht1.getnear()
  print(test)
  test2 = ht2.getnear()
  print(test2)
  test3 = ht3.getnear()
  print(test3)
  test4 = ht3.getwithnear()
  print(test4)
  return True
  
  
  
def temper() -> None:
  testweather()
  testhour()