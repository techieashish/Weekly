# Weekly
A simple script to download all the latest episodes of any  TV show by typing show name and season details.

#Libraries

1.	Requests | To install use :- pip install requests in the terminal

2.	Beautifulsoup | To install use :- pip install beautifusoup in the terminal.

Download ZIP file for the repository/Clone the repository.

#Usage
1.Use python3 Weeky.py

2.Downloaded file format .mp4

#To schedule the downloader to run weekly:-

For Ubuntu and other Linux versions

	Open Terminal, type crontab -e

	Add this at end of file :- @weekly DISPLAY=:0 xterm -e python3 /path/to/myfolder/Weeky.py

	Save changes in crontab -e and exit.





