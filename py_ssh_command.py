# Author: Christoph Giese @cgi1
# Short script to execute command over ssh - if you have suitable .ssh/config in place!

import traceback
from traceback import format_exc as fe

def call_command_ssh(hostname, command):
    output = b"NONE"
    try:
        import subprocess
        output = subprocess.Popen(command, shell=True,
                                  stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        print(f"Debug>call_command_ssh> Exec {command}. Output: {output}")
        return output
    except:
        print(f"Error>Failed to call_command_ssh({hostname}, {command}) {fe()}")
    finally:
        return output
