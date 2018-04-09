import argparse


def listSnapshot(args):
	print args.snapshot

def shareSnapshot(args):
	print args.snapshot


parser = argparse.ArgumentParser()
parser.add_argument('--region', dest='region', default='us-east-1', help='AWS region to connect to')
parser.add_argument('--snapshot-id', dest='snapshot', required=True, help='snapshot ID')
subparsers = parser.add_subparsers(title='sub-commands', description='actions to execute')

parser_list_snapshot = subparsers.add_parser('list-snapshot', help='lists snapshot details')
parser_list_snapshot.set_defaults(func=listSnapshot)


parser_share_snapshot = subparsers.add_parser('share-snapshot', help='shares the snapshot with the specified AWS account')
parser_share_snapshot.set_defaults(func=shareSnapshot)
parser_share_snapshot.add_argument('--account-id', dest='account', required=True, help='AWS account ID with whom to share the snapshot')



args = parser.parse_args()
try:
	args.func(args)
except Exception as err:
	print str(err)



