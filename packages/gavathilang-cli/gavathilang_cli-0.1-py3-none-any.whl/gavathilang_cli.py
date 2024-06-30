#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
import os
import re
import argparse

def process_file(file_name):
    if not file_name.endswith('.gavathi'):
        print("Error: The file must have a .gavathi extension.")
        sys.exit(1)
        
    if os.path.exists(file_name):
        full_path = os.path.abspath(file_name)
    else:
        print("File does not exist.")
        sys.exit(1)

    with open(full_path) as file:
        if file.readline().strip() != 'hello gavathilang':
            raise ValueError("Error: starting of gavathilang should be 'hello gavathilang'")
        data = file.read()

    if data[-15:] != 'bye gavathilang':
        raise ValueError("Error: ending of gavathilang should be 'bye gavathilang'")

    keyword = {
        r'nahi tar jewha bhawa': 'elif',
        r'(bol naa bhawa)\s+': 'print',
        r'(hello gavathilang)\s+': '',
        r'(bye gavathilang)\s+': '',
        r'(bhawa he ahe)\s+': '',
        r'jewha bhawa': 'if',
        r'(asel)\s+': '',
        r'asel': '',
        r'jewha paryant bhawa': 'while',
        r'(ahe)\s+': '',
        r'ahe': '',
        r'(bhawa input de naa)\s+': 'input',
        r'(thamb bhawa)\s+': 'break',
        r'(chalu thew bhawa)\s+': 'continue',
        r'bye gavathilang': '',
        r'bol naa bhawa': 'print',
        r'nahi tar bhawa': 'else',
        r'nahi tar': 'else'
    }

    for pattern, replaceword in keyword.items():
        mypattern = re.compile(pattern=pattern)
        data = mypattern.sub(replaceword, data)
    
    exec(data)

def main():
    parser = argparse.ArgumentParser(description="GavathiLang CLI Tool")
    parser.add_argument("file_name", help="The .gavathi file to process")
    args = parser.parse_args()
    process_file(args.file_name)

if __name__ == "__main__":
    main()
