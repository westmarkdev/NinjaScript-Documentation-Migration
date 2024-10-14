










 


PrintTo







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?printto.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [Alert, Debug, Share](alert__debugging_and_sharing.htm) &gt;
PrintTo | [Previous page](print.htm)
[Return to chapter overview](alert__debugging_and_sharing.htm)










Definition
----------


Determines either tab of the NinjaScript [Output window](output.htm) the [Print()](print.htm) and [ClearOutputWindow()](clearoutputwindow.htm) method targets



Property Value
--------------


An enum value representing the target Output Tab.  The default value is PrintTo.OutputTab1. 


 


Possible values are:




|  |  |
| --- | --- |
| PrintTo.OutputTab1 | Output Windows tab named "Output 1" |
| PrintTo.OutputTab2 | Output Windows tab named "Output 2"  |



 


Syntax
------


PrintTo


 


Examples
--------




| ns Setting the default PrintTo in separate scripts (#1) |
| --- |
| protected override void OnStateChange()
{      
   if (State == State.SetDefaults)
   {
     Name = "Sample PrintTo Indicator #1";
     Description = @"Used to Print updates to Output 1";
 
     //Set this scripts Print() calls to the first output tab
     PrintTo = PrintTo.OutputTab1;
   }      
}
 
protected override void OnBarUpdate() 
{                  
   Print("This script will print messages to Output Tab 1");      
} |



 


 




| ns Setting the default PrintTo in separate scripts (#2) |
| --- |
| protected override void OnStateChange()
{      
   if (State == State.SetDefaults)
   {
     Name = "Sample PrintTo Indicator #2";
     Description = "@Used to Print updates to Output 2";
 
     //Set this scripts Print() calls to the second output tab
     PrintTo = PrintTo.OutputTab2;
   }      
}
 
protected override void OnBarUpdate() 
{                  
   Print("This script will print messages to Output Tab 2");      
} |



 


 




| ns Setting PrintTo conditionally in a single script |
| --- |
| protected override void OnMarketData(MarketDataEventArgs marketDataUpdate)
{
   if(marketDataUpdate.MarketDataType == MarketDataType.Ask)
   {
     //Print Ask updates to Output 1
     PrintTo = PrintTo.OutputTab1;
     Print("Ask: " + marketDataUpdate.Price);
   }
   
   else if (marketDataUpdate.MarketDataType == MarketDataType.Bid)
   {
     //Print Bid updates to Output 2
     PrintTo = PrintTo.OutputTab2;
     Print("Bid: " + marketDataUpdate.Price);
   }
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
 
 
 



