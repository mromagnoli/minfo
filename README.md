#mInfo (Movie info)

This is a peronal-hobby-self-training Python script intended to get all movie files in a directory and retrieve its IMDB ratings using the great [Open Movie DataBase (OMDB) Api](http://www.omdbapi.com/).

##Usage
###Set script to use it system wide
- Put the `minfo.py` file in some of your PATH dirs, for example `/usr/local/sbin`
- `$ sudo mv minfo.py minfo`
- `$ sudo chmod +x minfo`

###Getting ratings from your movies directory
- Get into your movies directory (or files of any kind with movies names)
- Execute `$ minfo`  
**Caution**: Your files names should not include *dots* except for the file extension.


###Getting special movies ratings
- From any dir execute `$ minfo -m MOVIENAME[, ...]`  
**Example:** `$ minfo -m frozen`  
**Example:** `$ minfo -m "Requiem for a dream,Terminator,World War Z"`



**TODO**

- Expand data retriving more info such as plot, actors, etc...
