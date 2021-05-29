BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

print(RED,"this will be in red")
print("and so is this")

def colour_print(text:str, effect:str) -> None:
    """Print 'text' using ANSI sequences to change colour, etc

    Args:
        text {str}: The text to print
        effect {str}: The effect we want
    """
    output_string = "{0}{1}{2}".format(effect,text,RESET)
    print(output_string)

colour_print("Hello , Red",RED)

print("This should be in the default terminal colour")
colour_print("Hello,Blue",BLUE)
colour_print("Hello,Yellow",YELLOW)
colour_print("Hello,Bold",BOLD)
colour_print("Hello,Underline",UNDERLINE)
colour_print("Hello,Reverse",REVERSE)
colour_print("Hello,Black",BLACK)

