## Chunk 1

**[13:22:26 --> 13:22:30]** **1-A:**  Okay, all as usual. Madeline has made
**[13:22:30 --> 13:22:35]** **1-A:**  uh awesome repository for us to clone um and we're gonna keep practising this.
**[13:22:35 --> 13:22:57]** **1-B:**  Because it's an amazing core skill of using clone code. Um we're gonna clone this thing um and I'll walk you through that in a couple of different ways and maybe even show you a couple other tota uh the sorts of things you could clone from GitHub um in any case we're really happy that you all came back. Today we're gonna talk about some of the more advanced things we can do in this desktop-clone code app now that we finally have it working.
**[13:22:57 --> 13:23:23]** **1-B:**  today should be um far easier because now it's functioning and you're gonna be able to actually do things with it uh and so I'm gonna lead you through some of the things you can do just within the interface, some ways you can think about your folder structures, organise different projects, and then uh Madeline um and uh Becca have some examples of projects that are using what are called skills. I don't know if anyone's heard that term at all in talking about LLMs a little bit maybe here and there. Um but that's gonna be a way for you to have some reco
**[13:23:23 --> 13:23:23]** **1-B:**  recurrent
**[13:23:24 --> 13:23:53]** **1-B:**  moves, I guess we could call it, that you wanna perform on your inputs to get them into outputs. Um we've been doing a lot of manual stuff so far and saving our prompts maybe to a markdown doc, but skills are gonna be a really cool way of doing repetitive tasks we have to do a whole bunch of times. So Danny, I think, sent you the address and you should be able to get here. If not any of um our GitHub repositories are all at the same um organisation, the learning lab. And if you click repositories,
**[13:23:53 --> 13:24:01]** **1-B:**  is the top one is always the one we're doing today essentially uh and so let's remind ourselves of how we get this thing. There are couple different ways we can do it.
**[13:24:03 --> 13:24:05]** **1-B:**  One, we can click this little arrow
**[13:24:05 --> 13:24:17]** **1-B:**  and we can download the zip file and unzip that, wherever we like to download things, default to our downloads folder or wherever else. And then the other ways we can do it are by clicking the same button
**[13:24:18 --> 13:24:24]** **1-B:**  And then copying this URL, which is going to help us clone the repository.
**[13:24:25 --> 13:24:42]** **1-B:**  And for people that were doing things in the command line, um you would change directories into wherever you like to work for a lot of folks Madeline helped you create a development folder, and then I would just type in get clone and then paste that in and hit enter.
**[13:24:43 --> 13:24:45]** **1-B:**  The other way we talked about doing it
**[13:24:45 --> 13:24:51]** **1-B:**  is going to plot code um and opening up a new session
**[13:24:52 --> 13:24:59]** **1-B:**  in whatever parent folder I want to put my repository in. And so for me that might be the development folder.
**[13:25:00 --> 13:25:07]** **1-B:**  And then I would say, hey, can you clone this in. And I would paste that in.
**[13:25:08 --> 13:25:13]** **1-B:**  So let's all do one of those three things. You can get Claude to do it, you can do it in terminal, you can download it.
**[13:25:14 --> 13:25:32]** **1-B:**  Uh and I'll just kinda like walk through it on the website as I give everyone a sec to get it done, just to kind of remind us again from six ten that's today, click the green button, and then we just copy this U_R_L_ or we download the zip, whatever we would prefer.
**[13:25:32 --> 13:25:41]** **1-B:**  And then once we have that U_R_L_ we either tell Claude to do it in the code tab, or else we can do it in the command line if we're comfy with the the terminal.
**[13:25:45 --> 13:25:45]** **1-B:**  Amazing.
**[13:25:47 --> 13:26:04]** **1-B:**  So no matter how we do it, we are now going to open up a new session in that folder. And again, the way we do that is with a new session. And then we select the folder of today's repository. So we're going to have to navigate our way down into there.
**[13:26:07 --> 13:26:09]** **1-B:**  And as always, let's just say hey.
**[13:26:10 --> 13:26:14]** **1-B:**  What's in this repo to get started?
**[13:26:14 --> 13:26:18]** **1-C:**  And Marlin, there's a little pop-up that says meet Fable 5. Do you wanna
**[13:26:18 --> 13:26:19]** **1-B:**  You can save that is.
**[13:26:19 --> 13:26:19]** **1-C:**  mention?
**[13:26:19 --> 13:26:23]** **1-B:**  I have no you're more friends with Fable five than I am. What is that? What is that?
**[13:26:23 --> 13:26:40]** **1-C:**  Yeah, so Fable five, uh some of you may have heard uh probably through various articles of Claude Mitosis, which was considered one of the kind of most powerful models. It was a big cyber security risk, 'cause it could uh code so well, it was very good at finding kind of back doors.
**[13:26:40 --> 13:26:57]** **1-C:**  back doors uh to many of the public uh kind of code streams that the internet is built on top of and many companies have. So they released cloud mythos early to about forty different companies to try to help them patch up their own kind of security issues.
**[13:26:58 --> 13:27:09]** **1-C:**  And now they have released a model uh that they say is in the Claude mythos tier. So this is the newest model. Uh I don't know if you guys remember from when Marlon was doing the drop-down, but we've
**[13:27:09 --> 13:27:35]** **1-C:**  we've played with sonnet, there was opus four point seven then four point eight. You now may need see this oped uh fable five. That will use your credits more quickly. Also know that it has a lot of constraints on its output in order to make it safe. So if you put in anything that's even slightly related to cyber security or even slightly related to biology, I ran it last night on just a few
**[13:27:35 --> 13:28:02]** **1-C:**  articles about uh biomedical companies and it immediately flagged no I'm unable to do any processes related to that. So it's a very powerful model, it's really wonderful, uh but just know as they slowly roll this out and figure out what it's safe for, uh you might just run into random triggers where it will refuse to do a task and it'll bump you down to the second best model, which is still really excellent, Opus 4.8.
**[13:28:02 --> 13:28:03]** **1-C:**  But for a lot of what you do
**[13:28:04 --> 13:28:18]** **1-C:**  uh while you have these free Harvard accounts. If you wanna make sure you don't run out of credits too quickly uh for almost all projects, especially the ones we're showing in this course it's on it. Should be totally fine. So if you wanna switch them off let's go.
**[13:28:18 --> 13:28:18]** **1-D:**  Okay.
**[13:28:18 --> 13:28:19]** **1-C:** 
**[13:28:19 --> 13:28:31]** **1-B:**  Um for sure. And and the uh it's a switch to whichever one you want. I think very few of you are gonna run out with Opus. Um if you wanna see where you're at, you can always type in slash usage and hit enter.
**[13:28:32 --> 13:28:58]** **1-B:**  And what'll happen, this works both in the terminal and the desktop app, is it's gonna show you where you're at in your use of things. I'm at zero percent on this account. Uh the other way of getting to that is over in settings. Um I can go to usage and it'll give me a g little graph about where I am in the current session, which is kind of like a five hour period, and where I am in the week or the month, depending on the organisation you're part of, will um track that time differently.
**[13:28:58 --> 13:29:19]** **1-B:**  But uh I would probably just use Opus and then and then if you get impatient with it being slow, turn the thinking down from high to low, that's what I've got here just because as I'm demoing things I don't want it to take forever. Um you can put it higher, you know, when you're just doing things at your your own pace at home. Uh and then kind of hit
**[13:29:19 --> 13:29:30]** **1-B:**  the you know the one at once before you start freaking out about about uh cutting yourself off. If you're in a single chat at a time I think it's gonna be hard to go over over the limit. We'll just see, it'll be impressive if you do.
**[13:29:31 --> 13:29:32]** **1-B:**  Alright so those are
**[13:29:33 --> 13:29:46]** **1-B:**  So that's the model and that's the usage. And we've got ourselves in, you know, a new a new repo. Um once we've asked that question, does everyone remember how to see the files in the repo? It's over in this
**[13:29:47 --> 13:29:51]** **1-B:**  little icon up in the top right corner which only shows up once I've started a conversation.
**[13:29:51 --> 13:29:56]** **1-B:**  And if I click files I'll be able to see all the examples from this week
**[13:29:58 --> 13:30:08]** **1-B:**  And as always, Madeline, um we have in here a day three handout zone where you have the paper handouts, but if you ever want to, you could come back in here and see the day three handouts.
**[13:30:08 --> 13:30:20]** **1-C:**  Exactly. And then there's the day one and day two recap, uh and a glossary. So we're just gonna keep building this up so at any time uh if you don't if you've lost a handout, you will be able to print it again or see it.
**[13:30:21 --> 13:30:33]** **1-B:**  Uh and remember all the HTML files you can go ahead and open those if you want to up in your browser. And so these are the top ten key takeaways from last time.
**[13:30:33 --> 13:30:41]** **1-B:**  And today we're actually going to show you how to you know, if you want to do something like this where you're creating a templated handout from your text that you're creating how to do that.
**[13:30:42 --> 13:30:47]** **1-C:**  So, Marlon, could you just go through one more time how to copy in a repo and then switch in new session?
**[13:30:48 --> 13:30:49]** **1-B:**  Absolutely.
**[13:30:49 --> 13:30:49]** **1-C:**  Okay.
**[13:30:49 --> 13:30:52]** **1-B:**  So um if I were in
**[13:30:52 --> 13:31:12]** **1-B:**  a new session and I'm in the parent folder, like the folder that I want the repo to go into. And so for me that's development. I already have this here in my history. If I didn't, I would go and open the folder and I would select development or desktop or downloads or wherever, you know, wherever I want to put it, I could create a whole brand new folder in here.
**[13:31:13 --> 13:31:18]** **1-B:**  And then once that is selected and I'm inside of there, I can just go ahead and ask
**[13:31:18 --> 13:31:37]** **1-B:**  Claude, can you clone this repo for me? And then I would paste in the link that I get from where are you? This green button here, which gives me the the uh URL for cloning it.
**[13:31:38 --> 13:31:40]** **1-C:**  But then you need to switch to that folder.
**[13:31:41 --> 13:31:45]** **1-B:**  And then yes, so to then open up a new session
**[13:31:46 --> 13:31:57]** **1-B:**  And we're gonna do this several times today 'cause we're gonna create some different projects. In any new session, what I need to do is change into the folder where I wanna be running things, and so I'll get out of development
**[13:31:57 --> 13:32:11]** **1-B:**  and I will open a new folder and it's wherever I know I put it inside of development, it's where I put clod code twenty twenty six six ten is the f is the one for today. Click that, select it, and then I'm in there.
**[13:32:12 --> 13:32:15]** **1-B:**  So I'm always gonna see whatever folder I'm working in down here.
**[13:32:17 --> 13:32:22]** **1-C:**  Okay. So you make one session just to clone it and make a separate session to then
**[13:32:22 --> 13:32:24]** **1-B:**  Exactly, and then I'm uh what I'm about to show you is event

## Chunk 2

**[13:32:25 --> 13:32:42]** **2-A:**  Eventually you're all gonna be in the position I'm in here and you already probably have a little bit in your s your history where you can now just select the folder you want within the desktop app. So I wouldn't actually have to go every time and select it and navigate it to development. I can just go back to development if I wanna work in the development folder, and if I wanna work in a different folder then I can select
**[13:32:42 --> 13:32:42]** **2-B:**  Or
**[13:32:42 --> 13:32:42]** **2-A:**  it here,
**[13:32:42 --> 13:32:42]** **2-B:**  could you
**[13:32:42 --> 13:32:43]** **2-A:**  'cause it's in my history.
**[13:32:43 --> 13:32:47]** **2-B:**  go to yesterday and show the git pull mic?
**[13:32:47 --> 13:33:14]** **2-B:**  most problems. But for instance, if you went to yesterday's, you could click into that date from yesterday, and if you wanted to see any updates that happened to a folder, if you guys start to use GitHub, I you would type in, can you please do a a git pull of this repo, um and it'll pull down uh any documents that were added from that first time that you downloaded those files. So GitHub again is a really great way to share those files, but it uh if you do it through the zip
**[13:33:14 --> 13:33:37]** **2-B:**  zipped um it can be kind of trickier to do this. Get pull, if you do a get pull, it it's this more living document, that's what makes it more similar to kind of a google doc, is multiple people can kind of collaborate on it, um and then pull down. So this for instance is pulling in uh and it's just kind of like letting us know uh more so that yes, there's more kind of chapters that were built. Awesome.
**[13:33:38 --> 13:33:47]** **2-B:**  And so that's our mausoleum story map was renamed to mom soon story maps that comes from the edit that you had sent in and then a few more chapters dropped as well. Uh for bioengineering.
**[13:33:48 --> 13:34:04]** **2-A:**  And so far you've been mainly cloning repositories that we've given you, but I really wanna encourage everyone to search around for repositories that could be valuable to you, especially as you start playing with these tools, 'cause again as Madeline said a million times, what really matters is the context that's getting into that context window.
**[13:34:04 --> 13:34:14]** **2-A:**  Um and until you've kind of made a practice of harvesting loads and loads of PDFs and markdown docs every day, you might not have a ton of context. And so it could be valuable to go poke around the internet and just see what's there.
**[13:34:14 --> 13:34:27]** **2-A:**  there. And so if you just search for, um, you know, GitHub repo on some topic, um I for instance know that there's an M_I_T_ Shakespeare repo that has all of Shakespeare's plays. If I click this,
**[13:34:29 --> 13:34:40]** **2-A:**  uh what I could do is same thing we've shown you, I can click the code button, I can copy this here, and I can say maybe I'll do this with yesterday's. Can we actually
**[13:34:42 --> 13:34:46]** **2-A:**  Add this Shakespeare repo.
**[13:34:49 --> 13:35:09]** **2-A:**  and I'll paste that Shakespeare repo in. Uh and there are loads and loads and loads of things that are relevant for all your disciplines. We poked around this morning. Um here is a Berkeley course on computational social sciences. Um this is something where if you were teaching a course on social sciences using AI and you know computational methods, this could be an interesting place to to start.
**[13:35:09 --> 13:35:16]** **2-A:**  Um there are lots of instances where people who are publishing papers um that maybe show up uh on archive
**[13:35:16 --> 13:35:43]** **2-A:**  On archive.org actually will give you access to the repository of their data and their methods and their scripts in case you want to test on their results and try to recreate them yourself or try to deploy whatever tool they've generated. Um so this skill of being able to clone GitHub repos is is is really valuable um and uh even if you've never done it before I think that you'll be able to find some samples out there that could be that could be useful to you. And so what I would encourage everyone to do is uh why why don't you give everyone a second
**[13:35:43 --> 13:35:47]** **2-A:**  On the side to do this right right now, 'cause I kind of want us to have two projects for the next moment.
**[13:35:47 --> 13:35:54]** **2-A:**  Um what if we uh just give you sixty seconds to ninety seconds, can everyone just in Chrome, Goo Google, GitHub,
**[13:35:54 --> 13:36:00]** **2-A:**  repo and then something you care about, something that you research, a class that you're teaching, let's just see if there's something there.
**[13:36:01 --> 13:36:01]** **2-B:**  Recipes.
**[13:36:02 --> 13:36:08]** **2-A:**  Um yeah, recipes, let's just give it a shot, and I'd love to hear from people what they find. Did any people with hit the jackpot for their department?
**[13:36:09 --> 13:36:18]** **2-A:**  Maybe some people, sure, we'll give you use this to make sure that you know if you're not listening to me. Everyone just give this a shot. Let's type in GitHub repo on you know something.
**[13:36:19 --> 13:36:22]** **2-A:**  Computational social science, human-computer, government.
**[13:36:23 --> 13:36:23]** **2-A:**  Yes.
**[13:36:23 --> 13:36:30]** **2-B:**  It seems like we're actually using it to our own risk when we put it into public space, right? So we're really not really teaching it to the space much.
**[13:36:31 --> 13:36:32]** **2-B:**  So we might not be able to do those.
**[13:36:32 --> 13:36:39]** **2-A:**  Eventually yeah you will. For the most part, all these are in the text files. Um and you're gonna be able to, you know, delete them if you want to delete them.
**[13:36:39 --> 13:36:47]** **2-A:**  typically the video takes up space. But typically all the things we're doing in the online is I'm not gonna involve like video files too
**[13:36:46 --> 13:36:51]** **2-A:**  too many images, too many PDFs, and those are the things that really suck up space on your computer.
**[13:36:52 --> 13:36:54]** **2-A:**  Text files are real, be it real, be be small.
**[13:36:54 --> 13:37:15]** **2-A:**  And so that you possibly don't want to use much of it if you don't need to. Well, but then you probably have some ways of dealing with this then. I mean just as an external hard drives on the cloud. Oh my God. Uh yeah. So then I think that may be there's some D_V_ for things we want to talk about with you basically. But when you're dealing with any s data that's so large scale you can't even hold it.
**[13:37:15 --> 13:37:23]** **2-A:**  is locally, because within your itty if you can get over the network. And so what server you do is create a some kind of like server connection to it. Uh
**[13:37:23 --> 13:37:23]** **2-C:**  Oh.
**[13:37:23 --> 13:37:24]** **2-A:**  there's a high-huh. lot of them.
**[13:37:24 --> 13:37:25]** **2-B:**  So you can just like search your
**[13:37:25 --> 13:37:26]** **2-A:**  Sure.
**[13:37:26 --> 13:37:27]** **2-B:**  every thing you have on the log on
**[13:37:27 --> 13:37:28]** **2-A:**  That's gonna be in a paper blog,
**[13:37:28 --> 13:37:29]** **2-B:**  and then
**[13:37:29 --> 13:37:29]** **2-A:**  it's
**[13:37:29 --> 13:37:30]** **2-B:**  type in something related
**[13:37:30 --> 13:37:35]** **2-A:**  exactly the same as the size of your computer look on this specific extern data base. You send the server and you have the
**[13:37:35 --> 13:37:36]** **2-C:**  One of these
**[13:37:36 --> 13:37:39]** **2-A:**  possibility of building your software in other high-high sizes that we we can create.
**[13:37:39 --> 13:37:39]** **2-C:**  Okay.
**[13:37:39 --> 13:37:41]** **2-A:**  So it's right out.
**[13:37:41 --> 13:37:41]** **2-C:**  Perfect.
**[13:37:41 --> 13:37:41]** **2-D:**  Oh.
**[13:37:41 --> 13:37:41]** **2-C:**  Oh.
**[13:37:41 --> 13:37:42]** **2-D:** 
**[13:37:42 --> 13:37:43]** **2-A:**  So it's a f so you're a natural
**[13:37:43 --> 13:37:43]** **2-D:**  Kind of.
**[13:37:43 --> 13:37:44]** **2-A:**  or a bird there's a chance that you
**[13:37:44 --> 13:37:45]** **2-A:**  This blue one's
**[13:37:45 --> 13:37:46]** **2-E:**  on the wall, not turned on yet.
**[13:37:46 --> 13:37:47]** **2-B:**  So this one's just a simple
**[13:37:47 --> 13:37:48]** **2-F:**  It's off, so hot.
**[13:37:48 --> 13:37:49]** **2-E:**  Simple as you can.
**[13:37:49 --> 13:37:49]** **2-F:**  Put it on.
**[13:37:49 --> 13:37:49]** **2-E:**  You can have another
**[13:37:49 --> 13:37:49]** **2-B:**  Just to
**[13:37:49 --> 13:37:51]** **2-E:**  professor, listen you can hear professors chatting.
**[13:37:51 --> 13:37:53]** **2-F:**  I don't know. I'm just thinking that I
**[13:37:53 --> 13:37:53]** **2-B:**  I don't either.
**[13:37:53 --> 13:37:54]** **2-F:**  I can use some time to work on the project.
**[13:37:56 --> 13:37:56]** **2-F:**  I don't know for
**[13:37:56 --> 13:37:57]** **2-E:**  No, that's
**[13:37:57 --> 13:37:59]** **2-F:**  I don't know if we could pretty much I think this is just art discussion,
**[13:37:59 --> 13:37:59]** **2-A:**  Alright.
**[13:37:59 --> 13:37:59]** **2-F:**  I believe.
**[13:37:59 --> 13:38:00]** **2-B:**  You take a pair of your keys
**[13:38:00 --> 13:38:00]** **2-A:**  Okay.
**[13:38:00 --> 13:38:01]** **2-B:**  and you
**[13:38:01 --> 13:38:02]** **2-A:**  I believe that's just art discussion.
**[13:38:02 --> 13:38:02]** **2-F:**  Yeah.
**[13:38:02 --> 13:38:03]** **2-B:**  It'll be clear to this Japanese
**[13:38:03 --> 13:38:03]** **2-F:**  Yeah, that's
**[13:38:03 --> 13:38:03]** **2-B:**  right now.
**[13:38:03 --> 13:38:04]** **2-F:**  what I got for Satsang.
**[13:38:04 --> 13:38:05]** **2-B:**  No, it's very
**[13:38:05 --> 13:38:05]** **2-F:**  So how was that?
**[13:38:05 --> 13:38:05]** **2-B:**  clear.
**[13:38:05 --> 13:38:06]** **2-F:**  I will keep doubting.
**[13:38:06 --> 13:38:07]** **2-B:**  You I I started like loving
**[13:38:07 --> 13:38:07]** **2-G:**  You're
**[13:38:07 --> 13:38:07]** **2-F:**  Or sample.
**[13:38:07 --> 13:38:07]** **2-G:**  like yeah.
**[13:38:07 --> 13:38:12]** **2-B:**  it now. I get how we're supposed to Yeah, work up come by the resource that's the way.
**[13:38:12 --> 13:38:12]** **2-B:**  It's really clear.
**[13:38:12 --> 13:38:13]** **2-G:**  So
**[13:38:13 --> 13:38:14]** **2-B:**  So yeah, let's keep the
**[13:38:14 --> 13:38:14]** **2-A:**  it wasn't
**[13:38:14 --> 13:38:14]** **2-B:**  same
**[13:38:14 --> 13:38:14]** **2-A:**  a terrifying
**[13:38:14 --> 13:38:14]** **2-B:**  concept
**[13:38:14 --> 13:38:15]** **2-A:**  step.
**[13:38:15 --> 13:38:15]** **2-B:**  of that.
**[13:38:15 --> 13:38:16]** **2-A:**  Not for you.
**[13:38:16 --> 13:38:19]** **2-B:**  So, if the green one's not white enough yet, feel free to look at the orange.
**[13:38:19 --> 13:38:21]** **2-B:**  But if the blue one's not white enough, then it's fine.
**[13:38:24 --> 13:38:32]** **2-A:**  On how you launch it out, you're gonna have people that are in a tunnel, who are tons of new hair, it's exactly my problem. If I could be half like over six hundred hairs, I'd be in exactly the same problem.
**[13:38:32 --> 13:38:32]** **2-B:**  Yeah,
**[13:38:32 --> 13:38:32]** **2-A:**  But I have six hundred hairs.
**[13:38:32 --> 13:38:35]** **2-B:**  I see what you mean. Can I ask a question, Miss
**[13:38:35 --> 13:38:36]** **2-A:**  So
**[13:38:36 --> 13:38:36]** **2-B:**  Marlin?
**[13:38:36 --> 13:38:36]** **2-A:**  let's go to the PowerPoint.
**[13:38:36 --> 13:38:45]** **2-B:**  So, I I have to I I understand I understand why some people think this might be a process. I get that. And I also heard that this GitHub
**[13:38:45 --> 13:38:45]** **2-A:**  You
**[13:38:45 --> 13:38:47]** **2-B:**  thing, you can choose for it to be public or private.
**[13:38:48 --> 13:38:49]** **2-B:**  So I'm going to assume for a second
**[13:38:49 --> 13:38:58]** **2-B:**  second that if when I google and I did I googled I said github pancakes github you pancakes see what happens that all the people who have something around pancakes opted to
**[13:38:58 --> 13:38:59]** **2-A:**  Yeah.
**[13:38:59 --> 13:38:59]** **2-B:**  make it public
**[13:38:59 --> 13:38:59]** **2-A:**  Yeah.
**[13:38:59 --> 13:39:02]** **2-B:**  or is the default you know public
**[13:39:02 --> 13:39:03]** **2-A:**  No,
**[13:39:03 --> 13:39:03]** **2-B:** 
**[13:39:03 --> 13:39:11]** **2-A:**  it just depends on the organization. You can have like a organization level default. So for us, our default is private for things we make here, and we make them public when we want to share them with somebody.
**[13:39:11 --> 13:39:15]** **2-B:**  so if I searched for whatever yours is it would not be public
**[13:39:15 --> 13:39:15]** **2-B:**  But sometimes it's
**[13:39:15 --> 13:39:15]** **2-E:**  Right, right,
**[13:39:15 --> 13:39:16]** **2-B:**  nice, like it's up
**[13:39:16 --> 13:39:16]** **2-E:**  exactly.
**[13:39:16 --> 13:39:28]** **2-B:**  in the corner. And so here's another question. So you know, we've always been, you know, saying be careful of what files and things you work with online because they might have some malware of a bad bug that gets in your machine. So
**[13:39:28 --> 13:39:28]** **2-A:**  Yep. Yep.
**[13:39:28 --> 13:39:28]** **2-B:**  I
**[13:39:28 --> 13:39:28]** **2-A:** 
**[13:39:28 --> 13:39:29]** **2-A:**  Yep.
**[13:39:29 --> 13:39:33]** **2-B:**  Is there any assurance that if you use any of these things
**[13:39:33 --> 13:39:33]** **2-A:**  Is that
**[13:39:33 --> 13:39:33]** **2-B:**  that there
**[13:39:33 --> 13:39:33]** **2-A:**  a lower,
**[13:39:33 --> 13:39:33]** **2-B:**  is um
**[13:39:33 --> 13:39:34]** **2-A:**  this is the really big question.
**[13:39:34 --> 13:39:35]** **2-B:**  some positive?
**[13:39:35 --> 13:39:37]** **2-A:**  So yes, this is a, this is an So interesting thing to
**[13:39:37 --> 13:39:37]** **2-B:**  the
**[13:39:37 --> 13:39:37]** **2-A:**  think
**[13:39:37 --> 13:39:37]** **2-B:**  answer
**[13:39:37 --> 13:39:38]** **2-A:**  about.
**[13:39:38 --> 13:39:39]** **2-B:**  is no, you can't be certain.
**[13:39:39 --> 13:39:40]** **2-B:**  So if I Well, open up
**[13:39:40 --> 13:39:40]** **2-A:**  so a thing
**[13:39:40 --> 13:39:40]** **2-B:**  something
**[13:39:40 --> 13:39:41]** **2-A:**  to know is
**[13:39:41 --> 13:39:41]** **2-B:**  with
**[13:39:41 --> 13:39:41]** **2-A:**  that GitHub,
**[13:39:41 --> 13:39:41]** **2-B:**  these programs,
**[13:39:41 --> 13:39:42]** **2-A:**  GitHub,
**[13:39:42 --> 13:39:42]** **2-B:**  I
**[13:39:42 --> 13:39:42]** **2-A:**  GitHub tries
**[13:39:42 --> 13:39:43]** **2-B:**  could to spoil
**[13:39:43 --> 13:39:43]** **2-A:**  scrape them.
**[13:39:43 --> 13:39:44]** **2-B:**  and surprise
**[13:39:44 --> 13:39:45]** **2-A:**  It has lots of bots doing this.
**[13:39:45 --> 13:39:45]** **2-B:**  you, right?
**[13:39:45 --> 13:39:49]** **2-A:**  So what I would do is I would never install something that has like
**[13:39:49 --> 13:39:53]** **2-A:**  zero or one stars that like no one has ever ever used before.
**[13:39:53 --> 13:39:53]** **2-B:**  You didn't put
**[13:39:53 --> 13:39:57]** **2-A:**  It's something that has been frequently used. I mean actually I'm going to say this to everyone just basically because it's an important point.
**[13:39:57 --> 13:39:58]** **2-B:**  sounds like I think So, everybody's
**[13:39:58 --> 13:39:58]** **2-A:**  so everyone
**[13:39:58 --> 13:39:59]** **2-B:**  gonna do this.
**[13:39:59 --> 13:40:13]** **2-A:**  is good, a good question happened about these GitHub repos and about security because um, GitHub is a you know, a good citizen of of the internet. I know it's owned by Microsoft now, but you can still believe that they don't, they they they they don't want to get sued by harming people.
**[13:40:14 --> 13:40:15]** **2-A:**  But but it is true
**[13:40:15 --> 13:40:39]** **2-A:**  It's true that like everything you use on the internet could involve some kind of malware or something like that. So you do need to be careful about things. And so with the GitHub Zone, they're going to do the best to scan things. One thing you want to be careful with, like one technique to use whenever you're installing packages or anything from the internet is to not to install things that are brand new, that no one has ever used before, that have no indication that anyone has ever downloaded that thing or used it properly. So on GitHub,
**[13:40:39 --> 13:40:43]** **2-A:**  one thing you'll notice is that there are stars
**[13:40:43 --> 13:40:44]** **2-E:**  We skipped it.
**[13:40:44 --> 13:40:44]** **2-A:** 
**[13:40:44 --> 13:40:58]** **2-A:**  uh and forks and people watching it. And so the M_I_ and and then there's also the organisation uh and so w like with a lot of resources, if something is made by a major research and institution, we are one of those, so we would like to think we can trust things that are
**[13:40:58 --> 13:41:26]** **2-A:**  built by MIT or built by Harvard or built by Berkeley. Um and another thing that is the number of stars and downloads that um in in uh repos or in P_M_ or Python packages have. And that gives you an indication of who's using these things and if the whole world is using this thing it doesn't prove that it's gonna be safe, um but there's a better chance that people will discover if it's not safe. Uh and so this gets quite beyond what we do today, but are there people that are gonna be coding things
**[13:41:26 --> 13:41:54]** **2-A:**  things that involve some of these Python or node packages. One technique to use is to have your settings so you never install anything until it's been released for seven days, because that's usually enough time for someone on the internet to have discovered this. And some of the modern package managers, again, this may be more for coders, but if people use Python they're familiar with PIP and there's also now something called uv. If people use javascripts they're familiar with npm or something called pnpm. The newer package managers actually have that in as the default.
**[13:41:54 --> 13:42:09]** **2-A:**  default um their default's usually twenty four hours, but that's uh then one of the the safest things you can do is just not install anything that has has been like like updated uh in the past twenty four hours or seven days or before anyone's had a chance to discover whether it's safe or not. Um
**[13:42:09 --> 13:42:09]** **2-E:**  Mm-hmm.
**[13:42:09 --> 13:42:20]** **2-A:**  so as we're looking around GitHub, before we clone the thing, we should assess uh how safe we we think it is. But um something that has a number of stars, a number of forks, a number of watches,
**[13:42:20 --> 13:42:24]** **2-A:**  which has been around for a while, and GitHub itself with its hoard of bots is not as popular.

## Chunk 3

**[13:42:25 --> 13:42:42]** **3-B:**  discovered any problems, um then we can assume that that thing is l likely to be safe. If you're concerned, grab Madeline and I and we'll come around and we can poke at it with you. I will say that as someone that authors a lot of get the packages, I constantly get um notifications from them, hey are you sure this thing is right, should this really be there?
**[13:42:43 --> 13:42:51]** **3-B:**  If I make a mistake and I commit an A_P_I_ key or a password um within four hours they found that thing and they're like, hey, are you sure you want this in there?
**[13:42:52 --> 13:42:56]** **3-B:**  Uh so they are stripping these things uh non-constantly in search of in search of learning things.
**[13:42:57 --> 13:42:57]** **3-C:**  So you like to go on.
**[13:42:57 --> 13:43:03]** **3-B:**  So so who has um who has discovered something that was actually relevant? Did anyone discover ref yes, what did you discovered?
**[13:43:03 --> 13:43:06]** **3-C:**  I discovered something that actually scrapes um
**[13:43:06 --> 13:43:16]** **3-C:**  um linguistic phenomena to show the differences in the uses of different um uh English translations and linguistic phenomena in in North American French.
**[13:43:16 --> 13:43:18]** **3-B:**  That was cool. Which is like the exact thing we were gonna work
**[13:43:18 --> 13:43:18]** **3-C:**  Exactly.
**[13:43:18 --> 13:43:19]** **3-B:**  on.
**[13:43:19 --> 13:43:19]** **3-C:**  Yeah.
**[13:43:19 --> 13:43:21]** **3-B:**  Kind of. That was good.
**[13:43:21 --> 13:43:23]** **3-B:**  Anyway, anyone else discover anything uh interesting?
**[13:43:25 --> 13:43:25]** **3-B:**  Yeah.
**[13:43:26 --> 13:43:33]** **3-B:**  I think I I think I have a a limitizer for the dialect that I'm interested in.
**[13:43:33 --> 13:43:35]** **3-D:**  That's cool. That's cool.
**[13:43:35 --> 13:43:39]** **3-B:**  Yeah, I mean, I I guess I didn't want to see how it works, but you
**[13:43:39 --> 13:43:39]** **3-D:**  Yeah,
**[13:43:39 --> 13:43:39]** **3-B:**  know, I I
**[13:43:39 --> 13:43:39]** **3-D:**  that's didn't really think cool.
**[13:43:39 --> 13:43:40]** **3-B:**  of what I'm for, so.
**[13:43:41 --> 13:43:59]** **3-B:**  Yeah, that's yeah absolutely. And I guess there's this pattern that you've been doing with Madeline where I've been giving you somewhat complex repos, but a lot of these are really complex. Um just getting in there asking Clyde to look around and see what's there, um ask questions about security house, how safe do you think this thing is? Um I think that's a great way to starting to explore things.
**[13:43:59 --> 13:44:07]** **3-B:**  Um and especially if there are any tools that you use in your work, right? Um and so for us as teachers, canvas is one of these things.
**[13:44:07 --> 13:44:36]** **3-B:**  things. Um there are some tools that you it sometimes provides to you for teaching and learning like scalar for doing um websites and blogs, uh time-line J_S_ for doing timelines and story map. All of these things exist out there as repositories that you can insect. And that's one of the most exciting things about this moment is up until, you know, twenty twenty three, there were so many black boxes that academics and educators were given from you know people in the ed tech industry, that we could not peer into it all.
**[13:44:36 --> 13:44:36]** **3-B:**  to it all.
**[13:44:37 --> 13:45:03]** **3-B:**  Uh and now with these tools, it's relatively easy to quickly peer into these tools and and and fork them or change them if you want to or just understand how they're constructed. We've been talking a lot with social scientists over the past um three weeks or so about just how how much work in the social sciences ends up happening uh in ways that that I mean I'm maybe I'm overstating it to say contorted, but I'm influenced at least by the tools that they need to use for data collection um and and data analysis.
**[13:45:03 --> 13:45:07]** **3-B:**  And there is something exciting about academics having more actual,
**[13:45:07 --> 13:45:07]** **3-A:**  you know,
**[13:45:07 --> 13:45:16]** **3-B:**  agency in constructing tools for themselves. Alright, so let's um if you feel comfortable, uh to clone clone one of these repos down, go for it.
**[13:45:16 --> 13:45:16]** **3-C:**  Can I
**[13:45:16 --> 13:45:16]** **3-B:**  Um
**[13:45:16 --> 13:45:16]** **3-C:**  ask you
**[13:45:16 --> 13:45:16]** **3-B:**  and
**[13:45:16 --> 13:45:16]** **3-C:**  a question?
**[13:45:16 --> 13:45:17]** **3-B:**  then yeah oh yeah.
**[13:45:17 --> 13:45:28]** **3-C:**  So I'm thinking like let's make pretend that I wanted to do some kind of assignment with students in my class where they needed to build some sort of toolkit and make it publicly accessible and some doesn't
**[13:45:28 --> 13:45:28]** **3-B:**  Yeah.
**[13:45:28 --> 13:45:29]** **3-C:**  matter what platform.
**[13:45:29 --> 13:45:32]** **3-C:**  So in this kind of hypothetical situation,
**[13:45:32 --> 13:45:47]** **3-C:**  often with the students it's the technical stuff that comes along with like building a website. And like I don't teach that, I'm not interested in them learning technical skills, like this is beyond the scope. But they can have fun with this if that pressure is relieved, I think. Sometimes some of them.
**[13:45:47 --> 13:45:47]** **3-B:**  Yeah.
**[13:45:47 --> 13:45:56]** **3-C:**  So is there i in this in this thing, this GitHub thing, I'm assuming first of all that the size of these files that live on there
**[13:45:56 --> 13:46:14]** **3-C:**  where I don't have to think about where they're stored, that there's some sort of licence usage thing going on here. So is it possible that as opposed to telling my students Google the thing you're interested in because that's not what they should do, like they should not be like tell me the things to pay attention to. They need to develop those skills through the classes that you're taking here.
**[13:46:14 --> 13:46:14]** **3-B:**  Yeah.
**[13:46:14 --> 13:46:23]** **3-C:**  But if we wanna give them some help to like translate what you have learned into a public product using tools,
**[13:46:22 --> 13:46:26]** **3-C:**  tools that can be fun to play with but are not the focus of the course,
**[13:46:26 --> 13:46:26]** **3-B:**  Yeah.
**[13:46:26 --> 13:46:27]** **3-C:**  could they then
**[13:46:27 --> 13:46:27]** **3-B:**  They could use it.
**[13:46:27 --> 13:46:33]** **3-C:**  these tools and then have it live in this public space where they have done their research and
**[13:46:33 --> 13:46:34]** **3-B:**  Yeah.
**[13:46:34 --> 13:46:48]** **3-C:**  this class has been set up so we know that they are doing the research and they are demonstrating what they understand but how that translates into a product can happen in these platforms without the constraints of like go to drop in, what are the workshop hours
**[13:46:48 --> 13:46:48]** **3-B:**  Mm.
**[13:46:48 --> 13:46:52]** **3-C:**  learn the how to use this tool? Like is this more or less correct?
**[13:46:52 --> 13:47:08]** **3-B:**  Yeah, I mean that is the the vision. I think Ji Ji and I, Professor Kim here too, is in a similar sort of boat where um you have this data suits you're working with. It's kind of like a database of uh geographical locations or moments in time that there are observations on artworks and things like that.
**[13:47:08 --> 13:47:16]** **3-B:**  And up until now, it's been clunky for them to get that into some kind of website. Uh and what's amazing about these tools that they get they make it really really easy
**[13:47:16 --> 13:47:43]** **3-B:**  be easy for students to do something like that without knowing anything about coding whatsoever. And so I think a lot of folks are excited about this. The fact that students without having to have too many technical skills could create something more complex than an essay, um but also easier to make than some of the video assignments that we support here in the class or virtual gallery assignments that involve knowing about 3D modelling or something like that. Like there is something pretty powerful about how these tools will allow everyone, students and researchers
**[13:47:43 --> 13:47:49]** **3-B:**  to communicate their ideas across a wide variety of media without any technical skill wh whatsoever,
**[13:47:49 --> 13:47:50]** **3-B:**  and that's very exciting.
**[13:47:50 --> 13:47:54]** **3-C:**  So it's the technical piece as opposed to the content knowledge having to get
**[13:47:54 --> 13:47:55]** **3-B:**  But, um but
**[13:47:55 --> 13:47:56]** **3-C:**  But in my case, or is it I'll stop.
**[13:47:56 --> 13:47:58]** **3-B:**  but but no, no, it's I'm telling serious thoughts.
**[13:47:58 --> 13:47:59]** **3-C:**  Oh,
**[13:47:59 --> 13:47:59]** **3-B:**  You see, it's probably just
**[13:47:59 --> 13:48:00]** **3-C:**  tell me to go.
**[13:48:00 --> 13:48:09]** **3-B:**  but what I was saying it's like here's the challenge too, 'cause because as soon as they're in there saying hey help me with the CSS so my timeline for Flavia looks good,
**[13:48:09 --> 13:48:09]** **3-B:**  Good.
**[13:48:10 --> 13:48:26]** **3-B:**  Uh clearly the same tool could also give them all the paragraphs that go in there too, right? And so there's a there's a question about how to ensure academic integrity that goes beyond the tool, because all these tools can totally be misused and just because um we want them to use the tool and make it the technical part, doesn't mean that
**[13:48:26 --> 13:48:42]** **3-B:**  That's a guarantee that it's gonna stay that way unless there are other things we do to kind of fight back against the misuse of the tools. And that's kind of beyond the scope of this workshop, but just so you all know, Box Center thinks about this constantly as how to help AI group assignments and look, you know, spoiler alert,
**[13:48:42 --> 13:48:44]** **3-B:**  it's usually gonna involve somebody in person touched them,
**[13:48:44 --> 13:48:55]** **3-B:**  where they're not just off on their own vibing something with Claude and turning it in without you ever having any evidence that they did it themselves. But there should be some in class oral pitch, there should be some kind of in class
**[13:48:55 --> 13:49:11]** **3-B:**  class on paper annotation and an in class oral defence of the project where they turn it in is something that actually proves they did the hard part and they didn't do what I think we're hinting they could do which is not just ask for the HTML code, but also ask for all the paragraphs of analysis which is not what we would want obviously.
**[13:49:12 --> 13:49:17]** **3-C:**  So yes and and the and would be you know I I'd and this is like a typical question. Faculty come in and they're like
**[13:49:17 --> 13:49:17]** **3-B:**  Yeah.
**[13:49:17 --> 13:49:19]** **3-C:**  I would like them to build this kind of thing.
**[13:49:19 --> 13:49:21]** **3-C:**  Web sites are a often an after
**[13:49:21 --> 13:49:21]** **3-B:**  Yeah.
**[13:49:21 --> 13:49:43]** **3-C:**  And then we talk about how and to what extent that's doable possible in your course, what are the things at least I know need to happen for your students to be able to do that assignment. This kind of creates a bottleneck because then you like you know you got all these people or they need all these RAs to manage websites and create them and that's like a whole other cost thing. So I'm thinking of this at kind of that level like
**[13:49:43 --> 13:49:43]** **3-B:**  Yeah.
**[13:49:43 --> 13:49:49]** **3-C:**  is it and I hear the ethical questions and I'm a total skeptic, I'm a good Gen Xer, I'm a New Yorker, I trust no one and nothing.
**[13:49:49 --> 13:49:57]** **3-C:**  and nothing and amen. And so here's the thing, but is there a way that the medium of delivery,
**[13:49:58 --> 13:50:14]** **3-C:**  right, like students' understanding can be packaged and conveyed without them getting stuck on the technical stuff and also faculty not getting stuck on the at limits that exist in terms of being able to provide all that individual course support. It kind of what I'm hearing is there are these other considerations.
**[13:50:15 --> 13:50:26]** **3-C:**  But yes, at least in principle, we could use it this way to like have a fun assignment and they could use these tools to do that, at least eliminating those variables. So
**[13:50:26 --> 13:50:26]** **3-B:**  So
**[13:50:26 --> 13:50:26]** **3-C:**  that's alright
**[13:50:26 --> 13:50:27]** **3-B:**  so
**[13:50:27 --> 13:50:27]** **3-C:**  to oh.
**[13:50:27 --> 13:50:42]** **3-B:**  I mean and that's the big thing we're working on like our our main learning how job and we love this is one of the exciting things we've done teaching faculty cloud code, but in a huge part of our job is working with faculty to design assignments like that and support them and that's kind of what we're trying to figure out. But I think the whole world's figuring out like what is knowledge work.
**[13:50:42 --> 13:50:51]** **3-B:**  work in communication going to look like seven to ten years from now um let's the AI's doing a lot of the writing for us, what are humans still doing in that in that case?
**[13:50:51 --> 13:51:00]** **3-B:**  So some of that is connected to what academic writing courses should look like, it's connected to what final project should look like, it's like a big question that I think overlaps figuring out something.
**[13:51:00 --> 13:51:18]** **3-B:**  We're not going to answer that one right now, but the uh But if anybody is interested in that, like while that's my day job is to help you guys the professors think about that half of the course is. But so let's let's go so now we have a couple projects in here, um uh and what I wanna do is help us think about like just understand something logistic certainly the nitty griddy of the of the interface and how to organise ourselves.
**[13:51:19 --> 13:51:27]** **3-B:**  One thing we should know is that um in here under where it says resense if I click this little settings zone over there,
**[13:51:28 --> 13:51:39]** **3-B:**  and I say group by project, then all of a sudden it will group it by all of my folders that I've opened up in there. That could be very very helpful so I can quickly talk back and forth between
**[13:51:39 --> 13:51:40]** **3-C:**  You should
**[13:51:40 --> 13:51:40]** **3-B:**  them.
**[13:51:40 --> 13:51:40]** **3-C:**  uh that.
**[13:51:40 --> 13:51:47]** **3-B:**  Yep, yep, I'll do it again. I and you can do a couple other things in here. So again, the settings will be up here, I'm gonna go back to the way it was where it was grouped by none.
**[13:51:48 --> 13:52:01]** **3-B:**  And in this zone here, if I could just click that, and I go to group by project, it'll group it automatically by every single project that I've opened on here. And that could be great, that's an automatic way of doing it.
**[13:52:02 --> 13:52:07]** **3-B:**  Um and uh especially if you don't have too many projects, I think that's a great way of organising it.
**[13:52:08 --> 13:52:24]** **3-B:**  And if you're happy here, stay here. Don't follow what I'm about to do. But I'm gonna show another thing for people that wanna k have even more fine grain control. I'm gonna go back to group by none. And with any of these things, if I say uh re under this repository or review, I'm gonna go here and I'm gonna say m

## Chunk 4

**[13:52:25 --> 13:52:52]** **4-A:**  Move to group. And I'm gonna add a new group and I'll call this group um Wednesday uh say uh and save it. Now I've got a group by Wednesday and I could um collapse ungrouped. And this is a very nice clean view for me. Uh and if I created a new project, let's say, um I could add that to a brand new group. I'm gonna uh open a brand new folder, put this in development, and I'm gonna call this my um
**[13:52:52 --> 13:52:58]** **4-A:**  Oops, open a folder in development. I'm gonna create a new folder.
**[13:52:59 --> 13:53:23]** **4-A:**  and I'm gonna call this my um writing zone, we'll call it. This is let's imagine like I'm gonna be working on writing things and Claude. Uh did anyone ever use any of those sort of like uh nerdy writing apps like Scrivener or Ulysses or Bear or Obsidian or any of these things? Um I'm kind of excited to think about like decking out Claude desktop in a way that can do some of those off like those sorts of things. Um so that's what's kind of inspiring this sort of thing. So this is gonna be my writing zone.
**[13:53:24 --> 13:53:25]** **4-A:**  Uh and so I'm in there.
**[13:53:25 --> 13:53:27]** **4-A:**  And I'm now gonna take
**[13:53:28 --> 13:53:34]** **4-A:**  this will be where I work on writing projects.
**[13:53:35 --> 13:53:50]** **4-A:**  Uh and so inside of here I I can actually rename this chat, I'm gonna call this my writing zone initialization. And then same deal, I can take this and I can move it to a group
**[13:53:50 --> 13:53:57]** **4-A:**  new group, and I'm going to call this my writing zone. This isn't the file name, so I'm going to feel comfy putting a space in there.
**[13:53:58 --> 13:54:07]** **4-A:**  So there we go. So everyone give that a try, just sort of organ take a sec to to you know hit that settings button um and maybe create yourself a group or at least organise by a project.
**[13:54:07 --> 13:54:20]** **4-A:**  Um and uh make sure you have at least two projects in there before I uh move forward because I wanna make sure that we can see what happens as we toggle back between them. If anyone has any issues, you slightly fewer helpers today, but I, Madeline and I will come around and help you out.
**[13:54:23 --> 13:54:24]** **4-A:**  Group by
**[13:54:26 --> 13:54:27]** **4-A:**  and then squad on.
**[13:54:34 --> 13:54:34]** **4-A:**  So
**[13:54:35 --> 13:54:35]** **4-A:**  So so
**[13:54:59 --> 13:55:01]** **4-A:**  It is. It is developed. Is that this developed?
**[13:55:01 --> 13:55:02]** **4-B:**  That's such that I don't understand.
**[13:55:04 --> 13:55:05]** **4-B:**  So I did this.
**[13:55:05 --> 13:55:08]** **4-A:**  So is anyone else not seeing group-wide projects?
**[13:55:08 --> 13:55:09]** **4-B:**  I did.
**[13:55:09 --> 13:55:09]** **4-B:**  In Group By
**[13:55:09 --> 13:55:09]** **4-A:**  Uh
**[13:55:09 --> 13:55:09]** **4-B:**  Project,
**[13:55:09 --> 13:55:10]** **4-A:**  custom
**[13:55:10 --> 13:55:10]** **4-B:**  I did it already.
**[13:55:10 --> 13:55:11]** **4-A:**  groups?
**[13:55:11 --> 13:55:11]** **4-B:**  I did it already.
**[13:55:11 --> 13:55:16]** **4-A:**  People are seeing Group By Project, but some folks have had a hard time creating custom groups.
**[13:55:16 --> 13:55:17]** **4-B:**  By Project, okay.
**[13:55:17 --> 13:55:19]** **4-A:**  I'm hopeful this is not a Windows versus
**[13:55:19 --> 13:55:19]** **4-B:**  Let's
**[13:55:19 --> 13:55:19]** **4-A:**  Mac thing.
**[13:55:19 --> 13:55:23]** **4-B:**  see, so here are the two, here's like two ideas with the buyers.
**[13:55:23 --> 13:55:23]** **4-A:**  Buyers,
**[13:55:23 --> 13:55:23]** **4-B:** 
**[13:55:23 --> 13:55:24]** **4-A:**  custom groups, so
**[13:55:24 --> 13:55:26]** **4-B:**  So, what now what am I doing, what am I supposed to be doing?
**[13:55:26 --> 13:55:28]** **4-C:**  I guess you could set the dog on fire.
**[13:55:28 --> 13:55:28]** **4-B:**  Alright,
**[13:55:29 --> 13:55:30]** **4-B:**  we have the alternately other.
**[13:55:30 --> 13:55:32]** **4-A:**  Some might say that to question the theory.
**[13:55:37 --> 13:55:40]** **4-B:**  When should I go to this is the one for today that has the picture copied.
**[13:55:40 --> 13:55:40]** **4-C:**  Yeah.
**[13:55:40 --> 13:55:40]** **4-B:**  Yeah.
**[13:55:40 --> 13:55:41]** **4-C:**  Oh my.
**[13:55:41 --> 13:55:43]** **4-B:**  That's the picture. Copy one.
**[13:55:43 --> 13:55:46]** **4-B:**  Click on it. Okay. You should be the dots.
**[13:55:47 --> 13:55:49]** **4-C:**  Mm-hmm. So really quickly, uh
**[13:55:49 --> 13:55:50]** **4-D:**  I have the same so problem.
**[13:55:50 --> 13:55:54]** **4-C:**  here is where you can automatically group by.
**[13:55:55 --> 13:56:05]** **4-C:**  Now if you're realizing here you don't have the new group option, uh that's more just in case that these groups aren't sufficient. You come into an individual chat.
**[13:56:05 --> 13:56:17]** **4-D:**  And then you hear th hit the three dots, and it's at the chat level that you can move to group and hit new group. So that's how you get to new group. If anyone's saying it you can't find the new group.
**[13:56:17 --> 13:56:17]** **4-A:**  It
**[13:56:17 --> 13:56:17]** **4-D:**  Yeah.
**[13:56:17 --> 13:56:18]** **4-A:**  should be there for everything.
**[13:56:18 --> 13:56:19]** **4-B:**  It should be there.
**[13:56:20 --> 13:56:21]** **4-B:**  So Madeline,
**[13:56:21 --> 13:56:21]** **4-D:**  Yes.
**[13:56:21 --> 13:56:21]** **4-B:**  if you're
**[13:56:24 --> 13:56:27]** **4-B:**  I don't know if that's just against a chapter either.
**[13:56:27 --> 13:56:30]** **4-B:**  Yes, I do get In fact there's a Wednesday, I don't think so.
**[13:56:30 --> 13:56:31]** **4-B:**  You're just.
**[13:56:32 --> 13:56:38]** **4-B:**  I don't even see a There birthday. w there aren't any bells and whistles by then you want something I want. And I can always go back and tell it Yes. be a s session.
**[13:56:38 --> 13:56:39]** **4-D:**  Well, I would say so.
**[13:56:39 --> 13:56:39]** **4-B:**  A group party.
**[13:56:39 --> 13:56:46]** **4-D:**  Continue head to the next session. So a chat with that cat in the session is what I'll be saying. A project can
**[13:56:46 --> 13:56:50]** **4-D:**  Can Convey more than one thing for a project within the app can be a way of sorting
**[13:56:50 --> 13:56:51]** **4-B:**  By project, yes.
**[13:56:51 --> 13:56:54]** **4-D:**  multiple different tasks and sessions or chats together.
**[13:56:54 --> 13:56:55]** **4-B:**  So it's not
**[13:56:55 --> 13:57:01]** **4-D:**  But also, we use the word project, we tend to mean one parent folder, on a specific
**[13:57:01 --> 13:57:01]** **4-B:**  Yes,
**[13:57:01 --> 13:57:01]** **4-D:**  groupings
**[13:57:01 --> 13:57:01]** **4-B:**  yes.
**[13:57:01 --> 13:57:06]** **4-D:**  of tasks within which you're doing things. So Marlin's writing zone.
**[13:57:07 --> 13:57:12]** **4-B:**  So here you're in your chat right now, there's a project option. But if you go to code, is there a project option?
**[13:57:12 --> 13:57:36]** **4-A:**  Yeah, so it this this is left we go one by one. So projects and chat, all on the cloud. It's just a way of organising a bunch of chats into a bundle that Anthropic's doing on its servers essentially. In co-work, confusingly enough, projects is gonna be a folder on your computer that you're working on. Um because co-work again is local rather than being cloud-based. And so the project here means it's a folder that I'm working in.
**[13:57:36 --> 13:58:03]** **4-A:**  And then in code, project has disappeared, but then for every session I need to put it in some kind of folder. And so you're totally right, we are using project interchangeably with folder there, and that's because it is the same thing and and you could also could call that a project or a repository, it's going to be a GitHub a folder that gets pushed up to GitHub. I'm sure we're being slippery with that language because but they are referring to the same thing. There's going to be a project
**[13:58:03 --> 13:58:15]** **4-A:**  which is a folder on your computer, you'll probably push that up to GitHub if you are a person that works on GitHub. And that's kind of the unit of work to think about as you're sketching out the work you're doing against these tools.
**[13:58:16 --> 13:58:17]** **4-A:**  Does that make sense? Does that make sense?
**[13:58:17 --> 13:58:20]** **4-B:**  For a session also for every session you do it creates a new thing.
**[13:58:20 --> 13:58:22]** **4-A:**  A session has to be in a project.
**[13:58:22 --> 13:58:24]** **4-A:**  You have to select a project that it's in.
**[13:58:25 --> 13:58:34]** **4-A:**  And so when I, and so like Matt was saying, think of session as a chat, like a new chat or a new task. It's gonna be a dialogue that I have with Claude.
**[13:58:34 --> 13:58:42]** **4-A:**  Every one of these things is a dialogue with Claude, me going back and forth with Claude, the app talking to each other. Um what happens in code though, is all of those are gonna live
**[13:58:42 --> 13:59:07]** **4-A:**  is in the context of a project folder. Um and again same thing with code code code work, they live in the context of a project folder. Whereas um Claude AI on the online it just lives in the context of Claude Online essentially. I realise it's confusing because there's so many different tools. If we focus on code for today, the key thing to know is every single chat you start for all the sessions has to exist in a folder. Um and those are gonna be called projects, repositories, whatever you wanna call them.
**[13:59:07 --> 13:59:07]** **4-E:**  Yeah.
**[13:59:07 --> 13:59:10]** **4-B:**  So this is something, I mean it's cosmetic in the sense that it's for you
**[13:59:10 --> 13:59:12]** **4-B:**  Let's just help you keep organized. That
**[13:59:12 --> 13:59:12]** **4-A:**  totally
**[13:59:12 --> 13:59:25]** **4-B:**  dragging a group that's together is not that like the context for groups, if that makes sense. If Yeah. you have docs in one folder slash session and docs in another,
**[13:59:25 --> 13:59:28]** **4-B:**  even if I put them together in the same group, like it's like
**[13:59:29 --> 13:59:31]** **4-B:**  And then we have a session that's not going to draw on the desktop.
**[13:59:31 --> 13:59:34]** **4-A:**  This is such an awesome, awesome question.
**[13:59:34 --> 13:59:57]** **4-A:**  It's for a given session or chat within cloud code, I need to determine what um path it's in, what path that is accessed to, and I can add additional paths. So if I start mentioning the other things I can, to we can give permission to see other things on our computer But that goes beyond what we're advised today, because sometimes it's good to know it's focused on this, instead of being too disorienting. Um and I think the reason we're gonna show you it were show this to you is that
**[13:59:57 --> 14:00:17]** **4-A:**  We're about to show how um the context that you're in can have a lot of influence about how to communicate with you about which resources are available about which scripts and tools are available that are specific to that project and that can be very helpful. I was talking to someone this morning, was w we're in both the same boat where you are thinking I need a computer for work and a computer for when I want to keep those projects, etcetera,
**[14:00:17 --> 14:00:23]** **4-A:**  I mean that kind of thing where like it we all work in different contexts. Sometimes we're teaching and research are connected, sometimes they're very not connected.
**[14:00:23 --> 14:00:30]** **4-A:**  But we might want to have different contexts for those different zones of our work lives. And this is gonna kind of help us out with that essentially. You have your hand up too.
**[14:00:32 --> 14:00:37]** **4-A:**  I think we you're partially answering what I'm saying, but what I what I'm going to ask which is
**[14:00:38 --> 14:00:50]** **4-A:**  like why would I or when are the moments when you think to start a new chat within the same like folder slash project? Like what would the is that
**[14:00:50 --> 14:00:59]** **4-A:**  Does that serve a purpose for blog or is that just like for you as someone who's trying to keep your brain around at least some part of this?
**[14:01:00 --> 14:01:17]** **4-A:**  like you need this initialization so then you might start a different chat that serves some other purpose within the project, is that the idea? Like how how do you make the choice versus just having like a writing zone chat where you do everything. Okay, we're not that awesome question. Uh Madeline's got the best question about contact, do you want to do context window limits, because this is your
**[14:01:17 --> 14:01:17]** **4-B:**  Yeah.
**[14:01:17 --> 14:01:22]** **4-A:**  specialization. Um and they they associate this with you, this is like a teaching move.
**[14:01:22 --> 14:01:31]** **4-A:**  Madeleine, in your minds is vegetable is your internal chemo, I think. She's drawn some of these items, so she should explain it, not me. Uh
**[14:01:31 --> 14:01:32]** **4-D:**  Yes, sir.
**[14:01:32 --> 14:01:33]** **4-D:**  Uh
**[14:01:33 --> 14:01:37]** **4-A:**  But but one one reason is is that context window, you're gonna hit the limits of it, and so
**[14:01:37 --> 14:01:37]** **4-D:**  Mm-hmm.
**[14:01:37 --> 14:01:37]** **4-A:** 
**[14:01:38 --> 14:01:38]** **4-F:**  So you're kind of
**[14:01:38 --> 14:01:39]** **4-A:**  you
**[14:01:39 --> 14:01:39]** **4-F:**  treating
**[14:01:39 --> 14:01:39]** **4-A:**  don't draw like that.
**[14:01:39 --> 14:01:39]** **4-F:**  what
**[14:01:39 --> 14:01:39]** **4-D:**  Like one
**[14:01:39 --> 14:01:40]** **4-F:**  can I window fit
**[14:01:40 --> 14:01:40]** **4-D:**  per session.
**[14:01:41 --> 14:01:41]** **4-A:**  What
**[14:01:41 --> 14:01:41]** **4-D:**  Yes.
**[14:01:41 --> 14:01:43]** **4-A:**  kind of fit in this, like, grain session?
**[14:01:43 --> 14:01:44]** **4-D:**  Yes.
**[14:01:44 --> 14:01:46]** **4-A:**  And remember what happens if they keep going past it.
**[14:01:46 --> 14:02:10]** **4-D:**  It gets compacted. So essentially y everything you're saying um and I'll do it really quick. Uh so it can be just for your own organisation. To be clear, there's nothing wrong with that. Because as we discussed previously, uh there are those um kind of and we have all of these research documents, but there's kind of two graphs to keep in mind, uh the context that's right at the beginning and right at the end is the most important. And also there's this context drop.
**[14:02:09 --> 14:02:24]** **4-D:**  just rocks. So even if you don't burn through your entire context window, the context, that's that first kind of half of session, is where the action is. So that's maybe why you even want to start a new context window before it automatically rolls over.
**[14:02:24 --> 14:02:24]** **4-B:**  That's the

## Chunk 5

**[14:02:25 --> 14:02:25]** **5-A:**  Uh
**[14:02:25 --> 14:02:27]** **5-B:**  When you say context window, you mean start a new session?
**[14:02:27 --> 14:02:32]** **5-A:**  So in each new session and we can use so uh the app is
**[14:02:32 --> 14:02:59]** **5-A:**  funny in that it was just recently made. So they're trying to come up with these naming conventions in order to help people uh keep them inside their head. And I I think for some reason they're imagining people to not move between chat work and code. I think they're imagining people will pick the different um interfaces based on their kind of level and comfort and they'll internalise that taxonomy. But all it is like you can think of
**[14:02:59 --> 14:03:10]** **5-A:**  a session, a chat and a task. Each of them is a context window, and each of them in other places if you guys were used to ChatGPT is a thread.
**[14:03:11 --> 14:03:16]** **5-A:**  And as Marlin said, this is just the place where you're having this back and forth interaction.
**[14:03:17 --> 14:03:30]** **5-A:**  in some way with uh the large language model. Sometimes there are background processes to this chat where it's going to fetch context, it's pulling things from web search, it's running a script that get added to the context window.
**[14:03:30 --> 14:03:37]** **5-A:**  So that's why when we imagine context window, we haven't really drawn it like this. It's beneficial to think of it as a single block.
**[14:03:38 --> 14:04:04]** **5-A:**  Previously the models had two hundred K token limit. Almost all of them have gone up. Uh to one mil, so Faible has one mil, uh four point eight and four point seven have one mil. So you guys are starting at this point. You can just kind of imagine basically from this point on it's one mil and we'll only get bigger. Uh but that is why you have these different moments of initialization. Uh and it's not just though part of the size. Because imagine um
**[14:04:04 --> 14:04:08]** **5-A:**  um you know that you fill this up with your context and your conversation.
**[14:04:09 --> 14:04:37]** **5-A:**  it gets compacted down and this is an actual slash command you can run at any time into a tiny little summary. And that summary the form of it is designated by a markdown file. Uh but again, due to these kind of graphs down here, it's not so much oh I've run out of my context window and now I'm relying on a summary that's a problem, uh but just for its own performance you probably wanna get out of there and start a new thread in order to have
**[14:04:36 --> 14:05:01]** **5-A:**  to have the best possible large language performance. And that's also partially when you hear of the really kind of dangerous A_I_ psychosis that occurs, I would say across the board almost every single one of those cases when you look into it, what has happened is someone has stayed in something like a writing zone for six months. They have never left that thread. So
**[14:05:00 --> 14:05:27]** **5-A:**  So if you guys remember at the beginning of every set, there should be that system prompt, but early on in these models that system prompt kept getting summarised and diluted and kind of changed and it kind of metamorphosised into a very kind of strange entity and so a lot of the safety guardrails then were diluted or just the the model starts to behave in very kind of strange ways. So definitely yes, it's good for your own mental model, uh but I would recommend switching
**[14:05:27 --> 14:05:38]** **5-A:**  switching into new sessions, new tasks, new chats pretty frequently instead of staying in one. And that's also why we're moving out of chat into these projects
**[14:05:38 --> 14:06:06]** **5-A:**  Because part of that is like Oh well I don't wanna go into a new session and have to copy and paste all my context. We fully agree. That's why you're building up these files and folders, so you can hit new session and already it's um enmeshed with that context through the folder, and you can even point it to specific elements that get entered into that context immediately. So that's why we're having you guys build up this kind of personal and project level context that you can continue to reuse.
**[14:06:08 --> 14:06:08]** **5-A:**  That's
**[14:06:08 --> 14:06:09]** **5-C:**  It's cool.
**[14:06:09 --> 14:06:09]** **5-A:**  me.
**[14:06:09 --> 14:06:09]** **5-C:** 
**[14:06:09 --> 14:06:29]** **5-D:**  Also the uh um you know I I think that this drawing I had has the context window is just such a cool thing to keep in your head. Um and every one of these sessions is one of those little windows almost. Imagine that like as an icon for what's happening each everyne each one of those things. Um also so one thing you might have noticed if you um have asked questions of the repo
**[14:06:29 --> 14:06:53]** **5-D:**  is that at the end of your um question if you did open it up in in twenty twenty six zero six one zero, you might see a poem. Um did anyone notice this? Did anyone get a limerick at the end? It's like why why is this? Who played this trick on you and how did they they do it? It's connected to everything Madeline saying about how we transport memory across context and things. What what what did you do Madeline?
**[14:06:53 --> 14:06:55]** **5-A:**  It was me. Um, yes. Uh so
**[14:06:57 --> 14:07:11]** **5-A:**  Per this uh building up context, it's one thing to open Claude code in a new folder. Uh but as we've discussed over and over again, uh the context that gets in first
**[14:07:11 --> 14:07:36]** **5-A:**  into a context window is really important. Uh but also i you wanna save yourself this kind of copy and paste. It's one thing if if I have a serious of files, so if I I might uh point out you have all of this excellent uh memory from working with chat GPT for a really long time. Um I also when we were working with A_I_ early on had all these memory docs. And every single time I started a new session, I was trying to point it to these memory docs.
**[14:07:37 --> 14:07:37]** **5-D:**  Mm
**[14:07:37 --> 14:08:06]** **5-A:**  And it's not that much work to hit copy, path, and paste, but when you're working with this all the time, it does start to get a little grating. So Claude, um everyone at Anthropic uses Claude constantly, so a lot of their changes um come out of working with these tools all the time. So what we're about to describe to you is not something you have to do. At this point, if you guys get to just making folders of really good context and you copy and paste those paths in, you're good.
**[14:08:06 --> 14:08:21]** **5-A:**  But if you start really using these frequently, there's a few document types uh that automatically load in that we want to talk to you about. So again, the first um document type that always loads in no matter what
**[14:08:23 --> 14:08:25]** **5-A:**  is that system prompt, that that safety bit.
**[14:08:26 --> 14:08:29]** **5-A:**  Next is the automatic memory that you set.
**[14:08:29 --> 14:08:39]** **5-A:**  And then the way I played a trick, if you wanna call it that, uh today, that gives you this limerick is something called
**[14:08:40 --> 14:08:57]** **5-A:**  a Claude M_D_ very original of anthropic, I know. Um so if you look in your project, you'll see so if everyone goes again to this little files explorer and hits files, you will see at the root level of this project
**[14:08:57 --> 14:09:25]** **5-A:**  There is a Claude dot M_D_ And to demonstrate to you how uh the kind of strong this Claude M_D_ is and how powerful text can be within these systems, it's not a script, I didn't turn anything on that was a button that said you must do this every single time. Genuinely at the very end of this otherwise normal doc I put in something called secret sauce and I said and every single thing with a limerick.
**[14:09:26 --> 14:09:33]** **5-A:**  And don't you dare mess up. And so once you guys downloaded this repository, this is one of the first things read in.
**[14:09:33 --> 14:09:42]** **5-A:**  So even though it's literally one line at the bottom of the document, on top of ten thousand, twenty thousand words, it's already read, and it's being consistent.
**[14:09:44 --> 14:09:56]** **5-A:**  So cloud M_D_s are really great ways uh to import mark-downs that are um and it has to be that mark-down file. So it has to be called cloud
**[14:09:55 --> 14:10:07]** **5-A:**  in caps, and it has to be a dot markdown file. But this is where you put things that are always true for your given folder.
**[14:10:08 --> 14:10:28]** **5-A:**  So there is a way to set a Claude markdown at the global root of your computer, and these are the things that are always always true, so like my name is Madeline Woods and I work at the box centre uh and please don't put emojis in your output, that is always true for me. But when it comes to this kind of project
**[14:10:29 --> 14:10:47]** **5-A:**  Uh a CLAW_D_M_D_ uh for this repository might just be information about how I want things structured. Uh for all of you it might be how I always want H_T_M_L_ files and I always want these H_T_M_L_ files to follow a certain styling convention. Uh but these are things that are always true.
**[14:10:47 --> 14:10:50]** **5-A:**  Uh so Marlon what are you up to right now Marlon? I see you're driving.
**[14:10:50 --> 14:11:07]** **5-D:**  Well I'm gonna get everyone to do one of these things, and I did a simple one where I'm gonna ask you if you're willing to to create a new folder and then create your own Claude.M_D_ and tell it to do something. All I did was say please always speak to me in French in this uh folder in this remote.
**[14:11:07 --> 14:11:08]** **5-B:**  Yo.
**[14:11:08 --> 14:11:14]** **5-D:**  But just to make sure we're capable of doing this, what I'd love us to do is either change Madeline's, get it to stop talking to you like a
**[14:11:14 --> 14:11:34]** **5-D:**  limerick-spouting pirate or create a new folder for yourself. And again, creating something that's like a a writing zone or a course development zone or something that's valuable, and just put something into a client M_D_ file and see if you can get a result, okay. I'm gonna show you one more time how to do both of these things. So over in the repository overview, this is where Madeline did her pirate thing.
**[14:11:34 --> 14:11:36]** **5-D:**  If I click client.M_D_
**[14:11:37 --> 14:11:50]** **5-D:**  And then crucially I click this code icon. We might remember from last time that's how I'm able to edit things over here. I can scroll down here and I can change Madeline's secret sauce from that to um please you know only
**[14:11:53 --> 14:11:55]** **5-D:**  speak in uh rhyming couplets.
**[14:11:58 --> 14:11:59]** **5-D:**  And then I can save that.
**[14:12:00 --> 14:12:15]** **5-D:**  And now it won't necessarily immediately affect this chart I'm in. Because this chart already has Cloud M_D_ at the beginning of the context window. Sometimes it's smart enough to load it now. It just doesn't always guaranteed load it now. But if I hit new session,
**[14:12:16 --> 14:12:24]** **5-D:**  um and it's in the same folder, and I can say describe this repo to me, um then it will see that cloud M_D_

## Chunk 6

**[14:12:25 --> 14:12:27]** **6-A:**  and it will respond in in rhyming couplets.
**[14:12:27 --> 14:12:51]** **6-A:**  There we go. So that was one. Again, where what I did is I went to files, into that cloth M_D_ hit the code button for view source, and then I edited it. The other thing, and again this is what I really wanna encourage everyone to do to create your own folder, we can start um thinking about how we'd use this as a writing tool is I created a new session and I put it in a brand new folder. And I'll just do this again totally from scratch.
**[14:12:52 --> 14:13:02]** **6-A:**  I'm gonna create uh a new folder that's called new writing project and then I'll open Claude in there.
**[14:13:03 --> 14:13:08]** **6-A:**  And then I'm gonna say please create a Claude
**[14:13:10 --> 14:13:38]** **6-A:**  .md file in this folder that and then I'll just put in whatever I want. It can speak to me in the language of my choice, it can know something about my course, I can paste in my professional bibliogra or my professional biography, um but uh once I do that, it's going to have that in every new session I start in that folder. So give everyone just two, three minutes to do this. This is like such a core skill that I sort of sure everyone does it once just to get over the hump. Um because you're probably gonna want to do this for every single project you ever create is have
**[14:13:38 --> 14:13:42]** **6-A:**  have uh it even just a minimal cloud.MD for it to know something about that project.
**[14:15:58 --> 14:16:04]** **6-B:**  or feel like a display or frame, or or theoretical lens, yeah.
**[14:16:04 --> 14:16:05]** **6-C:**  Let me do that.
**[14:16:07 --> 14:16:08]** **6-B:**  Then your students can also do it.
**[14:16:11 --> 14:16:27]** **6-A:**  Right, everyone doing okay getting this thing working? I'll show you kind of like a sample sort of work flow that you could do with something like this. Um in my folder what I've done is I'm creating a brand new project. This project is going to be me writing an imaginary research paper on content
**[14:16:27 --> 14:16:27]** **6-A:**  context engineering.
**[14:16:28 --> 14:16:56]** **6-A:**  I could also be, you know, teaching a course or something like that. And what I'm doing in my Quad M_D_ here is I'm gonna ask it to look at a certain folder. Um this is a folder in my downloads folder for A_I_ research on context engineering. And periodically what it's gonna do when I ask it to is it's going to um take those PDFs that I harvest from the internet and it's gonna convert them to markdown. So we know the, you know, text that the L_L_M_ likes better and it's also gonna create a summary for me.
**[14:16:56 --> 14:17:24]** **6-A:**  And so if what I do is create a new session um in my new writing project and then d what I do is I hop over here and I've downloaded all of these PDFs, I'm gonna put them in my A_I_ context engineering research folder. All of us have like insanely messy downloads folders, I'm sure. If you create a few subfolders in there, then it'll help your life. Everyday I could just be again harvesting hundreds of, you know, articles from the internet, copy pasting a million things. And then what I'll do is um I'm ready for you to harvest
**[14:17:25 --> 14:17:48]** **6-A:**  my downloads. And it will know that uh I've got this plan where I just suck PDFs down from the internet, got a lot of research on um and it's gonna go ask for um permission there and I actually am not always allow it to that path, 'cause you know I made that path especially for it. And off it goes, it's gonna go read those PDF docs and convert them to the Markdown docs.
**[14:17:48 --> 14:18:10]** **6-A:**  Uh and some d workflows like this is like the only example of it. We talk to people up that wanna get behind pay walls, which is a big pain for sure. A lot of us are doing research where we need to sign in through Harbor key first to get to some sort of database. Um finding some way where you can really quickly get from stuff you see on the internet to structure and cleaned up text within a cloud is gonna be like really really really important.
**[14:18:10 --> 14:18:31]** **6-A:**  And so the way I'm doing it here, not only in PDFs like crazy, I'm just gonna save them to a folder and periodically, Claude's just gonna grab that folder and just structure it all for me, convert it and summarise it. I could also just be dumping in things I get from um the internet. What I can do is uh on the internet here I could go to context engineering tips for instance and I'll just click the top of it.
**[14:18:32 --> 14:18:32]** **6-B:**  Oh
**[14:18:32 --> 14:18:56]** **6-A:**  Um and what I'm gonna do is I'm just gonna command a, command c, command a for select all, command c um and then in a brand new chat, if you're wondering why I want two sessions of the same thing, it's for this reason, um please uh write a new doc with this content for my new search project and I'll just paste in that in S_C_H_T_M_L_ and off it goes to kind of convert that into markdown.
**[14:18:57 --> 14:19:11]** **6-A:**  So to get these projects that like the the sample docks that Madeline and our team have been kind of assembling each day, where there's like those those nice folders of of inputs getting outputs, uh you wanna construct a kind of like harvesting um system or something like this.
**[14:19:12 --> 14:19:12]** **6-D:**  Hmm.
**[14:19:12 --> 14:19:24]** **6-A:**  Makes sense? Any questions about that or any other work those people have for things like this? 'Cause there's some folks already have something they use. Um Jung Yoo has been researching Zotero, a little implementations for instance, I don't know if anyone here uses Zotero or similar tools.
**[14:19:24 --> 14:19:25]** **6-A:**  Yeah.
**[14:19:26 --> 14:19:31]** **6-A:**  But finding some way to describe a table by raw data, getting it structured in a project, it's gonna be insanely valuable.
**[14:19:33 --> 14:19:35]** **6-A:**  Cool. Well so um
**[14:19:36 --> 14:19:46]** **6-A:**  We've created projects, we've started sorting them, so that uh our view is is not so disorienting. Um and I'm hopeful like at this stage this is like not a like a horrifically intimidating
**[14:19:46 --> 14:19:46]** **6-E:**  Mm-hmm.
**[14:19:46 --> 14:20:04]** **6-A:**  or forbidding place to work. Um and I'm kind of excited to like if anyone is interested in this and wants to think about how to use uh cloud code desktop as an authoring environment, I'd love to kind of like know about your experiences and help you guys out whatever way I can. Um so that you could just follow some pretty powerful things you could do in here as a sort researcher using this as a writing tool.
**[14:20:04 --> 14:20:21]** **6-A:**  Um we have some additional s uh models and samples today in the repository that I know that Madeline and and Becca wanna show us that we should probably turn to next. But if anyone wants to stick around and continue setting up kind of for for personal writings on some sort of happy to help out. But where do I go to get to the samples for today?
**[14:20:22 --> 14:20:25]** **6-F:**  So go to new session again. Uh
**[14:20:25 --> 14:20:26]** **6-A:**  and And I've
**[14:20:26 --> 14:20:26]** **6-F:**  again
**[14:20:26 --> 14:20:26]** **6-A:**  got
**[14:20:26 --> 14:20:27]** **6-F:**  let's just practise
**[14:20:27 --> 14:20:49]** **6-F:**  just yeah, this kind of recently opened folder. If you guys had opened it previously, it should just be right there, Claude_Code_20260610. Uh and then strangely they still don't have the files opened, but you can say any kind of question, uh and then you can open this side bar to view uh the top summary.
**[14:20:55 --> 14:21:20]** **6-F:**  So today we kept it very very simple, very small. So if we open examples uh we have two main ones at the root. Uh and we're kind of we we've given you a ton of examples. Uh we just don't want them to be overwhelming. Hopefully they're really good kind of context. Uh you can kind of do the math of transference of those into your own fields, but uh we have two to kind of think of. Of course preparation. So the kind of
**[14:21:20 --> 14:21:40]** **6-F:**  Things you might do before a class begins, and then we have a class processor. So the sorts of things you might want to do while the class is actively occurring and you're trying to stay on top of it. So these are going to be our two different examples, and if you guys are in your files, feel free to pop around, check them out.
**[14:21:40 --> 14:21:47]** **6-F:**  I'm going to kind of walk through each of these different folders, have a few different examples then within them.
**[14:21:48 --> 14:22:01]** **6-F:**  But really quickly, I'm just gonna introduce you to one more kind of automatic document uh that gets pulled into your context window. And this is something called a skill.
**[14:22:03 --> 14:22:14]** **6-F:**  Uh so skill skills dot M_D_ Again it's another mark down folder. This is the lingua franca of uh L_O_M_s if you think about it.
**[14:22:15 --> 14:22:19]** **6-F:**  And if Claude M.D.'s are the things that are always true,
**[14:22:21 --> 14:22:24]** **6-F:**  skills are the things that are uh

## Chunk 7

**[14:22:25 --> 14:22:25]** **7-A:**  That's sometimes true.
**[14:22:30 --> 14:22:49]** **7-A:**  And this is because they're more related to behaviors or processes that may have more variation or only you might do sometimes. So what happens is the skills
**[14:22:50 --> 14:23:05]** **7-A:**  Uh there are many different types of skills. We're gonna go through a few examples in a moment uh but the way you guys have been getting all of your handouts, and all the handouts look the same, that formatting, that reformatting, and I'll show you that exact skill in a moment,
**[14:23:05 --> 14:23:05]** **7-A:**  you
**[14:23:05 --> 14:23:23]** **7-A:**  is a skill. It is a markdown file that has the colours, the fonts, the structure that I expect, so that I can draft these handouts really quickly, literally every morning. Uh and then have them ready for you in like a nice looking way. That's a skill.
**[14:23:23 --> 14:23:28]** **7-A:**  Uh, going through literature reviews in a specific way, that's a skill.
**[14:23:28 --> 14:23:51]** **7-A:**  There's so many different like these are just quick examples, you have something in your head. There are so many different examples of skills, but again at the end of the day, all they are are long text descriptions of the way you like things done for a specific process. Occasionally within them you can cite a code. So if there's a code or script
**[14:23:53 --> 14:23:59]** **7-A:**  And it's the way you like a certain script done. So in one of these I have a vision model
**[14:24:00 --> 14:24:04]** **7-A:**  looking at board work and hand-written note cards.
**[14:24:05 --> 14:24:14]** **7-A:**  I've run this code multiple different times. So I have code that I know works and that I prefer. So instead of having an large language model whip up new code every single time,
**[14:24:14 --> 14:24:22]** **7-A:**  in my skill I've given it a a path uh or a um kind of information on what specific script I would like it to run.
**[14:24:23 --> 14:24:49]** **7-A:**  But when I first launched my chat as you guys continue to do this, you might have dozens, maybe hundreds of skills as you kind of become super users. And if like a CLODM D every single skill was loaded in, well even with one million tokens, you'd run out of context pretty quickly. So every skill isn't just text, but it's also a header. And that header has the name,
**[14:24:50 --> 14:25:17]** **7-A:**  And description of the skill and the description is quite long. So when you guys make skills documents and you start a new thread, so if you have skills in a specific project or you port skills into a specific project and you open a new session, one of the things that's loaded in instead is not all of these, but just the n those headers, so just the names and the descriptions which gives the large language model uh more understanding of what's available.
**[14:25:18 --> 14:25:21]** **7-A:**  So now let's kind of just go through these. So again,
**[14:25:21 --> 14:25:44]** **7-A:**  CLAW D_M_D_s, always true. Almost like adding to the system prompt. Skills are just things, processes, activities, uh that you are doing so frequently that if you copy and paste it even two times into a prompt, it would probably save you time to make a skill that you can go back to, you can edit and you can iterate on, as you'd like to drive. I don't know. Okay.
**[14:25:47 --> 14:26:00]** **7-A:**  Uh so uh Becca helped me out uh quite a bit. So oddly, you know, these are organised alphabetically, but let's get into course preparation if that would come kind of uh beforehand.
**[14:26:01 --> 14:26:11]** **7-A:**  So you'll see this file is kind of like a a mini version of a repo. And if at any point you guys wanted to just limit yourself
**[14:26:12 --> 14:26:25]** **7-A:**  to one of these folders. You could at any point hit new session, open folder, and instead of just stopping here, you could click into examples
**[14:26:26 --> 14:26:27]** **7-A:**  and then open
**[14:26:28 --> 14:26:30]** **7-A:**  course preparation.
**[14:26:31 --> 14:26:35]** **7-A:**  And now instead of being in that entire file
**[14:26:37 --> 14:26:45]** **7-A:**  I'm in here in this new column D is at my root, and I have these materials. So if you really wanna split off any of these examples, just feel free to open it in a new session.
**[14:26:46 --> 14:26:51]** **7-A:**  It's files all the way down, it's turtles all the way down. Uh but let's
**[14:26:53 --> 14:26:55]** **7-A:**  pop into I forget where we were.
**[14:26:58 --> 14:27:03]** **7-A:**  Okay. So popping in here, cl uh the the the the course preparation.
**[14:27:05 --> 14:27:21]** **7-A:**  For inputs we have a lot of context that actually Jung Yun put together for an example last week and maybe Jung Yun slash Becca do you want to kind of talk about this uh for this the outputs were the syllabus redesign.
**[14:27:21 --> 14:27:25]** **7-A:**  Uh and then also your CS20 um or CS200 review.
**[14:27:26 --> 14:27:37]** **7-B:**  Uh yeah, so you all ex have been hearing a lot probably over the last couple of years about re-centering academics and then more recently about the uh new grading um
**[14:27:37 --> 14:28:06]** **7-B:**  proposal which is now no longer a proposal, we're all heading towards it. So we thought it might be useful to see whether we could put together something that would help us take a look at our own, uh syllabuses, and see if we could get some advice on how we might implement uh some of what we're all being asked to do. So um John you put together a lot of advice on re-centring academics. Um and then we went in and added some more, including a lot of
**[14:28:06 --> 14:28:27]** **7-B:**  research on uh fair rating, fair differentiated rating, um and put that together into a tool which will take in a syllabus and produce a bunch of uh recommendations based on that syllabus of things that you might consider or think about um as you're preparing to uh in short, you could rate according to the one you rate.
**[14:28:28 --> 14:28:39]** **7-B:**  for um and uh it produces pretty decent reports. These are not reports that I would wanna generate and send out to all of the faculty as is, that they're kind of in quad speak.
**[14:28:39 --> 14:28:56]** **7-B:**  But their advice is actually pretty good and they're they're not too bad. So um in the repository there is a report that's based on my own class. Because I was willing to be the guinea pig for this, so you can see the syllabus and then the report that it generated for me.
**[14:28:56 --> 14:29:22]** **7-B:**  Uh I also took the liberty of uh pulling down the the syllabus from a couple of our workshop participants so um uh enormous thank you to Lindsey and Claire Marie, whose syllabus is I took and ran through this before I even asked them for their permission. Uh but then we did get their permission. Um and uh both of them are really uh uh wonderful teachers and then their reports show that they have
**[14:29:22 --> 14:29:29]** **7-B:**  um almost nothing to do um to get their courses ready for this. Uh I don't know if you put those into their Uh report
**[14:29:29 --> 14:29:29]** **7-A:**  they don't listen
**[14:29:29 --> 14:29:29]** **7-B:**  cart.
**[14:29:29 --> 14:29:31]** **7-A:**  to I haven't done a get ball, so that's
**[14:29:31 --> 14:29:40]** **7-B:**  Um so there may be PDFs there showing those reports, but you might find this fun to play with. Then put your syllabus in and see what it does and think about what kind of um
**[14:29:40 --> 14:29:57]** **7-B:**  um, you know, ways in which you would agree with it or disagree with it, what other contexts you might wanna put in there that you think is actually important to get the kind of advice that you would want to uh reframe your own syllabus still. That's what's in there. Um, and you could use it to generate advice on all kinds of things, not just uh
**[14:30:03 --> 14:30:15]** **7-A:**  So that is once again that's the kind of course preparation. There's also your leaping through recordings of a previous course, which I know you mentioned in the day previously, but that that's also uh
**[14:30:15 --> 14:30:18]** **7-B:**  Yeah, that you wanna just pull that one up for a minute. Um that's
**[14:30:19 --> 14:30:21]** **7-B:**  Yeah, I think that must be class processor.
**[14:30:22 --> 14:30:25]** **7-A:**  Uh class processor, yes, we've got board work.
**[14:30:25 --> 14:30:26]** **7-C:**  And here
**[14:30:26 --> 14:30:26]** **7-B:**  Yes,
**[14:30:26 --> 14:30:27]** **7-C:**  and
**[14:30:27 --> 14:30:27]** **7-B:**  so this,
**[14:30:27 --> 14:30:27]** **7-C:**  transcript.
**[14:30:27 --> 14:30:47]** **7-B:**  I did mention this on the first day, I showed you a a picture of um Anna Rog in front of uh a giant set of blackboards, uh writing on the blackboards and showed you how I was able to produce um a day of notes from which was uh notes from of what he had said interspersed with um a kind of boxes of what he had written on the boards.
**[14:30:48 --> 14:30:52]** **7-B:**  Uh so this is a little copy of the repository for doing that with the scroll
**[14:30:52 --> 14:31:19]** **7-B:**  the scripts for um downloading the class videos from panoptico, doing the transcription, capturing the still frames, um and then turning that into a set of slides and notes. So kind of interesting and you could figure out okay well maybe I'm not recording the videos the same way or maybe I have some separate nicely prepared notes that I already use that I'd rather use then the automated
**[14:31:18 --> 14:31:23]** **7-B:**  made a transcript or whatever it might be that you would wanna do, but it's a good thing to play around with um
**[14:31:24 --> 14:31:34]** **7-B:**  to see how you would do something generating from really any kind of handwriting or board work or images of text and any kind of video of somebody speaking.
**[14:31:35 --> 14:31:50]** **7-B:**  And it's kind of uh it's a pretty good example of um a situation where I've asked Claude to write some scripts to do something um that I wouldn't wanna spend the time writing the scripts or I might not know how to write the scripts to do, but it can do.
**[14:31:50 --> 14:32:05]** **7-B:**  very very easily for me. And then also asked it to do some things um like recognise handwriting that it's doing without using a script. Um it's using its own A_P_I_ and it's gotta use some of its by the intelligence uh to do it.
**[14:32:05 --> 14:32:15]** **7-B:**  So it's sort of figuring out how to do both of those different types of tasks um that uh I need do the right the right one the right way.
**[14:32:16 --> 14:32:19]** **7-A:**  Is it a right thing to hang up? Uh so W
**[14:32:19 --> 14:32:20]** **7-D:**  Wee?

## Chunk 8

**[14:32:54 --> 14:33:00]** **8-A:**  So this is partly why we're keeping it really clean, even under a folder. So for instance uh working with syllabi,
**[14:33:01 --> 14:33:22]** **8-A:**  um this is why you have different um files in your inputs folder. Uh we have then kind of input agnostic operations and prompts. And then outputs that outputs folder is just where the outputs eventually land. So it could be a case where you point Claude and say hey, I have
**[14:33:22 --> 14:33:31]** **8-A:**  You know, twenty different syllabi in this input, please loop through and do the operations or prompts on each and put a new output in each.
**[14:33:31 --> 14:33:40]** **8-A:**  That's what I was doing today, 'cause we have these example syllabi and I'm wanting to loop through quickly. But now let's say you look at this and you just wanna stay in this repo. What do you do?
**[14:33:40 --> 14:33:47]** **8-A:**  Well, you can drag and drop your syllabus or copy it into Claude and say please add it to inputs.
**[14:33:47 --> 14:33:51]** **8-A:**  But then all you have to do is in this file structure,
**[14:33:51 --> 14:33:54]** **8-A:**  so in each of these individual files, see these three little dots?
**[14:33:55 --> 14:33:57]** **8-A:**  If you click on those three little dots,
**[14:33:59 --> 14:34:03]** **8-A:**  you have the ability to copy the path.
**[14:34:03 --> 14:34:05]** **8-A:**  Copy path or relative path.
**[14:34:06 --> 14:34:10]** **8-A:**  And so all you do is you go into the chat window,
**[14:34:10 --> 14:34:16]** **8-A:**  you paste the path to your um specific syllabus,
**[14:34:17 --> 14:34:25]** **8-A:**  and you say can you please just run these operations on just this syllabus.
**[14:34:25 --> 14:34:36]** **8-A:**  and it will create an output for you, and so it won't necessarily look at all the other syllabi. But it can be helpful to keep these. So you could technically pull in, create an entirely new folder,
**[14:34:37 --> 14:34:47]** **8-A:**  and only pull in the operations, et cetera. But I will say these machines can handle such scale. We keep talking about the context window running out, but one million tokens is a lot.
**[14:34:48 --> 14:35:00]** **8-A:**  So feel free actually to have multiple different examples and kind of create these larger folders because as it's going through and it's running these operations on your individual syllabus,
**[14:35:01 --> 14:35:14]** **8-A:**  it might be the case that it can reference what we did previously to create outputs on syllabi and then it has all that context right there in those tabs. So just really feel free in your chat.
**[14:35:14 --> 14:35:22]** **8-A:**  hot, to just point very discreetly to the specific files that you have added um that are related to your topic.
**[14:35:23 --> 14:35:24]** **8-B:**  Cool.
**[14:35:24 --> 14:35:25]** **8-A:**  Yeah no please.
**[14:35:26 --> 14:35:34]** **8-B:**  Oh, well, I think you might get are you going to keep running through this example? I mean, you who knows? I guess like I guess my question is
**[14:35:36 --> 14:35:43]** **8-B:**  Is somewhat clearly started? I've got this folder with these files that are all part of this project.
**[14:35:43 --> 14:35:43]** **8-A:**  Mm-hmm.
**[14:35:43 --> 14:35:50]** **8-B:**  But if I want to run this on my own syllabus, I guess I just don't exactly understand,
**[14:35:50 --> 14:35:52]** **8-B:**  like, step by step how I would go about doing that if that makes sense.
**[14:35:52 --> 14:35:54]** **8-A:**  Yeah, that's totally okay.
**[14:35:54 --> 14:35:55]** **8-A:**  So I would say
**[14:35:55 --> 14:35:56]** **8-B:**  I don't know if that's useful for other projects.
**[14:35:56 --> 14:36:01]** **8-A:**  no it is, it is. Um there I there's two different ways to do it.
**[14:36:01 --> 14:36:08]** **8-A:**  Uh one would be kind of what we were just talking about. So the files there relate to files locally on your computer.
**[14:36:09 --> 14:36:09]** **8-B:**  Mm-hmm.
**[14:36:09 --> 14:36:14]** **8-A:**  So you could open the Claude dash code, you know, twenty point six oh six
**[14:36:15 --> 14:36:28]** **8-A:**  One oh. Uh repo, click through the folders to get to this example and just drop your syllabus in and then you can copy that path and say please run it with these operations to get an output.
**[14:36:28 --> 14:36:30]** **8-B:**  but then what if they don't have to ingest that?
**[14:36:30 --> 14:36:30]** **8-A:**  Right.
**[14:36:30 --> 14:36:30]** **8-C:**  I don't exactly.
**[14:36:30 --> 14:36:32]** **8-B:**  What am I running it? Just run it again.
**[14:36:32 --> 14:36:32]** **8-C:**  Yeah.
**[14:36:32 --> 14:36:33]** **8-B:**  Oh my.
**[14:36:33 --> 14:36:33]** **8-C:** 
**[14:36:33 --> 14:36:34]** **8-B:**  Yeah. I guess I just do it.
**[14:36:34 --> 14:36:34]** **8-C:**  Just do it.
**[14:36:34 --> 14:36:35]** **8-B:**  Yeah.
**[14:36:35 --> 14:36:35]** **8-B:**  It's a lot.
**[14:36:35 --> 14:36:39]** **8-A:**  Yeah. Yeah yeah. So we can do that live. Yeah. Are we do we wanna do
**[14:36:39 --> 14:36:44]** **8-D:**  Yeah, do you guys so you do you wanna come over to this one? Do you know where the hurr syllabus is?
**[14:36:44 --> 14:36:44]** **8-B:**  I'm just testing this.
**[14:36:49 --> 14:36:50]** **8-A:**  syllabus
**[14:36:55 --> 14:37:22]** **8-E:**  Okay folks, so this uh is the my syllabus here that's in the in the repository. It's in this input syllabus folder. So if you wanted to do yours, you'd just drop yours in here. Mine happens to be in a marked down file, but it could be a PDF, it could be a Word document, it would do okay with whatever you dropped it in. So you just you put it right in there. Uh once it is in there uh and then if you look in the uh
**[14:37:27 --> 14:37:31]** **8-F:**  I have a drop in there or like a do I need to do it in the my local file?
**[14:37:31 --> 14:37:39]** **8-E:**  I think you can just drag and drop it right in there. It'll work like your file system. So you could literally just put it into that folder.
**[14:37:40 --> 14:37:46]** **8-E:**  And then you can do what Madeline said and copy that path.
**[14:37:46 --> 14:37:51]** **8-E:**  You can copy the path, you can copy the relative path. Either one is going to work for you.
**[14:37:51 --> 14:37:51]** **8-F:**  I think the difference
**[14:37:53 --> 14:37:55]** **8-E:**  The path is the full path, all
**[14:37:55 --> 14:37:55]** **8-B:**  Yeah.
**[14:37:55 --> 14:38:18]** **8-E:**  ev basically like the absolute address of where that file is. The relative path is relative to the folder that this you've opened uh your application in. But as far as P_S_ code is concerned it's gonna im uh or sorry as as Claude code is concerned it's gonna interpret either one just fine. It's ne not gonna be confused. Um and then uh
**[14:38:20 --> 14:38:35]** **8-E:**  I'm gonna come over here and I don't exactly even know how Madeline has set this up. So I'm gonna have to guess a little bit. But luckily Claude's gonna help me out right. So I now am at at the command and I'm gonna say I'm uh I
**[14:38:38 --> 14:38:45]** **8-E:**  Oops I can't type on this keyboard uh would like to run the
**[14:38:45 --> 14:38:47]** **8-E:**  syllabus design skill
**[14:38:50 --> 14:38:51]** **8-E:**  on this
**[14:38:52 --> 14:38:59]** **8-E:**  syllabus. And oops, I've seem to have lost my copied path.
**[14:39:01 --> 14:39:02]** **8-E:**  Well, or I don't know how to paste
**[14:39:02 --> 14:39:03]** **8-A:**  It's just weird on the front.
**[14:39:03 --> 14:39:05]** **8-E:**  it's okay, I've pasted it.
**[14:39:05 --> 14:39:05]** **8-A:**  Cool.
**[14:39:05 --> 14:39:14]** **8-E:**  Okay so I'd like to run the syllabus design school uh skill on the syllabus. Um and I'll hit enter. And if it's confused
**[14:39:14 --> 14:39:19]** **8-E:**  It's probably gonna tell me that it's confused. Um but let's see what it thinks.
**[14:39:19 --> 14:39:22]** **8-B:**  To what final does the skill correspond to?
**[14:39:23 --> 14:39:32]** **8-E:**  Actually I don't know that right now because Marj Madeline put this together, but we can show you where the the skills actually live um
**[14:39:32 --> 14:39:33]** **8-F:**  Mm-hmm.
**[14:39:33 --> 14:39:33]** **8-E:** 
**[14:39:33 --> 14:39:46]** **8-E:**  So here let's see what it's saying. It's saying let me find that skill and proceed with the structure intact. And now it's uh looking um and it wants to just list my files. Okay fine, list the files.
**[14:39:47 --> 14:39:48]** **8-E:**  Um
**[14:39:52 --> 14:39:55]** **8-E:**  and let's see well it's doing this, whether
**[14:39:55 --> 14:39:55]** **8-B:**  So
**[14:39:55 --> 14:40:00]** **8-E:**  we can find it. So here in this folder there's a d it course preparation, there's a dot claude folder.
**[14:40:01 --> 14:40:26]** **8-E:**  And inside the dot-clod folder, so at the root of your project there will be a dot-clod folder and there's a skills folder in there. And then in the skills folder you'll see the name of each of your skills and in there the skill dot M_D_ and that's for project-based skills. There's also user-based skills. But that's where when you create a skill it will be. And if you open that skill up and look at it, you can actually read exactly what that skill is
**[14:40:27 --> 14:40:28]** **8-E:**  telling it to do.
**[14:40:28 --> 14:40:29]** **8-A:**  You can edit it.
**[14:40:30 --> 14:40:35]** **8-E:**  And edit it. You can argue with it, you can say I would never write this thing this way. And then, you know,
**[14:40:35 --> 14:40:35]** **8-B:**  I mean,
**[14:40:35 --> 14:40:35]** **8-E:**  it's
**[14:40:35 --> 14:40:38]** **8-B:**  so it's like a prompt. I guess that's what I'm not exactly understanding.
**[14:40:38 --> 14:40:39]** **8-E:**  a prompt.
**[14:40:41 --> 14:40:51]** **8-A:**  it's just a prompt. Yeah. That's conditional. It's like a conditional prompt. So instead of having to copy and paste, let's say you're running through lots of syllabi, but you're doing an action you do frequently and have opinions about.
**[14:40:52 --> 14:41:00]** **8-A:**  It's very early on people had prompt libraries where they were keeping prompts that were they were reusing constantly. This is just an automatic form of that.
**[14:41:01 --> 14:41:01]** **8-E:**  Okay.
**[14:41:01 --> 14:41:07]** **8-A:**  It's a way to hold prompts that you use uh autom like in different projects.
**[14:41:07 --> 14:41:29]** **8-A:**  uh and then giving those projects, the one difference is that YAML header so the header of the name and the description instead of saying alright now here's my prompt, I as a human have decided it's time to use this skill, instead the large language model, when you set it up in this way, has the ability to read the name and description automatically. So it knows it
**[14:41:29 --> 14:41:42]** **8-A:**  It basically has a map of your prompt library, of your skills, and then it can make an informed decision and say hey, I found the skill that might be useful for the short prompt you've given me of what you wanna do. Do you wanna use this skill?
**[14:41:42 --> 14:41:49]** **8-A:**  And you can say yes. Uh so then you're just not having to copy and paste or go looking for it necessarily.
**[14:41:50 --> 14:42:08]** **8-E:**  In this case I was pretty specific, I told it use the syllabus design scale because I didn't want it to mess up. But if somebody else came along and just said hey I want some help redesigning my syllabus, it would probably figure out that there was a syllabus design skill and just use it without that person even knowing that there was a syllabus design skill there.
**[14:42:09 --> 14:42:24]** **8-A:**  And uh I believe uh Becca in her design had a naming convention, so it's just tried to make this redesign document again that was in outputs. It's now saying oh it exists, I'm gonna read it and then rewrite it if I have to. So there we go.

## Chunk 9

**[14:42:25 --> 14:42:29]** **9-A:**  Now it's telling us what it found that I need to fix,
**[14:42:32 --> 14:42:33]** **9-A:**  which is helpful.
**[14:42:35 --> 14:42:49]** **9-A:**  Yeah, so uh that is that. So if you guys wanted to go in um there's course preparation, there's the class processor, uh we have outputs and
**[14:42:50 --> 14:43:17]** **9-A:**  As well down here there's more examples. Uh we have some examples from yesterday uh that you may have rememb may have been looking at that you enjoyed. And instead of just having inputs operations and outputs, this time we've also added in uh skills and a CLAW_M_D_ for each. So that's just showing you as you continue with these projects, just having inputs outputs with prompts is plenty. But as you start to use these more and go up in complexity
**[14:43:17 --> 14:43:45]** **9-A:**  complexity. Looking at the repo from yesterday, uh the projects that were in there versus the projects that are in here will show you just the small differences that adding a Cloud M_D_ or a scale can make. Now I know this a lot. We want you guys to kind of play with this. I will end on one little hint of what we're going to do tomorrow and what's kind of exciting about this. So you guys have seen over the past uh kind of few
**[14:43:45 --> 14:43:56]** **9-A:**  days. How we've been using uh transcripts from the previous day in order to make new handouts, uh those handouts are then styled.
**[14:43:57 --> 14:43:57]** **9-A:**  Uh
**[14:43:58 --> 14:44:26]** **9-A:**  Just so you know, this is our like key take-aways prompt related on our skills. This is that handout style skill. So that's just a reformatting skill. Uh this could be weirdly we are doing a lot of technical things, but things like this might be what you actually use the most. If you're going through class and you've prepared all the materials, and then you just wanna set Claude on a task of now reformat this so it all looks seamless and the same, you could do that and let it just loop through.
**[14:44:26 --> 14:44:53]** **9-A:**  And you certainly don't need to go with uh exactly my example. But you guys can look in here just to have an example of that. Uh but you'll also see in operations I have this APIs and uh vision beat. So this is helping me access external tools. So tomorrow what we're gonna talk about are APIs and we're going to talk about M_C_P_s.
**[14:44:53 --> 14:45:16]** **9-A:**  So many of you before and after classes have been kind of coming up and saying hey this is great, uh but what if I want to pull in uh documents from elsewhere? What if I want to push this to a website? Uh what if I want to use some of my other models? So your lab has a chat GBT account um or you're using Gemini?
**[14:45:16 --> 14:45:19]** **9-A:**  Uh that's what we're going to show you tomorrow. So as an example
**[14:45:19 --> 14:45:48]** **9-A:**  all. I pulled in some board description so I had a board transcription of some of the stills from Becca's class. Um but I also took in uh we've mentioned this kind of personal knowledge base before. Uh but this Luman figure who did this Zettel casting method of externalising his knowledge. And they have an A_P_I_ and we're gonna go through what this means tomorrow. But if all of the index cards he ever made.
**[14:45:49 --> 14:46:16]** **9-A:**  And so by using this A_P_I_ they have their keys available. It's just a way for services to kind of talk to one another. I can reach out and say hey I'd like an image of one of those uh index files and it will send me that image. So it wasn't locally on my computer, it's not a repo I downloaded, I'm just writing a script that says hey hello, could I please get a J_ PEG and it's sending me a J_ PEG back. I could have asked for more information, but I'm just asking for that J_ PEG.
**[14:46:16 --> 14:46:43]** **9-A:**  And then I did another thing. Uh much like uh Becca who's used Claude's vision end point to look at student work, that first day when you guys saw her exam was read, that's really beneficial. But if you're really, you're wanting to make sure for sure the transcription is accurate, like we had Monsoon became mausoleum yesterday for instance, a common method is to point multiple models at it.
**[14:46:43 --> 14:46:49]** **9-A:**  So here what I've done is I've introduced an A_P_I_ key through Gemini,
**[14:46:50 --> 14:47:10]** **9-A:**  and for that we'll get into this tomorrow, but you have to set up these kind of little secret keys or secret passwords that tell Gemini and other services that you know uh that you are a person who's paying and that y they know who you are. Um and then you can run this image through both Claude and Gemini.
**[14:47:11 --> 14:47:31]** **9-A:**  have them give you the kind of the ground truth, compare across them. So this is what A_P_I_ keys allow you to do. It allows you to extract information from external sources, push them to external sources, but then also pull in extra tools that you might want to use. And we'll cover that all tomorrow.
**[14:47:31 --> 14:47:39]** **9-A:**  But if you guys wanted to peek through this repository tonight, um this is just a quick example of how to get kind of two of these skills.
**[14:47:40 --> 14:47:43]** **9-A:**  Anything else we're on? I know we're almost out of time.
**[14:47:46 --> 14:47:53]** **9-A:**  Any questions before we wrap up? Mostly, hopefully you guys have just popped through these and kind of used these, but
**[14:47:53 --> 14:47:57]** **9-A:**  If we're letting last minute questions, we'll stick around after, as always, of course.
**[14:47:59 --> 14:47:59]** **9-A:**  Does it feel good?
**[14:48:00 --> 14:48:04]** **9-A:**  All right. Then also yours is in warranty at the top if you want to peek through it.
**[14:48:04 --> 14:48:09]** **9-B:**  You have me on the hook because I saw one ungrouped conversation that was mine.
**[14:48:10 --> 14:48:19]** **9-A:**  So you send us more recipes. Uh this is an example of getting PDFs into latex. Uh so there's a ClodMD, there's a summary, uh there are
**[14:48:20 --> 14:48:22]** **9-A:**  prompts, scripts, uh different styles and
**[14:48:22 --> 14:48:23]** **9-C:**  And
**[14:48:23 --> 14:48:23]** **9-D:**  we're Alright.
**[14:48:23 --> 14:48:38]** **9-C:**  actually this is very similar to this. Maybe just uh we really care about stylish print outs, spellings, about these amazing designs. The worst feel is just hey I want all our handouts to look the same. But then this is for a course where you have existing inputs in the form of um P_D_F_s,
**[14:48:39 --> 14:48:42]** **9-C:**  where you ended up with their their P_D_F uh
**[14:48:44 --> 14:48:47]** **9-C:**  T t t sh I'm gonna open this in Explorer.
**[14:48:49 --> 14:49:11]** **9-C:**  It look like this? And what this does is it translates this PDF into LaTeX, and then it renders that LaTeX according to a course style essentially. So everything looks exactly the same, and I'll kind of show what that looks like in the outputs. But this is maybe a more science-y version of um the skill exactly the same skill that Madeline's uh talking about or showing you.
**[14:49:12 --> 14:49:13]** **9-C:**  So we'll be off over to
**[14:49:14 --> 14:49:15]** **9-A:**  I thought this tripod was fighting you around.
**[14:49:15 --> 14:49:16]** **9-C:**  Explorer.
**[14:49:18 --> 14:49:22]** **9-C:**  and every single one of them gets rendered this way. And what's great is that LaTeX is
**[14:49:22 --> 14:49:24]** **9-C:**  It can read the Latex, or it cannot read the PDF,
**[14:49:24 --> 14:49:24]** **9-B:**  and that Hmm.
**[14:49:24 --> 14:49:41]** **9-C:**  means you can load up loads and loads and loads and loads of the Latex documents and it's all, it's gonna understand every single one of them, it's not gonna hallucinate, uh and so this is probably a useful skill to check out, that example for anyone that is working in piece set based courses or any courses where you use equations and things like that.
**[14:49:41 --> 14:49:48]** **9-A:**  But even not equations, if you're working in language classes and you have tables and you're pulling in multiple different sources and you'd like them to get normed,
**[14:49:48 --> 14:49:50]** **9-A:**  exactly the same process.
**[14:49:51 --> 14:49:53]** **9-E:**  So you went from P-U-F to Latex back to P-U-F?
**[14:49:53 --> 14:49:53]** **9-A:**  Yep.
**[14:49:53 --> 14:49:54]** **9-B:**  For me at once.
**[14:49:54 --> 14:49:55]** **9-B:**  Hmm?
**[14:49:55 --> 14:49:56]** **9-E:**  And you can move between.
**[14:49:56 --> 14:49:56]** **9-B:**  Hmm.
**[14:49:56 --> 14:49:56]** **9-E:** 
**[14:49:56 --> 14:49:58]** **9-B:**  Oh, sorry, I'm wondering if I have my phone.
**[14:49:58 --> 14:49:58]** **9-B:**  Oh.
**[14:50:00 --> 14:50:01]** **9-E:**  Yeah, this is P-U-F.
**[14:50:01 --> 14:50:02]** **9-A:**  And then you just have Latex.
**[14:50:04 --> 14:50:26]** **9-C:**  So if I'm using this working in the the language it knows best, this is the best basically. And really thinking of PDFs as only a a view layer or rendering layer, and not where the thinking happens. The thinking should happen in something that's kind of like animal and native. And so text file, mark down file, latex file, and then Hmm. PDF is really utility for showing people what could be under the pipeline. Does that make sense?
**[14:50:26 --> 14:50:28]** **9-E:**  Yeah, but why did you not just convert it to a mark down then?
**[14:50:29 --> 14:50:29]** **9-E:**  Blight
**[14:50:29 --> 14:50:29]** **9-C:**  Yeah.
**[14:50:29 --> 14:50:30]** **9-E:**  like that.
**[14:50:30 --> 14:50:34]** **9-C:**  Because it because it can be lighted and then that'll be good for equations and things like that.
**[14:50:34 --> 14:50:34]** **9-E:**  Okay.
**[14:50:34 --> 14:50:40]** **9-C:**  So it that depends Markian work down works great too for sure. But it doesn't have exact the same mark-up.
**[14:50:41 --> 14:50:47]** **9-C:**  So it's a lighted type. Um in some courses just there's they run on a lighted match, you specify if you want it to happen basically.
**[14:50:48 --> 14:50:48]** **9-E:**  Yeah.
**[14:50:49 --> 14:50:49]** **9-C:**  Cool.
