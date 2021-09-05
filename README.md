chatx-search
============

The Stack Overflow / Stack Exchange chat system
exposes a simple RSS interface to its search functionality.
This is fairly limited (it doesn't give you a lot of control
over the search expression or how far back to search etc)
but works nicely if your question is
"where was this mentioned recently"?

This project contains a few crude Python scripts
based on the [feedparser](https://pypi.org/project/feedparser/) module.
Several of them are very specific to Charcoal Test,
but the core functionality should be easy to extend
for other purposes as well if you should want to.

The central module here is `rss_search.py`
and the others are simple wrappers which parse out
results of a particular type.
See the source for details.


License
------

Licensed under either of

 * Apache License, Version 2.0 <!-- , ([LICENSE-APACHE](LICENSE-APACHE) -->
   <!-- or --> 
   http://www.apache.org/licenses/LICENSE-2.0)
 * MIT license <!-- ([LICENSE-MIT](LICENSE-MIT) -->
   <!-- or -->
   http://opensource.org/licenses/MIT)

at your option.

By submitting your contribution for inclusion in the work
as defined in the [Apache-2.0 license](https://www.apache.org/licenses/LICENSE-2.0),
you agree that it be dual licensed as above,
without any additional terms or conditions.
