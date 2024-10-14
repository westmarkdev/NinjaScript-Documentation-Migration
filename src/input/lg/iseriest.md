










 


ISeries<t>







| &lt;&lt; [Click to Display Table of Contents](NT HelpGuide English.html?iseriest.htm) &gt;&gt;
 [NinjaScript](ninjascript.htm) &gt; [Language Reference](language_reference_wip.htm) &gt; [Common](common.htm) &gt;
ISeries<t> | [Previous page](url.htm)
[Return to chapter overview](common.htm)










Definition
----------


ISeries<t> is an interface that is implemented by all NinjaScript classes that manage historical data as an ISeries<double> (Open, High, Low, Close, etc), used for indicator input, and other object data.  Please see the help guide article on [Working with Price Series](working_with_price_series.htm) for a basic overview on how to access this information.


 


Types of ISeries
----------------




|  |  |
| --- | --- |
| [Series<t>](seriest.htm) | Represents a generic custom data structure for custom development |
| [PriceSeries](priceseries.htm) | Historical price data structured as an ISeries<double> interface (Close[0], High[0], Low[0], etc) |
| [TimeSeries](timeseries.htm) | Historical time stamps structured as an ISeries<datetime> interface (Time[0]) |
| [VolumeSeries](volumeseries.htm) | Historical volume data structured as an ISeries<double> interface (Volume[0]) |



 


 


Methods and Properties
----------------------




|  |  |
| --- | --- |
| [GetValueAt()](getvalueat.htm) | Returns the underlying input value at a specified bar index value. |
| [IsValidDataPoint()](isvaliddatapoint.htm) | Indicates if the specified input is set at a barsAgo value relative to the current bar. |
| [IsValidDataPointAt()](isvaliddatapointat.htm) | Indicates if the specified input is set at a specified bar index value. |
| [Count](iseries_count.htm) | Return the number total number of values in the ISeries array |



 




|  |
| --- |
| Tips: (see examples below) 
1.By specifying a parameter of type ISeries<double>, you can then pass in an array of closing prices, an indicator, or a user defined data series.2.When working with ISeries<double> objects in your code you may come across situations where you are not sure if the value being accessed is a valid value or just a "placeholder" value. To check if you are using valid values for your logic calculations that have been explicitly set, please use .IsValidDataPoint(int barsAgo) to check.  |



 



Examples
--------




| ns Using ISeries as a method parameter |
| --- |
| //create custom a method named DoubleTheValue that accepts any object that implements 
// the ISeries<double> interface as a parameter
private double DoubleTheValue(ISeries<double> priceData)
{
     return priceData[0] * 2;
}
 
protected override void OnBarUpdate()
{
   // This custom method is then used twice, 
   //the first time passing in an array of closing prices 
     Print(DoubleTheValue(Close));
   //and the second time passing in a 20 period simple moving average.
     Print(DoubleTheValue(SMA(20)));
} |



 





| ns Checking ISeries value before accessing |
| --- |
| protected override void OnBarUpdate()
{
     // Only set our plot if the input is a valid value
     if (Input.IsValidDataPoint(0))
         Plot0[0] = Input[0];
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
 
 
 



</double></double></double></double></double></datetime></double></t></double></t></t></t></t>