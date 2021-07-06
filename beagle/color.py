from beagle import stomach

COLORS={
    'cyan':'\001\033[0;36m\002',
    'green':'\001\033[0;32m\002',
    'red':'\001\033[0;31m\002',
    'reset':'\001\033[0;0m\002',
    'yellow':'\001\033[0;33m\002',
    'purple':'\001\033[0;35m\002'
}

def success(message):
    message_color = COLORS['green']
    reset = COLORS['reset']
    print(f'{message_color}[+] {message}{reset}')

def error(message):
    message_color = COLORS['red']
    reset = COLORS['reset']
    print(f'{message_color}[-] {message}{reset}')

def normal(message):
    message_color = COLORS['reset']
    reset = COLORS['reset']
    print(f'{message_color}{message}{reset}')

def verbose(message, color):
    if stomach.verbose:
        color(f'{message}')
