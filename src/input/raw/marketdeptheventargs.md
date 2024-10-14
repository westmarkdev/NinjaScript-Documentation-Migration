










 


MarketDepthEventArgs







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?marketdeptheventargs.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [OnMarketDepth()](onmarketdepth.htm) &gt;
MarketDepthEventArgs | [Previous page](onmarketdepth.htm)
[Return to chapter overview](onmarketdepth.htm)










Definition
----------


Represents a change in level two market data also known as market depth and is passed as a parameter in the OnMarketDepth() method.   

 


Methods and Parameters
----------------------




|  |  |
| --- | --- |
| Instrument | A Instrument object representing the instrument of the market data |
| IsReset | A bool value representing if a UI reset is needed after a manual disconnect.
 
Note: This is only relevant for columns. Whenever this property is true, the UI needs to be reset. |
| MarketDataType | Possible values are:
MarketDataType.Ask
MarketDataType.Bid |
| MarketMaker | A string representing the market maker id |
| Operation | Represents the action you should take when building a level two book.
Possible values are:
Operation.Add
Operation.Update
Operation.Remove |
| Position | An int value representing the zero based position in the depth ladder. |
| Price | A double value representing the price |
| Time | A [DateTime](http://msdn2.microsoft.com/en-us/library/system.datetime.aspx) structure representing the time |
| ToString() | A string representation of the MarketDataEventArgs object |
| Volume | A long value representing volume |



 


Examples
--------




| ns |
| --- |
| protected override void OnMarketDepth(MarketDepthEventArgs marketDepthUpdate)
{
     // Print some data to the Output window
     if (marketDepthUpdate.MarketDataType == MarketDataType.Ask &amp;&amp; marketDepthUpdate.Operation == Operation.Update)
         Print("The most recent ask change is " + marketDepthUpdate.Price + " " + marketDepthUpdate.Volume);
} |



 


 




|  |
| --- |
| Tip: For an example of how to use IsReset please see \MarketAnalyzerColumns\AskPrice.cs |






 
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
 
 
 



