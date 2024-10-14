










 


Reset()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?reset.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt; [ISeries<t>](iseriest.htm) &gt; [Series<t>](seriest.htm) &gt;
Reset() | [Previous page](seriest.htm)
[Return to chapter overview](seriest.htm)










Definition
----------


Resets the internal marker which is used for [IsValidDataPoint()](isvaliddatapoint.htm) back to false.  Calling the Reset() method is unique and can be very powerful for custom indicator development. [Series<t>](seriest.htm) objects will always contain a value which is assigned, however calling Reset() simply means you effectively ignore the value of the current bar for plotting purposes. For calculation purposes you will want to use [IsValidDataPoint()](isvaliddatapoint.htm) to ensure you are not calculating off of any reset values assigned by the Reset() method.


 




|  |  |
| --- | --- |
| Series Type | Value after Reset() |
| Series<bool> | false |
| Series<double> | 0.00 |
| Series<datetime> | DateTime.MinValue |
| Series<float> | 0 |
| Series<int> | 0 |
| Series<long> | 0 |
| Series<string> | null |



 


Method Return Value
-------------------


This method does not return a value


 


Syntax
------


Reset()  

Reset(int barsAgo)


 


 
Parameters
------------




|  |  |
| --- | --- |
| barsAgo | An int representing from the current bar the number of historical bars the method will check.  If no barsAgo value is supplied, the current bar value will be reset instead (barsAgo 0) |




 


Examples
--------




| ns |
| --- |
| protected override void OnBarUpdate()
{
   // set MyPlot to Low of current bar minus 1 tick
   MyPlot[0] = Low[0] - (1 * TickSize);            
 
   //reset MyPlot every 10 bars
   if(CurrentBar % 10 == 0)
     MyPlot.Reset();    
 
   // only calculate MyPlot value if it has not be reset
   if(MyPlot.IsValidDataPoint(0))
     Print(CurrentBar + " Value is: " + MyPlot[0]);         
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
 
 
 



</string></long></int></float></datetime></double></bool></t></t></t></t></t>