def input_file_read(input_111):
    fh1 = open(input_111,'r')
    lines = fh1.readlines()
    fh1.close()
    return lines
def output_file_write(string_lines,output_111):
    fh2 = open(output_111,'w')
    for lines in string_lines:
        fh2.write(lines)
    fh2.close()
    return string_lines
def upper_case_output(upper_case):
    output_upcase = []
    for uppercase in upper_case:
        up_output = uppercase.upper()
        output_upcase.append(up_output)
    return output_upcase
"""
input_file = "input_111.txt"
output_file = "output_111.txt"
lines_1 = input_file_read(input_file)
lines_2 = upper_case_output(lines_1)
output_file_write(lines_2,output_file)
"""
def n_function(i_file,o_file):
    input_file_1=i_file
    output_file_1=o_file
    s_lines=input_file_read(input_file_1)
    os_lines = upper_case_output(s_lines)
    output_file_write(os_lines,output_file_1)
    print(os_lines)

import sys
import getopt
opt = sys.argv[1:]

options,args = getopt.getopt(opt,"i:o:")
ip_file = ''
op_file=''
for o1,a1 in options:
    if o1 in ['-i']:
       print("input file name given is:",a1)
       ip_file = a1
    if o1 in ['-o']:
        print("output file name given is :",a1)
        op_file = a1
n_function(ip_file,op_file)
