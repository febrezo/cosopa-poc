################################################################################
#
#    Copyright 2021 @ Félix Brezo (@febrezo)
#
#    This program is part of Cosopa. You can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
################################################################################

import argparse
from cryptography.fernet import Fernet
import sys

def encrypt_payload(file: str, key: bytes) -> bytes:
    with open(file, "rb") as input_file:
        message = input_file.read()
    return Fernet(key).encrypt(message)

def get_parser():
    """Defines the argument parser

    Returns:
        argparse.ArgumentParser.
    """
    parser = argparse.ArgumentParser(
        description= 'Cosopa | A Conditional Software Packing Python3 proof of concept.',
        prog='cosopa.py',
        add_help=False,
        conflict_handler='resolve'
    )

    parser.add_argument('-i', '--input', metavar='<PATH>', action='store', required=True, help='The path to the file to obfuscate.')
    parser.add_argument('-o', '--output', metavar='<PATH>', action='store', default="obfuscated.py", help='The path to the output file.')

    compare_group_about = parser.add_argument_group('About arguments', 'Showing additional information about this program.')
    compare_group_about.add_argument('-h', '--help', action='help', help='shows this help and exists.')
    compare_group_about.add_argument('--version', action='version', version=f'[%(prog)s] Cosopa 1.0', help='shows the version of the program and exits.')

    return parser

if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])
    print(f"[*] Generating random key…")
    key = Fernet.generate_key()  # store in a secure location
    print(f"[*] Random key generated as: {key.decode()}…")
    print(f"[*] Encrypting payload from '{args.input}' using the randomly generated key…")
    payload = encrypt_payload(args.input, key)
    print(f"[*] Building obfuscated Python file in '{args.target}'…")
    with open (args.target, "w") as target_file:
        target_file.write(f"import sys;from cryptography.fernet import Fernet as F;exec(F(sys.argv[1].encode()).decrypt({payload}).decode('utf-8'))")
    print(f"[*] You can know execute the payload using:\n\t$ 'python {args.target} {key.decode()}'.")
    print(f"[*] Note that a different offset will lead to execution errors. Use this wishfully.")

