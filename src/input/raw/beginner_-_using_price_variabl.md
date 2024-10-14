










 


Beginner - Using price variables







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?beginner_-_using_price_variabl.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Developing Indicators](developing_indicators.htm) &gt;
Beginner - Using price variables | [Previous page](using2.htm)
[Return to chapter overview](developing_indicators.htm)










 




|  |
| --- |
| Using Price Variables Overview
In this beginner level tutorial we are going to build a custom indicator that searches for a candlestick formation in which the closing price of a specified bar is greater than the closing price of the bar before it. This indicator will show you how to access price variables and use a conditional operator.
 
› [Set Up](set_up4.htm)› [Entering Calculation Logic](entering_calculation_logic.htm)› [Compiling](compiling.htm)› [Using](using.htm) |






 
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
 
 
 



