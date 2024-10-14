










 


AddPlot()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?addplot.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Indicator](indicator.htm) &gt;
AddPlot() | [Previous page](lines.htm)
[Return to chapter overview](indicator.htm)










Definition
----------


Adds plot objects that define how an indicator or strategy data series render on a chart. When this method is called to add a plot, an associated [Series<double>](seriest.htm) object is created held in the [Values](value.htm) collection.


 




|  |
| --- |
| Note:  Plots are ONLY visible from the UI property grid when AddPlot() is called from State.SetDefaults. If your indicator or strategy dynamically adds plots during State.Configure, you will NOT have an opportunity to select the plot or to set the plot configuration via the UI.  Alternatively, you may use custom public [Brush](brushes.htm), [Stroke](stroke_class.htm), or PlotStyle properties which are accessible in State.SetDefaults and pass those values to AddPlot() during State.Configure.  Calling AddPlot() in this manner should be reserved for special cases.  Please see the examples below. |



 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [ArePlotsConfigurable](areplotsconfigurable.htm) | Determines if the plot(s) used in an indicator are configurable within the indicator dialog window. |
| [Displacement](displacement.htm) | An offset value that shifts the visually displayed value of an indicator. |
| [PlotBrushes](plotbrushes.htm) | Holds an array of color series objects holding historical bar colors. |
| [Plots](plots.htm) | A collection holding all of the Plot objects that define their visualization characteristics. |




Syntax
------


AddPlot(Brush brush, string name)  

AddPlot(Stroke stroke, PlotStyle plotStyle, string name)


 




|  |
| --- |
| Warning: This method should ONLY be called within the [OnStateChange()](onstatechange.htm) method during State.SetDefaults or State.Configure |



 


 


Parameters
----------




|  |  |
| --- | --- |
| brush | A Brush object used to construct the plot |
| name | A string representing the name of the plot |
| plotStyle | A PlotStyle object used to construct the style of the plot
 
Possible values:
 
PlotStyle.Bar
PlotStyle.Block
PlotStyle.Cross
PlotStyle.Dot
PlotStyle.Hash
PlotStyle.HLine
PlotStyle.Line
PlotStyle.PriceBox
PlotStyle.Square
PlotStyle.TriangleDown
PlotStyle.TriangleLeft
PlotStyle.TriangleRight
PlotStyle.TriangleUp |
| stroke | A Stroke object used to construct the plot |



 


 




|  |
| --- |
| Tips:
1.We suggest using the NinjaScript wizard to generate your plots.2.[Plot](plots.htm) objects DO NOT hold the actual script values. They simply define how the script's values are plotted on a chart.3.A script may calculate multiple values and therefore hold multiple plots to determine the display of each calculated value. Script values are held in the script's [Values](value.htm) collection.4.If you script calls AddPlot() multiple times, then multiple Values series are added per the "three value series" example below5.For [MultiSeries scripts](multi-time_frame__instruments.htm), plots are synched to the primary series of the NinjaScript object.6.Plots will become visible once the script’s [BarsRequiredToPlot](barsrequiredtoplot.htm) value has been satisfied. By default, the value is 20. |



 


Examples
--------




| ns Indicator using various AddPlot() signatures |
| --- |
| protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name = "Examples Indicator";
 
     // Adds a blue line style plot
     AddPlot(Brushes.Blue, "MyPlot");
 
     // Adds a blue historgram style plot
     AddPlot(new Stroke(Brushes.Blue), PlotStyle.Bar, "MyPlot2");
 
     // Ensures that the width of the PlotStyle.Bar plot matches the width of the data series
     Plots[1].AutoWidth = true;
 
      // Adds a blue Dash-Line style plot with 5pixel width and 50% opacity
     AddPlot(new Stroke(Brushes.Blue, DashStyleHelper.Dash, 5, 50), PlotStyle.Line, "MyPlot3");
   }
} |



 


 




| ns Indicator using a public Series<double> to expose a plot with a friendly name. This is required for making plots accessible in the Strategy Builder
For an example on exposing other variables publicly, see [Exposing Indicator values that are not plots](exposing_indicator_values_that.htm) |
| --- |
| protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name = "Examples Indicator";
 
     // Adds a blue line style plot
     AddPlot(Brushes.Blue, "MyPlot");
 
     // Adds a blue historgram style plot
     AddPlot(new Stroke(Brushes.Blue), PlotStyle.Bar, "MyPlot2");
   }
}
 
protected override void OnBarUpdate()
{
   MyPlot[0] = Close[0] + High[0] / 2​;
   MyPlot[1] = Close[0] + High[0] / 2​;
}
 
[Browsable(false)]
[XmlIgnore]
public Series<double> MyPlot
{
   get { return Values[0]; }
}
 
[Browsable(false)]
[XmlIgnore]
public Series<double> MyPlot2
{
   get { return Values[1]; }
} |



 





| ns Indicator which adds three value series |
| --- |
| protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name = "Examples Indicator";
 
     // Add three plots and associated Series<double> objects
     AddPlot(Brushes.Blue, "PlotA");     // Defines the plot for Values[0]
     AddPlot(Brushes.Red, "PlotB");     // Defines the plot for Values[1]
     AddPlot(Brushes.Green, "PlotC");   // Defines the plot for Values[2]
   }
}
protected override void OnBarUpdate()
{
   Values[0][0] = Median[0];   // Blue "Plot A"
   Values[1][0] = Low[0];       // Red "Plot B"
   Values[2][0] = High[0];     // Green "Plot C"
} |



 


 




| ns Indicator which dynamically adds a plot in State.Configure |
| --- |
| protected override void OnStateChange()
{
   if (State == State.SetDefaults)
   {
     Name                 = "Examples Indicator";
 
     // logical property which user can set
     UseSpecialMode   = false;
     // Default brush selection pushed to the UI
     MyBrush = Brushes.Red;
   }
   else if (State == State.Configure)
   {
     // if user enables logical property
     if (UseSpecialMode)
     {
         // add plot using default selected brush and special plot name
         AddPlot(MyBrush, "My Special Plot");
     }
     else
     {
         // otherwise use default selected brush and regular plot name
         AddPlot(MyBrush, "My Regular Plot");
     }
   }
}
 
protected override void OnBarUpdate()
{
   if (UseSpecialMode)
     Value[0] = Close[0] + High[0] / 2;
 
   else Value[0] = Close[0] * TickSize / 2;
}
 
[XmlIgnore]
public Brush MyBrush { get; set; }
 
public bool UseSpecialMode { get; set; } |



 





 
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
 
 
 



</double></double></double></double></double>