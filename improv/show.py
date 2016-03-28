import subprocess
from time import sleep, time
import re
import threading
import random
voice = "Vicki"
phrasefile = "phrases.txt"
introfile = "intro.txt"
outrofile = "outro.txt"
activities = ["drinking", "playing sports", "having sex",
    "going on a date", "seeing a doctor", "riding the bus",
    "being useless"]

class IntroOutro:
    def __init__(self, show, intro_lines):
        self.show = show
        self.intro = intro_lines

    def __call__(self, actname):
        act = re.compile(r'%ACT')
        for l in self.intro:
            if l.startswith(". "):
                sleep(float(l.split(" ")[1]))
            else:
                l = act.sub(actname, l)
                self.show.say(l)


class Show:
    def __init__(self, phrases):
        self.phrases = phrases

    def say(self, phrase):
        print(phrase)
        subprocess.call(["say", "-v", voice, phrase])

    def say_rand(self):
        self.say(random.choice(self.phrases))

class AutoNag:
    def __init__(self, show, countdown=100, jitter=0.0):
        self.run = True
        self.show = show
        self.countdown = countdown
        self.default_interval = countdown
        self.jitter = jitter
        self.th = threading.Thread(None, lambda : self.hotloop())
        self.th.start()

    def __jitter__(self):
        return (1 - self.jitter * 2) * self.countdown * random.random()

    def hotloop(self):
        while(self.run):
            self.countdown -= 1
            if (self.countdown <= 0):
                self.show.say_rand()
                self.countdown = self.default_interval + self.__jitter__()
            sleep(1.0)

    def stop(self):
        self.run = False
        self.th.join()


def load_data(sourcefile):
    with open(sourcefile, "r") as f:
        return f.readlines()

def parse(inp, show, nag, nag_reflex=15):
    if inp.isnumeric():
        show.say(phrases[int(inp)])
    elif inp == "c":
        show.say_rand()
    else:
        show.say(inp)
    nag.countdown += nag_reflex

def main(**kwargs):
    phrases = load_data(kwargs["phrases"])
    introtext = load_data(kwargs["intro"])
    outrotext = load_data(kwargs["outro"])
    show = Show(phrases)
    nag = AutoNag(show, kwargs["nag_rate"])
    intro = IntroOutro(show, introtext)
    outro = IntroOutro(show, outrotext)
    act = random.choice(activities)
    intro(act)
    inp = ""
    while True:
        inp = input("> ")
        if inp == "q":
            break
        parse(inp, show, nag, 24)
    nag.stop()
    outro(act)