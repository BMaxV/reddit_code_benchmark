# reddit_code_benchmark

Ok so this blog claimed there were performance gains

https://www.tutorialdocs.com/article/7-habits-to-improve-python-programs.html

In this thread it was mentioned that benchmarks would be nice:

https://www.reddit.com/r/Python/comments/95rzyb/7_habits_to_improve_the_performance_of_python/

Turns out that's a valid concern, because two out of five examples provided did not support the claim of the blog author.

The generator is worse than the list comprehension and the dict loopup/assignment is worse than if/else.
