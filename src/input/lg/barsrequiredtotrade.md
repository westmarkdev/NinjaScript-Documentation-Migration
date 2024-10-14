










 


BarsRequiredToTrade







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?barsrequiredtotrade.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Strategy](strategy.htm) &gt;
BarsRequiredToTrade | [Previous page](getatmstrategyuniqueid.htm)
[Return to chapter overview](strategy.htm)










Definition
----------


The number of historical bars required before the strategy starts processing order methods called in the [OnBarUpdate()](onbarupdate.htm) method. This property is generally set via the UI when starting a strategy.


 




|  |
| --- |
| Note:  In a multi-series strategy this restriction applies only for the primary Bars object.  This means your can run into situations where the primary bars required to trade have been reached, but the additional bars required have not. Should your strategy logic intertwine calculations across different Bars objects please ensure all Bars objects have met the BarsRequiredToTrade requirement before proceeding. This can be done via checks on the [CurrentBars](currentbars.htm) array. |



 


 


Property Value
--------------


An int value representing the number of historical bars.  Default value is set to 20.


 




|  |
| --- |
| Warning:  This property should ONLY bet set from the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



 


 


Syntax
------


BarsRequiredToTrade


 




|  |
| --- |
| Tip:  When working with a multi-series strategy, real-time bar update events for a particular Bars object are only received when that Bars object has satisfied the BarsRequiredToTrade requirement. To ensure this requirement is met, please use the CurrentBars array. |



 



Examples
--------




| ns Setting the default BarsRequiredToTrade value |
| --- |
| protected override void OnStateChange() 
{
     if (State == State.Configure)
     {
         BarsRequiredToTrade = 20;
     }
} |



 


 




| ns | Checking BarsRequiredToTrade againt a CurrentBars array |
| --- | --- |
|  | protected override void OnStateChange() 
{
   if (State == State.SetDefaults) 
   {
     BarsRequiredToTrade = 20;
   }
   else if (State == State.Configure) 
   {
     // add 30 minute series for calcuation logic
     AddDataSeries(BarsPeriodType.Minute, 30);
   }
}
 
protected override void OnBarUpdate() 
{
   // do not process order logic until bars required to trade is met 
   // for both primary and 30-minute series have reached their bars required to trade
   if (CurrentBars[0] &lt; BarsRequiredToTrade || CurrentBars[1] &lt; BarsRequiredToTrade)
     return;
 
   //order logic
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
 
 
 



