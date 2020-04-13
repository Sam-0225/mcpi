from .minecraft import Minecraft
mc = Minecraft.create()


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


