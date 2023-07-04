import argparse

# Create a top-level parser
parser = argparse.ArgumentParser(description="Stack Overflow command-line", prog="so")
subparsers = parser.add_subparsers(help="Sub-commands")

# Create a parser for the question sub-command
parser_question = subparsers.add_parser("question", help="question help")
# Add sub-commands for the question sub-command
parser_question.add_argument("ask", help="ask a question")
parser_question.add_argument("search", help="search for a question")

# Create a parser for the answer sub-command
parser_answer = subparsers.add_parser("answer", help="answer help")
# Add sub-commands for the answer sub-command
parser_answer.add_argument("reply", help="reply to a question")
parser_answer.add_argument("vote", help="vote for an answer")

# Create a parser for the login sub-command
parser_login = subparsers.add_parser("login", help="login help")
# No sub-commands for the login sub-command

# Parse the arguments and perform the appropriate action
args = parser.parse_args()
if args.subcommand == "question":
    # Do something with the question sub-command arguments
    print(f"You asked: {args.ask}")
    print(f"You searched: {args.search}")
elif args.subcommand == "answer":
    # Do something with the answer sub-command arguments
    print(f"You replied: {args.reply}")
    print(f"You voted: {args.vote}")
elif args.subcommand == "login":
    # Do something with the login sub-command arguments
    print("You logged in")
elif args.subcommand == "":
    # No sub-command was given, print the usage message
    parser.print_usage()
