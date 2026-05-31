# Figma Design System: 09 Iconography

hello everyone and welcome to the ninth
episode in the series where we create a
design system in figmo called fds in
this episode we'll be doing iconography
and everything we've been doing so far
has been in this design tokens Library
we're now going to move into the
iconography Library so let's just jump
in and start with what are icons well
icons are small visual cues that help
users navigate interfaces perform
actions and understand functionality
without relying on text they used in
buttons toolbars menus and other
interactive elements to create a more
userfriendly experience and as for Icon
sizing well a general rule for icons is
that they should be used at the size
that were crafted and not resized for
example a 24 pixel icon should be used
at 24 pixels not resized to 32 pixels
this is why you see icon sets that
provide 16 pixel 24 pixel 32 pixel sizes
and larger icons called pictograms that
can get up to 64 pixels or 96 pixels
each icon increases in stroke weight as
it gets larger and we use trim areas
inside each icon to make sure the edges
of the icon don't touch the sides of its
container let's zoom into this home icon
example where the 16 pixel version has a
stroke and a trim area of 1 pixel the 24
pixel version has a stroke of 1.5 pixels
and a trim area of 2 pixels the 32 has a
stroke and trim area of 2 pixels and the
64 pixel version has a stroke of 3
pixels with a trim area of 4 pixels
and for crafting icons well here's a
step you would take to craft a 24 pixel
calendar icon step one 24 pixel frame
start with a 24x 24 pixel frame and then
name your icon this is the naming
convention you've got icon slame SL siiz
for example that would be icon SL
calendar
sl24 step two use basic shapes draw the
icon using primitive shapes try to snap
the points to pixels and then use 1.5
pixel line thickness step three modify
shapes change join and points to rounded
use border radius on Corners step four
flatten and style select all shapes and
flatten them and assign the content
primary semantic variable to the layer
step five create component delete the
guide create a component out of the icon
and add it to the rest of the set you
can see the guide here in the background
at the beginning that you use to guide
your way through and then you delete it
here before you make the component all
right fds is free so let's use a free
icon Library called feather icons from
Co beamus that cover the 24 pixel size
and have been turned into their 16 and
32 pixel sizes by Thomas peroff they
will act as a base set of icons for
everything we create in fds and we'll
create more of them and also pictograms
and illustrations if we need them in
future episodes okay and what do you get
16 24 32 and some status icons in those
sizes to to and if we zoom into them
let's just choose this one theyve all
been flattened to one layer you can see
that here and then content primary has
been assigned to them this is going to
allow you to use it in the future and
then just change its color to whatever
you want so if you have a icon that's
brand you can do that if it's a notice
you can do that if it's positive you can
do
that awesome but let's turn that back to
content primary and if we take a closer
look at the status icons you select the
back of the info icon we can see content
info and then it's eye has content
primary inverse which allows it to
switch to dark mode very easily let's go
do that
here and even though there's 285 icons
in each of those sets along with the
additional status ones we don't have a
UFO icon so let's go and craft it okay
I've zoomed right in let's select the
tools icon template that you can find
here that has the 16 24 32 and 64
sizes that you can change to the size
that you want over here let's go back to
24 all righty UFO hm I'm going to start
with an
oval and as soon as I start to draw this
out you can see that I'm trying to stay
within the
square let's try to do that for
now I'm going to get rid of the fill I'm
going to add a stroke but let's just
keep it at black change that from inside
to
Center all right then I'm going to
duplicate this by hitting command D just
going to move it up until we hit about
there and then just resize it so it
looks like the part that the alien sits
inside all
right that'll about do it let's move
this up a bit more move you up
all
right actually let's move them both down
and let's zoom in so I can double click
on this to go into edit mode hit the pin
tool hold down option to remove this
point press Escape then double click
again because I want to grab this point
and just move this
up let going and do the other
side okay
until this curve here starts to match
the curve below it it's still a bit out
let's go half a clip
up that looks about
right let's actually move that down
one yeah much better grab them both and
move them up because it's going to need
some lines let's press Al for line just
drag it down double click on it and move
the points back to there I'm going to
duplicate it by pressing command D and
then just move that over
duplicate it again and move this one
over to about there then I'm going to
resize this
one by double clicking on it and moving
that point up and then doing the same
over here okay so we want to get these
intersecting but remove this line if we
just select both of them and go flatten
and then go into select mode that's not
going to happen they still kind of
individual elements so let's undo
that select this one to move right then
you can double click on it again to
select it or you can go up to Eclipse
here and then use the more icon to go
down and go into edit object then I'm
going to grab the pin tool and I'm going
to move it along until it hits this
point here then I'm going to bring my
mouse over here and do it
again then I'm going to go into edit
mode and delete all of them there we
go let's move out
again all right so everything is still
separated but we need to select
everything and then go over to the
settings here and the stroke change your
end points to
round and then change join to round as
well all right let's just zoom out and
see what that looks like it's pretty
good that's four pixels from the top and
this is four from the
bottom these could probably be a little
bit further away so let's double click
on the path and move it down to there
let's do the same same
here okay the next step is to select
everything so let's just go over to the
layers and do that here and then make
sure they're in the icon folder which
they aren't so let's drag them into
there and then then right click and
select flatten all right something
interesting happened there so let's just
go
back go to mixed here on the end points
and change that back to round and while
we're here let's go over and add the
sematic variable of content primary then
we're going to come back to the layers
and go icon
slfo sl24 as its name change that to a
frame delete the
template select this and then create a
component so let's go and do that here
that'll become part of the rest of the
set but I'm just going to drag it up to
where it should be so let's go find the
24 pixel icons and then it's going to be
underneath type before I'm
isn't it and while we're here I forgot
to change the stroke from 1 to 1.5 so
it's going to make it thick enough for
when we zoom out to 100% you can
actually see everything nicely all right
now if we go to assets icons icon and
then find the icon let's go all the way
down to UFO we've only got the 24 pixel
version unlike the other ones that have
16 24 and 32 too so that's a bit of
homework for you you can take this icon
size it down to 16 pixels and then back
up to 32 pixels then you'll have the
whole
set and that's it for iconography in the
next episode we'll be looking at
variable scoping hope you're looking out
yourselves and each other and I'll see
you in the next one bye
[Music]