code = {' ': '/', 'A':'._', 'B': '_...', 'C': '_._.',
          'D': '_..', 'E': '.', 'F': '.._.', 'G': '__.', 
          'H': '....', 'I': '..', 'J': '.___', 'K': '_._', 'L': '._..', 
          'M': '__', 'N': '_.', 'O': '---', 'P': '.__.', 'Q': '__._', 'R': '._.',
            'S': '...', 'T': '_', 'U': '.._', 'V': '..._', 'W': '.__', 
            'X': '_.._', 'Y': '_.__', 'Z': '__..', '1': '.____', '2': '..___', '3': '...__', 
            '4': '...._', '5': '.....', '6': '_....', '7': '__...', '8': '___...', '9': '____.', '0': '_____'}

message = input("Enter your message: ")
coded_message = ""

for i in message:
     coded_message += code[i.upper()]
print(coded_message)
