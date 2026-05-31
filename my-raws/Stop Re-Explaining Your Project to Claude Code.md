# Stop Re-Explaining Your Project to Claude Code

Every codec code session starts with
five to 15 minutes of context
establishment. It requires manual
digging through all conversations
finding where things left off and my
most common prompt was hey what I was
working on. You close a clo code window
and the context is lost. So you need to
reestablish it and you do the same work
again next time. Okay, how do I find
those two files? Which files did I
create? What decisions were made? and
all of that you need to explain every
session and this really wastes so much
energy. So you have a a bunch of
cloudcut code sessions and there is no
end to them. There is no way to capture
a state of of the work on this project
and the next day you just close
everything. It gets too crowded and you
start everything from scratch. In this
video I'm going to show you a three
things. A session file that survives
across your clo conversations. Obsidian
dashboard that gives you a live project
state instead of stale cloud.mmd and a
handoff prompt that transfers exactly
what matters to your agent. Okay, a
cloud code session is just a single chat
conversation which you have here in a
terminal and once the context gets
filled up as in my case I can check my
live context with a context command. I
spent more than 200k tokens in the
session. So the context window is full
but my work is still not over. And a
session file helps you to keep track of
across multiple cloud code
conversations. Here's example of how the
session file can look. The session file
is just a markdown file which contains a
goal which wanted to achieve the
background context on this project. The
definition of done and here the core
idea is to capture the progress as we
work. Here on the right we have those
cloud code sessions. Okay. So once the
context window filled up we update our
progress status in this node and then we
transfer the context to another agent to
another cloud code session to start
fresh. So this way you can capture your
work across multiple working sessions
multiple days. A very simple example I
have this project. I'm developing a
course right now and I have those
working sessions inside of this uh
dashboard and it displays me my sessions
where I was working and uh here we are
capturing the progress on what I've done
in that session and those sessions file
can really span multiple cloud code
conversations multiple days of work even
multiple weeks of work for each of cloud
code sessions you have its own session
file Well, with the ability to track the
state of the project which you're
working on. So that's very cool. A
session file for your project is still
not enough to capture the complete state
of your project. And this is where we
introduce this concept of uh dashboards
which enable dynamic memory. Those
dashboards they can contain the project
state uh work in progress current tasks
sessions context uh which already shown
your working plans and this something
that changes all the time depending on
the current state of the project and I
want to make a clear distinction between
static memory which is claw.md which
captures points which don't change much
for example your working style who you
are what are your preferences how do you
like to interact with AI that's clcmd
and here I shown you session file
example of a session file and you can
see that it's being linked to this
dashboard so and this dashboard contains
overview of the project active sessions
uh plans open tasks this is example of
of a simple dashboard and here what I
really love that uh what we are doing
here is we're using the data view plugin
to look for the files which contain link
to this dashboard and you can aggregate
all of the sessions, all of the plans.
Here is the plans and you can do it for
any type of projects for any type of
your files. You could also have here a
reference documents for example and this
is supported all within the single
dashboard. So to demonstrate how this is
working, what I can do is uh I can
provide this u path to this dashboard
and tell to read it. I'm telling that
okay so let's load the state of this
project it uh reads a smartman file it
sees that it has those queries and then
it resolve them through this data core
plug-in data core actually in data view
are u similar plugins um we have similar
capabilities now the most important
piece that we dynamically resolve those
queries we have plans we have all
attached session files and now agent can
see okay what we were doing there And
this way we just loaded u everything
into our memory and we can continue
working from where we stopped and that's
been a dynamic memory enabled by the
dashboards. Yeah. To sum it all up we
have a markdown node and we have
embedded uh views. It could be bases. It
could be data view with all of our
sessions with our tasks with our plans.
Then we can ask clot to resolve those
queries and in the end we just get a
table loaded into the clo context. You
can ask it to read the files or not to
read the files. It's our decision. But
the main idea that we are here aligned
with clot. Now clot exactly the same
picture as I do and I can continue
working where I left off. It's very very
convenient. and I use it all the times
and I recommend you to audit your quad
autom to see what's uh stale there and
update it. Move out all of your project
so many changes dynamically into those
dashboards to make sure that you always
have up to-date memory. Now we have
those sessions and dashboards for
tracking. That's very good. But actually
what happens if you hit uh your context
window limit? Right now I'm here at 200k
tokens and there's this concept of a dam
zone. Here is a diagram. Okay, you can
imagine that this is 1 million context
windows. This whole box here you have
loaded your systems uh plus memory
instructions and you keep executing you
keep uh chatting with a clot until you
hit uh this this boundary. I define it
as uh 200k tokens. That's my rule. If
you're using software engineering, the
rule might be a bit more strict. Some
people say, "Okay, it's high key
tokens." It's somewhere in in that zone
where clo starts cutting corners. It
just becomes lazy. It becomes um
forgetful and continue working beyond
200k tokens is just uh harmful. So, and
what people do here, there are a few
ways. Um a standard way is to do a
compaction. If you're familiar with the
compaction, so there is this compact
command uh free up context by
summarizing the conver conversation so
far. So this command is great and it
solves this issue but I have a few
problems with that command and one of
the problems is that um I can't capture
my learnings right now with that
command. So how do I transfer the
context to another agent and I I want to
write this information in my obsidian
into a session file. That's the first
piece which I'm missing. Second piece is
that this command is not flexible. I
can't change the prompt for compaction
because it's um a custom slash command
which I have no control over. and say
what if I want to have a to start a new
session to present a plan what was done
before and what is the proposed plan for
the next steps let's say you've been
working uh with a cloud code session you
hit your 200k tokens then what I do from
there is I run this handoff command
which uh captures what what I've done in
that session what are the next steps and
what's the intent for the next session
so let me just demonstrate that and
before closing my session I also on uh
retrospective skill which I showed in
one of the previous videos to capture
the learnings. uh in this session I was
uh doing the outline for my video
preparing the presentation and uh there
are a few moments which u kind of went
wrong and you can see that okay cloth
captured 12 corrections and I'm saying
okay this is bad um this is AI slope
and we are analyzing what is the work
which we've redone and then we are
proposing the additional changes to our
skills and here is the proposed diffs
which I agree with uh and I tell let's
apply those divs and this is extremely
valuable so that next time whenever I go
through this uh workflow I don't have to
explain again that it needs to be done
in this particular way it's been
extremely helpful now we added uh few
pieces to our memory and we are at 23%
of our context window and right now I'm
going to run this end of command and
I'll tell continue um and by continue
means if I want to work in on that
project I type continue. If you want to
park this, I type park. But let's try uh
continue. And that's my most common
scenario. What it's going to do is it
reads this workflow on how to continue
work. Now it analyzes if there are any
uh comments left, if there's any
feedback. It also grabs my CMAX
workspace ID. I use this terminal called
CMAX. It's uh very useful and you you
can see how useful it is right now uh in
the in the way that agent can actually
programmatically interact with this
terminal. Uh it can type to any terminal
window which is open here to any surface
and I use this to restart my work. Right
now agent is generating um a handoff. It
wrote this handoff file. Right now it
schedules this auto continue. So I'm not
uh touching anything. Right now agent
from me just uh types um the next prompt
and starts a new session and it tells
another agent to okay here's a handoff
follow the instructions and this is
continuation from the previous session
and this is what was done here is the
current state and here are the proposed
next steps that's the power so now we
are that 4% uh context window we are
just restarted everything and we can
continue our work this way. Well, if I
want to park this, I would type hand off
park and then we would update our
progress into a session file in
Obsidian. And this way I can capture uh
the current state of the project and
then whenever I want to continue on in
this project, this is a video. I can
just u read it from the session file in
Obsidian directly. And now that you know
how to never lose your context ever
again, you might also find it useful on
how to build a dashboard for your life.
Here's example of mine dashboard. That's
the next video.