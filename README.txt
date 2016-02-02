Use OOD to process twitter-like messages.
Process one message at a time.
Find @reply #topic and urls.com in a message.
Test your code for all possible options (unit tests).




Instructor notes:



Using the above, here are some tests I might perform:
is mentioned “franky” => true
is topic “hollywood” => true
is referenced URL “http://cnn.com” => true
is mentioned “george” => false
number of mentions (regardless of who) is 1 => true
number of topics is 1 => true
number of URLs is 1 => true



Grading Criteria

This is a quick checklist of how you’re going to be graded for this assignment.
significant number of commits for your project, preferably daily
well-organized code
appropriate documentation, especially to clarify your understanding of the requirements
more unit tests than actual code
good use of classes and objects and library classes (instead of reinventing your own), especially when it comes to core data structures (lists, tables/dictionaries, string handling, etc.)
