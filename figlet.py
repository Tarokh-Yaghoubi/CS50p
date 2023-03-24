import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    inp = input("Input: ")
    sys.exit(figlet.renderText(inp))
 
if sys.argv[1] == '-f' or sys.argv[1] == '--font':
    if len(sys.argv) != 3:
        sys.exit("Invalid usage")
    
    o = figlet.getFonts()

    if sys.argv[2] not in o:
        sys.exit("Invalid usage")
    else:
        inp = input("Input: ")
        figlet.setFont(font=sys.argv[2])
        sys.exit(figlet.renderText(inp))

else: sys.exit("Invalid usage")