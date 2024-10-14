










 


GetBarPaintWidth()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?getbarpaintwidth.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Chart Style](chart_style.htm) &gt;
GetBarPaintWidth() | [Previous page](downbrushdx.htm)
[Return to chapter overview](chart_style.htm)










Definition
----------


Returns the painted width of the chart bar.  The GetBarPintWidth() method will return a minimum value of 1.


 




|  |
| --- |
| Note:  This is an [abstract](https://msdn.microsoft.com/en-us/library/sf985hc5.aspx) method which is required to compile a ChartStyle object.  If you do not plan on recalculating a barWidth, simply return the default barWidth parameter which is passed in this method.  Please see the Examples section of this page for more information. |



 


Method Return Value
-------------------


An int value


 


Syntax
------


You must over ride this method using the following syntax:



public override int GetBarPaintWidth(int barWidth)  

{  

   

}


 


Method Parameters
-----------------




|  |  |
| --- | --- |
| barWidth | An int value representing the current width of the bar to calculate |



 



Examples
--------




| ns Returning the default barWidth |
| --- |
| public override int GetBarPaintWidth(int barWidth)
{
     return barWidth      
} |



 


 


 




| ns Calculating and returning a new barWidth from the original barWidth |
| --- |
| public override int GetBarPaintWidth(int barWidth)
{
   // calculate a new bar width 
   return 1 + 2 * (barWidth - 1) + 2 * (int) Math.Round(Stroke.Width);
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
 
 
 



