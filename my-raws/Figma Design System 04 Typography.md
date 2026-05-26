# Figma Design System: 04 Typography

hello everyone and welcome to the fourth
episode in a series where we create a
design system in figma called fds in
this episode we'll be creating
typography okay so what is typography
typography is more than just picking
fonts it's the art of arranging type to
make written language legible readable
and Visually appealing in a design
system typography plays a crucial role
in establishing the visual identity and
hierarchy of content to set up our
typography we start with the font family
which is a group of type faces you use
across your system fds uses inter as its
default type face with SF Pro display
and text for iOS and Roboto for Android
each font family comes with different
weights which is how thick each
character is we use regular and semi
bold and fds for groups we use two
groups that can cover most use cases you
can add others like label and Link but
for fds we'll start with heading and
text for scale or sizing we use a
combination of a global fourpoint scale
and t-shirt sizing to create our type
scale in this example you can see the
style name followed by its size and line
height you can see that on the right
hand side the scale is going down from
48 to 40 to 32 to 24 then makes a
fourpoint drop to 20 then 16 and so does
the line height where it goes from 56 48
40 32 28 and 24
okay so what is t-shirt sizing instead
of naming our text Styles what their
role would be like H1 H2 and body we use
t-shirt sizing to make them more
scalable and yes it's what you would
expect from 2xs to 5xl in this example
an H1 and one product can be heading XL
and then another product and can be
heading L calling it H1 means that all
of your products have to use that style
and size and you would have to create
multiple typography sets to provide what
each product needs for naming we name
our typography styles using this naming
convention we've got the group on the
left hand side which is heading and text
the size all the way from 2xs up to 5xl
then the weights regular and semi bold
which for example gives us heading slal
slsi bold text slal SL regular and text
slal slsi bold we're going to start with
just semi bold for the headings then
roduce extra weights later and when
figma updates with typography variables
we'll create variables for family size
line height weight and letter spacing if
you'd like to read more about typography
and see some examples you can visit the
typography page in my system called
scale and the link I'll put in the
description okay if you watched episodes
two and three of this series you'll know
that I provide a link to all the files I
use so you can follow along from the
beginning and also get the outcome of
each episode in the beginning file I'll
prepare some of what we're going to
create before we begin and this episode
is no different you can see that the
Styles have been laid out on a table
saving us both time and getting right to
the best way I found to create type
Styles quickly so let's get into it and
to do that I'm going to use a similar
technique that we used in the other
episodes where I use the styler plugin
to take the name of the layer and create
a style out of it so you saw that before
when I was making color Primitives into
Styles before converting them into
variables we zoom in to heading 5xl you
can see that here we've got web slhe
heading SL 5xl SL semibold on the right
hand side we've got all of its details
so the weight size line height letter
spacing if we come over to here you can
see all the values here now this is true
for every other layer as well if we go
down to text regular there we go just
zoom out again and go to iOS so the same
thing has happened here here but instead
of web we've got iOS at the beginning
and heading 5xl we've got Android
instead of iOS or web at the beginning
and you know what the next step is right
we're just going to select all the
layers okay so we got the
headings and the text and I'm just
holding down command shift to do
this then go to
plugins styler and then generate
Styles okay it says it's created 16
let's go over and have a
look okay they're all out of
order and some of them haven't had their
regular Styles done either so before I
do the text again I'm going to just
reorder the headings so 4XL will go
there three 3 XL underneath
four 2
XL
Xcel
large
medium
small Xs and 2xs let's open to see if
they've all got semi balled yep that
looks
fine
okay for the text let's reorder them as
well so we've got extra large
large
medium small and
excess let's open up this layer so we
can see that the weights aren't all
there and let's try to run the regular
weights from L to XS
okay
check their naming yeah that's all
fine come on Styler you can do
it okay so it's just sitting there and
spinning and there you go plugins are
infallible sometimes sometimes they work
sometimes they don't so let's move on
and run styler on IOS and Android and
see if it works
there select all the headings for
iOS and the
next R
Styler okay 20 that time so let's go
have a
look let's just reorder our heading
let's place it up
there okay so it worked with
iOS let's do Android
now click click click click yep here we
go run Styler
again 20 so it's probably worked for
Android as well okay if something like
this happens when you're doing this
tutorial or in your own work you just
got to pull up your sleeves and put in
the work so let's go and create those
missing Styles manually and to do that
we just come over to local Styles press
plus go to text then go
web
slash Text slash what do we got
L then SL
regular and that's going to be
16 and
24 there we
go that looks all right so let's do that
again for
web text
M regular and I'm just going to copy
this for the next
one go to
14 20 and create style okay now we got
small here we go leave that at 12 and
change this to
16 create yep and then the last one
which is extra
small and that's 10
and
14 great now we reordered the headings
there but the text here needs to be
reordered and by that I mean regular has
to go above semi bold so let's do
that and and then let's open up iOS and
reorder everything
here and I'm just going to go and do
that fade out and then fade back in so
I'll see you
soon okay we're back you can see that
everything has been reordered we scroll
down the text has the right order of
size and also regular and semi
bold iOS is
okay and so is Android but what that
didn't do was assign the right style to
text L Ms and Xs I mean if I select text
XL you can see that it's there because
Styler when it makes that style assigns
it so let's go and select text and this
is a good way to learn how to actually
assign text Styles once you have them
right this is just a piece of text
without a style we're going to go over
here and go to Styles and we're going to
type in text and L regular so there you
go let's do that for the
rest probably just type text M once you
get to know
them regular as
well text
small and text
excess just double check
that and that's it we've got our Tex
Styles now Styler didn't work 100% of
the time but sometimes that happens
we're able to fix those gaps pretty
quickly but that's it for topography in
the next episode we'll be doing spacing
I hope you're looking after yourselves
and each other and I'll see you in the
next one
bye