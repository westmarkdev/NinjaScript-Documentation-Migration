










 


Creating the Strategy via Self Programming







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?creating_the_strategy_via_self.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Developing Strategies](developing_strategies.htm) &gt; [Beginner - Simple MA Cross Over](beginner_-_simple_ma_cross_ove.htm) &gt;
Creating the Strategy via Self Programming | [Previous page](creating_the_strategy_via_the_.htm)
[Return to chapter overview](beginner_-_simple_ma_cross_ove.htm)










If you have not done so already, press the "Unlock Code" button within the wizard to launch the NinjaScript Editor.


 


The [OnBarUpdate()](onbarupdate.htm) method is called for each incoming tick or on the close of a bar (user defined) when performing real-time calculations. Therefore, this is the main method called for strategy calculation and we will use this method to enter the script that check for entry and exit conditions.


 


The Entry and Exit Condition
----------------------------


Enter the code contained within the OnBarUpdate() method in the image below into the OnBarUpdate() method in the NinjaScript Editor:


 




| ns |
| --- |
| protected override void OnBarUpdate()
{
   if (CrossAbove(SMA(Fast), SMA(Slow), 1))
     EnterLong();
   
   if (CrossBelow(SMA(Fast), SMA(Slow), 1))
     EnterShort();
} |



 


Translated into English, the code contained within the OnBarUpdate() method above reads:


 


if the fast simple moving average crosses above the slow simple moving average within the last bar, go long


 


if the fast simple moving average crosses below the slow simple moving average within the last bar, go short


 


To accomplish this we used the following methods:


 


[CrossAbove()](crossabove.htm) - Checks for a cross above condition and returns true or false   

[CrossBelow()](crossbelow.htm) - Checks for a cross below condition and returns true or false   

[SMA()](moving_average_-_simple_sma.htm) - Returns the value of a simple moving average   

[EnterLong()](enterlong.htm) - Enters a market order long   

[EnterShort()](entershort.htm) - Enters a market order short





 
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
 
 
 



