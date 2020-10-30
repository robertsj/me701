"""
Module to convert pandoc html output with mathjaxto a Canvas equipped version
"""

import sys
import re
import urllib.parse
import os

def encodemath(s):
    """Given a LaTeX blurb, return the URI string in Canvas form.
    """
    single = urllib.parse.quote(s, safe='()')
    double = urllib.parse.quote(single, safe='()')
    return double

def makeimg(s):
    """ Make img from given LaTeX snipped."""
    
    e = encodemath(s)

    tmpl = """<img 
class="equation_image" 
title="{0}" 
src="/equation_images/{1}" 
alt="LaTeX: {0}" 
data-equation-content="{0}" 
/>"""
    return tmpl.format(s, e)
    

def find_inline_equations(s):
    """Given a string, find all $...$ pairs and return matched strings.
    """

    pattern = r'(?P<all><span class="math inline">\\\((?P<latex>.+?)\\\)</span>)'
    return re.findall(pattern, s)
    
def find_display_equations(s):
    """Given a string, find all $...$ pairs and return matched strings.
    """

    pattern = r'(?P<all><span class="math display">\\\[.*?\n(?P<latex>(?:.*?\n)+?).*?</span>)'
    return re.findall(pattern, s)
   
def convert(s):
    """ Take full markdown string and swap all math spans with img.
    """
    
    matches = find_inline_equations(s) + find_display_equations(s)
    
    for match in matches:
        
        full = match[0]
        latex = match[1]
        img = makeimg(latex)
        s = s.replace(full, img)
        
    return s
    

test = """<p>A discrete <em>random variable</em> <span class="math inline">\(X\)</span> can have only the discrete values <span class="math inline">\(X_1, X_2, X_3, \ldots, X_N\)</span>. Any of these values can be observed when a <em>sample</em> of <span class="math inline">\(X\)</span> is made. The <em>frequency</em> of observing each value of <span class="math inline">\(X\)</span> is governed by the <em>probability mass function</em> (pmf) <span class="math inline">\(f(X=x_i)\)</span> that must satisfy</p>
<p><span class="math display">\[lala
   f_i = f(X_i) \geq 0 \, i = 1 \leq x \leq N \, .
   g_i = x^2
\]</span></p>
<p>where</p>
<p><span class="math display">\[
   \sum^N_{i=1} f_i = 1 \, .
\]</span></p>
<p><strong>Exercise</strong>: Turn to your neigbor and expla"""

def canvas(in_file, out_file):
    
    assert os.path.exists(in_file)

    pandoc = 'pandoc      --mathjax   {} -o tmp.html'.format(in_file)
    
    assert os.system(pandoc) == 0
    
    s = None
    with open('tmp.html', 'r') as f:
        s = f.read()
        s = convert(s)
    
    assert s
    
    with open(out_file, 'w') as f:
        f.write(s)
    
    return
    
    
        


if __name__=='__main__':
    
    # Ensure a file is given for conversion
    assert(len(sys.argv) == 3)
    
    # Ensure that pandoc is available
    assert os.system('which pandoc') == 0

    canvas(sys.argv[1],  sys.argv[2])
   
    
