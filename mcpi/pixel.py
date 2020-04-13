from .minecraft import Minecraft
mc = Minecraft.create()

def Num_0(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[a, b, b, b, a],
              [a, b, a, b, a],
              [a, b, a, b, a],
              [a, b, a, b, a],
              [a, b, b, b, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def Num_1(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[a, a, b, a, a],
              [a, a, b, a, a],
              [a, a, b, a, a],
              [a, a, b, a, a],
              [a, a, b, a, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def Num_2(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[a, b, b, b, a],
              [a, a, a, b, a],
              [a, b, b, b, a],
              [a, b, a, a, a],
              [a, b, b, b, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def Num_3(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[a, b, b, b, a],
              [a, a, a, b, a],
              [a, b, b, b, a],
              [a, a, a, b, a],
              [a, b, b, b, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def Num_5(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[a, b, b, b, a],
              [a, b, a, a, a],
              [a, b, b, b, a],
              [a, a, a, b, a],
              [a, b, b, b, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def Num_6(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[a, b, a, a, a],
              [a, b, a, a, a],
              [a, b, b, b, a],
              [a, b, a, b, a],
              [a, b, b, b, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def Num_4(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[a, b, a, b, a],
              [a, b, a, b, a],
              [a, b, b, b, a],
              [a, a, a, b, a],
              [a, a, a, b, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def Num_9(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[a, b, b, b, a],
              [a, b, a, b, a],
              [a, b, b, b, a],
              [a, a, a, b, a],
              [a, a, a, b, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def Num_7(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[a, b, b, b, a],
              [a, a, a, b, a],
              [a, a, a, b, a],
              [a, a, a, b, a],
              [a, a, a, b, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def Num_8(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[a, b, b, b, a],
              [a, b, a, b, a],
              [a, b, b, b, a],
              [a, b, a, b, a],
              [a, b, b, b, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def A(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[a, b, b, b, a],
              [b, a, a, a, b],
              [b, b, b, b, b],
              [b, a, a, a, b],
              [b, a, a, a, b]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def B(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, b, b, b, a],
              [b, a, a, a, b],
              [b, b, b, b, b],
              [b, a, a, a, b],
              [b, b, b, b, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x



def C(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, b, b, b, b],
              [b, a, a, a, a],
              [b, a, a, a, a],
              [b, a, a, a, a],
              [b, b, b, b, b]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x



def D(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, b, b, b, a],
              [b, a, a, a, b],
              [b, a, a, a, b],
              [b, a, a, a, b],
              [b, b, b, b, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x



def E(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, b, b, b, b],
              [b, a, a, a, a],
              [b, b, b, b, a],
              [b, a, a, a, a],
              [b, b, b, b, b]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def F(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, b, b, b, b],
              [b, a, a, a, a],
              [b, b, b, b, a],
              [b, a, a, a, a],
              [b, a, a, a, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x



def G(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, b, b, b, b],
              [b, a, a, a, a],
              [b, a, a, b, b],
              [b, a, a, a, b],
              [b, b, b, b, b]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x



def H(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, a, a, a, b],
              [b, a, a, a, b],
              [b, b, b, b, b],
              [b, a, a, a, b],
              [b, a, a, a, b]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def I(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[a, b, b, b, a],
              [a, a, b, a, a],
              [a, a, b, a, a],
              [a, a, b, a, a],
              [a, b, b, b, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x



def J(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, b, b, b, b],
              [b, a, b, a, a],
              [a, a, b, a, a],
              [a, a, b, a, a],
              [b, b, b, a, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def K(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, b, b, b, b],
              [b, a, a, b, a],
              [b, b, b, a, a],
              [b, a, a, b, a],
              [b, a, a, a, b]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x



def L(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, a, a, a, a],
              [b, a, a, a, a],
              [b, a, a, a, a],
              [b, a, a, a, a],
              [b, b, b, b, b]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x



def M(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, a, a, a, b],
              [b, b, a, b, b],
              [b, a, b, a, b],
              [b, a, a, a, b],
              [b, a, a, a, b]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def N(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, a, a, a, b],
              [b, b, a, a, b],
              [b, a, b, a, b],
              [b, a, a, b, b],
              [b, a, a, a, b]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x



def O(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, b, b, b, b],
              [b, a, a, a, b],
              [b, a, a, a, b],
              [b, a, a, a, b],
              [b, b, b, b, b]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def P(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, b, b, b, b],
              [b, a, a, a, b],
              [b, b, b, b, b],
              [b, a, a, a, a],
              [b, a, a, a, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def Q(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, b, b, b, b],
              [b, a, a, a, b],
              [b, a, a, a, b],
              [b, a, a, b, a],
              [b, b, b, a, b]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x



def R(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, b, b, b, b],
              [b, a, a, a, b],
              [b, b, b, b, b],
              [b, a, a, b, a],
              [b, a, a, a, b]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def S(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, b, b, b, b],
              [b, a, a, a, a],
              [b, b, b, b, b],
              [a, a, a, a, b],
              [b, b, b, b, b]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x



def T(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, b, b, b, b],
              [a, a, b, a, a],
              [a, a, b, a, a],
              [a, a, b, a, a],
              [a, a, b, a, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x

def U(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, a, a, a, b],
              [b, a, a, a, b],
              [b, a, a, a, b],
              [b, a, a, a, b],
              [b, b, b, b, b]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x



def V(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, a, a, a, b],
              [b, a, a, a, b],
              [b, a, a, a, b],
              [a, b, a, b, a],
              [a, a, b, a, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x



def W(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, a, a, a, b],
              [b, a, a, a, b],
              [b, a, b, a, b],
              [b, b, a, b, b],
              [b, a, a, a, b]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x



def X(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, a, a, a, b],
              [a, b, a, b, a],
              [a, a, b, a, a],
              [a, b, a, b, a],
              [b, a, a, a, b]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x



def Y(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, a, a, a, b],
              [b, a, a, a, b],
              [a, b, b, b, a],
              [a, a, b, a, a],
              [a, a, b, a, a]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x



def Z(x, y, z, block):

    rec_x = x
    a = 0
    b = block

    blocks = [[b, b, b, b, b],
              [a, a, a, b, a],
              [a, a, b, a, a],
              [a, b, a, a, a],
              [b, b, b, b, b]
              ]

    for row in reversed(blocks):
        for block in row:
            mc.setBlock(x, y, z, block)
            x += 1
        y += 1
        x = rec_x


def draw(s: str, x, y, z, block):
    s = s.strip().upper()
    characterDict = {
        '0': Num_0,
        '1': Num_1,
        '2': Num_2,
        '3': Num_3,
        '4': Num_4,
        '5': Num_5,
        '6': Num_6,
        '7': Num_7,
        '8': Num_8,
        '9': Num_9,
        'A': A,
        'B': B,
        'C': C,
        'D': D,
        'E': E,
        'F': F,
        'G': G,
        'H': H,
        'I': I,
        'J': J,
        'K': K,
        'L': L,
        'M': M,
        'N': N,
        'O': O,
        'P': P,
        'Q': Q,
        'R': R,
        'S': S,
        'T': T,
        'U': U,
        'V': V,
        'W': W,
        'X': X,
        'Y': Y,
        'Z': Z
    }

    for i in range(len(s)):
        characterDict[s[i]](x + i*6, y, z, block)
        print(i)
    # for i in range(97, 123):
    #     print("'" + chr(i).upper() + "': " + chr(i).upper() + ",")
