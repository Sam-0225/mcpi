# CodingAPE Minecraft × Python curriculum
[CodingAPE 猿創力程式設計學校](https://www.codingapeschool.com/)</br>
[2018猿創力Minecraft程式冬令營-初階](https://www.codingapeschool.com/camp/minecraft)</br>
[2018猿創力Minecraft程式冬令營-進階](https://www.codingapeschool.com/camp/adv-minecraft)</br>
[2018猿創力Minecraft程式冬令營 Python](https://www.codingapeschool.com/camp/python/)</br>

## <a href='https://github.com/TeachCraft/TeachCraft-Examples/tree/master/minecraftstuff'>minecraftstuff</a> library [From Martin O'Hanlon, <a href='https://github.com/martinohanlon/minecraft-stuff'>repo</a>, <a href='http://www.stuffaboutcode.com/p/minecraft.html'>website</a>, <a href='https://www.amazon.com/gp/product/111894691X/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=111894691X&linkCode=as2&tag=teachcraft-20&linkId=62f6ef5032275ace368045b4b7535c8f'>book</a>]

#### minecraftstuff.MinecraftTurtle

- <a href='http://minecraft-stuff.readthedocs.io/en/latest/minecraftturtle.html#id1'>Official Documentation</a>

<details>
  <summary>
turtle = MinecraftTurtle(mc, pos)
  </summary>

> Create a Minecraft Turtle

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

```

</details>


<details>
  <summary>
turtle.forward(distance)
  </summary>

> Move turtle forward [distance] number of blocks

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

# Move turtle forward 5 blocks
turtle.forward(5)

```

</details>

<details>
  <summary>
turtle.backward(distance)
  </summary>

> Move turtle backward [distance] number of blocks

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.backward(10)

```

</details>

<details>
  <summary>
turtle.right(distance)
  </summary>

> Move turtle right [distance] number of blocks

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.right(10)

```

</details>

<details>
  <summary>
turtle.left(distance)
  </summary>

> Move turtle left [distance] number of blocks

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.left(10)

```

</details>


<details>
  <summary>
turtle.up(distance)
  </summary>

> Move turtle up [distance] number of blocks

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.up(10)

```

</details>

<details>
  <summary>
turtle.down(distance)
  </summary>

> Move turtle down [distance] number of blocks

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.down(10)

```

</details>

<details>
  <summary>
turtle.home()
  </summary>

> Move turtle back to the position it started in

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.down(10)
turtle.right(10)
turtle.home()

```

</details>

<details>
  <summary>
turtle.speed(integer)
  </summary>

> Change the turtles speed (1 - slowest, 10 - fastest, 0 - no animation, it just draws the lines)

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.speed(5)
turtle.down(10)
turtle.speed(10)
turtle.right(10)
turtle.home()

```

</details>


<details>
  <summary>
turtle.penblock(block_id, [block_data])
  </summary>

> Change the turtles speed (1 - slowest, 10 - fastest, 0 - no animation, it just draws the lines)

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

grass_block_id = 2
turtle.penblock(grass_block_id)
turtle.down(10)

wool_block_id = 35
wool_block_data = 1 #orange

turtle.penblock(wool_block_id, wool_block_data)
turtle.right(10)

```

</details>

<details>
  <summary>
turtle.penup()
  </summary>

> Put the pen up (stop drawing when the turtle moves)

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.down(10)

turtle.penup()

turtle.right(10)

```

</details>

<details>
  <summary>
turtle.pendown()
  </summary>

> Put the pen down (start drawing again when the turtle moves after you called turtle.penup())

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.down(10)

turtle.pendown()

turtle.right(10)

turtle.penup()

turtle.up(10)

```

</details>

<details>
  <summary>
turtle.isdown()
  </summary>

> Check if the pen is down, returning a boolean

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle
turtle = MinecraftTurtle(mc, pos)

turtle.down(10)

turtle.pendown()

turtle.right(10)

if turtle.isdown():
    print "Pen is down!"

```

</details>


<details>
  <summary>
turtle.setposition(x, y, z)
  </summary>

> Reset turtle's position to a given x/y/z coordinate

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle at player's current position
turtle = MinecraftTurtle(mc, pos)

turtle.down(10)

turtle.right(10)

# Have turtle reset back to player's position
turtle.setposition(pos.x, pos.y, pos.z)

```

</details>

<details>
  <summary>
turtle.setx(x)
  </summary>

> Reset turtle's position to a given x coordinate

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle at player's current position
turtle = MinecraftTurtle(mc, pos)

turtle.down(10)

turtle.right(10)

# Have turtle reset back to player's x position
turtle.setx(pos.x)

```

</details>

<details>
  <summary>
turtle.sety(y)
  </summary>

> Reset turtle's position to a given y coordinate

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle at player's current position
turtle = MinecraftTurtle(mc, pos)

turtle.down(10)

turtle.right(10)

# Have turtle reset back to player's y position
turtle.setx(pos.y)

```

</details>

<details>
  <summary>
turtle.setz(z)
  </summary>

> Reset turtle's position to a given z coordinate

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle at player's current position
turtle = MinecraftTurtle(mc, pos)

turtle.down(10)

turtle.right(10)

# Have turtle reset back to player's z position
turtle.setx(pos.z)

```

</details>

<details>
  <summary>
turtle.position
  </summary>

> Retrieve turtle's current x/y/z position

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle at player's current position
turtle = MinecraftTurtle(mc, pos)

turtlePos = turtle.position
print turtlePos.x
print turtlePos.y
print turtlePos.z


```

</details>

<details>
  <summary>
turtle.setheading(angle)
  </summary>

> Set the turtles headings

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle at player's current position
turtle = MinecraftTurtle(mc, pos)

turtle.setheading(90)

```

</details>


<details>
  <summary>
turtle.setverticalheading(angle)
  </summary>

> Set the turtles vertical headings

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle at player's current position
turtle = MinecraftTurtle(mc, pos)

turtle.setverticalheading(90)

```

</details>

<details>
  <summary>
turtle.walk()
  </summary>

> Force the turtle to walk along the ground

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle at player's current position
turtle = MinecraftTurtle(mc, pos)

turtle.walk()

```

</details>

<details>
  <summary>
turtle.fly()
  </summary>

> Allow the turtle to fly (e.g. not be forced to move along the ground)

```python

from mcpi import minecraft
from minecraftstuff import MinecraftTurtle

#Connect to minecraft server 127.0.0.1 as player 'steve'
mc = minecraft.Minecraft.create(address="127.0.0.1", name="steve")

#Get current player's position
pos = mc.player.getPos()


# create minecraft turtle at player's current position
turtle = MinecraftTurtle(mc, pos)

turtle.fly()

```

</details>

#### minecraftstuff.MinecraftShape

- <a href='http://minecraft-stuff.readthedocs.io/en/latest/minecraftshape.html'>Official Documentation</a>

#### minecraftstuff.MinecraftDrawing

- <a href='http://minecraft-stuff.readthedocs.io/en/latest/minecraftdrawing.html#minecraftdrawing'>Official Documentation</a>

## 添加新功能...
|Author|林聖閔Sam|
|---|---|
|E-mail|samuel951753@gmail.com|

請使用raspberryjuice-1.11.jar以上版本
api可見minecraft.py檔，有註解說明使用方法

新增以下功能:
- setSign() 生成告示牌，可設定方位、內容及告示牌形式
- spawnEntity() 生成實體
- block.py加入ID、名稱對照




## Block IDs

- <a href='http://minecraft-ids.grahamedgecombe.com/'>Website with lookup table</a>
- <a href='http://www.stuffaboutcode.com/p/minecraft-api-reference.html'>Using a python library</a> [Scroll down to 'Blocks' section]
- 也可直接在Minecraft中按 F3+H，即可在背包中看見物品ID

## Entity IDs
- mcpi中的Entity列表.md，含有中文翻譯

## Licenses

Minecraft: Pi edition LICENSE - [minecraft-pi-edition-LICENSE.txt](https://github.com/martinohanlon/mcpi/blob/master/mcpi/minecraft-pi-edition-LICENSE.txt)

minecraftstuff LICENSE - [minecraft-stuff-LICENSE](https://github.com/martinohanlon/mcpi/blob/master/mcpi/minecraft-stuff-LICENSE)