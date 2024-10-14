










 


OnBarsChanged()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?onbarschanged.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Drawing Tool](drawing_tools.htm) &gt;
OnBarsChanged() | [Previous page](isuserdrawn.htm)
[Return to chapter overview](drawing_tools.htm)










Definition
----------


An event driven method which is called any time the underlying bar series have changed for the chart where the drawing tool resides.  For example if a user has changed the primary instrument or the time frame of the bars used on the chart.


 


Method Return Value
-------------------


This method does not return a value



Syntax
------


You must override this method using the following syntax:



public override void OnBarsChanged()  

{  

     

}



Method Parameters
-----------------


This method does not accept any parameters



Examples
--------




| ns |
| --- |
| public override void OnBarsChanged()
{
    //bars have change, do something         
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
 
 
 



