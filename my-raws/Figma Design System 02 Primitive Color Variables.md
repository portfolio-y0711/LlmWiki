# Figma Design System: 02 Primitive Color Variables

hi everyone and welcome to the second
episode in the series where we create a
design system in figma called fds in
this episode we'll be creating our
primitive colors but before we get into
it let's answer this question what are
primitive colors primitive colors are
Baseline Hues like blue red and green
that act as the default color palette
for your design system fds has 13 which
are
actually brand blue purple
Violet red pink orange yellow green teal
Canan black and white all right what's
the brand color well the brand color is
your Brand's primary or main accent
color and for the other colors well
their hex values are up to you but I
started with my brand blue and created
the others by changing their Hue
saturation and lightness values to
create a set that looks like it's
cohesive tonally next up we create a nin
step tint and shade scale for the base
colors tints are created by increasing
the lightness value of the base color
and and shades are created by decreasing
it now there's two ways you can do this
manually where you overlay the base
colors with white and black with opacity
increments in both directions of 20 40
60 and 80 then flattening them and
literally color picking them one by
one who's got time for that well me
apparently or you could just use a
plugin thankfully there's one called
color tint and shade generator that will
give us the same outcome let's select
each color run the plugin and create
their color scales so let's grab brand
and it's he
value run the
plugin enter the hex
value and generate all right so it's
take that to zer0 let's see if the
others end up there just going to do
blue which is the same
color wonder if it remembers it nope so
let's enter that
in generate
okay and that placed it just above the
other one let's keep
going and we might uh speedrun the rest
of this so here we
go all right that plugin was great for a
n910 scale but we need 19 neutral TS
which come from black so we're going to
use the ones from the starter file that
I've already flattened and added their
values you can see that here we go all
the way from OD o all the way up to F2
and then just group them with the other
scales let's go back up here and select
everything it just generated move them
out of the way I'm just going to zoom
out so we can give them some space just
going to grab that first one and move it
down keep on doing that until they're
all
separated
okay just click and drag to select them
all again come to the bottom right and
select this icon just going to add some
space between each one I'm going to make
that 32 now they're created we need to
name them and we name our primitive
colors using this naming convention
color slal which will give us blue 500
or pink 100 for example and to do that
I'm going to click and drag to select
all the brand colors go to rename
it and rename selected
layers it's going to start up it's just
add
brand okay let's do that for all the
others that's blue and we'll speedrun
the rest just like we did the tint
sets
okay and with that done you should have
everything named properly so that's
brand blue
violet
pink yeah everything seems fine all
right now we need to name every single
column it's value right so I'm just
going to click and drag again to grab
the left hand
side use rename
it and this time select lay name and
then go for sl100
100 that's going to give every value
that should be 100 100 you can see that
there let's do that for the rest of
them this is
200
300
400
500
600 700 we're almost
there 800
and 900 okay let's select a random color
orange and you can see that everything
has its correct name okay before we go
to the next step we have to reverse the
order of these layers so let's use
reverse layer order
plugin and then just do that for each
set let's also select all of those
frames and run reverse layer
order so brand is at the top and sign is
at the
bottom now we need to turn our colors
into variables that's normally done by
opening the variables panel having a
collection there or creating one then
creating each color individually by
giving it a name then a text value
instead we can convert them into styles
with the style of plugin then convert
those Styles into variables with the
styles to variables plugin so let's
select all of these by clicking and
dragging and hold down shift while you
still got command held down and click
and drag the new neutrals all right now
go up grab the styler plugin and run
generate
Styles and we can see in the design
panel that they've all been created
fantastic but everything's out of order
so let's just put them back
in so we got
[Music]
blue
[Music]
purple
violet
red
pink orange
yellow green till Canan and neutral and
since most of the interface is going to
be made up out of brand and neutral
let's just move that underneath there
okay and let's just check finally to see
if they're all in order see how that one
was at the bottom
there all the others seem
fine okay let's run the styles to
variables plugin
it's got 118 color styles
great let's give our collection the name
Primitives and then convert Styles into
variables so let's open the variables
panel and there you go you've created
tint scales for each of your colors turn
them into a collection of variables
called Primitives you can now delete the
Styles as they are no longer needed
we'll also go into the variables panel
select all of them right click and
select hide from publ ing why well our
primitive color variables will be
assigned to our semantic color variables
and we'll only allow designers to use
the semantic variables so we can hide
them so color is assigned in the
interface in a way that will scale
better and also allow for Native light
and dark mode switching inside figma
let's select all the color
styles just delete them select the first
one hold down shift go all the way to
the bottom select 900 right click
anywhere go edit variables and then hide
from
publishing now that our variables are
set up you can really just select
everything here and delete it if You'
like to display your variables run a
plugin called variable color style
guide let's just select Primitives leave
this as it is and then create
swatches okay just zoom in and see what
we
got go all the way to the top we can see
that the
variable is assigned properly and you've
got some other information there like
the name hex value and
rgba I think this has an hsl yep so I'll
turn off RGB and then turn that back on
okay this needs to be aligned to the
right and there's some shortcuts up here
so you can just skip to each section and
from here you can just modify that
component to look consistent with the
way you'll document all of the variables
in this Library so let's do that by just
moving it up
here selecting the
color changing it to 32 by 32 give it a
border radius of
four change its width to
704 okay the card Auto needs to be
changed to
horizontal Swatch is fine the token
details Auto change to horizontal and
change top and bottom padding to
eight select the color code and change
that to horizontal as well then select
the text layers and color code and
change them to Auto width go to the card
layer and then turn off the Border okay
that's looking nice and
clean What's happen over here we've got
the
Swatch as
four and then the card has got eight all
right let's go and change the card layer
to four as well okay we've got some
stragglers over here on the right so
let's just make sure the auto layout is
correct let's change this to
there select all of
them go fill container all right that's
happening all the way down here as well
so let's speedrun
this
okay it looks like everything's fixed
but let's go
in select the index and change that
width to 704 as
well okay so we want to get these over
to the color and put them here just
going to grab this layer called
container and copy it bring it over to
here and paste it add a white fill
select the section layer here and delete
it go back to here let's grab everything
from index to C and copy it go back to
color select that container inside the
Primitive color page and
paste let's just select that container
and give everything more space so
32 okay looking
good okay just to clean the
documentation up a little bit let's go
back and change this to a capital
b capital
p let's do that here as
well and that's it for primitive color
variables in the next episode we'll be
creating semantic color variables and as
always I hope you're looking after
yourselves and each other and I'll see
you in the next one
bye