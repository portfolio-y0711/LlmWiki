# I Built the Same App With Claude Code and Codex

Claude Code, or Codex, which one is the
best for coding? Well, in this video,
I'm going to answer that question. I'm
going to run both Claude and Codex on
the exact same set of tasks and give you
my verdict on which one is better. Now,
by no means is this going to be
scientific. I'm just going to give them
a pretty complex app to build and see
what result we get. And I'm going to be
judging them on the following criteria.
We're going to first of all, look at the
speed. How long does it actually take to
run? We're going to look at the cost, so
the number of tokens, the usage, or how
quickly I run through my subscription.
We're then going to be looking at the
actual finished result. Is there bugs?
Does it work? Does it adhere to the spec
that we gave it? And then finally, we're
going to be looking at the code quality.
I'm actually going to get each model to
review the other model's code, and then
I'll manually review it myself as
someone who is a software engineer to
give you any insights I might have.
Anyways, with that said, let's get into
it. I think this is going to be fun to
see the actual live comparison between
these two tools, which are the most
hyped AI coding tools out there. So,
let's have a look at what we'll be
building. Now, I'm going to attempt to
build Collab MD, a real-time
collaborative markdown editor, which is
relatively complex and is going to test
how well these perform under real coding
situations. Now, we're going to be
looking at features like split-pane
markdown editor, real-time
collaboration, so we're going to be
connecting via what web sockets and
having to resolve maybe multiple
conflicts or changes on the same line,
cursor presence and awareness, document
management, auto-save and persistence.
And then if we get to it and it doesn't
break before then, we might add some
other features like a version history,
export, all of that kind of stuff. Now,
to keep this fair, I've written down the
core tech stack that I want both of
these models to use. I've given a really
quick architecture and kind of just an
overview of some flows, and then a quick
layout of the different UI components
and kind of how I want it to look. I'm
trying to keep it relatively open-ended,
but I also want to make sure that
they're going to use the same tech
stack, so we can evaluate them fairly.
Now, that's kind of the spec, and what
I'll do is I'll pass this spec to each
model before we start as context, and
then I'm going to go through a series of
prompts, which I have right here. So,
rather than just saying build the entire
project at once, I'm going to go through
eight different phases. The first phase
is going to be scaffolding the project,
where we'll use this prompt that's
already written. Next, we'll do the
basic editor and the preview. Then,
we're going to add the real-time
synchronization. Then, we're going to do
the cursor presence. And then, we'll go
through landing page, document CRUD,
we're going to do connection status,
error handling, reconnection, version
history, and then export and dark mode
again if we get to that phase. I don't
know how long this is going to take.
Now, I have all of these written out.
What I'm going to do is open up Claude,
open up Codex. Let me quickly go through
a few of my settings. Then, we're going
to start running this, and let's see
what we get. So, I'm pretty close to a
fresh install on both of these softwares
here. At least, I haven't used them very
much on my computer. I have Codex, but I
don't have any sessions because I was
running it on another computer. And I
have Claude code, where I just had a few
in the past few months, but I haven't
even been on this machine in again like
two or three months. Now, I have both of
them active in a uh directory, which
we'll have a look at in a second. And
I'm going to put both of them in kind of
the bypass permission or full access
mode, so I don't need to manually accept
all of the changes. Now, in terms of
models, I'm using Opus 4.7, and I've
just put it in the max mode, which is
the highest mode it has. Then, on the
Codex side, I'm using GPT 5.5, as you
can see here. I'm using it in extra
high, and I am not enabling the 1.5x
speed because I don't have the ability
to do that with Opus 4.7. Now, I
actually think Opus 4.6 is better, but
we're just going to use what they're
claiming is the best model. So, I'm
using Opus 4.7, 1 million context, GPT
5.5. The context is lower when it's
using Codex, but that's the best that
they have. And then, the highest
reasoning available. I don't care how
much this cost me or how long it's going
to run. Now, quickly, if we have a look
at my usage in Claude code, you can see
that I'm at 11% weekly, 5% 5 hours. So,
hopefully, we can get through this. And
then, if we go and have a look at, I
guess, the usage here for uh what do you
call it, Codex, you You can see I'm at
100% that I have remaining and 99% for
the weekly. So, we can go back to those
values and see how quickly we rip
through the subscription in a second.
Now, you might also be wondering, how am
I actually going to evaluate these at
the end? Well, I will do a code analysis
and one of the reasons I can do that is
because I actually do know how to code
and learned it for a long period of
time. And with that in mind, if you want
to learn how to code, then I need to
tell you about today's sponsor,
boot.dev, which is one of the best
learning platforms out there and my
long-term partner. Now, one of the
biggest problems that I see with people
learning how to code is boredom. They
watch tutorials, copy code, feel
productive for a week, and then quit.
Now, boot.dev takes a completely
different approach. It's very hands-on
and honestly feels more like a game than
just a course. Now, you're learning
back-end development by actually
building things, not just watching
videos. You work through real challenges
in Python, SQL, and Go, earn XP, level
up, fight bosses, and progress through a
full back-end curriculum. Now, it sounds
gimmicky, but it actually works because
you're doing the same kind of
problem-solving that you do on the job.
Now, they also have an AI tutor called
Boots, which doesn't just dump answers
on you. It asks follow-up questions and
helps you reason through problems when
you get stuck, which is way closer to
how you actually learn. Now, all of the
content is free to read and watch, and
if you want the interactive coding,
progress tracking, and AI help, that's
part of the paid plan. Now, if you want
to check it out, go to boot.dev and use
my code Tech With Tim to get 25% off
your first year. Big thanks to boot.dev
for sponsoring this video. Now, let's
get back to it. Okay, so I'm going to
start by loading in the markdown file.
We're going to give it the first prompt.
Let's start running it. So, prompt one
is in. Let's start running these
approximately at the same time and let's
see what we get. Okay, so Claude Code
just finished here. We're about the
6-minute mark. Uh I said that it's
working properly, had some issue that I
need to fix. Looks like this one is
almost done here for Codex, but it's
still running. So, once it's done, I'll
be right back. Okay, so finally, Codex
has finished here. Funny enough, it tore
down the process that Claude code was
doing, so it was able to run on the same
port because there was a conflict that
it found. And in this case, it ran for
14 minutes. I don't think Claude says
the exact amount of time it ran for, but
anyways, it was about 6 minutes in my
estimations, and so this one took 8
minutes longer to run. But, if we
quickly pop open the code, we'll see
Let's quickly look at Claude. We can see
we have clients, right? Let's zoom in a
little bit here. We have our source,
okay? We have our server, we have our
source here.
If we look again, we just have a few
files, okay, that's fine. And then if we
look at Codex, you'll notice that if we
look in the client, and we look in the
source, we have a lot more directories.
The scaffolding is a little bit more
complete. If we go to the server, you
can see same thing. We have like a types
file, DIST, data, all of this stuff that
we don't have in the Claude version. I
know I'm going through this very
quickly, but the point is that while
Codex did take a lot longer to run, it
just did a lot more. Now, if we open up
the Codex app, this is what it looks
like. And from Claude's side, even
before Codex was running, I didn't see
anything appearing at all in the browser
when I asked it to run it. So, just to
be fair to Claude, can you run the
application, pre- please, so I can
preview it?
Let's see if it can do that because
again, it never gave me a preview. It
didn't verify anything. It just said,
"Hey, you can run the server." But with
Codex, it actually opened up the
browser, it went through, it verified
that it was working, it created a new
document. I was watching it do this in
real time using the computer use task,
and I gave Claude the same ability to be
able to do that, but it just didn't do
so. Okay, so it now ran it. However, it
still didn't run it in like the preview
tab that it it did in Codex, but you can
see this is what it looks like. Of
course, I can't press the button yet,
but at least it's kind of spun up. Okay.
Okay, let's move on to the next task
here. Same thing, I'm going to paste in
the next prompt. What I'm going to be
doing here is building kind of the split
screen editor. So, I'm saying left pane,
right pane, add a top bar, all of this
kind of stuff. Same thing, let's run
them relatively at the same time, and
let's see what the next progress is. All
right, so now this time both of them
finished at the same time. Uh the Codex
application is running right now on
5174.
The chat or the Cloud Code one, sorry,
is not running for some reason. So, same
thing, let's quickly tell it, "Can you
make sure this is running on port 5173
so I can access the user interface?"
And let's see if I can get that spun up.
It seems to have some issues getting it
working in deployment, but while it's
doing that, uh let's have a look at
CollabMD here. So, there's a new
document. If I click into it, uh we get
some kind of infinite loop happening.
So, obviously, that's a bug that we're
going to have to fix. If we go back, we
can delete a document. We can make a new
document. And then, okay, there we go.
If it's in another one, we can say
hello, and okay, yeah. So, same thing,
we got some bug.
Now, go back here. Let's see, do we get
it running? Nothing is listening. Okay,
let's see if it runs. Okay, so Cloud
Code is now up and running. I'm here.
However, the new document button doesn't
seem to be working. So, it said I can go
to /doc/test,
and there we go. So, let's go maybe like
hello world. And at least the editor is
working this time. So, I mean, the
button didn't work, but it looks like
overall the features are better than we
had in Codex. And it's not giving me
this like weird um you know, infinite
loop bug. So, anyways, let's continue
now. I'm going to tell both of these the
issues that I just quickly found, and
then give them the next prompt, and
let's see what the next iteration looks
like. All right, so I told them both the
issues. The next thing that we're going
to do is add the real-time collaboration
here, so that both people can kind of be
messaging or changing it at the same
time. And let's go ahead and submit
these. See what we get. All right, so
interestingly, Codex wrapped up first
this time around the 7-minute mark.
Cloud Code is still going, finding some
problems here. Again, it's having a lot
of trouble actually running the dev
servers and getting the deployment up,
as you saw, whereas Codex seems to not
have any issues. So, while that's
running, let's have a look at Codex's
finished version here. Just refreshed.
Let's see if we open it up. Uh let's
open a new one because this one's
destroyed from the last time. And let's
do something. So, I don't know.
Hello world. Let's try to do like some
Python code or something. Python. And
let's go def function. Okay, that seems
to work. 1 2 3. Cool. All right, nice.
So, that looks like it's good. Now, if I
open up another tab here, let's see if
we can edit it in a real time. And it
looks like it's even maybe doing the
cursor thing. So, if I type here, we can
see in the other one, it's like pretty
much happening instantly. Actually, it's
probably easier if I open these real
time, so we can see it. So, if I go like
Hello world, looks like that's updating.
Let's close that off. Let's see if I
delete someone else's. And it looks like
the real time collab is working. It's
actually already giving us the cursor
identity thing. Although, that was weird
that it says user 83 there. Um yeah, not
sure why we're getting that. But,
anyways, you guys get the idea. Looks
like that is working. And the real time
stuff is functioning, which is pretty
cool. Okay, now let's wait for Cloud
Code to finish and test its version.
Okay, so Cloud Code is done. We're just
testing this out. We can see seems like
it is working. It's giving us the cursor
intent as well, and even the highlight
same thing is functioning. The button
was working. Not when I pressed share,
but when I pressed the new document,
that seemed to work. Although, it
doesn't seem to be saving the documents.
Maybe it needs to refresh. So, that's
maybe an interesting bug that we can
have a look at. Anyways, point is,
that's functioning. Now, let's move on
to our next prompt. Okay, so we're
moving on. Next one I said is just add
the cursor presence, even though it kind
of already has that. This is prompt is a
little bit more specific, so we can
actually see where each user is, how
many users are connected, all of that
kind of stuff. Obviously, I'm not
testing this completely at scale, but
that's going to run. Now, while it's
doing that, let's quickly just dive into
the code before we go too much further.
So, if we go in the Claude app, we have
a look at client, we have SRC, we have
some components, some pages. Just open
these up, make sure we don't have any
massive components here. Overall, looks
fine. Looks like it's using, I believe,
Tailwind here for all of the styling.
Okay, we have this kind of new editor
object. If we go pages, we have an
editor that's created here. Again, not
too big. Seems fine. If we go index.css,
not really much going on there. Yeah,
just have the Tailwind imports. Moving
over, we have some scripts. I'm not sure
what this is doing, async smoke.mjs.
Okay, interesting. If we go to the
server, we have the database that's just
stored there. And then we have SRC, we
have DB, we have index, and then we have
this. Okay, so not too much code
overall. I'd say that's pretty good. If
we have a look at Codex, let me just
close all this for now. Go clients.
Looks a little bit more structured. So,
we have types, pages, lib, components.
Things are a little bit more separate
out in terms of the API calls. Now, it's
doing the presence awareness, obviously,
so we're getting that as well. For the
users, okay.
Distribution, we have the assets. Got
that. Node modules. What else we have?
We have logs. Looks like it's actually
storing the logs, which is useful. And
then, if we go to the server, we have
our data, our dist, node modules, our
source, we have our types, DB, and then
index.ts.
Nothing's too big. Nothing's crazy
unstructured. So, overall, looks pretty
good. Let's see what this next prompt
gives us. Okay, so it's been about 5
minutes here. Claude code wrapped up at
1 minute ago. Codex is still going here,
and it's trying to now actually test
everything. So, that's one thing I
noticed with Codex is that it spends a
long time trying to verify its work, and
actually go through like the browser
control steps, which obviously takes a
little bit longer. Whereas, Claude code
kind of just like finishes it, and it
doesn't actually verify it. It's not
going and doing all of the testing in
the browser like Codex is, even though
I'm not directly asking it. So, that's
kind of an interesting thing at this
point. Anyways, let's wait for them to
finish and we'll see where we're at. All
right, and Codex just wrapped up here
about 3-4 minutes later. And again, it
was doing a lot of the verification and
said that that worked. Now, if we
quickly just open these up, I have a
bunch of browser windows now I got to
organize. So, this is the Claude Code
version on the right side. You can see
that we have kind of like the user
showing up, the different cursor icons.
On the left side, we have the Codex
version. Now, what's kind of interesting
is the cursor only appears when it's
actually active in the browser. So, like
when I'm moving between the browser
windows, you can see the other cursor
kind of disappears, which is cool to
see. You can see everything's showing up
here. Shows us the icons on the top,
which I think looks a little bit better.
And then it seems to be saving it if I
go back here in the correct area. Again,
overall, you get the idea. It's working.
It's functioning. And we are good to go.
And now we're going to move on to the
last prompt. So, I actually had a few
other prompts, but I'm just going to
combine all of them together so we can
kind of throw a larger task at these and
see if it can complete just all of the
other features that I wanted done for
this app. So, for the final prompt, I
kind of just combined steps five, so the
landing page all the way to the polish,
to the version history, to the export
and dark mode. I just took all of them
and combined them together. I passed it
both to Claude and to Codex. Let's see
what we get. Okay, so finally, both of
these are done. Now, in the case of
Codex, this took uh what is it? 26
minutes to run, which is a long time.
And Claude Code took maybe 7 or 8
minutes. Now, the one thing that I did
notice here is that uh Codex was doing a
lot of testing, so it was actually
trying to spin up the browser, go
through it. It did mess something up, so
I gave it one additional prompt say,
"Hey, you got to fix the styling." It
like disconnected something. But, it was
spending a majority of the time actually
trying to test all of the features that
it wrote. Whereas, what Claude Code did
is just write all of the features,
that's it, I'm done, go, you know, check
it out yourself. So, if we look at the
finished apps, to be honest, they're
almost identical and I didn't really
notice any major like flaws in either of
them. Uh if we have a look, this one
created a bunch of tests itself. You can
see it has this like little green thing
to show you where you people are active
in it. So, we can see if we go back like
one person is here because it's open in
the same window. If I open it again, you
can see now it should update and show
two in a second, but I guess maybe
that's a bug. I don't know. It has like
a dark and light mode. You have the
ability to export it as like markdown or
as an HTML file.
And what else do we have? We have the
ability to share where it's like copies
the link and you can paste it in another
browser. And then again, you could see
all of the people that are in here and
it works, you know, in in real time in
terms of all of the updates as you can
see. Now, in terms of the Sorry, this
was the Cloud Code one. In terms of the
CodeX one, same thing. We have the dark
and the light mode. If I click into a
document,
we can see that I can swap that over
dark mode here. 1 2 3, we get our code
block, you know, pi
Hello world, whatever. If I open the
same one, so let's open that here. We
should see now that this will get
updated to two in a second. Let's
refresh. Yeah, you can see two.
We have the cursors, the highlight. Same
thing, share, put it in another window.
Now, if we go back here, we get three.
And you can see we have everything kind
of showing up and appearing and we can
see all the active cursors and whatnot.
Let's go back here and you can see, you
know, it's kind of popping up. So,
overall, we got pretty much the exact
same result at the end of this. I mean,
few very minor differences. So, now it's
really a matter of having a look at the
code quality and seeing which one gave
us a better outcome. So, if we start
with the Cloud app here, like we showed
before, if we look at the client, we
have our SRC, we have components, lib,
and then pages. We have a not found
page, editor page. This looks a little
bit messy to me at just first glance
when I'm kind of reading through this.
We have a lot of nesting going on,
although I that's just kind of
JavaScript and TypeScript code for you.
We have a bunch of inline comments,
which I don't really love. We have
direct calls to APIs, you know, directly
inside of use fetches. That's usually
not a best practice. And you also
typically want to have some kind of
function for that, so that's not great.
Again, just a lot of like very kind of
complicated code at first glance. Um
obviously, the styling, we can't really
avoid that if we want to use Tailwind.
This is a bit weird to see for exporting
the HTML, but I guess that's just how it
did it. We have a toast. We have a theme
toggle. I'm not going to go through
everything, but I'm just generally
trying to get kind of a sense of what
does the code kind of look like? At
least it's pretty modular on the
component level here. So, we have a lot
of different things for like, okay, we
have the history panel. We have the
markdown editor. Again, I don't love all
of this stuff um in the same file as the
component, but it's not too bad. Split
pane.
Yeah, same thing. We got a lot of kind
of nesting going on here. But overall,
it's not too bad. So, that's from the
client side. Then, let's have a look at
the server. SRC, index. We have all our
API routes just kind of dumped together,
but it's only 200 lines, so it's not
horrible. We have something for the YJS
here. For the database, yeah, we're just
creating everything in one file, and
that's kind of all we have from the back
end. There's not really too much more
going on there. So, overall, code is not
too bad, but I think definitely, you
know, would not be the most maintainable
thing in the world long-term. Now, let's
have a look at Codex. So, we have our
client code, types, pages, libs,
components. Kind of same thing as what
we had before. Seems like Let's go
through here. Markdown editor is okay,
not too large.
Looks like it's a little bit more
modular in terms of we have some
separate use effects. We're calling
individual functions. I don't see
anything that's too crazy with the
nesting. It looks a little bit easier to
read.
If we go into the API, notice that we
have all the API stuff in a separate
file, which I I like to see. And it's
all typed correctly, it looks like. Same
thing for the presence, that's handled
in a separate file.
Again, looks pretty clean. I'm just
skimming through it to get a quick
sense. Theme, that's in a separate file,
I don't think we had that before.
User types, we have a types file, which
I don't believe we had before. app.tsx.
Then am I missing anything? No, overall
it seems like it did maybe a better job
at simplifying the code because it looks
like we have just a lot less code on the
client side than we did in our uh Claude
application. Now, we also put everything
in a data folder, that's good. We had
logs, which we didn't have in the other
application. From the server side, we
have our SRC, we have types, DB, okay.
DB looks similar. Yeah, very similar to
what we had before, a bit longer, but
some more functions to kind of separate
things out. We have a nice index file
here. Again, just skimming through for
the API. We have our types, and that's
kind of it. I mean, this doesn't have a
ton of code, to be honest, for this, you
know, type of application. So, overall,
I would say both code bases are
generally decent. Um you know, they're
definitely not the most modular or
following all of the best practices. I'm
sure if we went through it line by line,
we could find a lot of mistakes or
things that we just wouldn't want to
include in a production code base.
Overall, if I was going to pick a code
base I would want to have, I would
probably lean more towards the Codex
application, just because it seems like
the code is a little bit higher quality.
It seems like it's separated out a
little bit, and also it seems like we
have less code on the client side
compared to the Claude app, but I
haven't had enough time to really fully
figure that out. Whereas with Claude,
again, it seems fine, but it feels like
it's a little bit more overly
complicated in terms of what it's doing
there. We have so a lot of nesting, we
have a lot of weird, hard to parse, you
know, kind of files and comments. And
even if we look uh what is it? At the
client side here for, I I know,
something like this, we can see that we
don't really have a ton of inline
comments, whereas Claude tends to kind
of dump a bunch of comments in the code,
which I really don't like and is not a
great practice, especially as the code
base gets larger and larger. So, now
what I want to do is I want to take
these code bases, I want to pass them to
the opposite model. I'm going to get
them just to roast the code just so I
get a sense of what those models think,
and then we're going to wrap it up with
kind of our final evaluation. Okay, so
I'm not using those scientific prompt in
the world here, but I just said, "Hey,
review this code base, give me the
overall quality, what can be improved,
common mistakes, whatever." So, for
Codex, I'm giving it the Claude app, and
for Claude, I'm giving it the Codex app,
and let's see what it says. Okay, so
Codex is just wrapping up here, took
about 7 minutes. In the case of Claude,
this is maybe 2 minutes, and that's kind
of a trend I'm noticing here is that
Claude seems to be kind of right to the
point a lot faster, whereas Codex was
actually running tests on the
application. It was going in, testing
it, seeing, "Does this actually work?
What's going on? Let me create an
artifact. Let me test the server."
Whereas Claude just read the code. So,
let's go to Codex first reviewing
Claude's code, and let's see what it
says. Okay, so it says, "Websocket
writes can create documents outside of
the REST life cycle. Deleted documents
can be restructured by open clients. No
auth." That's fine, both those have
that. "Persistence is synchronous and
full document per update." Okay.
"History restore can restore stale
content." Generally says the code is
fine. However, the main pattern to
improve is the local fetch, like I was
talking about, where it's calling from
inside of the component. Tooling and
repo hygiene. Okay.
Client build, and then recommended
priority. Okay, not bad. And then with
Claude, it gave me a whole host of
issues of the Codex one. Not all of them
are really that actionable. Fake save
indicator, okay. Disk write on every
keystroke, I believe this one has this
well. Auth, that's not an issue. I think
that one's not an issue as well.
Directory mismatch, that's a small one.
Patch on every keystroke, migration
leaves orphan tables, okay. And And it
gives me kind of a nice table here of
what to look at and some
recommendations. So, I think at this
point I kind of have enough information
to give my overall recommendation on
which one you should use. Now, first
things to note, Claude seems to be a
little bit more direct, to the point,
just does kind of exactly what you ask
it. Codex on the other hand is a little
bit more proactive. Now, that means it
does take a little bit longer, but it's
kind of doing things that it knows it's
going to need to do, but you haven't
directly asked it for, like running the
server. You know, testing it, right?
Fixing a bug, whatever. Now, Claude is
definitely significantly faster. Now,
some tasks were getting similar, but in
most situations, I would say Codex is 50
to 70% longer, takes longer than running
the same task in Claude. So, when it
comes to building something from
scratch, it's always going to be faster
to do that in Claude. Whereas with
Codex, it seems like this is a little
bit more set up for larger applications,
things where there's a lot of testing,
where it's writing smaller amounts of
code, but it's a lot more complex
because it's doing a lot of kind of
deeper thinking and reasoning, at least
from what I can gather here. Now, in
terms of the overall code quality, it's
very similar, generally I would say. I
think with Codex it's slightly better,
but that's really just a preference. I
didn't read every line, so it's tough to
say. And then the last thing I want to
look at here is the usage, right? So, if
we look at our usage here, you can see
that I'm now up to 23% on my 5-hour
usage here, which is quite high. And the
context window was actually not that
large, which is interesting. Whereas
with um what do you call it, Codex here,
it automatically compacted its context
window probably three or four prompts
ago because it hit its maximum. We can
have a look at it here uh where it was
at, what do you call it, uh 258,000
tokens.
And then if we look at our usage,
let's go to rate limits, we can see that
our 5-hour window we're only down 5%.
So, I forget what the exact amounts
were, but I believe that with Claude,
we've used about two to two and a half
times more usage on our subscription
than we did with Codex. So, even though
Codex ran longer and did more thinking,
we got significantly more kind of tokens
per the cost compared to Claude or these
Anthropic models, and that's been pretty
consistent with other experiments that
I've done. Now, I don't know the exact
number of tokens used for these. I
wasn't using the API. I don't have the
exact bill. But, the point is if we're
going to use Anthropic, at least in my
estimation here, it's going to be
probably three to four times more
expensive than using Codex for the same
task. So, overall, my kind of analysis
here is that you should probably be
using both of these. If you're spinning
something up completely from scratch and
you want it to be done super fast,
probably we're going to go with Claude,
right? If we're doing something where
we're debugging, testing, we really want
to verify something's working, where you
know, working in a larger application,
Codex seems to work better for that. And
again, I've used these in other
scenarios as well, where I'm kind of
pulling some of this analysis from. Both
of them are ultimately very capable
models. They perform very similarly, but
just better in certain situations. And
keep in mind that I had both of these in
extra high mode using, you know, the
most intense reasoning you can. Whereas,
if I were to drop it into just high or
medium, of course, both of them would be
a lot faster. And even with Claude here,
or with Codex, sorry, I keep mixing them
up. I can switch on the fast mode, and
it would still be cheaper at that 1.5x
rate compared to using Claude, and I
would get a faster response, which would
almost make up for that kind of speed
discrepancy that we're seeing. So,
anyways, guys, with that said, that's
going to wrap up this video. I know it's
not the most scientific method in the
world. I can do some stuff that's a
little bit more scientific in the future
if you guys want to see that, so let me
know. But, I wanted to just try these
out, give you my honest experience, and
show you what these things can do,
because everybody's been hyping both
models. They're still limited in certain
cases. It is amazing what they can do,
but you got to know how to use them,
obviously, how to prompt them, and which
one to pick for which task, which was
kind of the purpose of this video. So,
if you guys enjoyed, make sure to leave
a like, subscribe, and I will see you in
the next one.