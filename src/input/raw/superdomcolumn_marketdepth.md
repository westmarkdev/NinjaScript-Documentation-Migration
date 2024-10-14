










 


MarketDepth







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?superdomcolumn_marketdepth.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [SuperDOM Column](superdom_column.htm) &gt;
MarketDepth | [Previous page](superdom_column.htm)
[Return to chapter overview](superdom_column.htm)










Definition
----------


Provides Level 2 information for a SuperDOMColumn
-------------------------------------------------


 




|  |
| --- |
| Note:  In order to ensure you are using the same exact MarketDepth subscription that the SuperDOM's main price ladder is using, it is required that you create your own MarketDepth handler.  The NinjaScript Code Wizard was designed to automatically complete this process for you, and an example is outlined at the bottom of this page |



 


Property Value
--------------




|  |  |
| --- | --- |
| SuperDom.MarketDepth | A collection of MarketDepthRows |
| SuperDom.MarketDepth.Asks | A collection of orders on the ask side of the market |
| SuperDom.MarketDepth.Bids | A collection of orders on the bid side of the market |
| SuperDom.MarketDepth.Instrument | The instrument which is being updated |



 


 


Syntax
------


SuperDom.MarketDepth  

SuperDom.MarketDepth.Asks[int idx];  

SuperDom.MarketDepth.Bids[int idx];  

SuperDom.MarketDepth.Instrument



Examples
--------




| ns |
| --- |
| protected override void OnStateChange()
{      
   if (State == State.Active)
   {
     // subscribe to the same market depth events as the primary SuperDOM Price Ladder
     if (SuperDom.MarketDepth != null)
     {
         WeakEventManager<data.marketdepth<ladderrow>, Data.MarketDepthEventArgs&gt;.AddHandler(SuperDom.MarketDepth, "Update", OnMarketDepthUpdate);
     }
   }
   else if (State == State.Terminated)
   {
     // unsubscribe to the same market depth events as the primary SuperDOM Price Ladder
     if (SuperDom == null) return;
 
     if (SuperDom.MarketDepth != null)
     {
         WeakEventManager<data.marketdepth<ladderrow>, Data.MarketDepthEventArgs&gt;.RemoveHandler(SuperDom.MarketDepth, "Update", OnMarketDepthUpdate);            
     }
   }
}
 
// custom market depth handler  
private void OnMarketDepthUpdate(object sender, Data.MarketDepthEventArgs e)
{
   // Print some data to the Output window
   if (e.MarketDataType == MarketDataType.Ask &amp;&amp; e.Operation == Operation.Update)
     Print(string.Format("The most recent ask change is {0} {1}", e.Price, e.Volume));
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
 
 
 



</data.marketdepth<ladderrow></data.marketdepth<ladderrow>