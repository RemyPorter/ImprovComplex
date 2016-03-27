This uses the OSX `say` command line tool, so this is OS specific.

This program creates a passive-aggressive computer that guides an improv show. It is meant to be used with an operator.

You launch the program with: `python3 -m improv`

This will recite an intro, and then provide you with a `> ` prompt. At the prompt, you may type any sentence, and when you hit enter, the computer will say that.

You may also type simply "c" (case matters), which will cause the program to speak a random phrase from phrases.txt or "q", which causes the program to speak its outro. While the program is running, on a random interval it will automatically nag the performers by reciting a random phrase from phrases.txt.

The three key files are:

    * intro.txt
    * outro.txt
    * phrases.txt

Phrases.txt is simply that, a list of phrases that are "built in" to the program. It's one phrase per line. The program will recite whatever is in there.

Intro.txt and outro.txt are slightly different- they are meant to be pre-prepared scripts for the show, to both introduce and play off our performers. Every line of text will be recited.

Inside of these files, you may use "%ACT" as a variable. It will be replaced with whatever activity was chosen during the Intro. Any line that starts with ". " (note the space!) is viewed as a pause. It should be followed by a number that represents the duration of that pause.

Longterm, I'll add some command line flags to this, but I whipped this up to run a team at a Bring-Your-Own-Team event, which is little more than improvisers partying.