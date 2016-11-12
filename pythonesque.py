import sys
import os
import subprocess
import re

def get_indent_level(line):
    if len(line.strip()) == 0:
        return -1
    index = 0
    while True:
        if line[index] == ' ':
            index += 1
        elif line[index] == '\t':
            index += 4
        else:
            break
    return index//4

filename = sys.argv[1]
original = [line.rstrip('\n') for line in open(filename)]
result = []

indent_level = -1

for index in range(len(original) - 1):
    line = original[index]
    next_indent_level = -1
    inc = 1
    while next_indent_level == -1 and index + inc < len(original):
        next_indent_level = get_indent_level(original[index + inc])
        inc += 1
    beginning = line.lstrip()

    if len(beginning) == 0:
        result.append('')
    elif beginning[0] == '#':
        result.append(line)
    elif beginning[0:4] == 'def ':
        if 'main' not in line:
            result.append('auto ' + beginning[4:len(beginning) - 1] + ' {')
        else:
            result.append('int ' + beginning[4:len(beginning) - 1] + ' {')
        indent_level += 1
    elif re.match('^\s?\S+\s?=\s?\S+$', beginning):
        result.append(('    ' * indent_level) + 'auto ' + beginning + ';')
    else:
        ends_with_colon = line[len(line)-1] == ':'
        if ends_with_colon and 'else' not in line:
            line = line[:len(line)-1].replace('if ', 'if (', 1).replace('while ', 'while (', 1).replace('for ', 'for (', 1) + ')'
        line = line.replace('else:','else',1)

        if next_indent_level > indent_level:
            updated = line + ' {'
            indent_level = next_indent_level
        elif next_indent_level < indent_level and next_indent_level >= 0:
            updated = line + ';\n'
            i = indent_level - 1
            while i >= next_indent_level:
                updated = updated + ('    ' * i) + '}\n'
                i -= 1
            indent_level = next_indent_level
        else:
            updated = line + ';'

        result.append(updated)

while indent_level > 0:
    indent_level -= 1
    result.append('}')

out_filename = 'out' + filename
output = open(out_filename, 'w')
for line in result:
    output.write('%s\n' % line)

# subprocess.Popen(['g++', out_filename]).wait()
