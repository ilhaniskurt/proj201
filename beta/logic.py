#
#   Script coded by İlhan Yavuz İskurt
#       ilhan.iskurt@sabanciuniv.edu
#

import parser

# Entry Point
def main():
  output = parser.getPickle(parser.PICKLE_NAME)
  print(output)

if __name__ == "__main__":
    main()