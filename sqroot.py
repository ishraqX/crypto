from Crypto.Util.number import long_to_bytes as l2b, getPrime, bytes_to_long as b2l, inverse

p = 159117138695601086935648462476725143896981591038416901486093706070754873563937272793294757366059667782136312013577603110660003394277897367203934519905683172161079448635248857040486200482627367334414675502994685936812333774063439076898281362682381888787053539531164627370506379676784327677612773681859553362469
a = 183170230465848410077175594145038110799
b = 177960951503783858139483105160729532851
c = 241771663291314104599898559749454094799
y = 81883801483428304918741984834363388238539421922474300691841915944763281416203781633389084991872486015041884084357260412052258732056118424392145242000539134316390251752292462492913837148154805999331901388735321855253311517735430229163344305926114721299791844599487270387540543138183327842649901510556454592197

inv = inverse(a, p)
inv2 = inverse(2 * a, p)

t1 = (y * inv) % p
t2 = (c * inv) % p
t3 = (b * inv2) % p
t3 = (t3 * t3) % p
k = (b * inv2) % p

y = (t1 - t2 + t3 + p) % p

# I googled for tonelli shanks implementation and this one came first
def legendre(a, p):
    return pow(a, (p - 1) // 2, p)

def tonelli(n, p):
    assert legendre(n, p) == 1, "not a square (mod p)"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r % p  # Corrected to take modulo p

s = tonelli(y, p) - k
if s < 0:
    s += p
print(l2b(s))

