import re
import argparse

def check_email(input_lst):
    pat = re.compile (r'[-\w][-.\w]*@[-\w][-\w.]+[a-zA-Z]{2,4}') 
    res = []
    for i in input_lst:
        res.extend(pat.findall(i))
    return ' '.join(res)

parser = argparse.ArgumentParser(description="Email script")
parser.add_argument("-email", dest="email", nargs='+', help="check input email")

args = parser.parse_args()

message = check_email(args.email)
print('founded emails: ', message)