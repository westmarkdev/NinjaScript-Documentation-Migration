










 


IsValidDataPointAt()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isvaliddatapointat.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [ISeries<t>](iseriest.htm) &gt;
IsValidDataPointAt() | [Previous page](isvaliddatapoint.htm)
[Return to chapter overview](iseriest.htm)










Definition
----------


Indicates if the specified input is set at a specified bar index value.  Please also see the [Reset()](reset.htm) method for more information.


 




|  |
| --- |
| Notes: 
•If called directly from the instance of the NinjaScript object, the value returned corresponds to the Inputs Series (e.g., Close, High, Low, SMA, etc.)•When checking a [Bar](bars.htm) or [PriceSeries](priceseries.htm), IsValidDataPoint() returns true as long as the barIndex value falls between 0 and the total count for that series.  These are special series which always contain a value set at every slot index for multi-series scripting purposes (e.g., comparing two price series with various session templates, or one series has more ticks than the other)•For a [Value](value.htm) series or custom [Series<t>](seriest.htm), IsValidDataPoint() returns true or false depending on if you have set a value at that index location |



 



Method Return Value
-------------------


A bool value, when true indicates that specified data point is set; otherwise false.


 




|  |
| --- |
| Warning:  Calling IsValidDataPointAt() will only work a MaximumBarsLookBackInfinite series.  Attempting to check IsValidDataPointAt() MaximumBarsLookBack256 series throw an error.  Please check the Log tab of the Control Center |



 


 


Syntax
------


IsValidDataPointAt(int barIndex)


ISeries<t>.IsValidDataPointAt(int barIndex)


   

Parameters




|  |  |
| --- | --- |
| barIndex | An int representing an absolute bar index value |




 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   // only set plot value if hosted indicator is not reset
   if(SMA(20).IsValidDataPointAt(CurrentBar))
     MyPlot[0] = SMA(20)[0];     
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
 
 
 



</t></t></t></t>