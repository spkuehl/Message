parser.py contains a Tweet parsing class that will search a tweet and find all @replies topics and URLs it contains

Topics:
    A topic is a hash followed by a letter followed by zero or more letters and numbers
        ex: #hello2016 is a topic

    A 'topic' containing a non-leading hash is not a topic
        ex: #hello# and hello#hi are not topics

    Any character that is not a letter or integer will signal the end of the topic and not be included
        ex #hello_2016 the topic is only #hello


@reply:
    An @reply is the '@' symbol followed by up to 20 or more letters, integers or underscores any following characters
    are ignored
        ex: @johndoe_3
        ex: @johndoe3.14 = @johndoe3

    An '@reply' containing an '@' or immediately followed by an '@' is not an @reply
        ex: @johndoe@home is not an @reply
        ex: @01234567890123456789@ is not an @reply

    Any character that is not a letter, integer or underscore will signal the end of the @reply and not be included
        ex: @johndoe3 = @johndoe3.for_real

URL:
    A URL is http://t.co/ followed by 10 numbers and integers
        ex: http://t.co/0123456789


Instructor notes:
Using the above, here are some tests I might perform:
is mentioned “franky” => true
is topic “hollywood” => true
is referenced URL “http://cnn.com” => true
is mentioned “george” => false
number of mentions (regardless of who) is 1 => true
number of topics is 1 => true
number of URLs is 1 => true