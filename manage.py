import sys
from pdf_utils.join_pdfs import join_pdfs

def main(*args, **kwargs):
    cmds = list(args[0])
    if cmds[1] == 'run':
        if len(cmds) >= 3:
            if cmds[2] == 'join_pdfs':
                join_pdfs()

if __name__ == '__main__':
    main(sys.argv)