# Most Active Cookie
- I thoroughly enjoyed this coding challenge. In my last internship, I had previous experience parsing files and loading them into PostgreSQL databases to later build Looker Dashboards (This experience sparked my interest in Data Engineering). Initially, I overthought the problem and made a couple of coding mistakes right away, but the solution became evident after I calmed down and reread the specs. 

## Some important notes about my solution:

* I initially stored the values in a dictionary object and was trying to implement a sorting algorithm for better lookup speed.
** However, after rereading the specs, I realized it would be more efficient to get the values I needed from the first time I read the CSV file. By storing the selected CookieId and Frequency of the Cookie in a dictionary, lookup for the most frequent cookieId would take a time complexity of O(1).

* There is a section of my code that you have to comment out for the unit test file to work; I wrote some logic to ensure the amount of input for the command line argv arguments was correct. 
I would have written some more logic to check if the values in the CSV file were correct before allowing them into my dictionary, but I thought that was outside the spec of the assignment.
I am unfamiliar with building systems, but I will research how to implement them. I appreciate you exposing me to this topic.
When handed an assignment to work on, I love learning how everything works, and I enjoy learning how to improve my code for future functionality.
