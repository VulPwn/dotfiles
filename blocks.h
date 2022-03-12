//Modify this file to change what commands output to your statusbar, and recompile using the make command.
static const Block blocks[] = {
	/*Icon*/	/*Command*/		/*Update Interval*/	/*Update Signal*/
	{"Thermal:",	"python ~/.config/scripts/thermal_check.py",		10,		0},

	{"Battery:", 	"python ~/.config/scripts/battery_check.py", 		60, 		0}, 

	{"CPU:",        "python ~/.config/scripts/cpu_check.py",                5,              0},

	{"Mem:", "free -h | awk '/^Mem/ { print $3\"/\"$2 }' | sed s/i//g",	30,		0},

	{"", "date '+%b %d (%a) %I:%M%p'",					5,		0},
};

//sets delimeter between status commands. NULL character ('\0') means no delimeter.
static char delim[] = " | ";
static unsigned int delimLen = 5;
