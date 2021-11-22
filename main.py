import time
import os
import platform

os.system("title YouTube Revenue Calculator")

version = "v0.1"

curos = platform.system()

if curos != "linux":

    clear = "cls"
    os.system("mode con cols=60 lines=20")

if curos == "linux":

    clear = "clear"

options = ['1', '2', '3']

def main():

    print(f'''
    
\x1b[38;5;9mYouTube \x1b[0mAd Revenue Calculator By ChrisLad
{version}

Calculate Views Per Day [1]
Calculate Views Per Month [2]
Calculate Views Per Year [3]
    
    ''')
    
    option = input("\x1b[38;5;51m->\x1b[0m ")
    
    try:
    
        if option not in options:
        
            print("Invalid Option!")
            time.sleep(1)
            os.system(clear)
        
        if option == "1":
        
            mode = "day"
        
        if option == "2":
        
            mode = "month"
        
        if option == "3":
        
            mode = "year"
    
    
        rev = input(f"Views per {mode} -> ")
        
        
        def day(rev):
        
            day = int(rev) / 1000 * 2
        
            return day
        
        def month(rev):
        
            month = int(rev) / 1000 * 2
        
            return month
        
        def year(rev):
        
            year = int(rev) / 1000 * 2 
        
            return year
        
        print(f"\nRough Estimate Of Ad Revenue For The {mode}: \x1b[38;5;46m${month(rev)}\x1b[0m")
        
        input("\nPress \x1b[38;5;226mENTER\x1b[0m To Continue")
        
        os.system(clear)
    
    except NameError:
        pass
    except ValueError:
        pass

    main()

if __name__ == "__main__":

    main()