#!/usr/bin/env python3

"""
Appends or updates generated tables to documentation in mavlink/
Doesn't accept any arguments by design.
"""

from os import path as p
from datetime import datetime
import sys
import subprocess

# allow running from anywhere
root_p = p.dirname(__file__)

# clone the malvink repository
if not p.exists(p.join(root_p, 'mavlink-repo')):
    subprocess.check_call(
        ['git', 'clone', 'https://github.com/marsh-sim/mavlink.git', 'mavlink-repo'],
        cwd=root_p)

# update to latest commit on the dialect branch
subprocess.check_call(['git', 'checkout', 'origin/dialect'],
                      cwd=p.join(root_p, 'mavlink-repo'))

# get commit hash
mavlink_hash = subprocess.check_output(
    ['git', 'rev-parse', 'HEAD'],
    cwd=p.join(root_p, 'mavlink-repo')).decode().strip()

# install packages required by upstream generator script
subprocess.check_call([sys.executable, '-m', 'pip',
                      'install', 'lxml', 'requests', 'bs4'])

# run upstream generator
subprocess.check_call([sys.executable, 'mavlink_gitbook.py'],
                      cwd=p.join(root_p, 'mavlink-repo', 'doc'))

# append generated tables to each document
for dialect in ['minimal', 'marsh']:
    out_p = p.join(root_p, 'docs', 'mavlink', dialect + '.md')
    table_p = p.join(root_p, 'mavlink-repo', 'doc',
                     'messages', '_html', dialect + '.html')

    # TODO: select only messages and enums in the given file
    # subset_p = p.join(p.dirname(out_p), dialect + '_subset.txt')

    print('Appending tables to:', out_p)

    out_lines = []
    with open(out_p, 'r') as content_file:
        found_separator = False
        for line in content_file:
            if 'AUTO-GENERATED PART BELOW' in line:
                found_separator = True
                out_lines.append(line)
                break

            out_lines.append(line)
        if not found_separator:
            raise ValueError(
                'line with comment about auto-generated content required', out_p)

    date = datetime.now().replace(microsecond=0)
    out_lines.append('\n')
    out_lines.append(
        'Generated on {} from commit [{}](https://github.com/marsh-sim/mavlink/tree/{})\n'.format(
            date.isoformat(), mavlink_hash[:7], mavlink_hash
        ))
    out_lines.append('\n')

    with open(out_p, 'w') as out_file:
        out_file.writelines(out_lines)
        with open(table_p, 'r') as in_file:
            for line in in_file:
                out_file.write(line)
