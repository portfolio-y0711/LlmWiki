# Figma Design System: 05 Spacing

hello everyone and welcome to the fifth
episode in the series where we create a
design system in figma called fds in
this episode we'll be creating spacing
variables and first things first you're
probably wondering why I'm wearing a cap
that's because I bash my head on a train
earlier this week and instead of you
having to deal with and get distracted
by this little plaster I'm just going to
put this
on and get on with
it okay so what is spacing spacing is
the space between text images buttons
and other interface elements that
ensures visual Harmony readability and
usability across the experiences that
you create if we look at our global
scale and t-shirt sizing we use a global
8o system where a baseline of eight
pixels is Multiplied to give us a set of
consistent and expected values in the
table below you can see all of the
values we'll be using along with their
T-shirt size names multipliers and pixel
values so the group of courses on the
left spacing then we go all the way from
2xs or 2 extra small all the way up to
12 Xcel or 12 extra large in the next
column you can see the multiplier and
then the value all the way from 2 up to
112 and if we look at some examples
these examples show how spacing can be
used at a component content and Screen
level for a component in this input
component the label and help text are
both 8 pixels away from the field inside
the field we use 16 pixel horizontal and
12 pixel vertical padding to frame the
text and error icon which is separated
by 8 pixels and you can see all that an
action here between the label and the
field is eight between the field and
help text is's eight horizontally from
left to right we've got 16 on the left
side or the leading side and 16 on the
right or trailing side and then in
between the text itself and the icon we
have eight which gives us this
composition the content
and for cards the content is given
breathing room with 16 pixel padding on
all sides 8 pixel between the heading
and text and 16 pixels between the text
and the author's details so here you go
you've got the 16 pixel padding all the
way around eight between the header and
the text 16 between the text and the
author's details and then the Avatar and
the details are separated by eight as
well and at a screen level for app
screens side margins of 24 pixels keep
the content away from the edge of the
screen and inside the content area we
separate each content block by
16 then use eight pixels between
headings and text and if we hide the
spacing and we can do that by just
selecting the spacing layer here and
turning it off you can see how providing
enough white space around each element
has created a layout that makes the
content easier to consume all right
let's stop talking about spacing
variables and go and make some we open
up local
variables got the semantic set already
open but we're going to create a
collection call it
spacing and then create our first
variable which is a number let's make
the smallest one
first and its pixel value is two okay
and I think we need 17 of these so let's
duplicate this 16 times one 2 3 4 five
six S
8 9 10 11
12 16 we might have one extra one but
we'll just delete that later on if
that's the case now we're going to go to
the name and just give them the names
that they should have so we're going to
have
small
medium large
Excel 2
Excel 3
Excel 4
XEL you get the idea can you see a
patent forming here that's right 6
XL 7
XL 8
XL
9
10 11
and 12 okay let's delete that last
one and let's go down the value column
and make them what they should be so
we've got four
8
12
16 24 all multiples of eight of course
from here onwards so we've got
40
48
56
64 72
80
88
96 104 and then
112 we're going to select all of them
right click and go new group with
selection and rename this
space okay now that I made let's go back
to one of our examples and see how we
could apply
them okay in this
card we go to The Container you can see
that there's 16 here we drop this down
there you go we can just scroll down
find Al which is 16 we'll do the same
thing
here inside the content it's 16 again so
we're just going to drop this down apply
variable go to L inside
text set
small and in between the author
also set small and if you are an
engineer have Dev mode I can turn that
on and see the spacing variables
there and that's it for spacing in the
next episode we'll cover layout and
break points I hope you're looking after
yourselves and each other and I'll see
you in the next one
bye