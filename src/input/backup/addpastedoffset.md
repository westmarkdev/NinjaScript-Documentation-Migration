










 


AddPastedOffset()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?addpastedoffset.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
AddPastedOffset() | [Previous page](drawing_tools.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


A [virtual method](https://msdn.microsoft.com/en-us/library/9fkccyh4.aspx) which is called every time a DrawingTool is copied and pasted to a chart.  The default behavior will offset the chart anchors price value down by 1, percent. However, this behavior can be overridden for your custom drawing tool if desired. 


 


Method Return Value
-------------------


This method does not return a value



Syntax
------


You must override this method using the following syntax:


public override void AddPastedOffset(ChartPanel panel, ChartScale chartScale)  

{  

   

}



Method Parameters
-----------------




|  |  |
| --- | --- |
| panel | A ChartPanel representing the the panel for the chart |
| chartScale | A ChartScale representing the Y-axis |



 


 


Examples
--------




| ns |
| --- |
| public override void AddPastedOffset(ChartPanel chartPanel, ChartScale chartScale)
{      
   foreach (ChartAnchor anchor in Anchors)
   {
     //bump each anchor 1 minute to the right
     DateTime tmpTime = anchor.Time;
     anchor.Time = tmpTime.AddMinutes(1);        
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
 
 
 



