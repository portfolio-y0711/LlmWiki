# Figma Design System: 11 Spinner Component

hello everyone and welcome to episode 11
of a series where we create a design
system in figma called fds in this
episode we'll be doing our first
component the
spinner and here we are in the fds
components web Library where we're going
to create the component and when we're
finished we're going to copy it over to
the fds components app Library so if
you're a designer that's working on a
web project you can get the spinner from
that library and if you're one that's
working on an app project you can get it
from there we're going to do that a
little bit during the series where we
have a button in both of these libraries
but sometimes you're going to end up
with components that are only available
in web and some that are just available
in the app and before we start we have
to make sure that this Library can see
the design tokens Library so let's just
click on that go over to assets and then
make sure it's published so I hit to the
library icon here you can see the
libraries you can see that this is the
fds design tokens one there's no changes
but I published it previously so we can
actually see it in the other libraries
you can see that I've done that with the
iconography Library as well and then
added it back to the design tokens
Library we'll be able to see both of
these and utilize the variables that are
in here inside our web library and then
the icons that are in here in that
Library as
well and to check this let's go to the
assets tab hit the library icon again
and we can see them here design tokens
and iconography have been added let's go
back to the file tab click on component
name double click on it and change this
to
spinner inside spinner go to
assets go to design tokens tools the
tools folder and then let's grab an fds
heading and drag it in it's going to
turn the X and the Y of that to Z and
z I'm going to select this and type
spinner and you can either do that
directly or you can do it over
here and then we've turned on the intro
text and what are we going to put in
there okay let's describe what a spinner
is by going to the component Gallery
website which is a great resource for
exploring what components are across
multiple Design Systems in the industry
and add component Gallery let's just
type in
spinner press enter and then let's just
copy and paste this back over to our
file and use that as the description
double click on this text and hold down
shift option command V that'll copy it
without using its
style and there we go now we're going to
resize this to give us some room let's
just make it
1024 for now then let's go back to the
file Tab and create a frame by hitting F
on your keyboard and
dragging that is 48x 48
and width and
height okay I'm just going to move it
over to here so it's about 48 from the
left and about the same from here so
let's go 1 2 3 1 two there we go let's
rename it
to
spinner and then create a component out
of
it right let's Zoom right in and then
hit o to draw an oval
drag that out and we want this to be
about 44x
44 this is going to be the large version
of the spinner so we're just going to
position it right in the middle like
that then we're going to remove its fill
and then add the stroke so the stroke is
going to be
border
brand we're going to change the
thickness with a variable to L
4 then we're going to change this from
in side to Center then we're going to go
up to the design panel and where ellipse
is just hit edit object then we're going
to tap on this section and remove it
just press enter then we're going to
come down to the start and end point and
make those
round okay then let's go rename that
path
spinner and then select the whole
component go over to spinner and add a
variant so that just multiplied it and
placed it it underneath itself we're
going to change this one to size equals
L and this one is going to be size
equals L as
well and then we're going to add another
variable and this can be size L as well
and just uh bear with me for a moment
because we're going to select this one
and change the
border to inverse and then change
this to negative because we're going to
add another variable by clicking on
this and renaming it with this at the
end of it so type
equals
primary now we can just go select the
next one and add another one over here
and type this is going to be
inverse and then we can select the
negative one and add negative here
here cool so now we have one size large
which is 48 and then we have the types
primary inverse and negative so let's
just zoom out for a
sec let's grab this and resize it then
select all three and I'm going to hold
down option and drag until I have
duplicates of them then I'm just going
to move them down there and then in the
size I'm going to change that from large
to M or medium then while we've still
got them selected we're going to go to
layout hit constrain properties and
change this to 24 now that resize the
variant but it didn't resize the path
and side so I'm going to select them all
by holding down command shift and then
finding the
paths and then changing this to
22 and I'm going to change the thickness
2
two then select them
all just make sure they're all one pixel
away from the left and the top and you
probably wondering why we have multiple
sizes well the large one can be used to
load a whole page and then we're going
to create some button components that
need a loading state so the 241 is going
into the large version of that and then
we're going to create one more size
which is small for a small button
let's select all these variants again
hold down option and drag move them over
to the right and then move them down
again then we're going to change this
to S right now we need to make these 16
so they're all still selected let's just
type that in
there and then do the same thing we did
last
time change this to 14
and then change the width to one now
let's just move into the small ones and
see if they are the right size and
that's okay because if we move it up and
left it's going to get cut off so let's
undo that zoom
out select the component and then come
over here to layout and hit resize to
fit make sure that that is still 48 from
the
left and also from the top so how far is
it away from that text Element 32 okay
one more and then one more
again great now if we drag one
out and just play around with it we've
got large medium and small let's go back
up to large and we've got primary
inverse which is white and negative
fantastic let's select that and delete
it and that's it we've finished doing
the web version of it now we need to
copy this over to the app version so the
designers there can just pull it
directly from that Library so let's go
to the layers panel just collapse that
select the component and the heading
copy them go over to
here go here and paste them now every
time you paste something in figar it
goes in a weird place so how I normally
get this aligned easier is to just make
a
square set this to 0 and zero and then
grab my element
and drag it into
position and we can press one on our
keyboard to center it go and change the
page name to
spinner and we're done so let's go back
to the web library and then go to assets
and we can see local assets here has one
component and if we click on it we can
see that we can insert the instance and
even play with the properties so let's
insert
one okay now every time you create a
component figma does this wonderful
thing where it adds white to everything
so let's go and select all the variants
just go back to
file remove
this go back to the app version and do
the same thing
there back to web select this instance
and let's just zoom in here we go
primary andse negative just like we saw
before we can also
check out how dark mode looks right so
imagine this was on a white background
and light mode which it's going to be
and then it was on a dark background so
let's just give it one I'm going to
group it add a
frame add some Auto
layout add some padding let's give
it
32 give it a border radius why not to
eight and then make its fill
L1 right now let's just say dark as the
name of this and then go it to
appearance get a semantic color and then
change that to dark there you go now if
I select it and then just change its
thing you've got inverse which is black
it's going to make it
disappear and then
negative let's delete those hit one
again and that's it we've cre the
spinner component in the next episode
we'll be creating the button component
so I hope you're looking after
yourselves and each other and I'll see
you in the next one bye