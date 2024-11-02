import json
import os
import platform
import ctypes
from pystyle import Colors, Colorate, Center
import requests
import time

ctypes.windll.kernel32.SetConsoleTitleW("snusbase")

os.system("mode con cols=120 lines=30")

snusbase_auth = 'YOUR-KEY'
snusbase_api = 'https://api-experimental.snusbase.com/'

logo = """
                                                  *                                        
                                                 **                                         
                                                 **                                         
                                                 **                                         
   ****                 **   ****        ****    **                       ****              
  * **** * ***  ****     **    ***  *   * **** * ** ****       ****      * **** *    ***    
 **  ****   **** **** *  **     ****   **  ****  *** ***  *   * ***  *  **  ****    * ***   
****         **   ****   **      **   ****       **   ****   *   ****  ****        *   ***  
  ***        **    **    **      **     ***      **    **   **    **     ***      **    *** 
    ***      **    **    **      **       ***    **    **   **    **       ***    ********  
      ***    **    **    **      **         ***  **    **   **    **         ***  *******   
 ****  **    **    **    **      **    ****  **  **    **   **    **    ****  **  **        
* **** *     **    **     ******* **  * **** *   **    **   **    **   * **** *   ****    * 
   ****      ***   ***     *****   **    ****     *****      ***** **     ****     *******  
              ***   ***                            ***        ***   **              *****
"""
    
logo = Center.XCenter(logo)

def printascii():
    print(Colorate.Vertical(Colors.black_to_white, logo, 1))

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def send_request(url, body=None):
    headers = {'auth': snusbase_auth, 'content-type': 'application/json'}
    method = 'post' if body else 'get'
    data = json.dumps(body) if body else None
    response = requests.request(method, snusbase_api + url, headers=headers, data=data)
    return response.json()

def search_snusbase():
    term = input("enter search term: ")
    search_type = input("enter search type (email, username, lastip, hash, password, name): ")
    clear_screen()
    search_response = send_request('data/search', {'terms': [term], 'types': [search_type], 'wildcard': False})
    print("search results:")
    print(json.dumps(search_response, indent=4))

    save_option = input("do you want to save the results in a text file? (yes/no): ").lower()
    if save_option == 'yes':
        filename = f"{term}_search_results.txt"
        with open(filename, 'w') as file:
            file.write(json.dumps(search_response, indent=4))
    elif save_option != 'no':
        print("invalid option. results not saved.")

    clear_screen()
    
def get_snusbase_stats():
    clear_screen()
    stats_response = send_request('data/stats')
    print("snusbase statistics:")
    print(json.dumps(stats_response, indent=4))
    input("press enter to return to the main menu...")
    clear_screen()

def get_ip_whois():
    ip_address = input("enter ip address: ")
    clear_screen()
    ip_whois_response = send_request('tools/ip-whois', {'terms': [ip_address]})
    print("ip whois information:")
    print(json.dumps(ip_whois_response, indent=4))
    input("press enter to return to the main menu...")
    clear_screen()

def search_hash_lookup():
    hash_value = input("enter hash value: ")
    clear_screen()
    hash_lookup_response = send_request('tools/hash-lookup', {'terms': [hash_value], 'types': ["hash"]})
    print("hash lookup results:")
    print(json.dumps(hash_lookup_response, indent=4))
    input("press enter to return to the main menu...")
    clear_screen()

def main():
    while True:
        printascii()
        print(Center.XCenter("choose an option:"))
        print(Center.XCenter("1. search snusbase"))
        print(Center.XCenter("2. get snusbase statistics"))
        print(Center.XCenter("3. get ip whois information"))
        print(Center.XCenter("4. search hash lookup"))
        print(Center.XCenter("5. exit"))
        print(Center.XCenter("6. credits"))

        
        choice = input("enter your choice: ")

        if choice == '1':
            search_snusbase()
        elif choice == '2':
            get_snusbase_stats()
        elif choice == '3':
            get_ip_whois()
        elif choice == '4':
            search_hash_lookup()
        elif choice == '5':
            print("exiting...")
            break
        elif choice == '6':
            show_credits()
        else:
            print("invalid choice. please choose again.")
            time.sleep(1)
            clear_screen()

def show_credits():
    clear_screen()
    pentagram = r"""
                                                       . ...........                      
                                                    ..(%&%&&&&&&&%(##/#,..                
                                                ..(###,,,,.......*(%&%&%&%(..             
                                             ...&/&#&%%#@%/...,(%%...,,%&%&&@....         
                                           . .&&&/,......./(#%&,,.......,&&*@@@..         
                                           .(@/#&,. .. ..,(&&&&#... .....&&,,,&%..        
                                        ...&(...#,. ....*&%*.,,&&%......%%*....#/...      
                                        ..&%....(**....#&,......,%&%.,.#%(.....,#&..      
                                       ..#&.......&/*&%,.. ..  ....(#((#*.... ..#@#..     
                                       ..&@..  ...&&&(...  ..  .....,#&&/.... ../@&...    
                                       .*&@......,&&%(.... ... .....&(/%@&*...../&&...    
                                       .*&@....*%(,./((....... ...,#&*,,,*&&#.,./&#...    
                                       ..%%../(#,.,,,#&(,,,,,*//##&%&(&%@&&&@@%,&@ ...    
                                       ../&#(&@&@,@@&&&%(%/(//*,/#&(,,......,,,&&#.... .  
     .*. ,,..                          .  @@,.... . ..,*(%,....,%&%.... ......&@%..       
    ,. .  .,..                           . @(/.       ..%&*... *&#.... ..  ..%#(..        
    ,,    ,,.                                           .((*..#,,    ... ..(#(. . ..      
   ,,      ,                    .   .,.       . /,.     . ...... .    ..,#%#.......       
   .       .                    .  .*.       &# .,,#*.   .,  %. ..      ..               .
  ..      .. /               .     *         ,*    ..% .//     ,*,.                 ,.    
 ..       ,. *                    ..         .,      .   ..                               
...      ..                  ...  ..         .#               .        , .                
..       ,...   ...    .  .   .   .   . @.   ,@                &              .           
.        ....            /         .    ,.   *&      ,                          .,        
         ...                       .                                             ... .    
         ...                    *%                 ,,                                   , 
          ..                                                                              
    """
    print(Center.XCenter(pentagram))
    print(Center.XCenter("made by wren"))
    input(Center.XCenter("press enter to return to the main menu..."))
    clear_screen()



if __name__ == "__main__":
    main()
