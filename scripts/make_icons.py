import struct, zlib, os
def make_png(size):
    w=h=size; raw=b''; cx=cy=w//2; r=w*0.42
    for y in range(h):
        raw+=b'\x00'
        for x in range(w):
            dx,dy=x-cx,y-cy
            if (dx*dx+dy*dy)**0.5<r: raw+=bytes([245,197,24,255])
            else: raw+=bytes([26,26,26,255])
    comp=zlib.compress(raw,6)
    def chunk(n,d):
        c=zlib.crc32(n+d)&0xffffffff
        return struct.pack('>I',len(d))+n+d+struct.pack('>I',c)
    return b'\x89PNG\r\n\x1a\n'+chunk(b'IHDR',struct.pack('>IIBBBBB',w,h,8,6,0,0,0))+chunk(b'IDAT',comp)+chunk(b'IEND',b'')
for folder,size in [('mipmap-mdpi',48),('mipmap-hdpi',72),('mipmap-xhdpi',96),('mipmap-xxhdpi',144),('mipmap-xxxhdpi',192)]:
    path=f'app/src/main/res/{folder}/ic_launcher.png'
    os.makedirs(os.path.dirname(path),exist_ok=True)
    open(path,'wb').write(make_png(size))
print("Icons created")
