### Run the Program

you can run the program by running

######>> python coffee_shop.py 
in the terminal

Python Version is 3.4

----
### Input Files

* `input.json` is the input file that was given
* `small.json` is the input file that I made to test some possible edge cases

----
### Output Files

* `output.json` is the output for the FIFO solution
* `output_better.csv` is the output to look at crunch times and possible optimizations for scalability
* `ouput_fifo_profit.json` is the total amount of profit they make in a day with the FIFO solution
* `output_for_money.json` is the improved profit algorithm

run the program to output these files.

----
# PART 1

----
### FIFO Solution

`fifo_solution()`

I decided to use two FIFO queues labeled `Q1` and `Q2` for simplicity where `Q1` was a queue of all drinks barista 1 had to brew and `Q2` was a queue of all drinks barista 2 had to brew. I also used two counters labeled `barista_1` and `barista_2` that recorded their updated start times of brewing a specific drink. 

for each order, I compared the start times of `barista_1` and `barista_2` on their current drink. Which ever barista had a smaller start time meant that that barista was going to finish making her current drink sooner than the other barista. So I appended the incoming order to that barista's queue and increased the start time of the assigned barista by how long it took to brew the new order.

Because another condition of the problem was that the barista can only make drinks while the starttime is less than or equal to the `DAY` (which in this case is a 100), once the two counters both exceeded that limit, the baristas no longer took further orders.

Then once I had all the information, I combined the two queues sort of like the sorting part of mergesort and outputted that as a json format. 


----
### Better Algorithm

`better_alg()`

I contemplated for a bit on which business need to optimize: throughput, shortest avg customer wait time, most profit made. 

The FIFO solution is what would occur in real life. Unlike a CPU scheduler where it alots each task a quantum and switches back and forth between tasks, in this example we are not given any further info that the barista can do that. For example while the latte machine is brewing which doesn't require effort from the barista, she can take the next order for example "tea" and start boiling hot water since the water boiler and latte machines are two different machines. Then once the latte finishes, she can stop working on making the tea, deliver the latte and resume working on the tea. 

I personally believe that excellent customer service is the most important aspect of the business to optimize. In an era where people no longer buy products but rather the access to use their service (Spotify, Uber, Airbnb, Dropbox) having excellent customer service is what keeps customers around and increase the brand name. 

----
### Engineering Decision

In this example excellent customer service would be a shorter wait time and better taste in the drink. However we are not given any metric regarding the taste of the drink. Calculating the shortest average waiting time wouldn't be possible technically in real life. I tried to think of way to have an average shorter wait time but I realized that this was very hard to do since crunch time (times like lunch or dinner where there are more customers) was a bottleneck for all future orders. So in here I broke up orders into `windows` of 4 ticks. 

For example where each entry is labeled `order_id`, `order_time`, `drink`, `brew time per drink`, `profit per drink`

```
[
	"(1, 7, 'latte', 4, 3)",
	"(2, 7, 'affogato', 7, 5)",
	"(3, 8, 'latte', 4, 3)",
	"(4, 8, 'affogato', 7, 5)",
	"(5, 9, 'affogato', 7, 5)",
	"(6, 10, 'tea', 3, 2)",
	"(7, 10, 'tea', 3, 2)",
	"(8, 11, 'affogato', 7, 5)",
	"(9, 11, 'latte', 4, 3)"
]
[
	"(10, 15, 'latte', 4, 3)"
]
```

There are nine orders within the first `window` of 4 ticks from time 7 to 11. Whereas there is only one order in the next `window` from time 12 to 16.

The windows that had more orders were bottlenecks to the system and I had trouble trying to reduce the average waiting time as long as these bottlenecks were in place as they would further delay future orders.

Possible ways to scale this to reduce the bottleneck is as follows.

tldr I did not continue solving this problem but optimized another aspect instead for part 2

----
### Scalability 

Possible ways to scale is to have more baristas so that they can take more orders. Let the baristas operate like a CPU scheduler so that if they're not specifically working on a drink but instead a machine is doing a specific task that frees up the barista, then let her work on the next drink. 

#####Vertical Scaling: 
Buy a bigger machine. So you operate in a batch. Instead of boiling small bit of water everytime to make tea, boil a lot at once in a bigger machine that is insulated and serve tea instantly for the next few orders

#####Horizontal Scaling:
Buy more machines. Make 2 teas at once.

----
# PART 2

----
### Maximizing Profit

`for_money()`

The idea is to maximize profit at the expense of customer service. 

```
	it takes 3 ticks to make $2 on tea for $0.66 per tick.
	it takes 4 ticks to make $3 on latte for $0.75 per tick.
	it takes 7 ticks to make $5 on affogato for $0.71 per tick.
```

You make the most profit by preparing a drink where the cost per tick is higher. You first iterate through all the orders and put the drinks in their respective backlogs (sort of like storage). Then you iterate through this list again but this time placing the orders to the barista's queues. One difference between this algorithm and the FIFO algorithm is that we want to prioritize the higher cost per tick since that is how we make more profit. So we prioritize making latte over affogato over tea. So if there is an order for tea, affogato, and latte in the backlog, we want our barista to make the latte first. We stop taking orders when all the orders in the backlog are finished or the day has gone.


`get_time()`

What this function ensures is that even though we want to prioritize latte over affogato over tea we need to get the drink within the barista's time. For example after the forloop we will have orders in the backlog. But what if barista_1 finishes making her current drink at tick = 15 and what we have in the backlog is (tea, starttime = 14), (latte, starttime = 17), (affogato, starttime=18). In this example even if there is latte in the backlog, we want the barista to make the tea because we don't want her to wait doing nothing.

On a more mathematical explanation. you earn $2 for 3 ticks for tea for $0.66 per tick and $3 for 4 ticks for latte for $0.75 per tick. However if the barista does nothing for a tick even if she makes a latte, she would make $3 for 5 ticks (accounting for the idle tick) for the latte for $.60 per tick which is less than just making the tea $0.66 per tick if the order has already been made before she completes her current drink.


The `fifo_solution_for_profit()` returns how much profit they make using the FIFO algorithm from part 1. In my two test cases, the optimized algorithm will result in equal or more profit than the FIFO algorithm.


NEVER DO THIS IN REAL LIFE. It will hurt the business in the long run since the customers who ordered tea will never get their tea while the baristas have orders for latte and affogato.

###unittest
----

I only unittested the helper functions. not the main functions for the algorithms. This is because the json file is read inside the main functions and the unittest will fail if developers mess around with the input json file. 


