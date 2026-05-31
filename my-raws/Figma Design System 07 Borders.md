# Figma Design System: 07 Borders

hello everyone and welcome to the
seventh episode in the series where we
create hello everyone and welcome to the
seventh episode in a series where we
create a design system in figma called
fds in this episode we'll be creating
border radius and width variables and
what are borders well borders outline
the edges of UI elements like buttons
cards and images and vary in roundness
radius thickness width and style solid
or dashed border radius is the applied
to corners of a UI element it used to
soften its appearance and create a more
friendly and approachable user
experience in this example you can see
how adding border radius made the design
on the left which looks corporate like
Microsoft look more consumer friendly
like apple on the right and if we scroll
down we can see that here where we've
got the sharp edges on the secondary
button the two input fields in the login
button and everything over here has got
rounded Corners making this one look a
bit more friendly than the one on the
left so
corporate sharp friendlier rounded and
for naming the T-shirt size border
radius variables handle the roundness of
Corners pill makes the left and right
sides of rectangles round and circle
well turn squares into circles and here
we go we got the name on the leftand
side with circle having a value of
50% pill having a value of
999 large 16 medium 12 small 8 and extra
small 4
okay border width refers to the
thickness of borders and determines how
thin or thick the lines appear adjusting
the width can add visual prominence and
emphasis to the element and communicate
to the consumer that an interaction
state has changed in this example you
can see how the border of an input field
becomes thicker when its state changes
from default to focused and we can see
that here where the default input field
has a one
pixel and when it's focused the Border
not only changes color but also changes
to two pixels and Border width variables
and name like the rest of the family
with widths from 1 pixel to 8 pixel the
1.5 pixel width is used for icons and
we'll render fine on high resolution
screens and in our table here we've got
the name and its size so XL has eight
large has four medium has two small is
1.5 and extra small is one all right
let's create our border variables so
let's open the variables panel and then
go to create collection we going to call
this one
border and we're going to create a
variable with a number and we're going
to do the Border radius set first so
let's type in
circle this can be 50 now you can't add
50% yet so hopefully figar is going to
update variables to allow for
percentages here so we can have this
represented correctly in design and
Engineering but we can tell the
engineers that this can switch from 50
pixels which is what this value was here
to 50% now we're going to go shift enter
to duplicate
that name this one pill and go
999 now it's set to 999 because it wants
to be the most you can ever add to
anything so can imagine a rectangle like
this having rounded Corners doesn't
matter what size that rectangle is you
still want that to happen right so let's
crack that right up let's go shift enter
again and we're going to add
large
at
16 shift enter again change this to
M at
12 shift enter again change this to
small at
8 and extra small
at
four okay let's select all of them then
right click and go new group with
selection call this one
border
radius then we're going to duplicate the
group and change this one to
width to create our width variables
which will make it easier for us so we
can just right click here and go delete
variable rename this one to extra large
and then we're just going to change the
values here to these values so let's add
eight then
four
[Music]
2
1.5 and then
1 okay we might do one more thing let's
just rename these as radius and
width because we've got that hierarchy
here border radius and Border width and
then just close the panel and zoom into
this card here and let's apply some of
them so I'm just going to select the
entire card and then I'm going to go and
add them so I'm going to scroll down
here to border radius and this one's at
16 so I'm going to select
large I'm going to go to all of these
and all I'm doing here is holding down
command shift and then clicking on them
which should give me the selection of
all of those rectangles then go and add
12 so let's find
12 there we
go cool and when you hand us over to an
engineer and they go into Dev mode
they're going to be able to see that
here it's got
16 border radius is radius L at 16
fantastic let's get out of that mode and
if we come down here and select the
input field and its focus State we can
add the 12 there so let's just scroll
down and find Border radius at 12 and
I'm going to be doing an update to the
uh Series where we go through scoping
right and so that's going to allow you
to go into Corner radius here and just
see the Border radius variables and the
same thing with the spacing or any other
variables just going to turn up where
it's supposed to go so look out for that
one soon but for now we're going to go
down and add a two pixel width to this
field now as you can see when I hover
over it you can't
see that little icon that allows you to
add variables to things so if I break
this apart and you can see that there so
what do we do okay you have to right
click and then go apply variable so
let's go down to
width and select two so that's going to
add the variable to the outline if we go
into struges per
side you can see that here now that
means you can have different ones per
side so we could even change this to
eight and see that coming like
that and again if we go into Dev mode we
can see that we've got
border width M at 2 pixel
and then we've got border Focus as the
sematic variable along with radius M at
12 and that's it for borders in the next
episode we'll update our type styles
with typography variables I hope you're
looking after yourselves and each other
and I'll see you in the next one bye