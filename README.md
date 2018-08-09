# reddit_code_benchmark

Ok so this blog claimed there were performance gains

https://www.tutorialdocs.com/article/7-habits-to-improve-python-programs.html

In this thread it was mentioned that benchmarks would be nice:

https://www.reddit.com/r/Python/comments/95rzyb/7_habits_to_improve_the_performance_of_python/

Turns out that's a valid concern, because one out of five examples provided did not support the claim of the blog author.

>The search speed of mappings (such as dict, etc.) is much faster than conditional statements (such as if, etc.). And there is no select-case statement in Python.

Isn't supported by the example provided.

Supposedly #5 needs less memory, I just timed it.

Here are my numbers:

2.1
0.01724725399981253
0.016332330999830447
0.012701691000074788
2.2
0.04615198600004078
0.03609853400030261
3
0.1179120030001286
0.14423205200000666
4
0.022899751999830187
0.05500739200033422
5
0.9053581710004437
1.042141163999986
