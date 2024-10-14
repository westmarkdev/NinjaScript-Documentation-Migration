










 


Format()







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?format.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Performance Metrics](performance_metrics.htm) &gt;
Format() | [Previous page](performance_metrics.htm)
[Return to chapter overview](performance_metrics.htm)










Definition
----------


This method allows you to customize the rendering of the performance value on the Summary grid.


 


Syntax
------


public override string Format(object value, Cbi.PerformanceUnit unit, string propertyName)   

{  

     

}


 


 


Examples
--------




| ns |
| --- |
| public override string Format(object value, Cbi.PerformanceUnit unit, string propertyName)
{
     double[] tmp = value as double[];
     if (tmp != null &amp;&amp; tmp.Length == 5)
         switch (unit)
         {
               case Cbi.PerformanceUnit.Currency : return Core.Globals.FormatCurrency(tmp[0], denomination);
               case Cbi.PerformanceUnit.Percent   : return tmp[1].ToString("P");
               case Cbi.PerformanceUnit.Pips : return Math.Round(tmp[2]).ToString(Core.Globals.GeneralOptions.CurrentCulture);
               case Cbi.PerformanceUnit.Points : return Math.Round(tmp[3]).ToString(Core.Globals.GeneralOptions.CurrentCulture);
               case Cbi.PerformanceUnit.Ticks : return Math.Round(tmp[4]).ToString(Core.Globals.GeneralOptions.CurrentCulture);
         }
     return value.ToString();
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
 
 
 



