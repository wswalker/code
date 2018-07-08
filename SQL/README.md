# SQL Code
This code uses some of my favorite SQL techniques from CTEs to the row_number() function.  

The queries in this folder reference the generic (hypothetical) tables outlined below:

**install**: Record of all installs for an app
* *id*: id for a person
* *timestamp*: 'yyyy-mm-dd hh:mm:ss' format of the time of the install
* *source*: where the install came from

**app_open** Record of all app opens for an app
* *id*: id for a person
* *timestamp*: 'yyyy-mm-dd hh:mm:ss' format of the time of the app open

**ftue**: Also known as the "first time user experience". This contains a record of all of the steps users perform in a ftue.
* *id*: id for a person
* *timestamp*: 'yyyy-mm-dd hh:mm:ss' format of the time of ftue engagement
* *step*: which step of the ftue the user has performed (for this example table: 1 = "started ftue" and 10 = "finished ftue")

**engagement** Contains all engagements (actions in an app) users perform
* *id*: id for a person
* *timestamp*: 'yyyy-mm-dd hh:mm:ss' format of the time of the app open
* *activity*: which feature the user is engaging in (for this table: menu, click, use)

**payment** Contains all logs where users have paid in an app
* *id*: id for a person
* *timestamp*: 'yyyy-mm-dd hh:mm:ss' format of the time of the payment
* *revenue*: $ value of payment in US dollars
