










 


PropagateIntervalChange()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?propagateintervalchange().htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt;
PropagateIntervalChange() | [Previous page](propagateinstrumentchange().htm)
[Return to chapter overview](add_on.htm)










Definition
----------


In an [NTWindow](ntwindow.htm), PropagateIntervalChange() sends an interval to other windows with the same Interval Linking color configured. 


 




|  |
| --- |
| Notes: 
1.A public Instrument property must be defined in order to use PropagateInstrumentChange(), as in the example below2.For a complete, working example of this class in use, download framework example located on our [Developing AddOns Overview](developing_add_ons.htm) |




Example
-------




| ns |
| --- |
| // This custom method will be fired when an interval selector in a custom NTTabPage changes intervals
private void OnIntervalChanged(object sender, BarsPeriodEventArgs args)
{
   if (args.BarsPeriod == null)
       return;
 
   PropagateIntervalChange(args.BarsPeriod);
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
 
 
 



