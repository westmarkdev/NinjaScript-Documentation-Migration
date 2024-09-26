










 


IsValidDataPoint()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?isvaliddatapoint.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [ISeries<t>](iseriest.htm) &gt;
IsValidDataPoint() | [Previous page](getvalueat.htm)
[Return to chapter overview](iseriest.htm)










Definition
----------


Indicates if the specified input is set at a barsAgo value relative to the current bar.  Please also see the [Reset()](reset.htm) method for more information.


 




|  |
| --- |
| Notes: 
•If called directly from the instance of the NinjaScript object, the value returned corresponds to the Input Series (e.g., Close, High, Low, SMA, etc.)•When checking a [Bar](bars.htm) or [PriceSeries](priceseries.htm), IsValidDataPoint() returns true as long as the barAgo value falls between 0 and the total count for that series.  These are special series which always contain a value set at every slot index for multi-series scripting purposes (e.g., comparing two price series with various session templates, or one series has more ticks than the other)•For a [Value](value.htm) series or custom [Series<t>](seriest.htm), IsValidDataPoint() returns true or false depending on if you have set a value at that index location |



 


 


Method Return Value
-------------------


A bool value, when true indicates that specified data point is set; otherwise false.


 


Syntax
------


IsValidDataPoint(int barsAgo)


ISeries<t>.IsValidDataPoint(int barsAgo)


 




|  |
| --- |
| Warning:  Calling IsValidDataPoint() will only work a MaximumBarsLookBackInfinite series.  Attempting to check IsValidDataPoint() MaximumBarsLookBack256 series throw an error.  Please check the Log tab of the Control Center. In addition since this method references BarsAgo data, and therefore cannot be used during [OnRender (see note 5)](onrender.htm).- instead please use the [IsValidDataPointAt](isvaliddatapointat.htm) during OnRender. |



 


   

Parameters




|  |  |
| --- | --- |
| barsAgo | An int representing from the current bar the number of historical bars the method will check. |



 


 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   // only set plot value if hosted indicator is not reset
   if(SMA(20).IsValidDataPoint(0))
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