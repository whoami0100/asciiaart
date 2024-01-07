from ascii_magic import AsciiArt
def main():
  a=input("enter your fav character:")
  if a=="doremon":
   art = AsciiArt.from_image("2.png")
   art.to_terminal(columns=150)
  elif a=="pikachu":
   art = AsciiArt.from_image("1.png")
   art.to_terminal(columns=150)
  elif a=="shinchan":
   art = AsciiArt.from_image("4.jpeg")
   art.to_terminal(columns=150)
  elif a=="gian":
   art = AsciiArt.from_image("6.png")
   art.to_terminal(columns=150)

  elif a=="nobita":
   art = AsciiArt.from_image("7.jpeg")
   art.to_terminal(columns=150)
  elif a=="gojo":
   art = AsciiArt.from_image("gojo.jpeg")
   art.to_terminal(columns=150)
  elif a=="sakuna":
   art = AsciiArt.from_image("sakuna.jpeg")
   art.to_terminal(columns=150)
  elif a=="shizuka":
   art = AsciiArt.from_image("sizuka.jpeg")
   art.to_terminal(columns=150)

  elif a=="itachi":
   art = AsciiArt.from_image("itachi1.jpeg")
   art.to_terminal(columns=150)
  else:
   print("character is not found")

if __name__=="__main__":
  main()
