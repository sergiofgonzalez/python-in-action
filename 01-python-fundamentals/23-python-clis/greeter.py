import argparse

parser = argparse.ArgumentParser(
    description='This program returns a greeting'
)

parser.add_argument(
    '-n', '--name', metavar='name', required=True,
    help='the person\'s name to greet'
)
parser.add_argument(
    '-t', '--type', metavar='greeting type', required=False,
    choices={'classic', 'modern'},
    help='the message type')

args = parser.parse_args()

if (not ('type' in args) or args.type == 'classic'):
    print(f'Hello to {args.name}!')
else:
    print(f'Top of the world to {args.name}!')
