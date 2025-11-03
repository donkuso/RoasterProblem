**Reflection**
The code went well! I really enjoyed this real world example and I could easily wrap my head around the problem at hand. 
The thing that I struggled the most with was how to integrate the required methods. It made sense to me to use OOP and classes. The integration of inheritance and polymorphism required further understanding of the topic (https://www.geeksforgeeks.org/python/inheritance-in-python/). The linked list was also hard to implement in this problem. It required abstract thinking. It wasn't necessarily used in the main function of the program, but the integration furthered my understanding of the concept. 

**Non-Technical Explanation**
The program is designed to help a client who is a warehouse manager for a coffee roasting company. In this case, there are three different beans used and three different blends being made that have a unique mix of those beans.

The program works so that the client can decide if they want to prioritize profit or reduce waste of a certain bean. The program then looks at what beans are present and which blends can be made. Using the identified strategy (profit or limit waste), the program chooses the best batch to be made one at a time. After each batch is made, it updates the warehouse to see whats left and continues until it can't make anymore batches. 

**In Defense of the Approach**
This approach is straightforward, transparent, and flexible. The recursive structure makes the logic easy to follow: a blend is made, the warehouse is updated, and it continues until the warehouse is empty/no more blends can be made. 
The code is also modular, which allows responsibilities to be seperated and also easy to follow. Since it is modular, new blends, beans, and strategies can be added without changing the core logic. 

Good results were distinguished with logic: 
    a good result for the income strategy meant that the total income was as high as possible
    a good result for the minimize-leftover strategy meant that the target bean had the smallest possible leftover amount while still maintaining logical use of the other beans

**Self grade**
I would give myself a 95/100.
I’m really proud of how organized and readable my code turned out, especially with the use of inheritance, polymorphism, lambdas, and a linked list. I ran into some tricky parts with debugging and recursion, but I worked through them, and everything functions as intended. The only small deduction might be for some inefficiency in how the recursive calls are structured, but conceptually, I feel confident in the design and implementation.

**Analysis Question**
Using the warehouse quantities and recipe ratios from the given example, I used my Income-focused Strategy to simulate which additional purchase would lead to the highest total income.
After running the simulation, the Rwanda purchase produced the highest income overall. The reason is that Rwanda beans tend to be a limiting factor in many of the blends — they appear frequently in the recipes and often run out first. Adding more Rwanda beans allows more high-value blends to be produced before the warehouse runs out of ingredients.