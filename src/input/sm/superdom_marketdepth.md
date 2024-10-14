


MarketDepth









 


MarketDepth















Definition
----------


The OnMarketDepth() method is called and guaranteed to be in the correct sequence for every change in level two market data (market depth) for the underlying instrument.


 


Method Return Value
-------------------


This method does not return a value.


 


Method Parameters
-----------------


 


 


Syntax
------


 


 


 



Examples
--------




| ns |
| --- |
|  | protected override void OnMarketDepth(Data.MarketDepthEventArgs marketDepthUpdate)
{
     if (marketDepthUpdate.MarketDataType == MarketDataType.Ask &amp;&amp; marketDepthUpdate.Operation == Operation.Update)
          // Do something
} |






 
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
 
 
 



