import replit
from rich.console import Console

console = Console()
usr = ""
readdchat = ""

def register():
  print("Registration\n")

  usr = input("Username: ")
  psw = input("Password: ")

  replit.db[usr] = psw

def login():
  print("Login\n")

  usr = input("Username: ")
  psw = input("Password: ")

  try:
    value = replit.db[usr]
    if(value == psw):
      print("Logged")
      return usr
    else:
      print("Impossible to login")
  except:
    print("Impossible to login")

def main():
  global console
  global usr
  global readdchat
  console.clear() 
  print("1) Login")
  print("2) Register")
  chs = input("\n")
  if(chs.lower().startswith("1")):
    console.clear()
    usr = login()
    console.clear()
    while(True):
      readdchat = replit.db["chat"]
      console.print(readdchat)
      message = input("Message: ")
      replit.db["chat"] = replit.db["chat"] + usr + ": " + message + "\n"
  elif(chs.lower().startswith("2")):
    console.clear()
    register()
    console.clear()
  else:
    console.clear()
    main()
  
main()