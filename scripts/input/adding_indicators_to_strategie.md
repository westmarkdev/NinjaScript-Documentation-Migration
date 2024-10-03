










 


Adding Indicators to Strategies







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?adding_indicators_to_strategie.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Educational Resources](educational_resources.htm) &gt; [Tips](tips.htm) &gt;
Adding Indicators to Strategies | [Previous page](tips.htm)
[Return to chapter overview](tips.htm)










When backtesting strategies it can be useful to add the indicators you use for calculations onto the chart to make it easier to check your strategy for accuracy. Instead of doing this step manually every time you run the strategy you can program it to automatically load the indicators for you.


 


For example:


 


To add a volume indicator to your charts you need to add this code snippet into the [OnStateChange](onstatechange.htm) section of your code for the State: State.DataLoaded




| ns |
| --- |
| protected override void OnStateChange()
{
     if (State == State.DataLoaded)
     {
           AddChartIndicator(VOL());
     }
} |



 


To choose which panel you want your indicator plotted on you can use this code snippet into the State.DataLoaded state:




| ns |
| --- |
| VOL().Panel = 2;
AddChartIndicator(VOL()); |



 


To customize plot colors:




| ns |
| --- |
| VOL().Plots[0].Brush = Brushes.Red;     // Plots the VOL with a red plot |



 


To customize plot width:




| ns |
| --- |
| VOL().Plots[0].Width = 4;   // Plots the VOL bars with a width of 4 |



 


To customize the plot dash style:




| ns |
| --- |
| VOL().Plots[0].DashStyleHelper = DashStyleHelper.Dash; |



 


To customize the plot style:




| ns |
| --- |
| VOL().Plots[0].PlotStyle = PlotStyle.Bar;
VOL().Plots[0].AutoWidth = true; |



 


To customize lines you can do it the same way as above.




| ns |
| --- |
| RSI(14, 3).Lines[0].Value = 20;
RSI(14, 3).Lines[0].Brush = Brushes.Green; |



 


Remember, you need to use the [AddChartIndicator()](addchartindicator.htm) method to add your indicator if you wish to use any of the plot / line indicator customization examples.





 
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
 
 
 



