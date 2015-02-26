````
                  ██                     ██                 
  █████          ░░                     ░██                 
 ██░░░██ ██    ██ ██ ██████████        ██████  ██████       
░██  ░██░██   ░██░██░░██░░██░░██ █████░░░██░  ██░░░░██ █████
░░██████░░██ ░██ ░██ ░██ ░██ ░██░░░░░   ░██  ░██   ░██░░░░░ 
 ░░░░░██ ░░████  ░██ ░██ ░██ ░██        ░██  ░██   ░██      
  █████   ░░██   ░██ ███ ░██ ░██        ░░██ ░░██████       
 ░░░░░     ░░    ░░ ░░░  ░░  ░░          ░░   ░░░░░░        
                           ██                        
                          ░██                        
 ██   ██  █████   ██████  ░██  ██████  ██████  ██████
░░██ ██  ██░░░██ ██░░░░██ ░██ ██░░░░██░░██░░█ ██░░░░ 
 ░░███  ░██  ░░ ░██   ░██ ░██░██   ░██ ░██ ░ ░░█████ 
  ██░██ ░██   ██░██   ░██ ░██░██   ░██ ░██    ░░░░░██
 ██ ░░██░░█████ ░░██████  ███░░██████ ░███    ██████ 
░░   ░░  ░░░░░   ░░░░░░  ░░░  ░░░░░░  ░░░    ░░░░░░  

````
Heavily based on [a script from sleepanarchy.com](http://sleepanarchy.com/p/H84iMD/raw)

# What does it do? #
Extracts colors in hex format from (g)vim themes. The output is formatted in the **X resources** convention.

### Sample here: ###
````
*.foreground: #f8f8f2
*.background: #282a36
*.cursorColor: #f8f8f2
*.color0: #f8f8f2
*.color1: #64666d
*.color2: #8be9fd
*.color3: #ff79c6
*.color4: #ff79c6
*.color5: #f8f8f2
*.color6: #50fa7b
*.color7: #f1fa8c
*.color8: #ff79c6
*.color9: #f1fa8c
*.color10: #ff79c6
*.color11: #ff79c6
*.color12: #bd93f9
*.color13: #bd93f9
*.color14: #bd93f9
````

There are also functions for printing the output as a flat list of colors (see ``printout`` function)

# Logic #
The **vimGroups** variable defines the which [highlight groups](http://vimdoc.sourceforge.net/htmldoc/syntax.html) are extracted and their priority.

The **normal** group is treated separately and the Normal background and foreground color become the *foreground* and *background* property (not just *colorN*)

# Usage #
Run with python3 and point to a theme file.
``python3 gvim-to-xcolors.py ~/.vim/colors/dracula.vim``

# Works well with #
I use it to generate i3wm colorschemes in conjunction with Charles Leifer's [themer](http://charlesleifer.com/blog/using-python-to-generate-awesome-linux-desktop-themes/)
