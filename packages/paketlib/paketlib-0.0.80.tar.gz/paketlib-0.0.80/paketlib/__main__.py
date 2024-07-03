import pprint
from . import api, console, paket, path, pkcrypt, proto, search

shell = console.Console()

while True:
    shell.path = '~/paketlib/'
    shell.format = "(~bold~~path~~reset~) $ "
    shell.input()
    t_input = shell.inputstr.strip()
    if t_input == 'help':
        shell.print('help menu:\n\tip [ip] - ip search\n\tuserbox [authtoken] [query] - userbox search\n\tleakosint [token] [query] - leakosint search\n\tdbsearch [database] [query] - search in database\n\tgetmessage - get message from paketapi servers\n\tgetbootcode - get boot code from paketapi servers\n\thelp - show this menu')

    elif t_input.startswith('ip'):
        t_ip = t_input.split(' ')[-1].strip()
        for a, b in search.ipLookup(t_ip):
            shell.print(f'[+] {a}: {b}')

    elif t_input.startswith('userbox'):
        pprint.pprint(search.SearchUserBox(t_input.split(' ', 2)[2], t_input.split(' ', 2)[1]))

    elif t_input.startswith('leakosint'):
        search.SearchLeak(t_input.split(' ', 2)[2], t_input.split(' ', 2)[1])

    elif t_input.startswith('dbsearch'):
        search.dbsearch(t_input.split(' ', 2)[1], t_input.split(' ', 2)[2])

    elif t_input == 'getbootcode':
        shell.print(api.getbootcode())

    elif t_input == 'getmessage':
        shell.print(api.getmessage())

        