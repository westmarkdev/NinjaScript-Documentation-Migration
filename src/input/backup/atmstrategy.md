










 


AtmStrategy







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?atmstrategy.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
AtmStrategy | [Previous page](alert_rearmalert().htm)
[Return to chapter overview](add_on.htm)










AtmStrategy contains properties and methods used to manage [ATM Strategies](advanced_trade_management_atm.htm). When working with an [AtmStrategySelector](atmstrategyselector.htm), selected objects can be case to AtmStrategy to obtain or change their properties.


 




|  |
| --- |
| Notes: 
1. For a complete, working example of this class in use, download framework example located on our [Developing AddOns Overview](developing_add_ons.htm)
2. For more information on working with the ATM strategies programmatically in general, please see the [Using ATM Strategies](using_atm_strategies.htm) section. |





Example
-------




| ns |
| --- |
| // Using AtmStrategy to handle user selections in an ATM Strategy Selector
myAtmStrategySelector.SelectionChanged += (o, args) =&gt;
{
   if (myAtmStrategySelector.SelectedItem == null)
       return;
   if (args.AddedItems.Count &gt; 0)
   {
       // Change the selected TIF in a TIF selector based on what is selected in the ATM Strategy Selector 
       NinjaTrader.NinjaScript.AtmStrategy selectedAtmStrategy = args.AddedItems[0] as NinjaTrader.NinjaScript.AtmStrategy;
       if (selectedAtmStrategy != null)
       {
           myTifSelector.SelectedTif = selectedAtmStrategy.TimeInForce;
       }
   }
}; |






 
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
 
 
 



