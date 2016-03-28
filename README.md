This uses the OSX `say` command line tool, so this is OS specific.

This program creates a passive-aggressive computer that guides an improv show. It is meant to be used with an operator.

You launch the program with: `python3 -m improv`

This will recite an intro, and then provide you with a `> ` prompt. At the prompt, you may type any sentence, and when you hit enter, the computer will say that.

You may also type simply "c" (case matters), which will cause the program to speak a random phrase from phrases.txt or "q", which causes the program to speak its outro. While the program is running, on a random interval it will automatically nag the performers by reciting a random phrase from phrases.txt.

The three default files are:

    * intro.txt
    * outro.txt
    * phrases.txt

Phrases.txt is simply that, a list of phrases that are "built in" to the program. It's one phrase per line. The program will recite whatever is in there.

Intro.txt and outro.txt are slightly different- they are meant to be pre-prepared scripts for the show, to both introduce and play off our performers. Every line of text will be recited.

Inside of these files, you may use "%ACT" as a variable. It will be replaced with whatever activity was chosen during the Intro. Any line that starts with ". " (note the space!) is viewed as a pause. It should be followed by a number that represents the duration of that pause.

Most of these defaults and settings can be overridden.

```
Options:
  -h, --help            show this help message and exit

  File Options:
    Specify where to get settings for for phrases, intros and outtros.

    -p PHRASES, --phrases=PHRASES
                        Where to load the phrasebank from.
    -i INTRO, --intro=INTRO
                        Where to load the intro-script from.
    -o OUTRO, --outro=OUTRO
                        Where to load the outro-script from.

  Show Settings:
    How to run and manager a show.

    -n, --no-autonag    Disable automated nagging- run interactive only.
    -t NAG_RATE, --nag-rate=NAG_RATE
                        The frequency of nagging, meausred in seconds.
    -j JITTER, --jitter=JITTER
                        How much the timing can drift from the nag-rate, from
                        0-1
    -v VOICE, --voice=VOICE
                        The synthesized voice to use. See system documentation for the "say" command.
```