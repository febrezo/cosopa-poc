# Conditional Software Packing: A Python PoC

This repository contains a tiny proof of concept to illustrate the concept of Conditional Software Packing as a potentially complementary MITRE ATT&CK technique to [T1027.02 Obfuscated Files or Information: Software Packing ](https://attack.mitre.org/techniques/T1027/002/).
This Proof of Concept is provided to illustrate the potentials of the technique using a GLP-ed `cosopa.py` file. To achieve the obfuscation, the built-in `cryptography` library is used.

Note that payloads will need Python3 to be installed in the target system to execute the payload, but this could be updated to different terminals.
No dependencies are required.

## Usage

Simply, clone the repository and launch `python3`:

```
python3 cosopa.py --help
usage: cosopa.py -i <PATH> [-o <PATH>] [-h] [--version]

Cosopa | A Conditional Software Packing Python3 proof of concept.

optional arguments:
  -i <PATH>, --input <PATH>
                        The path to the file to obfuscate.
  -o <PATH>, --output <PATH>
                        The path to the obfuscated file.

About arguments:
  Showing additional information about this program.

  -h, --help            shows this help and exists.
  --version             shows the version of the program and exits.
```

To create an obfuscated Python payload from a given `sample.py` file, the commands required are defined as follows

```bash
$ python3 cosopa.py -i example/sample.py
[*] Generating random key…
[*] Random key generated as: N6pjR_Su_NN9va2_HwYFiaq9am0N00YxGfnMV-i5Dqc=…
[*] Encrypting payload from 'example/sample.py' using the randomly generated key…
[*] OPTION 1: Building an obfuscated Python file in 'obfuscated.py'…
[*] You can know execute the payload using:
    python obfuscated.py N6pjR_Su_NN9va2_HwYFiaq9am0N00YxGfnMV-i5Dqc=.
[*] OPTION 2: Building obfuscated Python string to be copy-pasted in a terminal with Python
    python3 -c "import sys;from cryptography.fernet import Fernet as F;exec(F('N6pjR_Su_NN9va2_HwYFiaq9am0N00YxGfnMV-i5Dqc='.encode()).decrypt(b'gAAAAABidOg-FYIjAjtgOYqL0AuVSFlfp7Gg6rEx65gMeDikL0aGdNMZO0zXMOyXeZ_iLaknshIqyEFsN-OJmmz5Tjg1XbbAVciUJo4qYr7nAJulUzqJgdaatPRNV8PxHFveVdJFfCQwQvBUbtwt4oip5fCFveAghpHM_pvyKtNt1ahy9o6dZ5w=').decode('utf-8'))"
[*] Note that a different offset will lead to execution errors. Use this wishfully.
```

The resulting payload MIGHT be executed in any system using either native Python code.
The util can be launched either invoking the command or launching it via de command line.
Note that if dependencies are to be installed, the Python script used as payload might need to deal with them by itself.

