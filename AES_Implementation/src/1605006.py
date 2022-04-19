#from bitvector_demo import *
from time import time
from BitVector import *
Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

Mixer = [
    [BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03"), BitVector(hexstring="01")],
    [BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02"), BitVector(hexstring="03")],
    [BitVector(hexstring="03"), BitVector(hexstring="01"), BitVector(hexstring="01"), BitVector(hexstring="02")]
]

InvMixer = [
    [BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09")],
    [BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B"), BitVector(hexstring="0D")],
    [BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E"), BitVector(hexstring="0B")],
    [BitVector(hexstring="0B"), BitVector(hexstring="0D"), BitVector(hexstring="09"), BitVector(hexstring="0E")]
]

x=input("Enter the key: ")

print("Key: ",x,sep=" ")
print("Select Type: ","1.Plain Text","2.Any other object",sep=" ")
type=input()
if type=="1":
    text=input("Enter the plain text: ")
    print("Plain Text: ",text,sep=" ")
else:
    filename=input("Enter filename: ")
    str0=filename.split(".")[1]
    str1="1605006."+str0
    binaryFile=open(str1,'wb')
def readFile(filename):
    l=[]
    file = open(filename, 'rb')
    while True:
        byte = file.read(1)
        if byte:
            l.append(byte)
        else:
            break
    return l

def writeFile(binaryFile,byteList):
    for i in byteList:
        binaryFile.write(i)

def bytesToHex(byteList):
    list1=[]
    for j in byteList:
        c=j.hex()
        list1.append(c)
    return list1

def hexToBytes(hexList):
    li=[]
    for i in hexList:
        b=bytes.fromhex(i)
        li.append(b)
    return li
print("\n")
print("Key Scheduling: ")
q=16-len(x)
if q > 0:
    for j in range(q):
        x+="\0"


print("Round 0: ",end="")
list=[]
list1=[]
for i in x:
    h=format(ord(i),"x")
    list.append(h)
if q < 0:
    a=abs(q)
    for j in range(a):
        y=16
        list.pop(y)
        y+=1
    print(*list)
else:
    print(*list)
if type=="1":
    t=len(text)
else:
    byteList=readFile(filename)
    t=len(byteList)
d=(t//16)
m=t%16
if m!=0:
    m=16-m
if m==0:
    d-=1
for t in range(m):
    if type=="1":
        text+=" "
    else:
        byteList.append(bytes.fromhex("20"))

textList=[]
chunk=[[]]
if type=="1":
    for i in text:
        h=format(ord(i),"x")
        textList.append(h)
else:
    textList1=bytesToHex(byteList)
for t in range(d+1):
    if type=="1":
        chunk.append(textList[(t*16):((t+1)*16)])
    else:
        chunk.append(textList1[(t*16):((t+1)*16)])

state=[[0]*4 for i in range(4)]
keyList=[[]]
keyList0=[[0]*4 for i in range(4)]
for i in range(4):
    for j in range(4):
        keyList0[i][j]=list[i+(j*4)]



w0=list[0:4]
w1=list[4:8]
w2=list[8:12]
w3=list[12:16]
bg = w3[1::] + w3[:1:]

round1=[]
for j in bg:
    b = BitVector(hexstring=j)
    int_val = b.intValue()
    s = Sbox[int_val]
    s = BitVector(intVal=s, size=8)
    #print(s.get_bitvector_in_hex())
    round1.append(s.get_bitvector_in_hex())
#print(round1)
rc=["01"]
for i in range(1,4):
    rc.insert(i,"00")

gw3=[]
bv1=BitVector(hexstring=rc[0])

bv2=BitVector(hexstring=round1[0])

bv3=bv1^bv2

gw3.append(bv3.get_bitvector_in_hex())
#gw3.append((BitVector(hexstring=rc[0])^BitVector(hexstring=round1[0])).get_bitvector_in_hex())
for i in range(1,4):
    gw3.insert(i,round1[i])
#print(gw3)
start1=time()
for i in range(1,11):
    w4=[]
    w5=[]
    w6=[]
    w7=[]
    for j in range(4):
        w4.append((BitVector(hexstring=w0[j])^BitVector(hexstring=gw3[j])).get_bitvector_in_hex())
    for j in range(4):
        w5.append((BitVector(hexstring=w4[j])^BitVector(hexstring=w1[j])).get_bitvector_in_hex())
    for j in range(4):
        w6.append((BitVector(hexstring=w5[j])^BitVector(hexstring=w2[j])).get_bitvector_in_hex())
    for j in range(4):
        w7.append((BitVector(hexstring=w6[j])^BitVector(hexstring=w3[j])).get_bitvector_in_hex())
    round1stkey=w4+w5+w6+w7
    print("Round "+str(i)+": ",end="")
    print(*round1stkey)
    keyList.append(round1stkey)
    w0=w4
    w1=w5
    w2=w6
    w3=w7
    bg = w3[1::] + w3[:1:]

    round2=[]
    for j in bg:
        b = BitVector(hexstring=j)
        int_val = b.intValue()
        s = Sbox[int_val]
        s = BitVector(intVal=s, size=8)

        round2.append(s.get_bitvector_in_hex())

    AES_modulus = BitVector(bitstring='100011011')

    bv1 = BitVector(hexstring="02")
    bv2 = BitVector(hexstring=rc[0])
    bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
    rc[0]=bv3.get_bitvector_in_hex()

    gw3=[]
    gw3.append((BitVector(hexstring=rc[0])^BitVector(hexstring=round2[0])).get_bitvector_in_hex())
    for k in range(1,4):
        gw3.insert(k,round2[k])
end1=time()
t1=end1-start1
#for i in range(len(keyList)):
    #print(*keyList[i][:])
def xorOp(stateList,keyItemList):
    for i in range(4):
        for j in range(4):
            stateList[i][j]=(BitVector(hexstring=stateList[i][j])^BitVector(hexstring=keyItemList[i][j])).get_bitvector_in_hex()
    return stateList

def substitute(stateList):
    for i in range(4):
        for j in range(4):
            b = BitVector(hexstring=stateList[i][j])
            int_val = b.intValue()
            s = Sbox[int_val]
            s = BitVector(intVal=s, size=8)
            stateList[i][j]=s.get_bitvector_in_hex()
    return stateList

def LeftshiftRow(stateList):
    stateList[1][:]=stateList[1][1::] + stateList[1][:1:]
    stateList[2][:]=stateList[2][2::] + stateList[2][:2:]
    stateList[3][:]=stateList[3][3::] + stateList[3][:3:]
    return stateList


def multiplication(bv1,b):
    AES_modulus = BitVector(bitstring='100011011')

    bv2 = BitVector(hexstring=b)
    bv3 = bv1.gf_multiply_modular(bv2, AES_modulus, 8)
    return bv3
def mixColumn(stateList,mixerList):
    result=[[0]*4 for u in range(4)]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                if k==0:
                    result[i][j]=multiplication(mixerList[i][k],stateList[k][j]).get_bitvector_in_hex()
                else:
                    bv4=multiplication(mixerList[i][k],stateList[k][j])
                    bv5=BitVector(hexstring=result[i][j])
                    bv6=bv4^bv5
                    result[i][j]=bv6.get_bitvector_in_hex()

    return result

def RoundKeys(keyList,y):
    keyList1=[[0]*4 for v in range(4)]
    for i in range(4):
        for j in range(4):
            kl=keyList[y][:]

            keyList1[i][j]=kl[i+(j*4)]
    return keyList1
def cipherText(State):
    list=[]
    for u in range(16):
        list.append("0")
    for i in range(4):
        for j in range(4):
            list[i+(j*4)]=State[i][j]
    return list
def func(list):
    L=[[0]*4 for w in range(4)]
    for i in range(4):
        for j in range(4):
            L[i][j]=list[i+(j*4)]
    return L
def encryption(State,KeyList):
    for i in range(1,11):
        CState=substitute(State)
        CState=LeftshiftRow(CState)
        if i!=10:
            CState=mixColumn(CState,Mixer)
        CState=xorOp(CState,RoundKeys(KeyList,i))
        for u in range(4):
            for v in range(4):
                State[u][v]=CState[u][v]

    return CState
LISTS=[]
print("Cipher Text in Hex: ")
start2=time()
for p in range(1,d+2):
    for i in range(4):
        for j in range(4):
            state[i][j]=chunk[p][i+(j*4)]
            #state[i][j]=textList[i+(j*4)]
    currentState=xorOp(state,keyList0)
    NewState=encryption(currentState,keyList)
    cipherList=cipherText(NewState)
    LISTS.append(cipherList)
    print(" ",end="")
    print(*cipherList,end="")
end2=time()
t2=end2-start2
print("\n")
def Invsubstitute(stateList):
    for i in range(4):
        for j in range(4):
            b = BitVector(hexstring=stateList[i][j])
            int_val = b.intValue()
            s = InvSbox[int_val]
            s = BitVector(intVal=s, size=8)
            stateList[i][j]=s.get_bitvector_in_hex()
    return stateList
def RightshiftRow(stateList):
    stateList[1][:]=stateList[1][3::] + stateList[1][:3:]
    stateList[2][:]=stateList[2][2::] + stateList[2][:2:]
    stateList[3][:]=stateList[3][1::] + stateList[3][:1:]
    return stateList
def InvmixColumn(stateList,mixerList):
    result=[[0]*4 for u in range(4)]

    for i in range(4):
        for j in range(4):
            for k in range(4):
                if k==0:
                    result[i][j]=multiplication(mixerList[i][k],stateList[k][j]).get_bitvector_in_hex()
                else:
                    bv4=multiplication(mixerList[i][k],stateList[k][j])
                    bv5=BitVector(hexstring=result[i][j])
                    bv6=bv4^bv5
                    result[i][j]=bv6.get_bitvector_in_hex()

    return result

def decryption(State,KeyList):
    for i in range(1,11):
        CState=RightshiftRow(State)
        CState=Invsubstitute(CState)
        if i!=10:
            CState=xorOp(CState,RoundKeys(KeyList,10-i))
            CState=InvmixColumn(CState,InvMixer)
        else:
            CState=xorOp(CState,keyList0)
        for u in range(4):
            for v in range(4):
                State[u][v]=CState[u][v]

    return CState

stringList=[]
print("Deciphered Text in Hex: ")
start3=time()
for q in range(1,d+2):
    cstate=xorOp(func(LISTS[q-1]),RoundKeys(keyList,10))
    newState2=decryption(cstate,keyList)
    plainText=cipherText(newState2)
    print(" ",end="")
    print(*plainText,end="")
    for e in range(16):
        stringList.append(plainText[e])
    if type!="1":
        byteList1=hexToBytes(plainText)
        writeFile(binaryFile,byteList1)
end3=time()
if type!="1":
    binaryFile.close()
t3=end3-start3
print("\n")
if type=="1":
    print("Deciphered Text in ASCII: ")
    for i in stringList:
        str=bytes.fromhex(i).decode('utf-8')
        print(str,end="")
    print("\n")

print("Execution Time ")
print("Key Scheduling:",t1,"seconds",sep=" ")
print("Encryption Time:",t2,"seconds",sep=" ")
print("Decryption Time:",t3,"seconds",sep=" ")
