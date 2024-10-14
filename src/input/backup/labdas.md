


Lamba Expressions









 


Lamba Expressions















The NinjaScript framework utilizes [Lambda expressions](https://msdn.microsoft.com/en-us/library/bb397687.aspx) in various classes, so it is important to fully understand these highly specialized expressions as a NinjaScript developer. Lambda expressions are like anonymous methods, and are often used to define delegates using the [Language Integrated Query (LINQ)](https://msdn.microsoft.com/en-us/library/bb397926.aspx) model. Unlike methods, Lambda expressions contain no access modifiers, return types, or other components of method declaration. Lambdas are created once in the place at which they will be used, rather than being declared outside of the main script logic and re-used multiple times.


 


Syntax
------


Input Parameters =&gt; Expression


 


Examples
--------




| ns |
| --- |
| // Define a new delegate
delegate double newDel(double i);
 
// Use the delegate with a Lambda expression to obtain a price equal to a number of ticks above the current bar's High
newDel myDel = x =&gt; High[0] + (x * TickSize);
 
// Now, we can use the myDel delegate, using a Lambda expression, to quickly refer to a price any number of ticks above the current High
Draw.HorizontalLine(this, "myLine", myDel(3), Brushes.Aqua); |






 
 var lastSlashPos = document.URL.lastIndexOf("/") &gt; document.URL.lastIndexOf("\\") ? document.URL.lastIndexOf("/") : document.URL.lastIndexOf("\\");
 if (document.URL.substring(lastSlashPos + 1, lastSlashPos + 4).toLowerCase() != "~hh") {
 if (document.all) setTimeout(function() {
 nsrInit();
 }, 20);
 else nsrInit();
 }
 
 
 $('.sync-toc').show();
 $('p.crumbs').hide();
 }
 
 
 



