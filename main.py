from ascii_magic import AsciiArt
def main():
 print("----------Choose your fav character your the given below -------------")
 print("1.Doraemon")
 print("2.Pikachu")
 print("3.Shinchan")
 print("4.Gian")
 print("5.Nobita")
 print("6.Shizuka")
 print("7.Enter own picture ")
 a=int(input("Enter any number 1-7:"))
 if a==1:
   art = AsciiArt.from_image("2.png")
   art.to_terminal(columns=100)
 elif a==2:
   art = AsciiArt.from_image("1.png")
   art.to_terminal(columns=100)
 elif a==3:
   art = AsciiArt.from_image("4.jpeg")
   art.to_terminal(columns=100)
 elif a==4:
   art = AsciiArt.from_image("6.png")
   art.to_terminal(columns=100)
 elif a==5:
   art = AsciiArt.from_image("7.jpeg")
   art.to_terminal(columns=100)
 elif a==6:
   art = AsciiArt.from_image("sizuka.jpeg")
   art.to_terminal(columns=100)
 elif a==7:
   path=input("Enter the path where is your picture is Located")  
   art = AsciiArt.from_image(path)
   art.to_terminal(columns=100)
 else:
   print("character is not found") 
if __name__=="__main__":
  main()
