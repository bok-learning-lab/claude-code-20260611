## Chunk 1

**[13:24:51 --> 13:25:18]** **1-A:**  Alright everyone, so we're gonna get started in observance of ye olde Harvard time, a thing that is dead but very much alive in my heart. Uh we still might have people coming through, uh but num there will also be a staff members from the learning lab and we'll just introduce ourselves really quickly. So hello everyone, my name is Madeline Woods uh and I'm the assistant director of the learning lab for AI initiatives and I'll be kind of co-presenting very often with this guy.
**[13:25:19 --> 13:25:23]** **1-B:**  Hey all, I'm Marlan Kuzmak. I'm the director of the Learning Lab, that's this place. Thanks for coming.
**[13:25:24 --> 13:25:32]** **1-A:**  And then we are doing like kind of a lightning round of other people that we'll have floating around to kind of help you for the rest of the day. So my first, if I'm going through the room, is we got Jonah.
**[13:25:32 --> 13:25:36]** **1-C:**  I guess I'm Jonah, I teach here and I in the first year writing programme.
**[13:25:38 --> 13:25:42]** **1-C:**  I I'm Ian. Uh I do uh I work for Hewlett-Packard.
**[13:25:52 --> 13:25:57]** **1-A:**  And then there's oh there's me. Time Christine, I'm one of the Assistant Directors of that early.
**[13:25:58 --> 13:26:07]** **1-B:**  And you should really ask any of us questions at any moment, like some things we do will uh we're trying not to go too fast. Oh, oh, it's a one more person came out.
**[13:26:07 --> 13:26:08]** **1-A:**  Hi I'm Jordan.
**[13:26:10 --> 13:26:25]** **1-B:**  And again to really just grab one of us, the whole point we ha the reason we're almost outnumbering you is what we wanna be able to catch you up if anything ever doesn't makes sense or your s your computer glitches. So really really just reach out um or just look visibly confused and we will come round and and help you out.
**[13:26:26 --> 13:26:38]** **1-A:**  Amazing. Uh so you all have kind of three handouts. One more will join you uh kind of at the end. But really quickly, uh the first one, if it were to be considered a series, is this summer of
**[13:26:38 --> 13:26:52]** **1-A:**  of cloth sheets. Uh this is our run of show, if you think of this theatrically. Uh this will just cover what we're doing today, but this is a multi-day series. Uh there's no expectation that you can you w like
**[13:26:52 --> 13:27:05]** **1-A:**  have to come all of the other days, they do stack on top of one another. So if you get through today and you're just wondering what's the content of the days after this and how does it all fit together uh there's a little description down here.
**[13:27:05 --> 13:27:13]** **1-A:**  So that's the first handout to kinda help orient you as we continue. Uh but now we're gonna get into it. So we are going to be
**[13:27:14 --> 13:27:33]** **1-A:**  Uh presenting a little bit uh while you guys do a lot. Uh so we want this to be as applied as possible, and for you guys to be uh practising and kind of doing a lot of the activities and moves as we go. Uh so the next sheet we have is this uh Claude three interfaces.
**[13:27:34 --> 13:28:02]** **1-A:**  So this is a map of all the different interfaces that we're going to cover over the course of this four day series. Uh for the first day we're just going to cover two. Uh we're going to cover the web UI, so just the web interface. So if you go into Chrome or Safari or whatever your web browser is, uh and we'll discuss chat, just to go through uh some really basic learnings about large language models, but it'll help us build really
**[13:28:02 --> 13:28:26]** **1-A:**  really clear intuitions about what comes later when, for instance, we scale up to something like Quadcode. Uh then we're gonna have you guys move into the desktop app that you guys all downloaded. So the app is uh really great, uh it's very new, so there will be some quirks that we're covering. But it was made to give you access to all of the things essentially. So within the app you can access chat.
**[13:28:27 --> 13:28:53]** **1-A:**  You can also access this kind of intermediatory mode called co-work that is something kind of between a chat and code and then of course you can get into the code panel. Uh once we get a few day like tomorrow, for those of you who are used to working in terminal, you have an IDE, maybe you have Visual Studio code, uh we will have you get into that IDE and CLI. But if none of these words make sense to you right now,
**[13:28:53 --> 13:29:08]** **1-A:**  you right now. That's okay. Uh because there is just a panel of cloud code within the app uh that w kind of black boxes a lot of the um kind of tricky things about using the I_D_E_ or C_L_I_ and there's some trade-offs to that, but really you do get
**[13:29:08 --> 13:29:10]** **1-A:**  almost all of the access to all of the tools.
**[13:29:10 --> 13:29:11]** **1-B:**  Ninety
**[13:29:11 --> 13:29:11]** **1-A:**  And they evil
**[13:29:11 --> 13:29:11]** **1-B:**  five
**[13:29:11 --> 13:29:11]** **1-A:**  through
**[13:29:11 --> 13:29:11]** **1-B:**  percent.
**[13:29:11 --> 13:29:11]** **1-A:**  total.
**[13:29:11 --> 13:29:14]** **1-B:**  So you you should not feel like you're missing out if
**[13:29:14 --> 13:29:14]** **1-A:**  You
**[13:29:14 --> 13:29:14]** **1-B:**  you're not
**[13:29:14 --> 13:29:14]** **1-A:**  are not.
**[13:29:14 --> 13:29:15]** **1-B:**  a developer.
**[13:29:15 --> 13:29:34]** **1-A:**  You are not. Nope. So that's kind of the state of play. So again today we're going to be starting in the web interface and then we're going to be moving into the app. We have some considerations here of why you'd want to move into each and we will continue to hit this, but there are security implications.
**[13:29:34 --> 13:29:48]** **1-A:**  So as you give Claude more access, of course there are risks. So we're gonna help you mitigate those risks. Those risks aren't necessarily high, but this is also just kind of an overview of the ways in which uh these things click together.
**[13:29:49 --> 13:30:10]** **1-A:**  So first, as I said, we're gonna start in the web interface. I know you guys downloaded this app, we're gonna get there soon, but if everyone on your computer open Chrome, open Safari, uh whatever kind of web browser you prefer and get into klaud.ai
**[13:30:19 --> 13:30:23]** **1-A:**  So behold the web interface.
**[13:30:25 --> 13:30:25]** **1-A:**  Alright.
**[13:30:27 --> 13:30:40]** **1-A:**  So the first thing we're gonna talk about before we get into our first activity is just tokens. So does anyone know what a token is or does anyone want to share kind of what a token is or or like
**[13:30:40 --> 13:30:43]** **1-A:**  like tokens are in the case of large language models.
**[13:30:43 --> 13:30:44]** **1-D:**  Yes.
**[13:30:44 --> 13:30:54]** **1-A:**  So when we think about in linguistics what morphemes are, it's the smallest bits of language and tokens take language and process it into mathematical bits.
**[13:30:54 --> 13:31:00]** **1-A:**  Well that and I can see Cheng-Yuan in the back uh as a linguistics PhD very happily kind of
**[13:31:01 --> 13:31:23]** **1-A:**  um going around. So we will share this later. This is a a website you guys can visit later. It's called Tick Tokenizer. But it shows you the ways in which language has been tokenized according to certain models. So this is GPT-4.0. Uh but if you type something into this box, you get like hello and you can now see the ways in which language, natural language, has been broken up
**[13:31:24 --> 13:31:37]** **1-A:**  by this model. So this happens during the training phase when language is being first processed by a model and it's kind of learning the patterns within it. But once a model is trained, it continues to view language this way.
**[13:31:38 --> 13:31:39]** **1-A:**  So every time you put in a prompt,
**[13:31:40 --> 13:31:48]** **1-A:**  what the large language model is seeing and processing is not the words in some kind of human way.
**[13:31:48 --> 13:32:12]** **1-A:**  It's viewing it also not necessarily as little chunks of text, but it's seeing it as strings of numbers. And the ways in which it splits up the text is very strange. So for some of you, Marlon is typing unhappily, unhappily, unhappily. If he hovers over parts of this word, you'll see unlike in language, it's split very strangely.
**[13:32:13 --> 13:32:16]** **1-A:**  Unhappily is split into app
**[13:32:16 --> 13:32:44]** **1-A:**  Ili and then unna with the uh H_ kind of being pulled away. So there are many reasons for this. Humans did not decide how this language was split up. Unlike in linguistics there's no kind of natural rules to this. And so hopefully what we pull from this is this is a very inhuman sort of knowledge. It's an inhuman sort of machine. So it's very good at mimicking patterns of what human knowledge is, but just as a constant reminder, we're gonna keep coming back to this motif.
**[13:32:45 --> 13:33:12]** **1-A:**  LLMs at their base are just machines that take in strings of numbers and output new strings of numbers. They do this very well but strings in and strings out is this constant pattern. We're just gonna learn how to improve the strings going in to get better strings out and then also how to stack those processes to make you know kind of more complex outputs or more complex machines.
**[13:33:13 --> 13:33:20]** **1-A:**  So, the decision between like blue, yellow, blue green, like is not actually related to your content of the word.
**[13:33:20 --> 13:33:34]** **1-A:**  It's not related to the content of the word and in fact this is just a view to help you delineate between these chunks. Uh the chunks, if you hover Marlin like over numbers, um so that number is what relates to one ha.
**[13:33:35 --> 13:33:40]** **1-B:**  We can see it a bunch of times. One three seven five hundred. Every time it shows up, there's my one three seven five hundred.
**[13:33:41 --> 13:33:42]** **1-A:**  So that's not a like
**[13:33:45 --> 13:33:47]** **1-A:**  It doesn't mean anything that that is the chunk of it.
**[13:33:47 --> 13:34:11]** **1-A:**  No, no. The chunk um that has been chosen uh and we won't get too far into this. We have lots of articles available in uh the GitHub repository uh that was sent to you and we'll pull that up in a minute and walk through it uh because we want you guys to investigate this. So we won't get too much into the technicalities. But almost certainly when this model was being trained uh it ran into uh the word app.
**[13:34:11 --> 13:34:25]** **1-A:**  before it ran into the word unhappily. So it decided apt is a chunk. This is a really important unit of meaning, of information. Ily, it probably ran into quite quickly, 'cause that's very common in English.
**[13:34:25 --> 13:34:37]** **1-A:**  So when it finally came across the word unhappily, it had this leftover chunk, unhap, and it had to turn that into a new token. Uh, so that's how it kind of goes through and starts to split language.
**[13:34:37 --> 13:34:45]** **1-A:**  So looking at this, it's all numbers, uh you know turtles all the way down, it's numbers all the way down. Uh so you might think it's quite good at math.
**[13:34:46 --> 13:34:49]** **1-A:**  Well we'll we'll put that to the test. So Marlin, do you wanna do this live?

## Chunk 2

**[13:34:51 --> 13:35:09]** **2-A:**  So all of you now on your computer in Claude, uh let's just take uh a string of numbers, uh at least kind of five digits by five digits. And if everyone wants to put that in, feel free to just put in something quickly, see what you get.
**[13:35:20 --> 13:35:25]** **2-A:**  So as you guys go through Marlon, this is one of Marlon's favourite uh exercises.
**[13:35:25 --> 13:35:52]** **2-B:**  I've stated these two exercises like we do this with all the undergrads that do you know AI literacy things with us, 'cause they're just killer ways of building these foundational intuitions about how these things you know think. Some of you might have encountered stuff like this before. If so you know think about this in a sort of meta way. These are great things to do with your students. So the first one about yeah, it's just number after number, predicting the next number, and then this one it's it's wrong, but it like how wrong is it? I asked it to do with Python and so it did a Python script.
**[13:35:52 --> 13:36:09]** **2-B:**  um that actually multiplied them together and it got this number. And so everyone, you know, give this a try on your own with any random numbers. And it it makes sense to do this in uh I'll show you in a second. You can switch to the sonnet. If you get too good an answer, you might switch to a worse model to deliberately get the bad answer.
**[13:36:10 --> 13:36:16]** **2-B:**  But can anyone um note anything they see about the relation between the two answers, the wrong answer and the right answer?
**[13:36:17 --> 13:36:21]** **2-B:**  Anything we notice uh is it like totally wrong? It's not totally wrong,
**[13:36:21 --> 13:36:21]** **2-B:**  right?
**[13:36:22 --> 13:36:25]** **2-B:**  What are the things that gets right? Math people.
**[13:36:25 --> 13:36:27]** **2-C:**  The order's of magnitude.
**[13:36:27 --> 13:36:28]** **2-B:**  The order of magnitude
**[13:36:28 --> 13:36:28]** **2-C:**  The first
**[13:36:28 --> 13:36:28]** **2-B:**  is right.
**[13:36:28 --> 13:36:29]** **2-C:**  three buttons.
**[13:36:29 --> 13:36:33]** **2-B:**  You're the first person ever to notice that the order of magnitude is right first. Like, that doesn't happen. You can't notice.
**[13:36:35 --> 13:36:39]** **2-C:**  But like the first like two or three buttons, like it takes a while to get into.
**[13:36:39 --> 13:36:41]** **2-B:**  Yeah. So the first three are right.
**[13:36:41 --> 13:36:42]** **2-C:**  Yeah.
**[13:36:42 --> 13:36:51]** **2-B:**  And then the last three are right. Okay. And then the total number of digits or the order of magnitude is right. That's kind of interesting. So it's wrong, this is not
**[13:36:51 --> 13:37:20]** **2-B:**  you know, given enough your scientific research. But it's true, the it's like close to to being right. Um and in some cases maybe that's okay. Maybe that this is close enough. If I actually just cut it off and I just said, you know, five point five two times, you know, ten to the ninth or whatever it is, I don't ten to the twelve, uh that that that would be that would be okay. Um but it's not actually true. And it's this this is that says a lot about how these models are uh close to truth, capable of persuading you that they they are true if you're not careful.
**[13:37:20 --> 13:37:22]** **2-B:**  cool. Um but not actually true.
**[13:37:22 --> 13:37:22]** **2-D:**  Actually,
**[13:37:22 --> 13:37:46]** **2-B:**  And it gets back to like what m Matthew was saying about the way they are trained and the way they predict. And so it seemed loads and loads and loads of instances of two times two and of maybe twenty two times twenty three or twenty three times twenty three, um and it seems load loads of instances of something that's six digits multiplied by something that's eight digits. And so it picks up on a lot of those patterns and it gets pretty darn close to the real answer just by
**[13:37:46 --> 13:38:13]** **2-B:**  Predicting patterns, but it's not the real answer essentially. But what it's amazing at is it see millions of intro Python courses online where everyone learns to write a function that multiplies two numbers together. It is never gonna get that thing wrong. And so what it does instead is it it writes that function and then runs that function, it's guaranteed to get the answer right. And so we're really leveraging what it's trained to do well if we say hey write a Python function that does this.
**[13:38:13 --> 13:38:19]** **2-B:**  Rather than just say, hey, can you vibe this? Just what does it seem to you the answer to this large multiplication question should be.
**[13:38:20 --> 13:38:21]** **2-B:**  So
**[13:38:21 --> 13:38:24]** **2-A:**  But this isn't just limited to numbers either.
**[13:38:24 --> 13:38:34]** **2-A:**  So knowing how to ask the right question and then relying on, and we'll continue to break this down, but tool calls, we're prompting it to trigger a tool call or just to use the proper tool.
**[13:38:35 --> 13:38:36]** **2-A:**  So in this case, if you understand large language models,
**[13:38:36 --> 13:38:38]** **2-A:**  you know it can't do these calculations.
**[13:38:39 --> 13:38:44]** **2-A:**  You need to ask it to use Python or, you know, there are many ways to do this.
**[13:38:44 --> 13:38:46]** **2-A:**  But let's do another example.
**[13:38:46 --> 13:38:50]** **2-A:**  in text, uh unless you've got like a live version of
**[13:38:50 --> 13:38:50]** **2-B:**  I
**[13:38:50 --> 13:38:51]** **2-A:**  the don't s Marlin.
**[13:38:51 --> 13:38:52]** **2-B:**  I don't have a Marlin. But uh you Okay. already did.
**[13:38:52 --> 13:39:12]** **2-A:**  so you may have had this experience, or your students may have had this experience, where they say behold I am hoping to do a close reading of this given text. Uh please do this close reading. Uh well in this case it might say I'm sorry, there is no Act one, Scene nine.
**[13:39:12 --> 13:39:12]** **2-A:**  I
**[13:39:12 --> 13:39:14]** **2-A:**  Uh or it might hallucinate and act
**[13:39:14 --> 13:39:14]** **2-B:**  Did
**[13:39:14 --> 13:39:14]** **2-A:**  one
**[13:39:14 --> 13:39:14]** **2-B:**  again.
**[13:39:14 --> 13:39:14]** **2-A:**  scene nine.
**[13:39:14 --> 13:39:15]** **2-B:**  It did again.
**[13:39:15 --> 13:39:16]** **2-A:**  It did it do it again?
**[13:39:16 --> 13:39:16]** **2-B:**  I love
**[13:39:16 --> 13:39:16]** **2-A:**  Alright,
**[13:39:16 --> 13:39:17]** **2-B:**  it when demos
**[13:39:17 --> 13:39:17]** **2-A:**  go for it
**[13:39:17 --> 13:39:17]** **2-B:**  actually
**[13:39:17 --> 13:39:17]** **2-A:**  press.
**[13:39:17 --> 13:39:19]** **2-B:**  work live and they don't embarrass me in this.
**[13:39:19 --> 13:39:19]** **2-A:**  Yeah.
**[13:39:19 --> 13:39:22]** **2-B:**  So it still doesn't think there's an act one scene nine.
**[13:39:22 --> 13:39:36]** **2-A:**  Well that's which is intriguing. Uh so what can you do? Well I know Marlon doesn't have this copy and pasted ready to go. Um so Huh. Can't do this one live. Uh but uh once you paste in and say are you sure?
**[13:39:37 --> 13:39:37]** **2-A:**  Uh
**[13:39:37 --> 13:40:03]** **2-A:**  Uh 'cause here's act one, my friend. Let let's see what we got. And then it goes up, a very uh a Claud classic you might say, um which you'll hear a lot is I apologize. I'm so sorry. You're totally right. Uh and then it will go on and just like with python, once you give access to the right tools, the right grounding, uh you prompt it in a specific way with enough context. Actually we don't we don't have it printed out, but uh Marlin went through this close reading and it
**[13:40:03 --> 13:40:29]** **2-A:**  and it it wasn't uh a bad close reading. Again, Marlin also hails from X-Pause in another life. Uh and so that's kind of uh again, a motif we're gonna keep hitting. If you ask a question quickly without proper context, the L_L_M_'s gonna go poorly. But sometimes we have this analogy of kind of driving a car. Sometimes people get into a car and if you've never learned how to drive a car, you might put it out of neutral and just immediately roll into a bush. And you'll go
**[13:40:29 --> 13:40:50]** **2-A:**  Oh, this is this is an awful car. This is an awful technology. I hate this. Uh but if you learn how to kind of take all the steps and prepare it, you'll be able to drive uh to many places and go pretty far. So we're gonna keep covering that. Um so these are the ways do we wanna do um population pyramids while we're kind of waiting for Becca? Uh another example of this is
**[13:40:52 --> 13:40:57]** **2-A:**  if you're getting to again slightly more complexity, is help me make an interactive data vis.
**[13:40:58 --> 13:40:59]** **2-A:**  using X_ and X_
**[13:41:01 --> 13:41:21]** **2-A:**  And earlier this is uh less hard to um less easy to do live now, but back in the day if you said make me a graph, uh really quickly, it would produce something like this instead. Uh so this is using a diffusion model instead of a large language model. See when you would say hey please create me a visual
**[13:41:22 --> 13:41:29]** **2-A:**  uh create me something, so make me um different population pyramids showing the differences between Japan and Nigeria.
**[13:41:29 --> 13:41:50]** **2-A:**  It would take that prompt and instead it would make an image pixel by pixel. We won't get too much into the diffusion models, but it just slowly renders based on many, many images it's seen that have been tagged in a certain way what the pixels all arranged should look like. Uh but for those of you who work with data with data you know this is not at all anything close to a population pyramid.
**[13:41:49 --> 13:42:17]** **2-A:**  pyramid, let alone something you would wanna use in a statistics class. So if you instead pop open something called Claude artifacts, uh and you guys can try this yourselves, you can try it with something right now if you're in your chat window uh what it looks like is just always start a new chat, and we'll get to why in a moment. But if I start a new chat uh and somewhere there it is
**[13:42:17 --> 13:42:24]** **2-A:**  is usually artifacts. But let me just say um please I put this on Lopez.
**[13:42:26 --> 13:42:30]** **2-A:**  Please make me an interactive artifact.
**[13:42:30 --> 13:42:45]** **2-A:**  And it could be anything. If you guys don't have data with you right now, you might wanna say um displaying jump mechanics. And video games. Or some kind of interactive unit. So this will take a moment um to pop through.
**[13:42:47 --> 13:42:59]** **2-A:**  But while that cooks up, uh we had uh Jungyun did this one actually. If you instead provide the context
**[13:43:00 --> 13:43:28]** **2-A:**  Hey, please make this for me with this CS V_ uh but please make me an artifact. You'll start to see these tools open up. So it will read a front-end design skill that has access to. This is just text that improves its prompt. It will actually use code uh to look at the CS V_ structure, and it will import it in to actually create an interactive. And you can't see this but normally you can scroll through. If you push play it shows the change over time.
**[13:43:28 --> 13:43:49]** **2-A:**  Uh so these artefacts are really wonderful, because you can really quickly and I'm not sure it's probably still cooking and yours will cook away too uh but at some point you'll get a nice little window that you can open up, and it'll give you an example of what this looks like. And this is just like multiplication, uh instead of doing kind of a naive one-shot making an image,
**[13:43:49 --> 13:43:50]** **2-E:**  instead Uh-huh.
**[13:43:50 --> 13:43:54]** **2-A:**  it's using the tools it has access to that do this work best.
**[13:43:54 --> 13:44:15]** **2-A:**  which is to say code. So it's seen a lot of GitHub repos, a lot of stack overflow of people creating data visualizations of population pyramids and that's what it uses on the back end of an importing a CSV. So now you're seeing this like jump mechanic game. For instance, just with that one prompt now I have this interactive.
**[13:44:16 --> 13:44:27]** **2-A:**  which isn't working too great it seems. Uh that's a way that you can kind of start to prompt back and forth. But you'll see there's this view icon.
**[13:44:28 --> 13:44:36]** **2-A:**  And then there's this code um icon and if you at some point flick, yeah, so it looks like you can kind of change the different attributes down low.
**[13:44:36 --> 13:44:41]** **2-B:**  Maybe you have less gravity and then I'll really be able to go. There we go, that's so satisfying.
**[13:44:42 --> 13:44:50]** **2-A:**  Uh but if you want it to then kind of continue with this again, this is what's on the back end in order to create something like this. It's not

## Chunk 3

**[13:44:51 --> 13:44:54]** **3-B:**  not just asking for a visual, instead it's asking for this entire code package.
**[13:44:55 --> 13:44:59]** **3-B:**  So I think we have, well you were wondering jump mechanics.
**[13:44:59 --> 13:44:59]** **3-C:**  So yeah,
**[13:44:59 --> 13:45:00]** **3-B:**  You just put
**[13:45:00 --> 13:45:00]** **3-C:**  we had
**[13:45:00 --> 13:45:00]** **3-B:**  that?
**[13:45:00 --> 13:45:02]** **3-C:**  a lot of things about the way it goes wrong and this
**[13:45:02 --> 13:45:02]** **3-B:**  Yeah.
**[13:45:02 --> 13:45:15]** **3-C:**  week we're gonna help you figure out how to make it go right. Uh but so that there's light at the end of the tunnel and you see where it's headed in very concrete ways for an actual professor that does actual teaching and research um we have Becca, our Executive Director,
**[13:45:15 --> 13:45:20]** **3-C:**  who will come in and show you some of the cool things you've been making. Do you wanna say hi?
**[13:45:20 --> 13:45:24]** **3-D:**  Hi everyone, I'm I'm Becca, I'm the Executive Director of the Beck Center. Um
**[13:45:24 --> 13:45:51]** **3-D:**  Um I have been learning how to use generative AI um from Marlin and Madeline and others on this team for the last bunch of months and uh having an excellent time doing it. And um I just want to show you some of the things that I've come up with and done with it so you can have a sense of what you might do um and probably won't want to do these same things, but just to just to get a few ideas. So
**[13:45:52 --> 13:45:58]** **3-D:**  One of the things that I wanted to do was in preparation for my summer course at the summer school,
**[13:45:58 --> 13:46:05]** **3-D:**  typically I've been teaching that course in two three-hour long Zoom sessions each week, which is brutal.
**[13:46:05 --> 13:46:17]** **3-D:**  And so I thought I would like to transfer a bunch of that into more of an asynchronous online course format and have shorter in-person or in Zoom sessions. So I took all my course materials.
**[13:46:18 --> 13:46:43]** **3-D:**  I downloaded all of the course videos, I exported my uh canvas course site, um I took all of my problem bank all of uh problems and uh put them into a project in Claude and I used that uh together with some prompting to build an asynchronous online course which I built in the the fancy new LXP uh
**[13:46:43 --> 13:47:09]** **3-D:**  platform, which I even got it to automatically build for me. So here's just an a lesson that it managed to build out of these materials. Uh this is a lesson where I'm teaching the the Monty Hall uh probability problem. Um and so it started out by uh cutting a segment out of my lecture, a short segment out of the lecture 'cause I told that I didn't want long videos, where I uh oops, that's not the
**[13:47:09 --> 13:47:13]** **3-D:**  First one. No, that's right, that's right.
**[13:47:14 --> 13:47:37]** **3-D:**  Um the statement of the problem. So it's cut out a short segment of the video there which uh states the problem. Um and then after that after I stated the problem, I asked all of the students, um what do you think is the right thing to do? Should the contestant in this problem keep the door that they originally chose or should they switch? And so uh the
**[13:47:39 --> 13:47:58]** **3-D:**  we created a quiz next. And this was all automatically created, a quiz where then the student is going to choose um whether you know sort, take their own position. Do they switch or do they stay? Then after that uh we put in a vibe-coded interactive um that
**[13:47:59 --> 13:48:05]** **3-D:**  where they get to develop their own intuition for how this works. So um this is something that where
**[13:48:06 --> 13:48:25]** **3-D:**  it's basically a a JavaScript playable interactive where they can learn about a concept. You could do this for any kind of concept you want, um that then I could insert into this course. Um and then finally followed it with another clip out of my lecture where I reveal the solution.
**[13:48:25 --> 13:48:41]** **3-D:**  So this whole learning sequence just pulled out of my existing course materials. Um he did this for the entire course. Um it's pretty cool. Um another thing uh that uh I wanted to show is
**[13:48:46 --> 13:49:10]** **3-D:**  Um in my class this semester I did a lot of uh hand-written assignments, you can imagine there would be reasons for wanting to do a bunch of in-class assessments now that we're all trying to deal with A_I_ and that have uh more things that are happening right in front of our noses. And so I worked actually to um get some help from A_I_ decoding all of the handwriting.
**[13:49:10 --> 13:49:38]** **3-D:**  So uh here for instance is a student response to an in-class assignment um that I've now scanned in and I'm looking at this student's hand-written uh assessment that I would have to grade. So I have on any given day, sixty five of these that I have to deal with and they're not that easy to decipher. Um and so is there a way I could get A_I_'s help grading something like this?
**[13:49:37 --> 13:50:04]** **3-D:**  Um and uh I was able to work with Claude, um this in fact act actually comes from my final exam, but I did this mostly with these low stakes in class assessments. Um I worked with Claude to be able to uh draft a rubric so it works from my problem and solution and the existing rubric that I have and my standards for how r writing the solution to the problems.
**[13:50:04 --> 13:50:21]** **3-D:**  ones. Um and uh we draft uh a rubric, so it's supposed to uh you know ha has rubric items for each of the different point values for this question. Um and uh
**[13:50:24 --> 13:50:26]** **3-D:**  it has some inputs that it works with.
**[13:50:27 --> 13:50:51]** **3-D:**  So it takes in the the prob the problem prompt, the solution, uh the sample student work, other rubric references, and it puts together a specific rubric for the the question. It then takes in these uh student answers, anonymized student answers, and uh uses its vision to turn them into actual text and then
**[13:50:52 --> 13:51:10]** **3-D:**  grades it. And so here's the actual grade that it produced for this student, the comments it produced. Um and it's kind of interesting. It notices uh here that the student starts out with an initial attempt that it that the the student uh crosses out diagonally.
**[13:51:11 --> 13:51:21]** **3-D:**  Um it recognises the student writing this kind of U_U_U_ R_R_R_ up up right right right for moving through this lattice.
**[13:51:21 --> 13:51:47]** **3-D:**  And uh then recognises further on that the student gets to a correct but not final answer, where they've left an answer in this kind of factorial notation rather than a complete numerical answer. But recognises that in my rubric I said that answers that are left in that notation should receive full credit, and it properly gives the student full credit for this problem. Um it doesn't do perfectly on all of this,
**[13:51:48 --> 13:51:55]** **3-D:**  giving commentary on students. So as I go through and review all of these and decide whether this is actually useful to me,
**[13:51:55 --> 13:52:05]** **3-D:**  um it does get it wrong at various points. But I have to say, it doesn't get it wrong gets it wrong at a uh a lesser rate than my uh T_F_s.
**[13:52:06 --> 13:52:10]** **3-D:**  Um so that's one example. And uh one other is uh
**[13:52:11 --> 13:52:15]** **3-D:**  very last one here. So these are all teaching examples. Is um
**[13:52:17 --> 13:52:39]** **3-D:**  Here's a a video um of uh my co-instructor for CS1200, teaching last semester in a classroom on blackboards, was able to take this video, download the video, have Claude extract the frames from the video, and from it create notes for the course. So in the blue
**[13:52:40 --> 13:52:42]** **3-D:**  is its transcription of everything that was on
**[13:52:42 --> 13:52:42]** **3-C:**  the Hmm.
**[13:52:42 --> 13:52:43]** **3-D:**  board.
**[13:52:43 --> 13:52:54]** **3-D:**  Um and uh in between are the notes based on the transcript of what Anurag was saying in that class. So given a day of class it can just automatically produce these notes.
**[13:52:55 --> 13:53:01]** **3-D:**  So just a few examples of kind of cool things. That is that's
**[13:53:01 --> 13:53:02]** **3-A:**  not.
**[13:53:02 --> 13:53:02]** **3-D:**  Oh.
**[13:53:03 --> 13:53:04]** **3-D:**  Thanks.
**[13:53:04 --> 13:53:04]** **3-E:**  It's quite calm.
**[13:53:04 --> 13:53:24]** **3-C:**  So uh that is the sort of where we're headed. The light at the end of the tunnel is that we we can get to the point where Becca is at. Uh it and and so uh Madeleine's about to explain to us kind of why we're gonna be using these more complex versions of Claude. I just wanna sh uh ask for a show of hands, how many of you managed to get that desktop app installed though before we go further?
**[13:53:25 --> 13:53:33]** **3-C:**  And how many people have not managed to get it installed? Anyone? Well amazing, okay. Well I'm not gonna worry about it then. Amazing, amazing. So so if we have that open, then
**[13:53:33 --> 13:53:48]** **3-C:**  open. That's where we're gonna head next. And the whole reason we're gonna use that app and not just the interface online is so that we can do some of those more complex operations that Becca is doing, uh and we avoid some of those problems that Madeleine kind of outlined uh in the first three activities.
**[13:53:48 --> 13:53:48]** **3-B:**  Okay.
**[13:53:48 --> 13:53:49]** **3-C:**  Alright, but sorry, Madeline, who who went?
**[13:53:49 --> 13:53:55]** **3-B:**  No no no, not at all. Uh well something maybe I'll we'll we'll get into the app, but really quickly
**[13:53:56 --> 13:54:09]** **3-B:**  Let's just talk about what happens when you open a large language model interface. So we've discussed uh the model quite a bit, uh and once again we'll keep coming back to this. Uh but strings in, strings of numbers,
**[13:54:09 --> 13:54:24]** **3-B:**  comma separated values, um become strings of numbers out. Uh but when you're having an interaction with the large language model, for those of you who have been using uh one for several years, maybe in an account, could be Chat GPT, it could be Gemini,
**[13:54:25 --> 13:54:45]** **3-B:**  You might notice it seems to have more information about you and your context in the world than just those strings of numbers you put into the prompt. So it seems to behave in a way that shows more context than just saying this string of five numbers by this string of five numbers. And where does that come from?
**[13:54:45 --> 13:54:48]** **3-B:**  Uh this comes from what we call the context window.
**[13:54:50 --> 13:54:50]** **3-B:**  So

## Chunk 4

**[13:54:51 --> 13:54:55]** **4-A:**  Whenever you're interacting uh with a large language model,
**[13:54:56 --> 13:55:03]** **4-A:**  it all happens within this context window. And before you ever even begin a conversation,
**[13:55:03 --> 13:55:07]** **4-A:**  something is loaded into that context window.
**[13:55:08 --> 13:55:12]** **4-A:**  And you may have heard this term, but this is the system prompt.
**[13:55:14 --> 13:55:37]** **4-A:**  So there's things that vary between all of the different companies. Uh the first is the model. So the actual kind of uh you know number kind of pattern creator and seer uh that you're choosing to interact with, and those models continue to improve. But the other thing that impacts the ways models behave is this thing called uh the system prompt.
**[13:55:37 --> 13:56:03]** **4-A:**  And I've just got a short little extract of the system prompt. Uh Marlin might be able to search for it online because Claude, unlike chat T_P_T_ I'm anthropic rather, uh they do publish their system prompts. They want people to kind of see uh the different system prompts they have available. Uh so if you go, if you just look it up, um you can pick the system prompt for different models. Uh is this for four point eight or four
**[13:56:03 --> 13:56:03]** **4-B:**  point 4.8.
**[13:56:03 --> 13:56:04]** **4-A:**  seven? Okay.
**[13:56:04 --> 13:56:28]** **4-A:**  So this is the newest system prompt, and I do recommend uh just popping through in here at some point, uh because it's really fascinating how many decisions are being made for you uh before you ever interact with the model. Uh a lot of this is related to safety and security, so it's uh how is it behaving, um does it assist with uh self-harm, building a bomb, some of the kind of like ethical situations.
**[13:56:29 --> 13:56:32]** **4-A:**  And so when you've heard about people jailbreaking a model,
**[13:56:32 --> 13:56:59]** **4-A:**  model. Uh what they mean is they put in a prompt that somehow circumvents this prompt or kind of tricks the model into ignoring uh this initial most important prompt. And we'll get into the ways in which uh and kind of why this prompt is able to have so much primacy over the conversation. Uh but a lot of it is related to safety, but a lot of it is also related to style of speech. So when you hear people say, oh I prefer
**[13:57:00 --> 13:57:22]** **4-A:**  How Claude interacts with me over chat. Part of that comes down to training data. Uh so Claude is kind of famous for running a book abattoir. It uh took a bunch of books, ripped the spines off and scanned them. Uh we've had a few faculty come in the past few weeks who got checks from Anthropic for this practice in fact. Uh but also it tends to uh yeah,
**[13:57:22 --> 13:57:26]** **4-A:**  so here we go. Um keep a natural tone, responds in promin
**[13:57:26 --> 13:57:28]** **4-C:**  Well, look how many times it has to say no bullet.
**[13:57:28 --> 13:57:29]** **4-C:**  pull-ups. It's like once
**[13:57:29 --> 13:57:29]** **4-A:**  No bolts,
**[13:57:29 --> 13:57:29]** **4-C:**  in each
**[13:57:29 --> 13:57:29]** **4-A:**  no
**[13:57:29 --> 13:57:29]** **4-C:**  of
**[13:57:29 --> 13:57:29]** **4-A:**  bolts.
**[13:57:29 --> 13:57:31]** **4-C:**  these paragraphs, no pull-ups.
**[13:57:31 --> 13:57:39]** **4-A:**  And this was a thing uh really associated with chat GPT early on. So you'll also, when you read through this document, if you've been working with large language models for a while,
**[13:57:39 --> 13:57:50]** **4-A:**  you'll see in this document a direct kind of reactive conversation with both the training data as well as the way it's trying to differentiate itself from some of the other models online.
**[13:57:51 --> 13:57:53]** **4-A:**  Uh so this is the system prompt.
**[13:57:53 --> 13:57:56]** **4-A:**  And every single time you interact
**[13:57:57 --> 13:58:15]** **4-A:**  with a quad, the model, you'll be interacting with a system prompt. Doesn't matter if it's in chat, doesn't matter if it's in a co-work, doesn't matter if you become a really intensive uh kind of developer like user and are using c code and a C_O_I_ this system prompt in is in every single little thing.
**[13:58:16 --> 13:58:21]** **4-A:**  Now the next thing you might have noticed using these tools for a while is something we call memory.
**[13:58:23 --> 13:58:26]** **4-A:**  Or they call memory and memory is an interesting word.
**[13:58:26 --> 13:58:28]** **4-A:**  It might feel like some kind of
**[13:58:30 --> 13:58:56]** **4-A:**  you know psychological quality or you might think oh it has some kind of like really innate interesting technology that allows it to have memory about me and this is how it knows about your context but also across multiple different chats if you notice you pick up a project in a new thread or a new chat and it seems to kind of remember the information about your last thread this comes from memory but memory again it's not psychological and it's not technically difficult
**[13:58:56 --> 13:59:16]** **4-A:**  really difficult. All it is, motif is more text. So just like the system prompt is text, if Marlin goes in, and this might look a little different, ah, 'cause it's not the Harvard account. Uh but if you go down to settings, capabilities, you'll get into generate memory from chat history.
**[13:59:16 --> 13:59:43]** **4-A:**  and you can turn that on. You can also keep it off, and we'll talk about ways to kind of uh still get the same benefits without uh the kind of automated nature of this. But it is really helpful, it's just a way to automatically have more context for the large language model about who you are and what you're doing. Uh so Marlin, I'm not sure if metal has that much uh but yeah, okay, so just based the metal is just one of our various studio accounts.
**[13:59:43 --> 13:59:50]** **4-A:**  So even based on not that much work, uh you can kind of see uh these memories and how they're structured.
**[13:59:53 --> 14:00:09]** **4-A:**  So if you turn it on, slowly it'll see, okay what are the projects that this person is interested in. Um brief history, uh the kind of coding languages you use or the human languages you use, uh the sorts of projects you're interested in.
**[14:00:10 --> 14:00:16]** **4-A:**  And, again this just helps the large language model come up with ultimately a better output.
**[14:00:17 --> 14:00:26]** **4-A:**  It's just trying to stack these first input strings with as much information as possible, or what entropic and others call high signal tokens,
**[14:00:27 --> 14:00:31]** **4-A:**  uh that will help draw the response in the correct direction for your context.
**[14:00:32 --> 14:00:36]** **4-A:**  context used in so many different ways. Uh so system prompt, then memory,
**[14:00:36 --> 14:00:54]** **4-A:**  but the kind of motif you'll see over and over again, and this is that third handout you guys have, is the it's just, it's all text. It's all text. Uh so the applications for this are very strong in STEM,
**[14:00:54 --> 14:00:58]** **4-A:**  but for those of you who are in the humanities or pseudo humanities in this room,
**[14:00:58 --> 14:01:00]** **4-A:**  um and even if you're in STEM uh
**[14:01:01 --> 14:01:13]** **4-A:**  Text is the heart of this technology. It's the beating heart of this technology. So if you are really strong and thoughtful with how you put together large amounts of text
**[14:01:14 --> 14:01:42]** **4-A:**  And you can do that in a thoughtful kind of operational way, you will be able to make truly incredible things with this. So just as Becca was showing you, the ways in which you get to that sort of output is just by really uh intentionally arranging this context. And it all becomes tokens no matter what you put in. So again over here, it doesn't matter if it's a PDF, if it's a CS_V_ um even images when you put them in get a vision description of
**[14:01:41 --> 14:01:48]** **4-A:**  and that's textual for the large language model to interact with. It's turned into tokens and then there's the in and the out.
**[14:01:49 --> 14:01:57]** **4-A:**  So we've got just a description of the different file types that you can interact with. You'll see very much that we
**[14:01:58 --> 14:01:59]** **4-A:**  Work a lot with markdown.
**[14:02:00 --> 14:02:07]** **4-A:**  Markdown is one of the most kind of popular ways to create documents to feed to large language models,
**[14:02:07 --> 14:02:09]** **4-A:**  especially when you get up to CLAWD code.
**[14:02:09 --> 14:02:10]** **4-A:**  But eventually,
**[14:02:11 --> 14:02:12]** **4-A:**  you know, HTML,
**[14:02:12 --> 14:02:15]** **4-A:**  any of these structured languages are really, really helpful.
**[14:02:17 --> 14:02:20]** **4-A:**  So as you start to do your projects,
**[14:02:21 --> 14:02:30]** **4-A:**  Uh this is this is what happens in a context window. So no matter what your system prompt goes in and if you've turned in memory this goes in. Boom.
**[14:02:32 --> 14:02:40]** **4-A:**  Then you have your first prong. So hey, I would like to make this thing.
**[14:02:41 --> 14:02:48]** **4-A:**  What happens then is a large language model response, it gives the output, and maybe it's not quite right.
**[14:02:49 --> 14:02:51]** **4-A:**  So you try to nudge it in a direction.
**[14:02:52 --> 14:02:53]** **4-A:**  And this goes on and on and on.
**[14:02:54 --> 14:03:14]** **4-A:**  And then maybe you say, oh, you need it in this direction. Uh also here's my uh P_D_F_ that might assist you with this. Here's a mark-down file. Uh here's the data that might help you. On and on and on. But you'll see at some point you're gonna hit a wall. You're gonna run out of information.
**[14:03:15 --> 14:03:22]** **4-A:**  So with all the newer models, the size of the context window is one million tokens.
**[14:03:22 --> 14:03:31]** **4-A:**  So one million of those little pieces that we showed you right at the beginning. For older models it's two hundred K_ Uh so again about the length of a of a novel.
**[14:03:32 --> 14:03:42]** **4-A:**  But not all tokens within this context window are made equal. So really quickly, just as you guys continue to build things that are more complex like code bases,
**[14:03:42 --> 14:03:44]** **4-A:**  you're feeding in chapters,
**[14:03:44 --> 14:03:45]** **4-A:**  huge amounts of context,
**[14:03:46 --> 14:03:48]** **4-A:**  not just one Shakespeare act,
**[14:03:48 --> 14:03:49]** **4-A:**  but all of the works of Shakespeare,
**[14:03:49 --> 14:03:51]** **4-A:**  you'll run out of context.
**[14:03:52 --> 14:03:55]** **4-A:**  So what will happen is a new context window will spawn,
**[14:03:55 --> 14:03:57]** **4-A:**  and again,
**[14:03:57 --> 14:03:59]** **4-A:**  system prompt always.
**[14:03:59 --> 14:04:12]** **4-A:**  memory always. And then so it can pass on the conversation, a summary of that last context window is passed through. And this happens with Anthropics through something called Compact.
**[14:04:13 --> 14:04:21]** **4-A:**  This is a again not a special technology though. This compact is created using another document of text.
**[14:04:22 --> 14:04:27]** **4-A:**  Uh you can also look that up online. We can circulate it later, but it it gives a pretty uh
**[14:04:28 --> 14:04:41]** **4-A:**  opinionated version of how to summarise information. So I've actually you can make your own slash commands. We'll get to that later. I have a version called M_W_ compact because I just kind of disagree with some of the generalisations they've made here.
**[14:04:42 --> 14:04:50]** **4-A:**  Uh but again, it's not something technical. It's just another large language model is called in to read your context window and turn it into a summary. Uh

## Chunk 5

**[14:04:51 --> 14:05:05]** **5-A:**  that has then passed. And then you can kind of continue your conversation. Uh so that is fully the context window. And all we're going to be doing genuinely for the next few days is
**[14:05:07 --> 14:05:26]** **5-A:**  Because it's just text-in text-out, coming up with uh better or more sophisticated ways of automatically feeding in this context window. Giving you guys agency over the context window as much as possible, 'cause when you first start prompting with AI, let's say you don't pass in any documents, most context windows end up looking
**[14:05:27 --> 14:05:42]** **5-A:**  AI dominated. Like you've maybe put in this many tokens in a full conversation and the AI because the responses are so long and if you're not pulling it back this is how much they've interjected into the conversation and instead we're trying to flip that ratio.
**[14:05:42 --> 14:05:53]** **5-A:**  We want you to put in as much high level context as possible so the AI puts in is creating like smaller more condensed more specific outputs.
**[14:05:54 --> 14:06:20]** **5-A:**  And last is just think of it like memento. Has anyone seen this movie? Sometimes we do this with students and they're like who's seen memento? And they all go I have no idea what you're talking about. And you go ah I'm dying. Um but uh every context window think of it like memento. You just want to think of how can I write on my arm in as a solid a way as possible to make sure the next version of me does a good job the next day.
**[14:06:20 --> 14:06:32]** **5-A:**  Okay, so just thinking of that. Um and we'll also talk about ways when things start to go wrong. Later you can end it half-way through, you can go back in time, uh but those powers will come as we continue forth.
**[14:06:33 --> 14:06:40]** **5-B:**  Another metaphor that no one has seen Memento, it's almost like an insanely smart student who hasn't done the reading for class that day.
**[14:06:40 --> 14:06:46]** **5-B:**  Um and if you let them fill up the whole context window it'll all sound kind of smart, but it won't be grounded in what you're actually trying to teach them.
**[14:06:46 --> 14:07:00]** **5-B:**  And so you wanna like kind of teach them in the context window what they need to know to then riff on that context and say smart things towards the end of the context window. So that's another, for people that haven't seen Memento, though I love Memento obviously.
**[14:07:00 --> 14:07:02]** **5-A:**  And if you're really into research,
**[14:07:02 --> 14:07:05]** **5-A:**  I know we're not getting too terribly technical,
**[14:07:05 --> 14:07:07]** **5-A:**  but for those of you who are interested,
**[14:07:07 --> 14:07:13]** **5-A:**  these documents are in a GitHub repo we're about to turn to. But again, not all context
**[14:07:14 --> 14:07:39]** **5-A:**  uh is equal either when you're putting it in. So not every single token within that context window is as strong as other tokens uh according to a lot of research. So you might be thinking, ah well my token that's inserted here should be as strong as something inserted here. Alas nay. Um there's a kind of primacy and recency bias.
**[14:07:41 --> 14:07:46]** **5-A:**  Uh and then there's something called context rot. So the first tokens a
**[14:07:46 --> 14:07:46]** **5-C:**  I
**[14:07:46 --> 14:07:53]** **5-A:**  model int like uh kind of sees or interacts with have it follows that the most over everything.
**[14:07:53 --> 14:08:09]** **5-A:**  And that's why anthropic make sure their system prompt is the first thing that model ever sees along with your memory. But then as you continue a conversation the most recent instruction you've given of no do this also has strength. However that stuff in between you're starting to lose it.
**[14:08:10 --> 14:08:29]** **5-A:**  Uh and then over the course of this long kind of band of context, uh as you add more context it's really really beneficial. And we're talking again like in the tens of thousands, even hundreds of thousands of tokens, putting in context is going to improve your output.
**[14:08:30 --> 14:08:37]** **5-A:**  But as you start to go further along uh this uh thing called context rot starts
**[14:08:37 --> 14:09:03]** **5-A:**  starts to set in and the quality of your output will go down all the way to the very kind of tail end of its memory. So sometimes people do that compact step before you ever get close to the end of your conversation because they just want to keep refreshing. So we'll see this often and you'll start to experience it as we do examples but the first bit, the last bit, and then you want to build context absolutely, but know that there is a drop-off point.
**[14:09:04 --> 14:09:26]** **5-A:**  Okay, so we're gonna now get into the app, ladies and gentlemen. You downloaded the thing. Let's pop in there and we have a few different examples which are all contained within a GitHub repository. Uh so how many people use GitHub out of curiosity or know of GitHub?
**[14:09:27 --> 14:09:27]** **5-D:**  Nice.
**[14:09:27 --> 14:09:28]** **5-B:**  Like a few big different things.
**[14:09:29 --> 14:09:29]** **5-A:**  Huh?
**[14:09:29 --> 14:09:30]** **5-B:**  it was two very different questions.
**[14:09:30 --> 14:09:34]** **5-A:**  Well, there's Git. Okay how many people use GitHub? Or in what way?
**[14:09:35 --> 14:09:37]** **5-B:**  You said how many use it and then how many know of it.
**[14:09:37 --> 14:09:39]** **5-A:**  Okay, that's that's true true.
**[14:09:39 --> 14:09:39]** **5-B:**  But I know how
**[14:09:39 --> 14:09:51]** **5-A:**  How many of you No, that's totally fair. You got me there. How many of you have heard of GitHub? Let's start there. Very good. How many of you use GitHub? Okay, nice. Um so
**[14:09:52 --> 14:10:11]** **5-A:**  For those of you who do not, but you've known of it, well now today is your day, you're gonna get in there. It's really not that spooky, uh we're not gonna have you create an account today. Uh it is very simply a way of uh sharing and collaborating on the creation of files.
**[14:10:11 --> 14:10:13]** **5-A:**  Coding is just reading and writing files.
**[14:10:13 --> 14:10:16]** **5-A:**  This is the way we're going to share with you a
**[14:10:16 --> 14:10:16]** **5-B:**  And
**[14:10:16 --> 14:10:16]** **5-A:**  so whole
**[14:10:16 --> 14:10:16]** **5-B:**  they were just
**[14:10:16 --> 14:10:17]** **5-A:**  stack
**[14:10:17 --> 14:10:17]** **5-B:**  downloading
**[14:10:17 --> 14:10:17]** **5-A:**  of files.
**[14:10:17 --> 14:10:18]** **5-B:**  something. We're not even using
**[14:10:18 --> 14:10:28]** **5-A:**  Oh, we're not even going to use terminal? Alright, perfect. So you were emailed a link to this GitHub uh repository, is what it's called.
**[14:10:30 --> 14:10:32]** **5-A:**  And once you open it
**[14:10:38 --> 14:10:49]** **5-A:**  And then you're gonna download, you'll click on this big green code button and there will be a drop down and you're just gonna go to the bottom to download zip.
**[14:10:50 --> 14:10:59]** **5-A:**  So later we'll show you uh the more usual ways of getting a GitHub repo onto your machine. But today we're just gonna download a zip file.
**[14:11:01 --> 14:11:06]** **5-A:**  And we're gonna open that file. So another thing uh for those of you who have not
**[14:11:06 --> 14:11:15]** **5-A:**  done uh development or coding before. Uh the thing about Claude is we're gonna get to these security concerns again. Is
**[14:11:17 --> 14:11:24]** **5-A:**  it's what's powerful and a bit what's dangerous about it. So when you're in a Claude, the web interface,
**[14:11:24 --> 14:11:26]** **5-A:**  You make an artifact, you get a really good output.
**[14:11:26 --> 14:11:51]** **5-A:**  But then it's just in your chats. You're having to go back into your chat, scroll up, look for the thing. It can't really live outside of your chat window. The reason to use the app is that it has access to your local files on your computer. So one, you're copying and pasting less. Uh you're dropping in individual PDFs less. Uh and then it can write to new files directly onto your computer for you to have.
**[14:11:51 --> 14:12:05]** **5-A:**  Uh but some of you might realise, ooh, that could be quite spooky if it has access to my entire computer. So Claude has thought of this. It is really really siloed to whatever files you give it access to.
**[14:12:05 --> 14:12:33]** **5-A:**  So one of the safest things to do, and this is the case broadly with development, uh is to create a separate folder on your computer uh the root or just around um where people can kind of do development um or do coding. So just if on your computer if you want to now, create something called development, called code, called Claude, and then drop that zipped folder into it. You can do that, you don't have
**[14:12:33 --> 14:12:42]** **5-A:**  have to do that today um we'll probably do that tomorrow, but that as well. But that is something if you wanted to have everything organised, you could do. Yes.
**[14:12:43 --> 14:12:54]** **5-E:**  I just noticed um I don't know if it's yesterday or something, it seems like there is a folder called CLAW that acts like a external disk. Is that in a in one itself?
**[14:12:55 --> 14:13:00]** **5-A:**  It makes one itself because of the things that's in the folder. So if you wanted if you download CLAW
**[14:13:00 --> 14:13:09]** **5-A:**  On the desk, uh yes, there are various settings um that are within that folder, but those are not where you would want to
**[14:13:09 --> 14:13:11]** **5-A:**  builds or continue to put GitHub repositories.
**[14:13:11 --> 14:13:13]** **5-E:**  Oh, you want to make them separate things.
**[14:13:13 --> 14:13:20]** **5-A:**  Yes, yeah, that's just holding settings, skills, books and things we'll get into later. Marilyn, is there something you wanted to
**[14:13:20 --> 14:13:30]** **5-B:**  Yeah, just on one tip, the thing that you download is a zip file. Folks are probably familiar with this, but you just have to unpack that zip file by double clicking on it, and then you get the actual folder.
**[14:13:30 --> 14:13:30]** **5-A:**  Yes.
**[14:13:30 --> 14:13:32]** **5-B:**  And then you could copy that somewhere you want.
**[14:13:33 --> 14:13:35]** **5-B:**  I'm on on a PC, uh we also could
**[14:13:35 --> 14:13:36]** **5-B:**  Could control you on a Mac.
**[14:13:37 --> 14:13:37]** **5-A:**  Yeah.
**[14:13:37 --> 14:13:45]** **5-B:**  This is the one thing that will be a little different today is PCs and Macs will handle this file copying different. The key thing is for today just get it somewhere you can find.
**[14:13:46 --> 14:13:57]** **5-B:**  That's the main thing. It's unzip that folder and get it somewhere you can find and then we'll help you open it up in Quad. And we'll get into more of the management of, you know, your development structure tomorrow as well once we're in terminal.
**[14:13:59 --> 14:14:00]** **5-B:**  So should uh
**[14:14:02 --> 14:14:07]** **5-B:**  Everyone download that thing and then maybe I can just give people a quick tour of the interface of this app.
**[14:14:07 --> 14:14:07]** **5-A:**  Yep.
**[14:14:09 --> 14:14:23]** **5-B:**  So give everyone if you're having any issues getting that folder down again please grab one of us we are so insanely happy to help out. Um I'm just gonna give you a quick overview of the interface of the of the desktop app. The chat here
**[14:14:25 --> 14:14:50]** **5-B:**  there's three tabs across the top. If you're not seeing this, there is a little toggle up here that you can hit. If ever you're not seeing this side bar, I can toggle it on and off up there. Um and in the chat I'm kinda just interacting with Claude.AI, the website, just the same thing we were just looking at in our browser. Um this is kind of like a one site web browser when I hit um chat. I'm just looking at Claude.AI and it actually is gonna

## Chunk 6

**[14:14:51 --> 14:14:58]** **6-A:**  I have my entire chat history too. And this is this is all stuff that Anthropic is saving in the cloud for me. And I can go from machine to machine,
**[14:14:58 --> 14:15:02]** **6-A:**  I can go from browser to browser. If I'm logged in as me,
**[14:15:02 --> 14:15:07]** **6-A:**  then I'm gonna see all these chats that are there in the chat tab or in Claude.ai.
**[14:15:09 --> 14:15:32]** **6-A:**  But then the the things we're gonna focus on today and the rest of the week are the next couple of tabs. And one of them is co-work and one of them is code. We're not gonna start on code today because it actually, especially on PCs, requires you to install a couple of extra things. If you wanna get ahead of the game and install that stuff tonight, um you should go ahead and give it a try if you wanna get in a little early tomorrow, and we'd be totally excited to Or help you.
**[14:15:32 --> 14:15:33]** **6-B:**  stay after today.
**[14:15:33 --> 14:15:37]** **6-A:**  Um yet we will get we will get it going. We'll also we'll help everyone um get it running. That's just
**[14:15:37 --> 14:15:49]** **6-A:**  It's just a little preview tomorrow. It's gonna be a little bit quirky for people that on Windows getting that started. Again, this is like five, ten minutes quirky, not like, you know, losing a hold whole day to it. But so today we're gonna stay in in co-work.
**[14:15:51 --> 14:15:57]** **6-A:**  And what's kinda cool about co-work and code is that they can affect the local files on my computer.
**[14:15:58 --> 14:16:05]** **6-A:**  Again, Madeline gave you that security thing. There that there's a danger to that as well, that they can affect my my local files, but that's kind of the game changer here.
**[14:16:05 --> 14:16:16]** **6-A:**  And so bare minimum means I don't have to do a ton of copying and pasting. If I've got that, you know, Shakespeare's Coriolanus or whatever, and I want Claude to see it, I can have that in a file and just say hey Claude go check this thing out,
**[14:16:17 --> 14:16:30]** **6-A:**  I don't have to copy paste myself. It's also gonna be able to write files um uh all on its own. Um so what I'm gonna get us all to do today is to work in co-work in that sample folder we gave you, and I'm gonna walk through right now the steps on how to get there.
**[14:16:30 --> 14:16:34]** **6-A:**  I'm gonna do it once quick, you can take a look at it, and then I'm gonna do it a couple times really slow. So that people
**[14:16:34 --> 14:16:37]** **6-A:**  so that people can follow me. What we're gonna do is in co-work
**[14:16:38 --> 14:17:06]** **6-A:**  I'm going to say work in a project, and I'm going to choose a folder, and then I'm going to navigate to wherever I put this folder, and hit select folder, and then I'm going to say go ahead, you can use the files there. Okay? So now we're all we're all going to do that and I I'm going to do it slowly three times so people can follow me, um it because the we're going to take a a break so we all get to that that stage, okay? So again, um I can either I can go into projects and hit new project,
**[14:17:05 --> 14:17:07]** **6-A:**  Or if I'm under task,
**[14:17:08 --> 14:17:14]** **6-A:**  what I can do is click here and say create new project or choose a different folder.
**[14:17:15 --> 14:17:25]** **6-A:**  If I create project, it's going to say do I want to start from scratch, import a project or use an existing folder. I'm going to say using an existing folder because I downloaded that one.
**[14:17:26 --> 14:17:54]** **6-A:**  I'm gonna select, and then the key thing is I've gotta navigate not to the zip file but to the uncompressed version of it. Okay, so for me I'm going to desktop into my cloud clu project and I'm gonna select that folder and I'm gonna hit select and then go ahead and create the project and say hey no problem, you can start there. Alright? So one more time I'll I'll go I'll do that and maybe um if Madeline wants to i someone had a had a question?
**[14:17:54 --> 14:17:55]** **6-C:**  Yeah.
**[14:17:55 --> 14:17:55]** **6-D:**  Yeah.
**[14:17:55 --> 14:17:55]** **6-C:**  um
**[14:17:56 --> 14:17:57]** **6-E:**  even the subfolders too?
**[14:17:58 --> 14:18:16]** **6-A:**  Totally, totally, totally, exactly. So I mean that's a bit of an awesome thing to be aware of is that whatever folder you select, it's going to be able to look at everything else. And that's why I wouldn't give it access to my desktop or, you know, my root drive or something like that. Because whatever folder you give it, um it's going to be able to access to everything underneath, right?
**[14:18:16 --> 14:18:37]** **6-A:**  So we'll just be a little bit careful about giving it access to desktop or even downloads. It is a killer demo. That's very it's a brave thing to do for sure. And it is magical.
**[14:18:37 --> 14:18:39]** **6-F:**  It's very effective, yeah.
**[14:18:39 --> 14:18:42]** **6-A:**  I just uh we're not we're not gonna do that that one here.
**[14:18:42 --> 14:18:45]** **6-A:**  Uh we've given you a sample folder that we're gonna help you or organize.
**[14:18:45 --> 14:18:45]** **6-F:**  Yeah.
**[14:18:45 --> 14:18:48]** **6-A:**  So again um there are a couple ways we can do it.
**[14:18:48 --> 14:18:49]** **6-F:**  Was there a question though?
**[14:18:49 --> 14:18:49]** **6-G:**  Like Yeah.
**[14:18:49 --> 14:18:49]** **6-F:**  uh
**[14:18:49 --> 14:18:55]** **6-H:**  For manual we need to pick it out of it's just like in the downloads folder thing to do it for manual.
**[14:18:55 --> 14:19:06]** **6-A:**  You could totally do it in the downloads folder, just gotta make sure you uncompress that. Like a .pkg a .pkg you right click, I think it's uh uncompress or unzip and a you can double click it and then you get the actual folder.
**[14:19:07 --> 14:19:07]** **6-F:**  Yeah, and then
**[14:19:07 --> 14:19:15]** **6-F:**  And tomorrow we'll talk about setting up the development folder if you want, but that's also part of it, just if you give it access to have your downloads folder
**[14:19:15 --> 14:19:17]** **6-A:**  So I create a new project,
**[14:19:17 --> 14:19:20]** **6-A:**  use existing folder, select a folder,
**[14:19:21 --> 14:19:23]** **6-A:**  navigate to that folder,
**[14:19:25 --> 14:19:33]** **6-A:**  and I'm going to select it, and this time I'm going to give it a better name, and I'm going to call it um M_ Clod projects for Monday.
**[14:19:35 --> 14:19:37]** **6-A:**  Maybe this is actually just a project.
**[14:19:41 --> 14:19:52]** **6-A:**  And so we all get to a something that looks something like this once we do that. We select a folder, create a project, and again grab one of our folks if anyone has any difficulty getting to the screen. And once we're here
**[14:20:19 --> 14:20:20]** **6-F:**  What is that camera for? They're
**[14:20:20 --> 14:20:20]** **6-H:**  Oh, oh, shh.
**[14:20:20 --> 14:20:22]** **6-F:**  probably not here as well. It's like they're really fancy drawing.
**[14:20:22 --> 14:20:24]** **6-I:**  Oh, but you're not pushing on the shelf.
**[14:20:24 --> 14:20:26]** **6-F:**  So if I, I would actually be in that gallery.
**[14:20:26 --> 14:20:27]** **6-A:**  Absolutely.
**[14:20:27 --> 14:20:29]** **6-A:**  It'll be a way to be actually talking about it
**[14:20:29 --> 14:20:29]** **6-F:**  Yeah,
**[14:20:29 --> 14:20:35]** **6-A:**  or tricks of your style. So if you have an actual file, it's kind of like you're just in the right place. If you copy it out, it could get too long, and you don't want to do it.
**[14:20:35 --> 14:20:37]** **6-A:**  So, but it's cool.
**[14:20:37 --> 14:20:42]** **6-F:**  But I had to do this. Let me ask this. It's like the complete opposite of adventurer it was.
**[14:20:42 --> 14:20:43]** **6-I:**  Oh, perfect.
**[14:20:43 --> 14:20:43]** **6-F:** 
**[14:20:44 --> 14:20:46]** **6-H:**  So I didn't really see how you could put that in a good time.
**[14:20:46 --> 14:20:48]** **6-I:**  People who use the internet are cyber
**[14:20:48 --> 14:20:48]** **6-H:**  Yeah.
**[14:20:48 --> 14:20:49]** **6-I:**  using the internet now,
**[14:20:49 --> 14:20:50]** **6-H:**  Yeah.
**[14:20:50 --> 14:20:50]** **6-I:**  I think.
**[14:20:50 --> 14:20:50]** **6-H:** 
**[14:20:50 --> 14:20:50]** **6-H:**  Yeah, of course.
**[14:20:51 --> 14:20:52]** **6-I:**  There was a very high demand.
**[14:20:52 --> 14:20:52]** **6-J:**  Yes.
**[14:20:52 --> 14:20:53]** **6-I:**  We don't have to show the items.
**[14:20:54 --> 14:20:56]** **6-H:**  So why did you keep on letting people
**[14:20:56 --> 14:20:58]** **6-I:**  I have so many people I
**[14:20:58 --> 14:20:58]** **6-H:**  Is
**[14:20:58 --> 14:21:00]** **6-I:**  didn't let in front of the computer and I didn't get to
**[14:21:00 --> 14:21:00]** **6-H:**  you all there?
**[14:21:00 --> 14:21:04]** **6-I:**  put everything out on the two pages double-paged.
**[14:21:16 --> 14:21:16]** **6-A:**  Okay.
**[14:21:18 --> 14:21:40]** **6-A:**  So let's do some basic operations on some of these files just to kind of make sure that it's working for us. One one initial thing we can do I I mentioned we can change um the model. Harvard's paying for this, uh and so we may as well use a good model. Uh you might go over the limit if you use the maximum model like all day and all night. Uh it it
**[14:21:40 --> 14:21:49]** **6-A:**  initially you are never gonna go over the limit if you're in one single chat talking to to Claude, especially in that chat. You could use the highest model with this four point eight all day long.
**[14:21:49 --> 14:22:05]** **6-A:**  We're gonna show you how to start running many many many operations at once when you have big jobs to do. That's when you could go over the limit and you should think about what model you use. Uh I'm gonna change right now from Sonnet four point six to Opus four point eight. That's the best model. It's high reasoning right now. I actually
**[14:22:06 --> 14:22:19]** **6-A:**  Maybe I want it to go a little faster just 'cause I'm doing a demo today and I don't want it to think all day long. And so I'm actually gonna change the effort level from high to low because I want it to be fast. So that's what I'm gonna do.
**[14:22:19 --> 14:22:19]** **6-H:**  So
**[14:22:19 --> 14:22:26]** **6-A:**  And then my first question is just gonna be what do you see in this folder? Let's see what happens.
**[14:22:26 --> 14:22:35]** **6-A:**  So everyone give that a shot, just ask it, what do you see in the folder? You can say else stay on sonnet. If you wanna just practice changing models, it's a good thing to get the hang of.
**[14:22:36 --> 14:22:40]** **6-A:**  So the key thing with Opus 4.8 is it is the best model, the most expensive model,
**[14:22:40 --> 14:22:40]** **6-F:**  Yes,
**[14:22:40 --> 14:22:40]** **6-A:**  it's
**[14:22:40 --> 14:22:41]** **6-K:**  Right.
**[14:22:41 --> 14:22:41]** **6-F:**  the
**[14:22:41 --> 14:22:41]** **6-A:**  a little
**[14:22:41 --> 14:22:41]** **6-F:**  high end.
**[14:22:41 --> 14:22:44]** **6-A:**  it's a little slower to keep it at maximum thinking,
**[14:22:44 --> 14:22:44]** **6-F:**  It's like the
**[14:22:44 --> 14:22:45]** **6-A:**  high thinking.
**[14:22:45 --> 14:22:47]** **6-F:**  higher models are the better.
**[14:22:48 --> 14:22:49]** **6-A:**  And here we go, it tells me something about it.
**[14:22:52 --> 14:22:52]** **6-A:**  Yeah.
**[14:22:57 --> 14:23:17]** **6-A:**  Yes, so on a on a Mac yeah, the this is the quirky thing is on a Mac you'll get this system-wide pop-up, right, that says hey can I have access to your desktop? And that's 'cause you're accessing one folder on your desktop. And so it's not gaining access to your full desktop, that warning, but that warning is confusing. It's only gonna be working in that in that folder. Um but because that warning
**[14:23:17 --> 14:23:17]** **6-H:**  Okay, so
**[14:23:17 --> 14:23:23]** **6-A:**  creeps me out, what I tend to do is create another folder somewhere else like in downloads or
**[14:23:23 --> 14:23:27]** **6-A:**  um and in like we're gonna show you how to create it in your home directory um to tomorrow, but
**[14:23:27 --> 14:23:28]** **6-H:**  Right.
**[14:23:28 --> 14:23:29]** **6-A:**  it's we're doing the formal thing.
**[14:23:29 --> 14:23:29]** **6-I:**  Okay.
**[14:23:29 --> 14:23:41]** **6-A:**  It's it's not gonna access your full desktop, it's only accessing the tablet folder. It just asks you whenever you know, you you you get access to the single file on the desktop, you'll see it it came down like this size, all right.
**[14:23:41 --> 14:23:41]** **6-I:**  Okay.
**[14:23:41 --> 14:23:41]** **6-A:** 
**[14:23:41 --> 14:23:43]** **6-F:**  Is there something that we don't know?
**[14:23:43 --> 14:23:43]** **6-I:**  Does it make sense that concept?
**[14:23:43 --> 14:23:49]** **6-A:**  If you put it document, it's gonna say it can access documents, it's only gonna access in that one thing. Um
**[14:23:49 --> 14:23:50]** **6-I:**  Is it only accessed
**[14:23:50 --> 14:23:51]** **6-F:**  It's an example of another task.
**[14:23:52 --> 14:23:59]** **6-A:**  Exactly. Exactly. And until you turn it off, it won't. Um, you close that. If you close it, it's no longer accessing that.
**[14:23:59 --> 14:23:59]** **6-F:**  It shouldn't.
**[14:23:59 --> 14:24:21]** **6-A:**  Now that that's said, what's what's a little bit stressful is when if you've ever accidentally gave it access to the full desktop, you'd see the same warning. And so even though 'cause we've been very careful and you're saying hey only look at this folder, we're getting the same warning in either case. And that's why I would kinda ultimately create a special folder somewhere where it's not asking me that. 'Cause what what thing that would become a real pain is this kind of
**[14:24:21 --> 14:24:49]** **6-A:**  Um, yes fatigue, this the where a plot's gonna keep asking you without permission to do this, without permission to do this, and even though you you really think you're always gonna say no when appropriate, you will eventually wear down like another data reference. I don't know if anyone's seen The Simpsons where Homer was in charge of um taking care of the power plant and had to keep any yes, and he got this little bird to keep pecking on the uh yes or no. Got tired of it. It's easy to fall into that mode because once you're moving quickly with this plot's gonna be asking you for permission.
**[14:24:49 --> 14:24:50]** **6-A:**  constantly at ninety nine

## Chunk 7

**[14:24:51 --> 14:25:19]** **7-A:**  At the end of the talk you're gonna say yes, so this is the thing to be wary of. But for today you can give access to this folder, um and we're gonna send it at a different project later. Uh if we ask what's in the folder, we'll see here are some things in the folder. And the very first thing I thought it might be fun to do is uh reorganise some images. So if I go to my desktop and I show you what's inside of this folder, you'll see that in recipe photos there are a bunch of photos of recipe cards that have really weird names.
**[14:25:19 --> 14:25:41]** **7-A:**  they're inappropriate. Uh and what I might actually wanted to do is rename these photos according to whatever they were a recipe of and then actually why not actually get it to create a text or a markdown document, as Madeline called it, that actually has the recipe in it. So here we go, I'm gonna hop back into Claude, and I'm gonna say for the recipe photos,
**[14:25:42 --> 14:25:44]** **7-A:**  can you rename them all
**[14:25:46 --> 14:26:12]** **7-A:**  appropriately given the recipe, and then also create, I gonna say markdown doc of the actual recipe on the card. Also give me some historical context on the two-dish and what makes this the recipe interesting.
**[14:26:12 --> 14:26:14]** **7-A:**  Cool version of it.
**[14:26:17 --> 14:26:36]** **7-A:**  So let's give that a try. And I'm doing this because it condenses a lot of things the product can do. So one, it can work on many many files at once, it can change file names, it can read images, it can write text docs, it can just transcribe what's on the image, but then also it can think for itself a little bit and create the some kind of content.
**[14:26:36 --> 14:26:36]** **7-A:**  If
**[14:26:36 --> 14:26:37]** **7-B:**  Okay.
**[14:26:37 --> 14:26:42]** **7-A:**  I were an art historian, maybe I'd wanted to actually give me some interpretation of a work.
**[14:26:42 --> 14:26:45]** **7-A:**  If I was a literary scholar working on manuscripts,
**[14:26:45 --> 14:26:53]** **7-A:**  I might want it to give me the content of the manuscript, or maybe a marginalia on the document. So let's all give this a try and just see what happens.
**[14:26:55 --> 14:27:02]** **7-C:**  And then Marlon, is the only way to see what's in the folders and how they're being changed going to the Finder and
**[14:27:02 --> 14:27:03]** **7-A:**  No,
**[14:27:03 --> 14:27:03]** **7-C:**  no?
**[14:27:03 --> 14:27:05]** **7-A:**  as of as of this week yeah.
**[14:27:05 --> 14:27:06]** **7-C:**  That was just sold on yesterday evening.
**[14:27:06 --> 14:27:07]** **7-D:**  This is
**[14:27:07 --> 14:27:07]** **7-A:**  This
**[14:27:07 --> 14:27:07]** **7-D:**  different
**[14:27:07 --> 14:27:07]** **7-A:**  happens
**[14:27:07 --> 14:27:07]** **7-D:**  to
**[14:27:07 --> 14:27:08]** **7-A:**  this.
**[14:27:08 --> 14:27:08]** **7-D:**  what you do have in iTunes.
**[14:27:08 --> 14:27:17]** **7-A:**  Just that happens constantly surprising us. And so now co-work actually does allow me to get in here. Um actually no, but before it was there, it was in context, in context.
**[14:27:19 --> 14:27:21]** **7-A:**  If I click this, now they've gone away again.
**[14:27:23 --> 14:27:25]** **7-A:**  Okay, never mind, never mind.
**[14:27:25 --> 14:27:25]** **7-C:**  To the chain.
**[14:27:25 --> 14:27:34]** **7-A:**  Initially initially they were all there. There's a little bit of quirkiness about about what shows up in this panel. Um it's gonna show me all of the files and folders that are in context right now.
**[14:27:35 --> 14:27:39]** **7-A:**  It's a little uneven in what it what it shows here to be totally honest.
**[14:27:40 --> 14:27:47]** **7-A:**  Alright, so it's plugging away, it continues to move here. You can hit any of these little disclosure triangles to see what it's doing.
**[14:27:49 --> 14:27:51]** **7-A:**  It's kind of interesting to see
**[14:27:52 --> 14:27:52]** **7-A:**  How it's working.
**[14:27:52 --> 14:27:56]** **7-C:**  I think there's a script above Marlin too that might be more interesting.
**[14:27:59 --> 14:28:01]** **7-C:**  Yeah, so here's it's moving
**[14:28:02 --> 14:28:02]** **7-E:**  And you've
**[14:28:02 --> 14:28:28]** **7-A:**  Yeah, for any for any um people that do no one needs to know how to code, but for anyone that that codes and wants to kind of understand how it's doing this, um the the magic is that uh CLAW can generate text, but it can generate commands that can run in the terminal or shell. And in this case what it's done is it's generated new names for the files and then it generated the shell script for moving the files to those new locations. So M_V_
**[14:28:28 --> 14:28:31]** **7-A:**  this doc oh god you disagree with me?
**[14:28:31 --> 14:28:54]** **7-A:**  In any case, it's writing the shell script that will move the file from its old location to the new file name location. Uh and that's kind of uh how Claude performs those operations. So I'm gonna hop back over to um my explorer again, I apologise, I'm not actually a Windows person, I'm just doing my best. Um and what we see is it has renamed everything to Christmas fruitcake cookies, to dumplings,
**[14:28:55 --> 14:29:02]** **7-A:**  um to Eagle brand ice cream, to French toast cupcakes. So everything has a brand new name, and then also
**[14:29:04 --> 14:29:18]** **7-A:**  it has a document next to it that has the ingredients list, has the directions, has a little history of French toast cupcakes and what makes this an interesting recipe. So that worked for me. Everyone again so everyone give it a try and just see if it
**[14:29:18 --> 14:29:24]** **7-A:**  If it's working for you and our helpers will come around to make sure that's it's working out okay, yes.
**[14:29:24 --> 14:29:25]** **7-C:**  A markdown of what app do you open that?
**[14:29:26 --> 14:29:29]** **7-A:**  So it's gonna work in the this app tomorrow.
**[14:29:29 --> 14:29:29]** **7-C:**  That's great.
**[14:29:29 --> 14:29:30]** **7-A:** 
**[14:29:30 --> 14:29:30]** **7-F:**  Okay.
**[14:29:30 --> 14:29:35]** **7-A:**  Uh but you have to be on the Mac. So Even though I said I would not do this
**[14:29:37 --> 14:29:39]** **7-A:**  for people that wanna like look ahead for tomorrow,
**[14:29:39 --> 14:29:39]** **7-F:**  Yeah.
**[14:29:41 --> 14:29:43]** **7-A:**  if you were to if you actually open up
**[14:29:46 --> 14:29:48]** **7-A:**  This same folder in quad code,
**[14:29:48 --> 14:29:49]** **7-A:**  my
**[14:29:51 --> 14:29:53]** **7-A:**  quad projects, this one.
**[14:29:54 --> 14:29:58]** **7-A:**  Trust workspace, this is just a sneak preview of what's
**[14:29:58 --> 14:29:58]** **7-C:**  You got
**[14:29:58 --> 14:29:58]** **7-A:**  gonna happen
**[14:29:58 --> 14:29:58]** **7-C:**  a yellow
**[14:29:58 --> 14:29:58]** **7-A:**  tomorrow.
**[14:29:58 --> 14:29:59]** **7-C:**  chat though.
**[14:30:00 --> 14:30:07]** **7-A:**  Um you have to say one thing in here, we're gonna be able to see the files in here um and in my uh
**[14:30:13 --> 14:30:41]** **7-A:**  I can look at any of my documents inside of Claude code. Um the reason I'm doing this is because most people who if you're if you have a development background, you're gonna look at this in V_S_ code or uh or or it you know some tool you use for writing code. Um we're gonna get you all working within the Claude app to do this. So that it's all gonna work just fine. Uh again, the only reason we're not jumping ahead to this is because there's a couple quirks with getting this working for Windows folks. Um but for for right now you can just go ahead and open it up.
**[14:30:41 --> 14:30:45]** **7-A:**  up on whatever app it defaults to in your Explorer Finder.
**[14:30:46 --> 14:30:48]** **7-A:**  So alright, so but back to co-work.
**[14:30:49 --> 14:31:15]** **7-A:**  So we've all created a task. It read some images, it generated some content, um and we can imagine how this could apply to a lot of different types of data. Uh already Becca showed you that s a lot of student work is coming in on papers, the ability to take photos of things that students do in class, another cool use case is if you are someone that does a lot of board work, you could at the end of every single class just go up and take shots of the board that day, um you could even record yourself talking quickly into your phone,
**[14:31:15 --> 14:31:28]** **7-A:**  You could shove all those files into a folder, um and Claude can help you keep track of a kind of teaching journal so you can find your way back to those documents, um you'd work on manuscripts you were saying, any of th you you work on a lot of the photos of things, you've done some
**[14:31:28 --> 14:31:28]** **7-C:**  Lots
**[14:31:28 --> 14:31:28]** **7-A:**  examples.
**[14:31:28 --> 14:31:39]** **7-C:**  of photos. Uh we've had people annotate syllabi, annotate translations, uh so it it's also good at not just picking out the text for its own sake, uh but if you have some kind of source text
**[14:31:39 --> 14:31:57]** **7-C:**  text or source document that then people are marking up in some way. Uh there's some prompting you probably want to do uh to really make sure that goes well, but it it picks up pretty well on um student annotations. And then you can put those all together across a huge amount of students, uh and yes you can do it at the individual student level,
**[14:31:57 --> 14:32:06]** **7-C:**  but you can see very quickly, almost in real time in the same class, what the patterns are across your students of what they're annotating, where they're stumbling, what
**[14:32:06 --> 14:32:14]** **7-C:**  but you know questions they've written down, etcetera. So sometimes we compare this to a old um are they clicker the kind of A_ B_ C_ D_ uh buttons students
**[14:32:14 --> 14:32:15]** **7-G:**  Yes, see clickers.
**[14:32:15 --> 14:32:15]** **7-C:**  so we get.
**[14:32:15 --> 14:32:16]** **7-G:**  Clickers.
**[14:32:16 --> 14:32:34]** **7-C:**  Um clicker is it clickers? Yes. Uh now imagine if you do that on paper and you're not even taking photos, but maybe they're all uploading it to Slack or Canvas uh and eventually you're able to w and we'll show you how to connect to those tools, automatically pull those images down, loop through and then suddenly have it essentially a data set.
**[14:32:34 --> 14:32:39]** **7-C:**  that's of information to to look at or query. That's like this at scale.
**[14:32:39 --> 14:32:59]** **7-A:**  And so so we've processed a whole bunch of like inputs that have come in and now what we'll do is create just a little taste of an output. We're gonna give you tons of ideas of cool things you can build with this, but just to get the ball rolling why don't we ask it to create a web page that embeds all these recipes. Um and so what I'm gonna type in is uh can you create
**[14:33:02 --> 14:33:22]** **7-A:**  An HTML doc that embeds all of these recipes, both the images and the text about them you created, one single stylish HTML file.
**[14:33:25 --> 14:33:29]** **7-A:**  And so for those of you that have seen some faculty start to use Quadcode, this is something a lot of folks are doing.
**[14:33:29 --> 14:33:32]** **7-A:**  Matthew Schwartz in physics, I don't know if anyone knows him,
**[14:33:32 --> 14:33:44]** **7-A:**  but has taken his whole course and created a really interesting online interactive physics textbook. And this pattern of doing a lot of thinking and analysis as you know a faculty member, whether it's for research or planning or teaching,
**[14:33:45 --> 14:33:52]** **7-A:**  but then using HTML or something web-based to present that to students can be really powerful because there's so much freedom for you.
**[14:33:52 --> 14:34:12]** **7-A:**  view um over over what the output will end up looking like. And while clot it's hard to actually create Word docs and PowerPoint presentations that look really great, it's insanely easy for clot to work with H_T_M_L_ and C_S_S_ 'cause it knows code. You don't need to know code at all, you just need to know to ask for an H_T_M_L_ doc.
**[14:34:12 --> 14:34:13]** **7-C:**  Yep, and then test it. So like
**[14:34:13 --> 14:34:14]** **7-A:**  Clot's
**[14:34:14 --> 14:34:14]** **7-C:**  Becca's
**[14:34:14 --> 14:34:14]** **7-A:**  gonna
**[14:34:14 --> 14:34:20]** **7-C:**  example also was uh an example of making a web page kind of interactive that then was I framed.
**[14:34:21 --> 14:34:22]** **7-C:**  The Sergeant of Armory.
**[14:34:22 --> 14:34:24]** **7-A:**  So here it goes, it's doing its thing.
**[14:34:24 --> 14:34:25]** **7-C:**  The zipper's not ready.
**[14:34:25 --> 14:34:30]** **7-A:**  So close. Everyone give this a try and then um we'll see who who wins.
**[14:34:33 --> 14:34:35]** **7-A:**  Okay, I'm gonna let it go ahead and do it.
**[14:34:38 --> 14:34:42]** **7-C:**  Uh do we wanna talk about the other uh examples? So there's a few other oh, perfect, never mind.
**[14:34:43 --> 14:34:47]** **7-A:**  So just in time I have it here, I can say that I wanna open up Microsoft Edge.
**[14:34:49 --> 14:34:50]** **7-A:**  And then I'll have my recipe card collection.

## Chunk 8

**[14:34:51 --> 14:34:58]** **8-A:**  But what's another way that you can open up HTMLs by just clicking through? Or I know we're not doing the paths right now, but um
**[14:34:59 --> 14:35:00]** **8-B:**  Yeah, well in here, so I have um
**[14:35:00 --> 14:35:01]** **8-A:**  Okay.
**[14:35:01 --> 14:35:04]** **8-B:**  open an edge, I can show in folder.
**[14:35:06 --> 14:35:17]** **8-B:**  It's c sometimes it will open up automatically. Um sometimes I'll have to, you know, it it should prompt you to open in your browser or choice. Uh if it's not your browser or choice then we can help you change your default browser.
**[14:35:17 --> 14:35:33]** **8-A:**  But you'll see up here, it's not an actual web site. Like if you sent this to someone they wouldn't be able to open it. This is just the path on your computer. So it's just rendering what's locally on your computer. If however you made something and you make something in the course of this class that then you'd wanna share it with your students
**[14:35:33 --> 14:35:48]** **8-A:**  Yes, there are a ton of easy ways to immediately and for free get those up, and feel free to talk to us and we'll help you through it. So, if you did wanna turn this into something shareable we can but right now this is just local. But here we go. So here is your stylish
**[14:35:48 --> 14:35:53]** **8-A:**  or stylised website, as you call that. Uh here you go.
**[14:35:54 --> 14:35:54]** **8-B:**  Cool.
**[14:35:54 --> 14:36:20]** **8-A:**  And so we have a few more examples in this folder. Uh you'll we're gonna continue this motif throughout the workshop. So every single day uh we're going to present to you all another GitHub repo which is just a bunch of folders with examples uh that hopefully you can play with. We're just trying to give you a sandbox with some structure. Uh but eventually you'll be making your own folders. So uh there's a few other examples. Again we have uh
**[14:36:20 --> 14:36:50]** **8-A:**  Some context research, so the research documents we were initially talking about um that have kind of the context rot etcetera, that's in here. You could point it there and say hey, could you please summarise these articles for me or let me know what one of the most important figures are just to get that experience for instance. So there Marlin goes uh with with that. Um that's a really quick example, we could ask like turn these into a web page, it doesn't just have to be a summary.
**[14:36:50 --> 14:36:53]** **8-A:**  Um yeah, there you go.
**[14:36:55 --> 14:37:13]** **8-A:**  Nice. Uh what else do we have Marilyn, if we get back into the folder, uh we also have yeah, we we're gonna have a glossary, different sheets, we have handouts, there's more uh there's kind of a literature example, I think we have all of
**[14:37:13 --> 14:37:20]** **8-A:**  Or no, never mind. I'm sure I'll go through that." Uh, population data, a recipe. We also our first
**[14:37:21 --> 14:37:30]** **8-A:**  version of this workshop, we had Pia Sorenson from Science of Cooking came in and she was very kind to let us kind of borrow things from that course. That course has been running for a really long time.
**[14:37:30 --> 14:37:31]** **8-A:**  So she has a lot of great structured content.
**[14:37:32 --> 14:37:46]** **8-A:**  So if for instance you wanted to play with what would it be like if I downloaded my canvas and all of my previous course materials and see what that's like. Uh we have for midterms, for syllabus, for course schedule, so you could also play later with what does it feel like to ask
**[14:37:46 --> 14:38:12]** **8-A:**  Hey, I have a guest speaker scheduled for October 8th. If now she can't come, uh so I have to schedule this doctor to come in no you know November twenty first. What are the four different ways or several different ways I could restructure my class and the assignments in order to make this work? See how that feels. Or if Becca talks about this in some of her other examples, uh you've given a midterm and suddenly many students have come down with the stomach flu.
**[14:38:12 --> 14:38:39]** **8-A:**  And you're gonna have to come up with a multiple different alternative exams. Uh how can you do that with some prompting, uh is another example. So we've got some mid-terms in there if you wanted to make a practice exam or a checklist. Uh those are the sorts of activities it's really good at. Again, because you're providing it with so much context that's yours, that you have vetted that you know is high quality, and you're pointing it at a small discrete task just based on that information.
**[14:38:40 --> 14:39:02]** **8-A:**  Uh so yeah, there's Marlin kind of going with these examples. So the last thing we'll hang out and then um hand out and then we'll answer questions, we're not going anywhere and again we're always here early tomorrow if you're struggling, uh but building off the recipe example, behold homework, um if you wish. Uh so
**[14:39:03 --> 14:39:23]** **8-A:**  One of the uh kind of like a nice heuristic way to plan projects that you might wanna do in your course that might be a good thing um totally up to you. Everything we're gonna do is self-contained in these classes, but if you have specific project in mind that you can work on a little bit every single day as we teach you new things, this can be a really good guide for that.
**[14:39:23 --> 14:39:31]** **8-A:**  Thank you Jenna. Uh so if everything are just strings in strings out, think of it like a recipe.
**[14:39:31 --> 14:40:00]** **8-A:**  So what are the ingredients, what are the inputs you need in terms of context? So what is the information? Time, reorganizing my class or um coming up with a script for a new lecture. I probably want all my course material. I want my syllabus, all of my readings, all of my P-sets, those could all be ingredients. Uh then of course you're probably thinking of an output. Kind of what is your ultimate output? But be more specific. Do you want it in a new file?
**[14:40:01 --> 14:40:20]** **8-A:**  Do you want it split out across, uh maybe ideas for slides plus a lecture? Uh and then the instructions to get there. So these are your prompts and you'll see a few things here, skills, scripts, tools. We haven't gotten there yet, that's what the next few days are for. Uh but all of this, what will teach you are just
**[14:40:20 --> 14:40:28]** **8-A:**  Ways of improving that context flow. How can you more quickly build up context as you build up context about you, yourself,
**[14:40:28 --> 14:40:29]** **8-A:**  your working style,
**[14:40:29 --> 14:40:32]** **8-A:**  as well as your specific discrete projects?
**[14:40:32 --> 14:40:35]** **8-A:**  And then as you continue to work with AI,
**[14:40:35 --> 14:40:39]** **8-A:**  if you find you're doing the same sorts of operations again and again,
**[14:40:39 --> 14:40:47]** **8-A:**  and you're tired of copying and pasting the same prompt for please make me slides, please make me a new set of tests, how can you
**[14:40:48 --> 14:41:13]** **8-A:**  capture and package those operations um all of that information into these sorts of uh buckets before you get to your outputs. Um so again this is just kind of a little analogy. Uh but if you wanted to fill this out feel free to stick around today. Um if you have a really clear idea of what you'd like to do, um we will also you don't necessarily have to fill out the sheet, uh but let us know.
**[14:41:13 --> 14:41:37]** **8-A:**  Because we can set up the examples beforehand. We want this to be as applied and as useful for you guys as possible in your own context. So we're gonna hang around afterwards. If you have an idea for a project, let us know and we'll try to build that out beforehand. And if we have your permission, even go hunt down some of your own materials to show as an example tomorrow in the next few days.
**[14:41:37 --> 14:41:40]** **8-B:**  If you want you could look y like so last week's repository is just up
**[14:41:40 --> 14:42:09]** **8-B:**  stop there right now. And you'll see tomorrow when you come in, we're gonna have a folder called recipes that will have um some samples from us but some samples from from you all if you're interested. For instance last week um some of the faculty wanted to have uh a r a resource for T_F_s that are learning to teach chemistry and their idea is that you would have a resource that models the errors that certain sorts of students make. And so what we did is generated for them out of that context and some research
**[14:42:09 --> 14:42:19]** **8-B:**  search um on uh I mean Jean Yun are you here? What is the re you jump in, this your your baby. So your research was on different sorts of modes of um mistakes that people make in stem courses essentially.
**[14:42:20 --> 14:42:32]** **8-C:**  So we populate our context with a little bit more research on um you know stuff on chemistry education, whereas in the common failure modes and mistakes and misunderstandings that arise at, you know, college level chemistry education.
**[14:42:32 --> 14:42:43]** **8-C:**  So with that and with the prompt that we were or the recipe we were provided we were able to mock up some prompts that you would put into Clause so we can simulate the role of a student for T_F_ training.
**[14:42:45 --> 14:42:58]** **8-B:**  So I any of you checked this out last time. But uh if people wanna feel this out right now, then we will as our homework get a little bit of a template ready for you for next time that you can fork. Again, no obligation to do this, but if anyone wants to, we're excited to get you started.
**[14:42:58 --> 14:42:59]** **8-A:**  And then I've got yeah.
**[14:43:13 --> 14:43:26]** **8-A:**  So we have the prompts and every single different uh kind of project, and we can share last week's project tonight over email, so that you could peek through them. Uh and what you're describing is pretty common, it's called like a prompt.
**[14:43:26 --> 14:43:37]** **8-A:**  library, many places kind of slowly develop prompt libraries. And people tend to share in to libraries, but people also keep their own separate kind of prompt libraries or um personal context
**[14:43:37 --> 14:43:38]** **8-C:**  I just need to specify.
**[14:43:38 --> 14:43:38]** **8-A:**  things.
**[14:43:38 --> 14:43:41]** **8-C:**  So I'm looking at, for example, the population data folder.
**[14:43:41 --> 14:43:41]** **8-A:**  Yeah.
**[14:43:41 --> 14:43:47]** **8-C:**  So I can imagine you could probably do like an infinite number of things with this, but I just was curious.
**[14:43:47 --> 14:43:52]** **8-A:**  Kind of prompts, I think in like would I find that somewhere, some learning lab examples.
**[14:43:53 --> 14:43:54]** **8-C:**  It's
**[14:43:54 --> 14:43:54]** **8-A:**  It's that.
**[14:43:54 --> 14:43:54]** **8-C:** 
**[14:43:54 --> 14:43:55]** **8-A:**  You got it.
**[14:43:56 --> 14:43:56]** **8-A:**  Oh, here.
**[14:43:56 --> 14:44:09]** **8-B:**  But so we have we do have these for for some of them. We didn't have it for that one. But for the class schedule conflict I just did for um Pia Sorenson's class, that's in there. Um and last week we did the same thing. Uh Joanne Chang can't can't come that that week.
**[14:44:09 --> 14:44:09]** **8-A:**  I think
**[14:44:09 --> 14:44:09]** **8-B:**  Can you
**[14:44:09 --> 14:44:10]** **8-A:**  the resources
**[14:44:10 --> 14:44:10]** **8-B:**  can you fix it?
**[14:44:10 --> 14:44:14]** **8-A:**  is Marlin under day one, now that I remember this, but
**[14:44:14 --> 14:44:15]** **8-B:**  Resources
**[14:44:15 --> 14:44:16]** **8-A:**  Day one recap.
**[14:44:16 --> 14:44:17]** **8-B:**  day one recap. Activities, yes.
**[14:44:17 --> 14:44:19]** **8-A:**  Activities, population pyramids, operations
**[14:44:19 --> 14:44:20]** **8-B:**  Operations
**[14:44:20 --> 14:44:20]** **8-A:**  True's
**[14:44:20 --> 14:44:20]** **8-B:**  tool commands.
**[14:44:20 --> 14:44:20]** **8-A:**  okay.
**[14:44:20 --> 14:44:22]** **8-B:**  Analyse data prompt. There we go.
**[14:44:25 --> 14:44:27]** **8-B:**  So we are gonna overshare today.
**[14:44:27 --> 14:44:50]** **8-B:**  Um uh uh every day we're gonna share every single thing that we do with you and it's gonna be too much information, but that's 'cause we're gonna help you understand how you can actually ask Claude um to give you the amount of information you want. We are gonna have our entire transcript of every single thing Madeline and I say. We're gonna have screen-shots of everything, we're gonna have every single example we show you. You're never gonna look at all of that with your human eyes ever, but here's the thing, you can ask Claude to look

## Chunk 9

**[14:44:51 --> 14:45:16]** **9-B:**  for you, so you'll get the repo for tomorrow and you can ask, hey what are the ten top tips from yesterday, um and we hope this is a model of what faculty might think about doing in their courses going forward where you can vert present students with a lot of information that they can then query and you're grounding their learning in high quality context that you curate and we're asserting everything we've said, go ahead and use that, every example we get give you we approve of it um but then you will use Clod to actually find the parts of that that are valuable to you.
**[14:45:17 --> 14:45:17]** **9-C:**  Yeah.
**[14:45:18 --> 14:45:21]** **9-C:**  And Claude can help you develop prompts as well.
**[14:45:21 --> 14:45:21]** **9-C:**  Sorry, yeah.
**[14:45:21 --> 14:45:24]** **9-D:**  I was actually just going off off of all that
**[14:45:25 --> 14:45:40]** **9-D:**  Right here. What are the keys to a good quality prompt so that you don't make the mistakes that you need to be and get the kind of output that you want. Um is there like a like a list of things that every prompt that should have, I guess, I just I don't I don't
**[14:45:40 --> 14:45:40]** **9-B:**  We
**[14:45:40 --> 14:45:40]** **9-D:**  know.
**[14:45:40 --> 14:45:51]** **9-B:**  should. I mean, when you get papered, it is the the the big thing we've sent so far today is the context going into grounded is essential. I think back to that Corolla honest example, if it's just going on the average of the internet,
**[14:45:51 --> 14:46:04]** **9-B:**  that just is training data, it's really sure going to get important academic ideas wrong. And so giving it enough context to have all the information it needs to have to be factually accurate is just totally insanely important.
**[14:46:04 --> 14:46:19]** **9-B:**  And that that's kind of the context engineering part of it. The so-called prompt engineering part of it um is what Madeline's going to talk about now and there's kind of a neat way of thinking about the different coordinates of that prompting that she has a very elegant drawing of now. This is great, this is your v the best one ever.
**[14:46:19 --> 14:46:19]** **9-B:**  Never.
**[14:46:19 --> 14:46:20]** **9-C:**  It's been so long. Um
**[14:46:21 --> 14:46:50]** **9-C:**  Uh, so you're gonna see a lot of, like, people try to sell programmes of like how to prompt, best way to prompt. Uh Marlon and I have sacrificed ourselves uh to X, formerly known as Twitter, um in order to kind of scrape uh what the people who are working in development in these companies are constantly posting about how to prompt. But in essence there's a lot of hype around it but it's just this is gonna sound strange but the best prompt for your output is the best prompt that comes from you.
**[14:46:50 --> 14:47:01]** **9-C:**  from you. You have to kind of put yourself and your own departmental context in it. So if you look up online the way some people structure prompts, may not be correct for you very specifically.
**[14:47:01 --> 14:47:16]** **9-C:**  But if we're just gonna think of like a list of four things, uh you can think of it like the structure of an utterance uh for those of you who are from fields uh that kind of cover this. And it's really weird 'cause normally uh when you kind of cover the structure of an utterance you're thinking of yourself as the speaker and you as
**[14:47:16 --> 14:47:16]** **9-A:**  uh
**[14:47:16 --> 14:47:42]** **9-C:**  was audience members when we put this workshop together. I'm thinking of myself a speaker. Uh but it's almost like working with an L_L_M_ is interaction zero instead of interaction one. You have to go back in time and hear the L_L_M_ is the speaker, you are the audience, and then you're requesting form and content. Uh so very commonly in prompts you'll see these four different components. And many of these prompts will begin with
**[14:47:42 --> 14:47:47]** **9-C:**  You are. So the most famous version of this is the ChatGPT original system prompt.
**[14:47:48 --> 14:47:57]** **9-C:**  You are a helpful assistant is literally like the first thing that ever came out of a large language model company to help structure its thing.
**[14:47:58 --> 14:48:09]** **9-C:**  So in this case, if you're building a data visualization, you might say you are a specialist in data visualization and you are particularly good at using D3.
**[14:48:09 --> 14:48:21]** **9-C:**  Or something of that sort. You are building, uh for a faculty member doing X_Y_ and Z_ but maybe who comes from uh a more ethnographic field.
**[14:48:21 --> 14:48:28]** **9-C:**  So uh the ways in which you're gonna structure data has to have a a bit more texture as opposed to being more technical. Something of that sort.
**[14:48:29 --> 14:48:55]** **9-C:**  And then you're talking about the form and content. So I would like a uh population pyramid uh using this CSV. Uh but this is how I would like it to look. Uh this is how I would like it to be formatted and I would like it in this folder please. That's the basis of a really good prompt. Um and how that eventually kind of fits into your longer context window uh is again, you can't get away from the basics.
**[14:48:55 --> 14:49:21]** **9-C:**  Uh but just think of it as your system prompt, your memory. There will later be other um whoo, this is your like stick around. Um and eventually we'll get to other dock types that get inserted automatically in the conversation that you yourself can brew up that might and often relate to who you are as a person that will always be true in every single project for example. Uh but then you have your prompt.
**[14:49:22 --> 14:49:26]** **9-C:**  Um and this is just this little little guy. And if you really
**[14:49:27 --> 14:49:54]** **9-C:**  hit um the ball out of the park with this first prompt, then the A_I_ output is probably gonna be better. So then your whole context window is just stronger and healthier. If you have a really short prompt and you say uh make this and it makes something really bad, well then you've kind of uh poisoned your whole context window. This is also why you wanna start new chats. Um 'cause you might be saying, hey uh this recipe, I'm out of this ingredient, what
**[14:49:54 --> 14:50:02]** **9-C:**  and what could I replace it with. And then if you're still in that chat context window and then you go, also please summarise this article for me in the same chat.
**[14:50:02 --> 14:50:09]** **9-C:**  All of that context is going in. So that's why we're having you guys think of like clean new context windows every single time for your prompts.
**[14:50:10 --> 14:50:20]** **9-B:**  And I know we got to let you go, but then the one other little thing on the on the prompting is having a chain of things sometimes works better. There are lots of research on this that we can share with you. But even just saying getting output and then asking it all right, whether
**[14:50:20 --> 14:50:22]** **9-B:**  What are the top five things I should change about that?
**[14:50:22 --> 14:50:39]** **9-B:**  And then passing both of those on to the model will yield better better results. We've done this with translation courses here where you get initial translation, then you submit that translation to the LLM again, say find the top five problems with this, now go fix that, and you inevitably end up with better results just as you as a human do when you think critically about
**[14:50:39 --> 14:50:39]** **9-C:**  Or
**[14:50:39 --> 14:50:40]** **9-B:**  your with initial
**[14:50:40 --> 14:50:40]** **9-C:**  prompting,
**[14:50:40 --> 14:50:40]** **9-B:**  draft or something.
**[14:50:40 --> 14:50:46]** **9-C:**  I'll usually draft my prompt with one large language model and then say use this prompt and edit it and build it out.
**[14:50:46 --> 14:51:04]** **9-C:**  out in these ways, and it'll make me a much long longer prompt and and I'll say maybe involving the language from these two P_D_F_s or readings or articles. And then I'll go and start a new chat with this like super prompt that I've grown in partnership with another large language model that I see a question. Yeah.
**[14:51:05 --> 14:51:09]** **9-E:**  unrelated to this. From your experience, what you found
**[14:51:10 --> 14:51:12]** **9-E:**  to be the biggest limitations
**[14:51:12 --> 14:51:14]** **9-E:**  Then what can't Claude eventually answer?
**[14:51:15 --> 14:51:16]** **9-E:**  So what type of task?
**[14:51:20 --> 14:51:37]** **9-B:**  So, but I have pretty amazing, again this is the factual knowledge when you don't ground it in actual data. Like that's the key thing. That's still a real problem. Thank goodness for humans that you know we're doing this. And then I would say is that like um that we'll show you how to build these larger and larger systems that can acquire do more complex operations.
**[14:51:38 --> 14:51:47]** **9-B:**  But a kind of like next level problem I see which I think is still exciting for humans is the more of those summary and compaction activities that has to go through to create larger projects,
**[14:51:47 --> 14:51:57]** **9-B:**  The more it kind of like sands off the rough edges of ideas and the less in alignment with your original vision as a human it will end up being. And again, I think that's great for academics,
**[14:51:57 --> 14:52:03]** **9-B:**  it's great for artists, it's great for creative folks of all sorts, um because I think it's it's really really good at performing large scale
**[14:52:04 --> 14:52:11]** **9-B:**  average um high quality ideas, but it's less good at sticking in alignment with your um with your vision basically.
**[14:52:11 --> 14:52:13]** **9-C:**  It's also still really bad at like 3D space.
**[14:52:13 --> 14:52:39]** **9-C:**  base and spatial things. So if I'm making a front end website where I really need components to be arranged in a certain way on the X_Y_ let alone Z_ it it it can vibes based do it, like it knows oh it's kind of this quadrant is where this should be, this component should be. But I normally even still with how far it's come in terms of vibe coding and coding, which is one of the things it's best at, I still have to go into the actual like paged
**[14:52:39 --> 14:52:49]** **9-C:**  that it's made and I have to myself adjust the X_Y_ coordinates and the size of the box to get it correct. So it's still not there in in that.
**[14:52:50 --> 14:52:51]** **9-B:**  All right, we have to let everyone
**[14:52:51 --> 14:52:51]** **9-C:**  We
**[14:52:51 --> 14:52:51]** **9-B:**  go. Please,
**[14:52:51 --> 14:52:51]** **9-C:**  but there's
**[14:52:51 --> 14:52:52]** **9-B:**  please,
**[14:52:52 --> 14:52:52]** **9-C:**  one question.
**[14:52:52 --> 14:52:53]** **9-B:**  we're going to stick we're going to stick
**[14:52:53 --> 14:52:53]** **9-C:**  Yeah,
**[14:52:53 --> 14:52:55]** **9-B:**  around, but I just want but some people have
**[14:52:55 --> 14:52:55]** **9-D:**  But
**[14:52:55 --> 14:52:55]** **9-B:**  to
**[14:52:55 --> 14:52:55]** **9-D:**  free,
**[14:52:55 --> 14:52:56]** **9-B:**  run. I yeah, want to make everyone sure they
**[14:52:56 --> 14:52:56]** **9-D:**  be
**[14:52:56 --> 14:52:56]** **9-B:**  feel
**[14:52:56 --> 14:52:56]** **9-D:**  free.
**[14:52:56 --> 14:52:57]** **9-B:**  comfy going.
**[14:52:57 --> 14:52:57]** **9-C:**  Yeah.
**[14:52:57 --> 14:52:58]** **9-B:**  But but again,
**[14:52:58 --> 14:52:58]** **9-D:**  Yeah,
**[14:52:58 --> 14:52:58]** **9-B:**  we're not going anywhere.
**[14:52:58 --> 14:52:59]** **9-D:**  we can write
**[14:52:59 --> 14:53:00]** **9-B:**  We're delighted to stick around
**[14:53:00 --> 14:53:00]** **9-D:**  yes.
**[14:53:00 --> 14:53:00]** **9-E:**  Yeah.
**[14:53:00 --> 14:53:01]** **9-B:**  and answer answer
**[14:53:01 --> 14:53:01]** **9-D:**  Tomorrow.
**[14:53:01 --> 14:53:08]** **9-B:**  questions. And we hope that you guys will come back tomorrow too. And we're going to continue with the next tabs in the system going on to Claude code.
**[14:53:08 --> 14:53:08]** **9-C:**  Uh okay.
**[14:53:08 --> 14:53:16]** **9-B:**  Again, show up early if you want any help, especially on Windows machines with that. Uh but again, every day you were welcome to stay till four. We're not going anywhere. And we were delighted
**[14:53:16 --> 14:53:16]** **9-D:**  Yeah.
**[14:53:16 --> 14:53:17]** **9-B:**  to to answer more questions.
**[14:53:17 --> 14:53:17]** **9-C:**  Ha ha.
**[14:53:17 --> 14:53:18]** **9-C:**  Ah,
**[14:53:18 --> 14:53:18]** **9-D:**  Okay.
**[14:53:18 --> 14:53:18]** **9-C:**  ha.
**[14:53:18 --> 14:53:18]** **9-D:** 
**[14:53:18 --> 14:53:20]** **9-C:**  Nice, and we got our first recipe. So if anyone wants to donate,
**[14:53:20 --> 14:53:21]** **9-D:**  Oh my god, it was
**[14:53:21 --> 14:53:21]** **9-C:**  um
**[14:53:21 --> 14:53:21]** **9-D:**  so much fun.
**[14:53:21 --> 14:53:23]** **9-C:**  we're gonna build some.
