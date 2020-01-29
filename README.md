# event_to_eps
Tutorial for changing Tensorboard event file to eps file

RUN: bash event_to_eps.sh
	Note: There are two python script in this .sh file
	The first one is changing event file to csv file, the second one is changing csv file to eps file.


Folder tree stricture:

event_to_eps
|
|__.
|__event
|__csv
|__eps
|__event_to_csv.py
|__csv_to_eps.py


event folder:	put event file
csv folder:		put csv file, changing from event file
eps folder:		put eps file, changing from csv file
event_to_csv.py change event file to csv file
csv_to_eps.py 	change csv file to eps file (which I wrote before)
-------------------------------------------------------
