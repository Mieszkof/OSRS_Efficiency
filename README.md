# OSRS_Efficiency

To Run, simply copy both files to same directory and run efficiency.py

This script determines which training method is most effective for you to do are your current time value. In this case, time value refers to the profit per hour you could be earning doing other activities.

Start by inputting the number of methods you want to compare, followed by your time value.
For each method, input the name of the method, the exp per hour and the cost per exp. Input profitable exp as negative rates.
The script will then tell you which method is most efficient for you to do at your current time value.

How it works:

Example
You want to train crafting, and are chosing between 3 training methods:

Glass Blowing Orbs, at 90k exp/hr and 1.72 gp/exp
Green D'hide Bodies, at 307k exp/hr and 4.24 gp/exp
Battlestaves at 336k exp/hr and 4.98 gp/exp

At a quick glance, glass blowing seems to be the cheapest method for you to train. However, to earn the same exp you'd get from 1 hour of crafting D'hide bodies, you would need to do glass blowing for ~3.4 hours. The cost of crafting D'hide bodies for 1 hour is 1,301,680 gp, and the cost of crafting orbs for 3.4 hours is 529,380 gp. Assuming you trained using orbs, you would save 772,300 gp at the cost of an additional 2.4 hours of training. Effectively, you pay yourself 321,792 gp/hr by crafting orbs rather than d'hide, as the only difference is you spent an extra 2.4 hours training to save 772k.

Assuming you are able to make more than 322k/hr, its more efficient for you to train using the faster method then using the saved timed to earn money doing another activity.

Comparing glass blowing orbs to crafting battlestaves, you determine that crafting battlestaves is more efficient if you can earn more than 400k gp/hr with your time. 

Now let's assume you can earn about 500k gp/hr doing other activities. That would mean that both D'hide bodies and battlestaves are worth it for you to do over glass blowing orbs. To determine which is best between these two, you do another comparsion and find that crafting battlestaves will effectively cost you 2,632k gp/hr for the time saved compared to crafting D'hide bodies.
Since your time value is only 500k gp/hr, you determine that crafting D'hide bodies is your overall best choice, with your current time value.

Using the same example, but with a time value of 250k gp/hr, you would find that crafting glass orbs is your best method of training. This is because both D'hide bodies and battlestaves will cost more than 250k gp/hr for the time saved.

With a time value of 3000k gp/hr, you would find that battlestaves are the most efficient method for training. This is because although both D'hide and battlestaves are better than crafting orbs, assuming you can earn at least 400k gp/hr, the time saved crafting battlestave instead of D'hide will cost you 2632k gp/hr, less than the 3000k gp/hr you can earn doing other activites.
