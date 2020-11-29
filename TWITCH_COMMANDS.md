**MAIN COMMANDS**

The main commands recommended for use during runs. They can definitely have issues, but they've been tested the most and are generally expected to work.

[!blindtravel](https://raw.githubusercontent.com/Sharpieman20/Sharpies-Speedrunning-Tools/main/commands/!blindtravel)

This should be used when you want to build another portal in the nether **before** throwing any eyes.

Whenever you want to use it, press f3+c, pause, and then type !blindtravel and paste your clipboard into chat.

This command is tuned for PB pace, WR pace, top 10% stronghold luck runs. If you want a command more suited to the average case, check out !safeblind below.

**Rings**: Anywhere up to outside the third ring. Does not currently work for fourth ring.


[!blindcalc](https://raw.githubusercontent.com/Sharpieman20/Sharpies-Speedrunning-Tools/main/commands/!blindcalc)

This is the visual version of !blindtravel. It's useful to help understand how it works.


[!educatedtravel](https://raw.githubusercontent.com/Sharpieman20/Sharpies-Speedrunning-Tools/main/commands/!educatedtravel)

This should be used when you want to build another portal in the nether **after** throwing an eye.

Whenever you want to use it, throw an eye, stand still, put your mouse directly over the eye, press f3+c, pause, and then type !educatedtravel and paste your clipboard into chat.

**Rings**: Inside first ring. Potentially works outside first ring and inside second ring, but these are currently experimental


[!educatedcalc](https://raw.githubusercontent.com/Sharpieman20/Sharpies-Speedrunning-Tools/main/commands/!educatedcalc)

This is the visual version of !educatedtravel. It's useful to help understand how it works, or for scenarios 


[!advancedcalc](https://raw.githubusercontent.com/Sharpieman20/Sharpies-Speedrunning-Tools/main/commands/!advancedcalc)

The latest Advanced Calculator version. This is what all the other commands and calculators are based on.

Most useful for educated travel guessing stronghold location from one throw.



**EXPERIMENTAL COMMANDS**

These commands can work, but they have potential issues. Usable in actual runs, but heavy caution should be exercised when using them.


[!safeblind](https://raw.githubusercontent.com/Sharpieman20/Sharpies-Speedrunning-Tools/main/commands/!safeblind)

This is a blind travel command tuned more for easy-to-traverse nethers and for making a run completable in a reasonable amount of time.

If you're in a situation where you just need an okay blind travel (around 800-1200 blocks), then this command is going to be more reliable at getting you that than !blindtravel.

However, the downside is that you will often run too far in the nether to build your portal, and lose time.

Be careful of this command in spectator mode! It **will** give you better /locate distances than !blindtravel on average, but in real runs you have to go to the spot to build the portal, not simply /tp there!


[!educatedtravel](https://raw.githubusercontent.com/Sharpieman20/Sharpies-Speedrunning-Tools/main/commands/!educatedtravel)

Educated Travel beyond the exact inside of the first ring is experimental.

The workflow that best works for this command is to first use !doubletravel to get a spot to make your portal inside the second ring.

After you exit the nether and do your eye throw, !educatedtravel should do a pretty good job of getting you to the right spot in the nether to build a second portal.

**Rings**: Inside second ring.


[!doubletravel](https://raw.githubusercontent.com/Sharpieman20/Sharpies-Speedrunning-Tools/main/commands/!doubletravel)

This command can give you a spot inside the second ring to do an eye throw.

After doing this, usually you'd want to use !educatedtravel. The experimental !educatedtravel description goes more in-depth on this.



**SCUFFED COMMANDS**

These commands are NOT RECOMMENDED for use during runs. They are for theoretical testing purposes.

[!calculatedtravel](https://raw.githubusercontent.com/Sharpieman20/Sharpies-Speedrunning-Tools/main/commands/!calculatedtravel)

This should be used when you want to build another portal in the nether **after** throwing an eye.

Whenever you want to use it, throw an eye, stand still, put your mouse directly over the eye, press f3+c, pause, and then type !calculated and paste your clipboard into chat.

It uses the same concepts as the 8,8 rule and !onethrow to attempt to guess the stronghold from a single throw. 

**Warning**: This command is not very accurate, it might be worse than !educatedtravel on average, but it has a better chance of getting you extremely close to the stronghold.

**Rings**: Inside first ring only.


[!onethrow](https://raw.githubusercontent.com/Sharpieman20/Sharpies-Speedrunning-Tools/main/commands/!onethrow)

Uses the 8,8 rule to try and guess the stronghold's location from a single throw.

The closer you are to the stronghold, the more likely this command is to guess correctly.

**Rings**: Any ring.


**TODO**

!customblind

Also incorporates the angle you're facing. This is useful if there is some rough terrain.

Look in the direction that you want to go, press f3+c, pause, and then type !customblind and paste your clipboard into chat.

!customblindcalculator

This is the visual version of !blindtravel. It's useful to help understand the tradeoff of the angle and if you want to play around with the angle.