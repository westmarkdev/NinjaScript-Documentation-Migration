










 


Compiling







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?compiling.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Developing Indicators](developing_indicators.htm) &gt; [Beginner - Using price variables](beginner_-_using_price_variabl.htm) &gt;
Compiling | [Previous page](entering_calculation_logic.htm)
[Return to chapter overview](beginner_-_using_price_variabl.htm)










The indicator code is now complete and needs to be compiled. You can compile this indicator by selecting the Compile menu item from within the NinjaScript Editor Right Click, by clicking the Compile icon on the toolbar at the top of the window, or by pressing the F5 key on your keyboard. It is important to understand that this process makes the indicator ready for real-time use natively within NinjaTrader. It does not run as interpreted code, as many other applications do, but rather as a C# assembly. This provides you with the highest performance possible. If there are any errors reported during compiling, the error messages will be displayed at the bottom of the NinjaScript Editor.





 
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
 
 
 



