a = 'a'
e = 'e'
i = 'i'
o = 'o'
u = 'u' 


b = 'b'
c = 'c'
d = 'd'
f = 'f'
g = 'g'
h = 'h'
j = 'j'
k = 'k'
l = 'l'
m = 'm'
n = 'n'
p = 'p'
q = 'q'
r = 'r'
s = 's'
t = 't'
v = 'v'
w = 'w'
x = 'x'
y = 'y'
z = 'z'

def cc():
    sentence = input('> ')
    ac = (sentence.count(a))
    ec = (sentence.count(e))
    ic = (sentence.count(i))
    oc = (sentence.count(o))
    uc = (sentence.count(u))
    print('there are', ac + ec + ic + oc + uc, 'vowels in your sentence')
    bc = (sentence.count(b))
    cv = (sentence.count(c))
    dc = (sentence.count(d))
    fc = (sentence.count(f))
    gc = (sentence.count(g))
    hc = (sentence.count(h))
    jc = (sentence.count(j))
    kc = (sentence.count(k))
    lc = (sentence.count(l))
    mc = (sentence.count(m))
    nc = (sentence.count(n))
    pc = (sentence.count(p))
    qc = (sentence.count(q))
    rc = (sentence.count(r))
    sc = (sentence.count(s))
    tc = (sentence.count(t))
    vv = (sentence.count(v))
    wv = (sentence.count(w))
    xc = (sentence.count(x))
    yc = (sentence.count(y))
    zc = (sentence.count(z))
    print('there are', bc+cv+dc+fc+gc+hc+jc+kc+lc+mc+nc+pc+qc+rc+sc+tc+vv+wv+xc+yc+zc, 'consonants in your sentence')

cc()
   
