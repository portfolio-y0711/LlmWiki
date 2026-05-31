# I Built My Entire Design System in 4 Hours With AI. Full Tutorial (Claude + Cursor + Figma)

Your team takes two weeks to ship a new
feature. My team takes two hours. The
difference, we built our design system
in code and it took us one afternoon.
62% of devs waste time rebuilding
designs because of broken handoffs
between Figma and code. But what if I
told you you could take your entire
design system and rebuild it in code in
just one afternoon? So why doesn't
everyone have a design system in code?
because historically it's been
incredibly timeconuming and complex
until now. We need to establish our
design foundation. I'm going to have
Claude build out the full style guide
using our Figma component library. Take
a look. Here we have our foundations,
our colors. I t our typography, our
icons. This is a very mini version that
I'm showing. Of course, yours can be way
more robust. So, we're going to start a
new Claude conversation. A key here is
every time you start a new feature, a
new part of a project, you should open a
new claude window to chat with. This
means that that whole context will be in
this one chat. I'm also going to give
you a tip on how to make sure you save
all this at the end, so stick around. To
create the style guide, we're going to
prompt it. Create the style guide. Call
it style tokens.ts.
All color variables, typography,
spacing, borders. create a style guide
page and then extract those values from
the MCP connection. So look when it's
done we will have this um it is
definitely a very entry point version
but you can see that everything is
clearly defined here.
We have the color palette
icons some usage recommendations common
all pulled and extracted from the Figma
MCP. So now we have the single source of
truth for all of our components and
tokens from here on out. Every color,
every spacing style, every font all
pulled directly from Figma and codified
in Typescript. Now let's start to build
our component library. So I have already
started to compile this component
library and I'm going to show you how to
start it and to build upon it. Here you
can see that we have everything defined
and how we do it.
Let me go back to this one. So we have
the interactions, the designs and we
have very detailed how everything should
function.
This is pulled directly from our Figma
files and we work with our devs to make
sure this is clearly defined for them as
well. You can see we do this. We also
provide a usage example.
Perfect. Let's go ahead and build out
these KPI cards.
I'm going to use a very detailed prompt.
Let me show you. Let me walk through
what I've done here. I am creating a
workflow.
This is important because it's going to
set up Claude to go through each step of
my workflow before throwing and
designing something that might not be
following the exact guidelines that I'm
suggesting. So here's my workflow.
Initialize, setup, and analysis. So this
is basically looking at the Figma file.
Analyze and extract the component data.
This is really important. It's not going
to build it just from what it sees.
actually going to pull how every hover
state, every interaction works.
Follow the visual specifications.
Look at the behavioral specifications.
Now implement
then create the interactive component.
Build it fully. Add the proper
TypeScript. Include all variants. Create
a preview.
and make sure you are applying the
design tokens
preview property preview.
Now the component specific feature
should be built. Now documentation
generation
create a txt. So every single component
can have a txt with all of these rules
and specifications so that every time
you're using this component, it is
following this exact framework.
Now the output structure add it to the
component page in an additional tab
again. Here's the execution order. Go.
So I'm going to run this. See here, this
is the task list. This is amazing. I
love this about cloud code because it's
going to start work through that list
that I gave it and it's going to check
off each stage. It's getting the context
here.
Okay, so it has done every step and it
is documenting. It did step one, step
two, step three, four. Okay, so let's go
take a look and see it matches. We can
go here and head to metric card. So we
have this metric card. Here it is the
full design. It matches Figma perfectly.
It also has this documentation. So this
is for Claude and for the devs and for
the designers to understand this is
exactly what tokens it's using, how it's
being built. So whenever there's a
change in anything, we will update this
file and this component which will apply
to every place that this component lives
in the product. Okay. So now let's build
a real feature. We're going to build a
feature using a screen that features
this card in it. Let's build this
screen. So, we're starting to put these
components together.
This is a component. This is a
component. These are components. So, I'm
going to ask it to start to build the
screen and adhere to the components in
the platform. Okay. So, let's open a new
window. And we're going to paste the
prompt. Again, this is a very detailed
prompt. It's very similar to the one you
just saw. I'm asking it to follow the
specific workflow to make sure that it
is starting to build the screen adhering
to the components in the layout of the
screen.
Initiating, analyzing, generating the
screen specifications following the
exact Figma
implementation.
Create preview follow the design token.
So this is really important, right?
Follow the design tokens.
style the preview
content preview. So, it has to go
through every single one of these items
before it actually builds it. Let's see
what happens.
So, again, it's coming up with this
to-do list. It reviewed everything I
said, the KPI card, everything.
Let's see. Look, it has completed every
section,
every task.
So, in Philadelphia, let's go file
structure. This is great. Kept this
updated. Added new pages. Let's go test
it out. Okay. So, there's some spacing
issues going on [laughter] that we need
to fix. Um, which is fine. We'll get
into that. But for a first draft,
this being able to clearly define this
information, this KPI
component. Overall, good. Let me go in
and see if I can clean this up a little
bit. And let's see if we can get it
performing more correctly.
Back mode. So, it should be 16 point,
right?
Okay, let's go see. There we go. Fixed.
Beautiful. Follows the exact
Figma design
you see here. Now we can continue to add
components. So you'll see some of these
pages have these additional components
which we will build on. Now last thing,
remember I said a little tip about
setting up all of your separate chats. I
want to make sure that any content that
I've done, it's saved. So I want to say
save this chat record to
project
context dot
MD.
So now it's going to keep track of this
entire project.
See it's putting session three date and
what happened from this chat. So I
suggest doing this with all your chats.
And if you want to try this yourself,
this is what I recommend. Build your
style guide first. Start with one
component, build one feature, and use
notes.md. If you found this valuable,
give it a like and subscribe. I'm
creating more content on building faster
product teams with AI. Thanks for
watching. Now go build something
amazing.