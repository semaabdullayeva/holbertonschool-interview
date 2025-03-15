# Star Wars API

Install Node 10
```
https://intranet.hbtn.io/projects/2277#:~:text=%24%20curl%20%2DsL%20https%3A//deb.nodesource.com/setup_10.x%20%7C%20sudo%20%2DE%20bash%20%2D%0A%24%20sudo%20apt%2Dget%20install%20%2Dy%20nodejs
```
Install semi-standard

```
$ sudo npm install semistandard --global
```
Install request module and use it
```
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```
rite a script that prints all characters of a Star Wars movie:

The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name per line in the same order as the “characters” list in the /films/ endpoint
You must use the Star wars API
You must use the request module


```
alexa@ubuntu:~/$ ./0-starwars_characters.js 3
Luke Skywalker
C-3PO
R2-D2
Darth Vader
Leia Organa
Obi-Wan Kenobi
Chewbacca
Han Solo
Jabba Desilijic Tiure
Wedge Antilles
Yoda
Palpatine
Boba Fett
Lando Calrissian
Ackbar
Mon Mothma
Arvel Crynyd
Wicket Systri Warrick
Nien Nunb
Bib Fortuna
alexa@ubuntu:~/$ 
```
