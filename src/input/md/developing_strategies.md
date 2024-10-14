










 


Developing Strategies







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?developing_strategies.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt;
Developing Strategies | [Previous page](developing_outside_of_the_ninj.htm)
[Return to chapter overview](educational_resources.htm)










NinjaScript allows you to develop custom strategies in rapid time by using over 100 built-in system indicators, 3rd party indicators or [custom indicators](developing_indicators.htm). NinjaScript strategies are compiled and run natively within the NinjaScript application providing the highest performance possible.


 


Please take the time to review this section including the [Strategy Development Process](the_strategy_development_process.htm).


 


Prior to running strategies live, please be sure to review the sections about [Strategy Position vs. Account Position](strategy_position_vs_account_p.htm) and [Syncing Account Positions](syncing_account_positions.htm).


 


Tutorial Descriptions
---------------------


All internal NinjaScript indicators and sample strategies come with full source code and can be viewed within the NinjaScript [Editor](editor.htm). Please review the tutorials within this section for detailed walk throughs of custom strategy development.


 




|  |
| --- |
| ›[Level 1](beginner_-_simple_ma_cross_ove.htm) - Simple MA Cross Over (Demonstrates strategy construction by wizard and scripting)›[Level 2](intermediate_-_rsi_with_stop_l.htm) - RSI with Stop Loss &amp; Profit Target (scripting only) |






 
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
 
 
 



