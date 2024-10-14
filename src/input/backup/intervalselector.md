










 


IntervalSelector







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?intervalselector.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [NinjaTrader Controls](controls.htm) &gt;
IntervalSelector | [Previous page](instrumentselector.htm)
[Return to chapter overview](controls.htm)










Definition
----------


IntervalSelector is as a UI element users can interact with for selecting intervals. This can be used with interval linking between windows.     


 


Events and Properties
---------------------




|  |  |
| --- | --- |
| Cleanup() | Disposes of the IntervalSelector (Note: calling the [NTTabPage base.Cleanup()](nttabpage_cleanup.htm) is sufficient to clean up this control) |
| Interval | A BarsPeriod representing the interval currently selected |
| IntervalChanged | Event handler for when the interval changed |



 


 


Examples
--------


This example demonstrates how to use the interval selector and properly link its behavior to windows linking.


 




| C# |
| --- |
| private IntervalSelector   intervalSelector;        
 
private DependencyObject LoadXAML()
{
     // Note: pageContent (not demonstrated in this example) is the page content of the XAML
 
     // Find the Interval selector
     intervalSelector = LogicalTreeHelper.FindLogicalNode(pageContent, "intervalSelector") as IntervalSelector;
     if (intervalSelector != null)
          intervalSelector.IntervalChanged += OnIntervalChanged;
     
}
 
// This method is fired when our interval selector changes intervals
private void OnIntervalChanged(object sender, BarsPeriodEventArgs e)
{
     if (e.BarsPeriod == null)
         return;
}
 
/* IIntervalProvider member. Required if you want to use the interval linker mechanism on this window.
No functionality has been linked to the interval linker in this sample. */
public BarsPeriod BarsPeriod { get; set; }
 
// NOTE: Don't forget to clean up resources and unsubscribe to events
// Called by TabControl when tab is being removed or window is closed
public override void Cleanup()
{
     // Clean up our resources
     if (intervalSelector != null)
          intervalSelector.IntervalChanged -= OnIntervalChanged;
 
     base.Cleanup();
} |



 


 




| XAML |
| --- |
| <page xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:accountdata="clr-namespace:NinjaTrader.Gui.AccountData;assembly=NinjaTrader.Gui" xmlns:accountperformance="clr-namespace:NinjaTrader.Gui.AccountPerformance;assembly=NinjaTrader.Gui" xmlns:atmstrategy="clr-namespace:NinjaTrader.Gui.NinjaScript.AtmStrategy;assembly=NinjaTrader.Gui" xmlns:tools="clr-namespace:NinjaTrader.Gui.Tools;assembly=NinjaTrader.Gui" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
 
<grid>
     <grid.columndefinitions>
          <columndefinition width="Auto"></columndefinition>
          <columndefinition width="*"></columndefinition>
     </grid.columndefinitions>
 
     <tools:intervalselector grid.column="0" horizontalalignment="Left" x:name="intervalSelector"></tools:intervalselector>
</grid> |






 
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
 
 
 



</page>