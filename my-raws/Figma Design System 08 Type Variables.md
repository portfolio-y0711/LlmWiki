# Figma Design System: 08 Type Variables

hello everyone and welcome to the eth
episode in the series where we create a
design system in figma called fds in
this episode we'll be updating our type
styles with type variables now this
episode is going to be less of a
tutorial and more of a walkthrough this
comes down to how
[Music]
long it would take to create all the
Primitive type and semantic type
variables we need to drive our type
Styles and because there's no plug-in
that can structure them in the way they
should be structured to achieve the
outcome we need and with that said grab
this file from the link in description
and let's go okay so what are type
variables we type variables Drive every
value of a Tex stle like its font family
weight size line height and letter
spacing in a similar way to our color
variables they're created as Primitives
then assigned to semantic type variables
in this example you can see how they
come together to provide heading L's
values in figma and what they look like
in code AS primitive and semantic CSS
variable
and you can see the values that heading
L has here like it's family is family
enter weight is weight semi bold size is
size 5 XL line height is line height 5
XL and letter spacing is letter spacing
XS those are all the raw values and how
they get translated over to their CSS
variables is we've got a file that has
the root variables like fds type family
enter using enter the weight which is
semi bold using 600 100 there's the rest
then those are applied in a semantic
Mixon file we've got font family
variable fds type family inter which
points to this and then we use them in
our Styles sheets by including the
mixins then creating an H1 like this and
including the Mixon fds type heading XL
which is going to point to this which
then points to this that's how it all
comes together and in the variables
panel that we're going to have a look at
soon you'll find these two collections
primitive type and semantic type you'll
also see that I've changed the Primitive
and semantic color collections to
primitive color and semantic color to
match them okay let's look at the type
variables and how they're assigned to
our type Styles it's so add lib from
here so we won't need a tally
prompter all right and you figured out
by now we're using figma ui3 so where
are
they are there they are okay in this one
I'm also introducing a global unit
variable set so you can see that 2 2 4 4
you get the idea here these are just
values that are going to drive anything
that has a size value and in type
variables that can be size and letter
spacing so that goes all the way down to
120 but if we jump back up to the
Primitive type collection we can see the
different sets we've got here so we've
got family weight size line height and
letter spacing and from the top family
has inter SF Pro text and Roboto white
has regular and semi bold size is using
those global size variables for XS s
medium large all the way up to 10
XL line height is using XS small medium
large all the way up to 10 XL and if you
pair two of these where you might have a
size of large it's going to be 16 and
the large line height is going to be 24
which is how we've got our typ style set
up now and at the bottom we've got
letter spacing with excess small and
none so
-10.5 and zero okay that's all the
Primitive type variables let's going to
have a look at how we assign these to
the sematic type variables let's open
that collection and if we come back to
the top we can see that these two
variables are working together to give
us our modes of desktop mobile IOS and
Android with the breakpoint for desktop
being 1440 the breakpoint for mobile IOS
and Android being 393 and we can also
switch the family from inter for
responsive web to SF Tex for iOS and
Roboto for Android now if we go find our
heading Al which was in our example and
isolate that you can see how we're also
switching the size between the desktop
size and the mobile size so size is
switching from 5xl to 4XL and its line
height is switching from 5xl as well to
line height 4XL and if I break all of
those we can see that this style is
going to be 3 2 and desktop and 28 and
mobile and those are the line Heights
there let's undo that and if we come
back to all variables and scroll down we
can see that we've set up everything all
the
headings and all the text right so text
here is switching to regular from
semibold but there are semibold versions
of each one as well so we've got regular
and semi bulb there all the values are
staying the same between those two
weights and we just go all the way down
text accs which is 10 with a line height
of
14 all right we've got all of our
primitive type variables assigned to our
semantic type variables let's go and
take a look at how they're applied to
the Tex Styles here we are at all of our
type styles for web desktop mobile IOS
and Android and if we select heading Al
the same style it had applied to it last
time is still there right but if we open
it and then go to edit its settings and
we've got the name here semi Bold and
the properties here
here uh semantic type
family heading L semi bold
weight its size is hitting our semi bold
size the line height you guessed it is
heading L semi bold line height and the
letter spacing
is1 and we go down to another style
where we've got text Al regular the same
is set up here so everything's now
connected and we can start using them
okay so let's create a frame come down
here just going to drag it out select it
and tell it to be an iPhone 14
pro just going to move that back to here
and rename it type
variable test and let's just zoom
in I'm going to add some
text just call this hitting
L just position it about 32 from the
left 60 from the top is okay I'm going
to duplicate that come down here and
type in text
Al and then I'm going to go and add the
style so I'm going to type in heading
L let's go down and select it all right
going to do the same for text
L
regular let's give these a color as well
so so I'm going to go content
primary and content
secondary okay now I'm going to select
the frame and then apply one of the
modes to it so we can switch between
desktop mobile IOS and Android and see
the width not only change but also the
type family okay so let's go over to
layout scroll down and find semantic
type
breakpoint all right so that snapped it
back to desktop then we're going to go
to
appearance and then select semantic type
now desktop is the same because we're
already there but let's swap it to
mobile okay so what you saw there was
the heading go down and size but not the
text we don't need the text to go down
and size for responsive mobile but the
heading did now let's swap it to iOS
okay the family for both of them change
to SF Pro and then Android changes it to
Roboto let's just move this over here
and switch it back to Mobile so now
we're set up in figma in the exact same
way we're set up in code with our
sematic variables and their mixes and
just to recap we've got our primitive
type variables here where we're doing
things like setting up family weight and
size with global
units we've got semantic type where
we're setting up the modes and their
break points and families and we're
following that mixing approach that we
have in code with each style having its
weight size line height and letter
spacing variables and you can change
them by just doing it in the same way
that you've learned throughout the rest
of the series and that's it for type
variables in the next episode we'll be
doing iconography I hope you're looking
after yourselves and each other and I'll
see you in the next one bye