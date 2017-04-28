import r2pipe
import sys, glob, os

os.mkdir("masm32")
for file in glob.glob("obj/*.obj"):
    r2 = r2pipe.open(file)
    r2.cmd('f-entry0')
    r2.cmd('f-section..text')
    r2.cmd('f-sym..text')
    r2.cmd('f-section..text_0')
    r2.cmd('aaa')
    r2.cmd('zs '+ file[:-4].strip(sys.argv[1]+"/"))
    r2.cmd('zaF')
    r2.cmd('zos masm32/masm32.zig')
    r2.cmd('!gzip masm32/masm32.zig')
    r2.quit()
