#!/usr/bin/env python3

import subprocess

def genemarks2(fasta, output):

    type = 'bacteria'
    format = '--format gff3 --fnn ' + output + '.fnn ' + '--faa' + output + '.faa'
    subprocess.call(['gms2', '--seg', fasta, '--genome-type', type, '--output', output + '.gff', format])
