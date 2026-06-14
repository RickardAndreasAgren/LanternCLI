
from Hours.mood import Mood
from Hours.principles import AsPrinciple
from Light.above import TimeOfDay
from Space.weather import Weather
from Hours.seeker import Hour, Seek

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
  print("-.-")
  optionstest3 = ht3.optionsnear()
  print(optionstest3)
  optionstest4 = ht3.optionswithnear()
  print(optionstest4)
  print("-.-")
  asprinciple = AsPrinciple(ht3)
  print(asprinciple)
  return True

def testmood() -> bool:
  print("principle per mood:")
  mood2 = Mood.QUIET
  mood3 = Mood.RECEIVING
  mood4 = Mood.ARRIVING
  mood5 = Mood.LUMINOUS
  mood = Mood.TENDER
  principleseeker = Seek(when=TimeOfDay.now(), mood=mood)
  principleseeker.ensurehour()
  print(principleseeker.when)
  print(principleseeker.mood)
  print(principleseeker.hour)
  print(".")
  principleseeker2 = Seek(when=TimeOfDay.now(), mood=mood2)
  principleseeker2.ensurehour()
  print(principleseeker2.when)
  print(principleseeker2.mood)
  print(principleseeker2.hour)
  print(".")
  principleseeker3 = Seek(when=TimeOfDay.now(), mood=mood3)
  principleseeker3.ensurehour()
  print(principleseeker3.when)
  print(principleseeker3.mood)
  print(principleseeker3.hour)
  print(".")
  principleseeker4 = Seek(when=TimeOfDay.now(), mood=mood4)
  principleseeker4.ensurehour()
  print(principleseeker4.when)
  print(principleseeker4.mood)
  print(principleseeker4.hour)
  print(".")
  principleseeker5 = Seek(when=TimeOfDay.now(), mood=mood5)
  principleseeker5.ensurehour()
  print(principleseeker5.when)
  print(principleseeker5.mood)
  print(principleseeker5.hour)
  print(".")
  print("principle per time:")
  principleseeker2a = Seek(when=TimeOfDay.now())
  principleseeker2a.ensurehour()
  print(principleseeker2a.when)
  print(principleseeker2a.mood)
  print(principleseeker2a.hour)
  return True
  
def testjourney() -> bool:
  
  return True
  
def temper() -> None:
  testweather()
  print("========")
  testhour()
  print("========")
  testmood()
  print("========")
  print("========")
  testjourney()