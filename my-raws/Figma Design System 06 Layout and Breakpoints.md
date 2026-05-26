# Figma Design System: 06 Layout and Breakpoints

hello everyone and welcome to the sixth
episode in the series where we create a
design system in figma called fds in
this episode we'll be creating layout
and break points okay so what is layout
well layout is a set of vertical columns
that allow designers and Engineers to
define the layout of their screens in a
structured way fds uses a responsive 12
column grid for desktop and tablet that
becomes four columns on mobile or apps
each column contains 8 pixel padding on
either side and the 8 pixel side margins
provide a consistent 16 pixel gutter
size across the entire grid and if we
just come down here you can see that in
action we've got one
column and I can show you that there one
column with 8 pixel padding on either
side the rest of it going to be fluid of
course because it's responsive and then
you've got the 8 pixel margin on the
outside there's 12 columns there and
four columns for mobile all right so
what are break points well break points
are specific points at which the layout
of an interface adapts or breaks to
accommodate different screen sizes or
device orientations we have four
breakpoints that cover desktop tablet
and mobile devices the mobile breakpoint
can also be used for app design as it's
the same size as an iPhone 14 or 15 Pro
and if you look at the table here you've
got the device on the left which is
desktop tablet landscape tablet portrait
and mobile their names which are t-shirt
sizing again all the way from s for
mobile small medium large and Excel up
to desktop and their sizes which are
1440 1024 768 and
393 combined we can create variables
that snap between each breakpoint
automatically with the only thing left
for you to do is change the layout grid
let's hope figma updates variables so we
can tell the layout grid to change
automatically when you switch between
desktop and mobile okay let's create our
breakpoint variables and layout grids
it's going to open up the local
variables you see the spacing collection
there that we did last last time now
let's go and create a collection and
call this
layout inside there create a number
variable let's call this
XL 1440 and here's a trick I picked up
from a Community member called Abdul you
go shift enter to duplicate the variable
thanks a lot man awesome now let's go
L change that to 1024
duplicate it
again change that to M and
768 and then small which is
393 now let's select all of
them go new group with selection and
change that to
breakpoint and you might be wondering
why they aren't set up in modes like
desktop and mobile up here that you can
switch between well figma just really
released type variables and we're going
to do a typography update which would be
something like this so let's create a
collection called
typography in there we're going to
create a number and this will be
breakpoint but we're going to use one of
the variables that we just created let's
go and grab it change this mode to
desktop add another mode just resize
that so we can see it and go all the way
down to S and change this to mobile now
if we create our typography variables in
here we're going to have the desktop
sizing here and the mobile sizing here
and the way we're going to switch
between them is by selecting this Frame
going up to the
variable going into typography
breakpoint assigning it there and then
you can switch between typography de
toop to mobile like that and all the
desktop sizes for the typography will
switch to the mobile ones automatically
let's switch this
back and create our layout grids and
with this ttop Frame we're going to go
to layout press the plus open up the
grid change it from grid to columns
change this to
12 can change the color as well I'm
going to use the blue that I normally
use and bump that back down to 10% I'm
going to leave the type as stretch
change margin to 16 and gutter to
16 let's just close that okay so now we
need a mobile one so just going to zoom
out duplicate
this change it from desktop to
mobile Zoom back in so we can see what
we're doing go over to Styles add
another one called
mobile and then go and edit what mobile
is so let's hit the properties change
this to
four and we're done and that's it for
layout on break points in the next
episode we'll cover border radius and
withth variables I hope you're looking
after yourselves and each other and I'll
see you in the next one bye