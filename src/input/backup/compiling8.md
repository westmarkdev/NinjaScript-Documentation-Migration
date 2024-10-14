










 


Compiling







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?compiling8.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Developing Strategies](developing_strategies.htm) &gt; [Intermediate - RSI with Stop Loss &amp; Profit Target](intermediate_-_rsi_with_stop_l.htm) &gt;
Compiling | [Previous page](entering_strategy_logic.htm)
[Return to chapter overview](intermediate_-_rsi_with_stop_l.htm)










The strategy code is now complete and needs to be compiled.


 


•If you completed this tutorial via the Strategy Wizard, simply follow the wizard instructions to the end, at which point the strategy will compile.

•If you self coded this tutorial, you can compile this strategy from within the NinjaScript Editor right click menu by selecting the Compile menu item, or by pressing the F5 key.

 


It is important to understand that this process makes the strategy ready for real-time use and will run natively within NinjaTrader directly. It does not run interpreted as many other applications do. This provides you with the highest performance possible. If there are any errors reported during compiling, the error messages will be displayed at the bottom of the NinjaScript Editor.





 
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
 
 
 



