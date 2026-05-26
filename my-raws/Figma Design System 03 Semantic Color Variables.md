# Figma Design System: 03 Semantic Color Variables

hello everyone and welcome to the third
episode in the series where we create a
design system in figma called fds in
this episode we'll be creating our
semantic color variables but before we
do let's create the two primitive colors
I missed creating in the last episode
black and white which should be uh
pretty easy let's open up variables we
can see everything we did last time I'm
going to
create a color variable called black
change this to 00 0 hit enter I'm going
to create another
one called
White leave that as it is and later on
we're going to make some overlays so
we're going to need 50% black and white
so let's do that
now duplicate that go 50 open up a
Swatch change opacity here to 50 and
then do the same for
white
let's select them all right click and
then go new group and let's call this
primary then just move that to the top
all right now that's done let's learn
about semantic color variables semantic
colors have meaning and a name based on
how they're used not what they look like
a good way to visualize this is to look
at the example below the hex value has
been assigned to the Primitive color
and that's been assigned to the semantic
color which has been used as the
background of the button component for
dark mode you simply change the
Primitive variable that is assigned to
background brand from Brand 500 to Brand
400 and if your set of brand primitive
variables changes color like from Blue
to purple it'll do that across the
entire system and the products that
consume it and as for naming we use the
schema in the table below to name our
semantic variables okay so we start with
the group so which group do they belong
to content will be text and icons
backgrounds of course or anything in the
background borders are borders surfaces
are for like a elevation and then
overlay are for things when you see a
modal appear and then the background
goes dark the roles are primary
secondary tertiary so that's like
hierarchy brand mono link info notice
for like warning negative for things
like errors and positive for Success
appearance bold subtle and inverse
States so these are normally associated
with buttons like hover Focus pressed
selected and disabled and you've got
your values for like elevation from l0
to L6 plus 50 for the overlays I
mentioned just previously which gives us
things like content link hover
background primary press border subtle
surface L3 or overlay inverse 50 okay
now let's create our semantic variables
if we open up the variables window we
could create them manually by creating a
collection called semantic and then
spend one to two hours adding each one
individually instead I've used the
component the variables color style
plugin created in the last episode and
laid out what we need for our light and
dark modes in a table ready to be turned
into our variables you can see our
groups rols and modifiers come together
to form a set of variables that are easy
to read understand and create a mental
model when you read them that tell you
how to use them and if we zoom in and
just read some out we can see how that
mental model comes together content
primary so I want content which is
hierarchy
primary content link I want content
that's a
link content negative can be used for
negative text and icons we go to the
background background brand brand har
and brand press can be used for the
primary
button and yeah we just keep on going
through like uh border notice is a
border that's showing notice or like a
warning the surface levels are surface
L1 for level one L4 for level four and
then you have overlay 50 which is a
black at 50% if I select a color layer
you can see that I've got content
primary now in episode two we use the
styler plugin to create styles from
these types of layers and although it's
great at doing so there's nothing I've
found that will convert those Styles
into variables that retain the color
variable so how we've got neutral 900
they normally just get translated to hex
values that just means we'll have to do
a bit of manual work so let's select the
color layers and run the style of plugin
okay I'm just going to hold down command
shift and then start selecting all of
the content ones and hopefully when we
do this everything ends up in the right
order okay let's run sty
and then go generate
Styles and then take a look okay so we
got a Content folder but everything's
out of order let's going to create the
rest and then fix the order a bit later
okay background
set run Styler
again let's check that okay and that's
out of order as well let's grab the
Border ones
run Styler
again generate
Styles this is going to create the
surface ones as well as the effects for
the Shadows so let's do
that then the last two which are the
overlay ones one last
time all right
so everything's out of order I'm going
to go off and fix that and then
basically Fade Out and fade back in see
you
soon all right we're back and
everything's now put back into order so
we can also change the effect styles
that were called surface as well to
Shadow which will allow you to use like
L1 as the surface level and then L1
Shadow as the surface level one Shadow
okay now let's run the style to
variables plugin to convert those Styles
into variables
there it is and we're going to enter
semantic here
and create them all right says that 54
we created let's going to take a look
let's open up the variables panel and
drop this down and go to semantic okay
great just going to select uh each
one and yeah you can see that in the
value here it hasn't brought over the
assigned color variable and it's also
done something inter interesting where
it's taken out the space for each of
these so let's put them
back uh I expect I'm going to have to do
that throughout the whole set but that's
okay let's go to
background yeah similar
thing into border
that's fine surface is fine and overlay
just needs one there now if we select
all this is actually light mode so let's
change that to light and then all we
have to do from here is go back and
assign all the color variables again
like this right so this is actually the
hex value for neutral 900 but we're
going to have to drop that down every
single time go to libraries and then
type
in neutral 900 and even though that's
assigned properly we're going to have to
do that for all of the other ones as
well and instead of you are just sitting
there watching me do it or watching a
fast forwarded version and be doing it
I'm just going to fade out fix it then
come back see you soon okay we're back
again and you can see that light Mode's
been fixed all the color variables are
assigned to the semantic variables
properly and we have to do now to make
the dark mode is go up here and press
new variable
mode rename this to
dark but it's the same values right so
we have to go and change this to White
so we go all the way to the top so it
matches our setting over here where
we've got neutral 900 and then primary
right on the right hand side so this is
the color that content primary which is
like uh your headings are in light mode
and this is the color that it is in dark
mode basically so that makes sense and
again I'm going to have to go through
all of these and swap them for their
correct values here so uh uh yeah I'll
see you in a little
bit okay back for the third time awesome
we now have our semantic variables in
light and dark modes and if we scroll
down you can see everything's been
relink nicely
okay let's close that uh just like in
episode two we no longer need the Styles
so I'm just going to go and delete
them scal letter background border
surface over and we're going to keep the
Shadows because figma doesn't have
variables for them yet now if we come
back to the documentation it's kind of
done already all we have to do now is
assign the semantic variables we just
created to the color squares in our
table so content primary here that is
neutral 900 would change
to content primary now instead of going
through and doing all of that now fading
in and out again basically I'm going to
create two files one will be where we
picked up at the beginning of this
tutorial and one will be at the end
where all of this is done for you now
both of those are going to be available
in the link in the description and
that's it for semantic color variables
in the next episode we'll be doing
topography I hope you're looking after
yourselves and each other and I'll see
you in the next one
bye