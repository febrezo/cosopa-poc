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
$ python3 cosopa.py -i example/sample.py -o example/obfuscated.py 
[*] Generating random key…
[*] Random key generated as: LlEfXw3sKDZXPudw1nW_K7T1sRTpbaBY66wHnb11pWw=…
[*] Encrypting payload from 'example/sample.py' using the randomly generated key…
[*] Building obfuscated Python file in 'example/obfuscated.py'…
[*] You can know execute the payload using:
    $ 'python example/obfuscated.py LlEfXw3sKDZXPudw1nW_K7T1sRTpbaBY66wHnb11pWw='.
[*] Note that a different offset will lead to execution errors. Use this wishfully.
```

The resulting payload MIGHT be executed in any system using native Python code. Note that if dependencies are to be installed, the Python script used as payload might need to deal with them independently.

