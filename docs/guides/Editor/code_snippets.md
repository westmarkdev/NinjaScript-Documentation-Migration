---
title: Code Snippets
pathName: code_snippets
parent: ninjascript_editor_overview
status: review
section: guides
---

## Code Snippets

Code Snippets can provide you with useful code templates to speed up your coding process.

## Understanding Code Snippet shortcuts

{% table %}

* Shortcut
* Method Signature

---

* **dap**
* `Draw.AndrewsPitchfork(this, "MyAndrewsPitchfork", false, 10, Close[10], 5, High[5], 0, Low[5], Brushes.Blue, DashStyleHelper.Solid, 1);`

---

* **da**
* `Draw.Arc(this, "MyDrawArc", false, 10, Close[10], 0, Close[0], Brushes.LimeGreen, DashStyleHelper.Dot, 2);`

---

* **dd**
* `Draw.ArrowDown(this, "MyArrowDown", false, 0, High[0], Brushes.Red);`

---

* **du**
* `Draw.ArrowUp(this, "MyArrowUp", false, 0, Low[0], Brushes.Red);`

---

* **ddi**
* `Draw.Diamond(this, "MyDiamond", false, 0, High[0] + 2 * TickSize, Brushes.Blue);`

---

* **dt**
* `Draw.Dot(this, "MyDot", false, 0, High[0] + 2 * TickSize, Brushes.Blue);`

---

* **de**
* `Draw.Ellipse(this, "MyEllipse", 10, Low[10], 0, High[0], Brushes.Blue);`

---

* **di**
* `Draw.ExtendedLine(this, "MyExtendedLine", 10, Close[10], 0, Close[0], Brushes.Blue);`

---

* **dfc**
* `Draw.FibonacciCircle(this, "MyFibonacciCircle", true, 10, Close[10], 0, Close[0]);`

---

* **dfe**
* `Draw.FibonacciExtensions(this, "MyFibonacciExtensions", true, 15, Close[15], 10, Close[10], 5, Close[5]);`

---

* **dfr**
* `Draw.FibonacciRetracements(this, "MyFibonacciRetracements", false, 10, Close[10], 0, Close[0]);`

---

* **dft**
* `Draw.FibonacciTimeExtensions(this, "MyFibonacciTimeExtensions", false, 10, Close[10], 0, Close[0]);`

---

* **dg**
* `Draw.GannFan(this, "MyGannFan", true, 10, Close[10]);`

---

* **dh**
* `Draw.HorizontalLine(this, "MyHorizontalLine", Close[0], Brushes.Blue);`

---

* **dl**
* `Draw.Line(this, "MyLine", 10, Close[10], 0, Close[0], Brushes.Blue);`

---

* **dy**
* `Draw.Ray(this, "MyRay", 10, Close[10], 0, Close[0], Brushes.Blue);`

---

* **dr**
* `Draw.Rectangle(this, "MyRectangle", 10, Low[10], 0, High[0], Brushes.Blue);`

---

* **dre**
* `Draw.Region(this, CurrentBar, 0, Bollinger(2, 14).Upper, Bollinger(2, 14).Lower, Brushes.Green, Brushes.Blue, 50);`

---

* **drx**
* `Draw.RegionHighlightX(this, "MyRegionHighlightX", 10, 0, Brushes.Blue);`

---

* **dry**
* `Draw.RegionHighlightY(this, "MyRegionHighlightY", High[0], Low[0], Brushes.Blue, Brushes.Green, 20);`

---

* **drr**
* `Draw.RiskReward(this, "MyRiskReward", false, 0, High[0], 10, Low[0], 2, true);`

---

* **dru**
* `Draw.Ruler(this, "tag1", true, 4, Low[4], 3, High[3], 1, Low[1]);`

---

* **ds**
* `Draw.Square(this, "MySquare", false, 0, High[0] + 2 * TickSize, Brushes.Blue);`

---

* **dx**
* `Draw.Text(this, "MyText", "Sample text ", 0, High[0] + 2 * TickSize, Brushes.Blue);`

---

* **dxf**
* `Draw.TextFixed(this, "MyTextFixed", "Text to draw", TextPosition.TopRight);`

---

* **dtc**
* `Draw.TrendChannel(this, "TrendChannel", true, 10, Low[10], 0, High[0], 10, High[10] + 5 * TickSize);`

---

* **dtd**
* `Draw.TriangleDown(this, "MyTriangleDown", false, 0, High[0] + 2 * TickSize, Brushes.Red);`

---

* **dtu**
* `Draw.TriangleUp(this, "MyTriangleUp", false, 0, Low[0] - 2 * TickSize, Brushes.Blue);`

---

* **dv**
* `Draw.VerticalLine(this, "MyVerticalLine", 0, Brushes.Blue);`
{% /table %}

## How to insert Code Snippets via the mouse or F2 key

### Using the keyboard

Enter the text in the left column and press the "Tab" key within the NinjaScript Editor.

{% table %}

---

* **cb**
* `CurrentBar`

---

* **o**
* `Open[0]`

---

* **h**
* `High[0]`

---

* **l**
* `Low[0]`

---

* **v**
* `Volume[0]`

---

* **i**
* `Input[0]`
{% /table %}

### Previous Bar Values

{% table %}

---

* **c1**
* `Close[1]`

---

* **o1**
* `Open[1]`

---

* **h1**
* `High[1]`

---

* **l1**
* `Low[1]`

---

* **v1**
* `Volume[1]`

---

* **i1**
* `Input[1]`
{% /table %}

{% table %}

### Indicator Plotting

{% table %}
---

* **line**
* `AddLine(new Stroke(Brushes.Blue, 1), 0, "Line");`

---

* **plot**
* `AddPlot(new Stroke(Brushes.Blue, 1), PlotStyle.Line, "Plot");`
{% /table %}

### Arithmetic

{% table %}
---

* **abs**
* `Math.Abs(value)`

---

* **min**
* `Math.Min(value1, value2)`

---

* **max**
* `Math.Max(value1, value2)`

{% /table %}

### Event Handler Callback Methods

{% table %}

* account
* `protected override void OnAccountItemUpdate(Account account, AccountItem accountItem, double value) {}`

---

* **trade**
* `protected override void OnAddTrade(Cbi.Trade trade) {}`

---

* **barschange**
* `public override void OnBarsChanged() {}`

---

* **minmax**
* `public override void OnCalculateMinMax() { /*It is important to set MinValue and MaxValue to the min/max Y values your drawing tool uses if you want it to support auto scale*/ }`

---

* **calcperf**
* `protected override void OnCalculatePerformanceValue(StrategyBase strategy) {}`

---

* **connection**
* `protected override void OnConnectionStatusUpdate(ConnectionStatus orderStatus, ConnectionStatus priceStatus) {}`

---

* **datapoint**
* `protected override void OnDataPoint(Bars bars, double open, double high, double low, double close, DateTime time, long volume, bool isBar, double bid, double ask) {}`

---

* **execution**
* `protected override void OnExecutionUpdate(Execution execution, string executionId, double price, int quantity, MarketPosition marketPosition, string orderId, DateTime time) {}`

---

* **fundamental**
* `protected override void OnFundamentalData(FundamentalDataEventArgs fundamentalDataUpdate) {}`

---

* **data**
* `protected override void OnMarketData(MarketDataEventArgs marketDataUpdate) {}`

---

* **depth**
* `protected override void OnMarketDepth(MarketDepthEventArgs marketDepthUpdate) {}`

---

* **mergeperf**
* `protected override void OnMergePerformanceMetric(PerformanceMetricBase merge) {}`

---

* **moused**
* `public override void OnMouseDown(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint) {}`

---

* **mousem**
* `public override void OnMouseMove(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint) {}`

---

* **mouseu**
* `public override void OnMouseUp(ChartControl chartControl, ChartPanel chartPanel, ChartScale chartScale, ChartAnchor dataPoint) {}`

---

* **optimize**
* `protected override void OnOptimize() {}`

---

* **ordert**
* `protected override void OnOrderTrace(DateTime timestamp, string message) {}`

---

* **orderu**
* `protected override void OnOrderUpdate(Order order, double limitPrice, double stopPrice, int quantity, int filled, double averageFillPrice, OrderState orderState, DateTime time, ErrorCode error, string nativeError) {}`

---

* **position**
* `protected override void OnPositionUpdate(Position position, double averagePrice, int quantity, MarketPosition marketPosition) {}`

---

* **render**
* `protected override void OnRender(ChartControl chartControl, ChartScale chartScale) {}`

---

* **windowc**
* `protected override void OnWindowCreated(Window window) {}`

---

* **windowd**
* `protected override void OnWindowDestroyed(Window window) {}`

{% /table }

### Control Statements

{% table %}

---

* **if**
* `if (expression) {} else {}`

---

* **for**
* `for (int index = 0; index < count; index++) {}`

---

* **switch**
* `switch (expression) { case value1: break; case value2: break; default: break; }`

{% /table }

### Drawing

{% table %}

* Shortcut
* Method Signature

---

* **dap**
* `Draw.AndrewsPitchfork(this, "MyAndrewsPitchfork", false, 10, Close[10], 5, High[5], 0, Low[5], Brushes.Blue, DashStyleHelper.Solid, 1);`

---

* **da**
* `Draw.Arc(this, "MyDrawArc", false, 10, Close[10], 0, Close[0], Brushes.LimeGreen, DashStyleHelper.Dot, 2);`

---

* **dd**
* `Draw.ArrowDown(this, "MyArrowDown", false, 0, High[0], Brushes.Red);`

---

* **du**
* `Draw.ArrowUp(this, "MyArrowUp", false, 0, Low[0], Brushes.Red);`

---

* **ddi**
* `Draw.Diamond(this, "MyDiamond", false, 0, High[0] + 2 * TickSize, Brushes.Blue);`

---

* **dt**
* `Draw.Dot(this, "MyDot", false, 0, High[0] + 2 * TickSize, Brushes.Blue);`

---

* **de**
* `Draw.Ellipse(this, "MyEllipse", 10, Low[10], 0, High[0], Brushes.Blue);`

---

* **di**
* `Draw.ExtendedLine(this, "MyExtendedLine", 10, Close[10], 0, Close[0], Brushes.Blue);`

---

* **dfc**
* `Draw.FibonacciCircle(this, "MyFibonacciCircle", true, 10, Close[10], 0, Close[0]);`

---

* **dfe**
* `Draw.FibonacciExtensions(this, "MyFibonacciExtensions", true, 15, Close[15], 10, Close[10], 5, Close[5]);`

---

* **dfr**
* `Draw.FibonacciRetracements(this, "MyFibonacciRetracements", false, 10, Close[10], 0, Close[0]);`

---

* **dft**
* `Draw.FibonacciTimeExtensions(this, "MyFibonacciTimeExtensions", false, 10, Close[10], 0, Close[0]);`

---

* **dg**
* `Draw.GannFan(this, "MyGannFan", true, 10, Close[10]);`

---

* **dh**
* `Draw.HorizontalLine(this, "MyHorizontalLine", Close[0], Brushes.Blue);`

---

* **dl**
* `Draw.Line(this, "MyLine", 10, Close[10], 0, Close[0], Brushes.Blue);`

---

* **dy**
* `Draw.Ray(this, "MyRay", 10, Close[10], 0, Close[0], Brushes.Blue);`

---

* **dr**
* `Draw.Rectangle(this, "MyRectangle", 10, Low[10], 0, High[0], Brushes.Blue);`

---

* **dre**
* `Draw.Region(this, CurrentBar, 0, Bollinger(2, 14).Upper, Bollinger(2, 14).Lower, Brushes.Green, Brushes.Blue, 50);`

---

* **drx**
* `Draw.RegionHighlightX(this, "MyRegionHighlightX", 10, 0, Brushes.Blue);`

---

* **dry**
* `Draw.RegionHighlightY(this, "MyRegionHighlightY", High[0], Low[0], Brushes.Blue, Brushes.Green, 20);`

---

* **drr**
* `Draw.RiskReward(this, "MyRiskReward", false, 0, High[0], 10, Low[0], 2, true);`

---

* **dru**
* `Draw.Ruler(this, "tag1", true, 4, Low[4], 3, High[3], 1, Low[1]);`

---

* **ds**
* `Draw.Square(this, "MySquare", false, 0, High[0] + 2 * TickSize, Brushes.Blue);`

---

* **dx**
* `Draw.Text(this, "MyText", "Sample text ", 0, High[0] + 2 * TickSize, Brushes.Blue);`

---

* **dxf**
* `Draw.TextFixed(this, "MyTextFixed", "Text to draw", TextPosition.TopRight);`

---

* **dtc**
* `Draw.TrendChannel(this, "TrendChannel", true, 10, Low[10], 0, High[0], 10, High[10] + 5 * TickSize);`

---

* **dtd**
* `Draw.TriangleDown(this, "MyTriangleDown", false, 0, High[0] + 2 * TickSize, Brushes.Red);`

---

* **dtu**
* `Draw.TriangleUp(this, "MyTriangleUp", false, 0, Low[0] - 2 * TickSize, Brushes.Blue);`

---

* **dv**
* `Draw.VerticalLine(this, "MyVerticalLine", 0, Brushes.Blue);`
{% /table %}

## How to insert Code Snippets via the mouse of F2 key

### Via mouse or pressing the F2 key

1. Right mouse click in the NinjaScript Editor and select the menu name "Insert Code Snippet"

    ![NS_Editor_10](ns_editor_10.png)

2. A menu will display all available code snippets.

    ![NS_Editor_11](ns_editor_11.png)
