#!/usr/bin/env bash
rm result.txt

# Text Reset
RCol='\e[0m'

# Regular
Bla='\e[0;30m'
Red='\e[0;31m'
Gre='\e[0;32m'
Yel='\e[0;33m'
Blu='\e[0;34m'
Pur='\e[0;35m'
Cya='\e[0;36m'
Whi='\e[0;37m'

# Bold
BBla='\e[1;30m'
BRed='\e[1;31m'
BGre='\e[1;32m'
BYel='\e[1;33m'
BBlu='\e[1;34m'
BPur='\e[1;35m'
BCya='\e[1;36m'
BWhi='\e[1;37m'

# Underline
UBla='\e[4;30m'
URed='\e[4;31m'
UGre='\e[4;32m'
UYel='\e[4;33m'
UBlu='\e[4;34m'
UPur='\e[4;35m'
UCya='\e[4;36m'
UWhi='\e[4;37m'

# High Intensity
IBla='\e[0;90m'
IRed='\e[0;91m'
IGre='\e[0;92m'
IYel='\e[0;93m'
IBlu='\e[0;94m'
IPur='\e[0;95m'
ICya='\e[0;96m'
IWhi='\e[0;97m'

# Bold High Intens
BIBla='\e[1;90m'
BIRed='\e[1;91m'
BIGre='\e[1;92m'
BIYel='\e[1;93m'
BIBlu='\e[1;94m'
BIPur='\e[1;95m'
BICya='\e[1;96m'
BIWhi='\e[1;97m'

# Background
On_Bla='\e[40m'
On_Red='\e[41m'
On_Gre='\e[42m'
On_Yel='\e[43m'
On_Blu='\e[44m'
On_Pur='\e[45m'
On_Cya='\e[46m'
On_Whi='\e[47m'

# High Intensity Backgrounds
On_IBla='\e[0;100m'
On_IRed='\e[0;101m'
On_IGre='\e[0;102m'
On_IYel='\e[0;103m'
On_IBlu='\e[0;104m'
On_IPur='\e[0;105m'
On_ICya='\e[0;106m'
On_IWhi='\e[0;107m'

darkcyan="\e[1;36;40m"
black="\e[0;30;47m"
red="\e[0;31;47m"
green="\e[0;32;47m"
brown="\e[0;33;47m"
blue="\e[0;34;47m"
magenta="\e[0;35;47m"
cyan="\e[0;36;47m"
lightgray="\e[0;37;47m"
reset="\e[0m"

darkgray="\e[1;30;40m"
darkred="\e[1;31;40m"
darkgreen="\e[1;32;40m"
yellow="\e[1;33;40m"
darkblue="\e[1;34;40m"
darkmagenta="\e[1;35;40m"
white="\e[1;37;40m"


  function  colorize(){
    if [ $1 = "black" ]
      then mycolor=$black
    elif [ $1 = "red" ]
      then mycolor=$red
    elif [ $1 = "green" ]
      then mycolor=$green
    elif [ $1 = "brown" ]
      then mycolor=$brown
    elif [ $1 = "blue" ]
      then mycolor=$blue
    elif [ $1 = "magenta" ]
      then mycolor=$magenta
    elif [ $1 = "cyan" ]
      then mycolor=$cyan
    elif [ $1 = "lightgray" ]
      then mycolor=$lightgray
    elif [ $1 = "darkgray" ]
      then mycolor=$darkgray
    elif [ $1 = "darkred" ]
      then mycolor=$darkred
    elif [ $1 = "darkgreen" ]
      then mycolor=$darkgreen
    elif [ $1 = "yellow" ]
      then mycolor=$yellow
    elif [ $1 = "darkblue" ]
      then mycolor=$darkblue
    elif [ $1 = "darkmagenta" ]
      then mycolor=$darkmagenta
    elif [ $1 = "white" ]
      then mycolor=$white
    else
      mycolor=$white
    fi
    printf $mycolor"$2"
    printf $reset
    echo ""
  }





echo -e "\n"
true1=$(python3 capital_city.py Oregon)
true2=$(python3 capital_city.py Alabama)
true3=$(python3 capital_city.py "New Jersey")
true4=$(python3 capital_city.py Colorado)

true11=$(python3 capital_city.py oregon)
true12=$(python3 capital_city.py alabama)
true13=$(python3 capital_city.py "new Jersey")
true14=$(python3 capital_city.py colorado)

false1=$(python3 capital_city.py regon)
false2=$(python3 capital_city.py Aabama)
false3=$(python3 capital_city.py NewJersey)
false4=$(python3 capital_city.py Coorado)

false11=$(python3 capital_city.py Oregon_)
false12=$(python3 capital_city.py "")
false13=$(python3 capital_city.py " ")
false14=$(python3 capital_city.py Colordo)


result_true1="Salem"
result_true2="Montgomery"
result_true3="Trenton"
result_true4="Denver"

result_false="Unknown state"


if [ "$true1" != "$result_true1" ]
	then colorize "darkred" "FALSE"
	else colorize "darkgreen" "GOOD"
fi

if [ "$true2" != "$result_true2" ]
	then colorize "darkred" "FALSE"
	else colorize "darkgreen" "GOOD"
fi

if [ "$true3" != "$result_true3" ]
	then colorize "darkred" "FALSE"
	else colorize "darkgreen" "GOOD"
fi

if [ "$true4" != "$result_true4" ]
	then colorize "darkred" "FALSE"
	else colorize "darkgreen" "GOOD"
fi



if [ "$true11" != "$result_true1" ]
	then colorize "darkred" "FALSE"
	else colorize "darkgreen" "GOOD"
fi

if [ "$true12" != "$result_true2" ]
	then colorize "darkred" "FALSE"
	else colorize "darkgreen" "GOOD"
fi

if [ "$true13" != "$result_true3" ]
	then colorize "darkred" "FALSE"
	else colorize "darkgreen" "GOOD"
fi

if [ "$true14" != "$result_true4" ]
	then colorize "darkred" "FALSE"
	else colorize "darkgreen" "GOOD"
fi





if [ "$false1" != "$result_false" ]
	then colorize "darkred" "FALSE"
	else colorize "darkgreen" "GOOD"
fi

if [ "$false2" != "$result_false" ]
	then colorize "darkred" "FALSE"
	else colorize "darkgreen" "GOOD"
fi

if [ "$false3" != "$result_false" ]
	then colorize "darkred" "FALSE"
	else colorize "darkgreen" "GOOD"
fi

if [ "$false4" != "$result_false" ]
	then colorize "darkred" "FALSE"
	else colorize "darkgreen" "GOOD"
fi



if [ "$false11" != "$result_false" ]
	then colorize "darkred" "FALSE"
	else colorize "darkgreen" "GOOD"
fi

if [ "$false12" != "$result_false" ]
	then colorize "darkred" "FALSE"
	else colorize "darkgreen" "GOOD"
fi

if [ "$false13" != "$result_false" ]
	then colorize "darkred" "FALSE"
	else colorize "darkgreen" "GOOD"
fi

if [ "$false14" != "$result_false" ]
	then colorize "darkred" "FALSE"
	else colorize "darkgreen" "GOOD"
fi
