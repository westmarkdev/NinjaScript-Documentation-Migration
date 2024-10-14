










 


Plots







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?plots.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Indicator](indicator.htm) &gt; [AddPlot()](addplot.htm) &gt;
Plots | [Previous page](plotbrushes.htm)
[Return to chapter overview](addplot.htm)










Definition
----------


A collection holding all of the Plot objects that define their visualization characteristics.


 


Property Value
--------------


A collection of Plot objects.


 


Syntax
------


Plots[int index]


 




|  |
| --- |
| Note: The example code below will change the color of an entire plot series. See [PlotBrushes](plotbrushes.htm) for information on changing only specific segments of a plot instead. |



 


 


Example
-------




| ns |
| --- |
| protected override void OnStateChange()
{
   if(State == State.SetDefaults)
   {
       Name = "Examples Indicator";
       // Lines are added to the Lines collection in order
       AddPlot(Brushes.Orange, "Plot1"); // Stored in Plots[0]
       AddPlot(Brushes.Blue, "Plot2");   // Stored in Plots[1]
     }
}
 
// Dynamically change the primary plot's color based on the indicator value
protected override void OnBarUpdate()
{
   if (Value[0] &gt; 70)
   {
     Plots[0].Brush = Brushes.Blue;
     Plots[0].Width = 2;
   }
   else
   {
     Plots[0].Brush = Brushes.Red;
     Plots[0].Width = 2;
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
 
 
 



