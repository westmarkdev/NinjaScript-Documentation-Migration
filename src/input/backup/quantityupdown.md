










 


QuantityUpDown







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?quantityupdown.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Add On](add_on.htm) &gt; [NinjaTrader Controls](controls.htm) &gt;
QuantityUpDown | [Previous page](tifselector.htm)
[Return to chapter overview](controls.htm)










Definition
----------


QuantityUpDown can be used as an UI element users can interact with for selecting quantity.


 


Events and Properties
---------------------




|  |  |
| --- | --- |
| Value | An int representing the quantity |



 


 


Examples
--------


This example demonstrates how to use the quantity up/down selector and properly link its behavior with the ATM strategy and TIF selectors.


 




| C# |
| --- |
| private QuantityUpDown                  qudSelector;
private TifSelector                     tifSelector;
private AtmStrategy.AtmStrategySelector atmStrategySelector;
 
private DependencyObject LoadXAML()
{
     // Note: pageContent (not demonstrated in this example) is the page content of the XAML
     // Find the Quantity Up-Down selector
     qudSelector = LogicalTreeHelper.FindLogicalNode(pageContent, "qudSelector") as QuantityUpDown;
 
     // Find the TIF selector
     tifSelector = LogicalTreeHelper.FindLogicalNode(pageContent, "tifSelector") as TifSelector;
 
     // Be sure to bind our account selector to our TIF selector to ensure proper functionality
     tifSelector.SetBinding(TifSelector.AccountProperty, new Binding { Source = accountSelector,
          Path = new PropertyPath("SelectedAccount") });
 
     // When our TIF selector's selection changes
     tifSelector.SelectionChanged += (o, args) =&gt;
     {
          // Change the selected TIF in the ATM strategy too
         if (atmStrategySelector.SelectedAtmStrategy != null)
               atmStrategySelector.SelectedAtmStrategy.TimeInForce = tifSelector.SelectedTif;
     };
 
     // Find ATM Strategy selector and attach event handler
     atmStrategySelector = LogicalTreeHelper.FindLogicalNode(pageContent, "atmStrategySelector") as AtmStrategy.AtmStrategySelector;
     atmStrategySelector.Id = Guid.NewGuid().ToString("N");
     if (atmStrategySelector != null)
          atmStrategySelector.CustomPropertiesChanged += OnAtmCustomPropertiesChanged;
 
     // Be sure to bind our account selector to our ATM strategy selector to ensure proper functionality
     atmStrategySelector.SetBinding(AtmStrategy.AtmStrategySelector.AccountProperty,
         new Binding { Source = accountSelector, Path = new PropertyPath("SelectedAccount") });
 
     // When our ATM selector's selection changes
     atmStrategySelector.SelectionChanged += (o, args) =&gt;
     {
         if (atmStrategySelector.SelectedItem == null)
               return;
         if (args.AddedItems.Count &gt; 0)
          {
               // Change the selected TIF in our TIF selector too
               AtmStrategy selectedAtmStrategy = args.AddedItems[0] as AtmStrategy;
               if (selectedAtmStrategy != null)
                    tifSelector.SelectedTif = selectedAtmStrategy.TimeInForce;
         }
 };
 
}
 
private void OnAtmCustomPropertiesChanged(object sender, NinjaScript.AtmStrategy.CustomPropertiesChangedEventArgs args)
{
     // Adjust our TIF and Quantity selectors to the new ATM strategy values
     tifSelector.SelectedTif = args.NewTif;
     qudSelector.Value = args.NewQuantity;
}
 
// NOTE: Don't forget to clean up resources and unsubscribe to events
// Called by TabControl when tab is being removed or window is closed
public override void Cleanup()
{
    // Clean up our resources
     base.Cleanup();    
} |



 


 




| XAML |
| --- |
|  
<page xmlns="http://schemas.microsoft.com/winfx/2006/xaml/presentation" xmlns:accountdata="clr-namespace:NinjaTrader.Gui.AccountData;assembly=NinjaTrader.Gui" xmlns:accountperformance="clr-namespace:NinjaTrader.Gui.AccountPerformance;assembly=NinjaTrader.Gui" xmlns:atmstrategy="clr-namespace:NinjaTrader.Gui.NinjaScript.AtmStrategy;assembly=NinjaTrader.Gui" xmlns:tools="clr-namespace:NinjaTrader.Gui.Tools;assembly=NinjaTrader.Gui" xmlns:x="http://schemas.microsoft.com/winfx/2006/xaml">
 
<grid>
     <grid.columndefinitions>
          <columndefinition width="Auto"></columndefinition>
          <columndefinition width="Auto"></columndefinition>
          <columndefinition width="*"></columndefinition>
     </grid.columndefinitions>
 
     <tools:quantityupdown grid.column="0" value="1" x:name="qudSelector"></tools:quantityupdown>
     <tools:tifselector grid.column="1" x:name="tifSelector">
     <atmstrategy:atmstrategyselector grid.column="2" linkedquantity="{Binding Value, 
     ElementName=qudSelector, Mode=OneWay}" x:name="atmStrategySelector"></atmstrategy:atmstrategyselector>
</tools:tifselector></grid> |






 
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