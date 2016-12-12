Title: HowTo: Split MP3s by silence detection using mp3splt
Author: Victor
Date: 2012-04-01
Tags: media, mp3, tools
Category: notes

This is probably the most useful command when it comes to **splitting large mp3 files**. You'll need `mp3splt` (http://mp3splt.sourceforge.net) and you're ready to go:

~~~.shell
mp3splt -s -p th=-40,min=6,rm
~~~

Parameters explanation:  
* `'-s`': silence mode; activate silence detection  
* `'-p`': specify arguments for the silence mode  
* `'th=-40`': threshold level (dB) to be considered silence  
* `'min=6`': minimum number of seconds to be considered as splitpoint  
* `'rm`': remove silence from splitted files

Be sure to have a look at the `manpage`. Happy splitting! 