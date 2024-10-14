


Format()









 


Format()















Definition
----------


This method allows you to customize the rendering of the value in the Market Analyzer Column.


 


Syntax
------


public override string Format(double value)   

{  

     

}


 


Examples
--------




| ns |
| --- |
| public override string Format(double value)
{
     return (value == double.MinValue ? string.Empty : Instrument.MasterInstrument.FormatPrice(value));
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
 
 
 



