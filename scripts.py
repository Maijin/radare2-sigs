import r2pipe
import sys, glob, os

os.mkdir("masm32")
for file in glob.glob(sys.argv[1]+"*.obj"):
    r2 = r2pipe.open(file)
    r2.cmd('f-entry0')
    r2.cmd('f-section..text')
    r2.cmd('f-sym..text')
    r2.cmd('f-section..text_0')
    r2.cmd('e zign.mincc=1')
    r2.cmd('aaa')
    r2.cmd('e zign.minsz=16')
    r2.cmd('zs '+ file[:-4].strip(sys.argv[1]+"/"))
    r2.cmd('zaF')
    r2.cmd('zos masm32/masm32.zig.sdb')
    r2.cmd('z >> masm32/masm32.zig.txt')
    r2.quit()
