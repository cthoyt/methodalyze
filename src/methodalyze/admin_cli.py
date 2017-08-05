"""Administer the methodalyze DB.

Usage:
    methodctl users list [<statement_id>...]
    methodctl users add <username>
    methodctl users delete <user_id>...
    methodctl users deleteall
    methodctl statements list [<statement_id>...]
    methodctl statements add <statement>
    methodctl statements delete <statement_id>...
    methodctl statements deleteall
    methodctl methods list [<method_id>...]
    methodctl methods add <method_html>
    methodctl methods delete <method_id>...
    methodctl methods deleteall
    methodctl evaluations list [<evaluation_id>...]
    methodctl evaluations add
    methodctl evaluations delete <evaluation_id>...
    methodctl evaluations deleteall
    methodctl reset [-y]

Options:
    -y  Don't ask for confirmation. Dangerous!
"""
import sys

from docopt import docopt

from . import db


def main():
    args = docopt(__doc__)
    print(args, file=sys.stderr)

if __name__ == '__main__':
    sys.exit(main())