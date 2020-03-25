<!DOCTYPE html>
<html>

<head>
<style>
body {background:white; font-family:courier;font-size:48px;}
@keyframes blink {
    /**
     * At the start of the animation the dot
     * has an opacity of .2
     */
    0% {
      opacity: .2;
    }
    /**
     * At 20% the dot is fully visible and
     * then fades out slowly
     */
    20% {
      opacity: 1;
    }
    /**
     * Until it reaches an opacity of .2 and
     * the animation can start again
     */
    100% {
      opacity: .2;
    }
}

.saving span {
    /**
     * Use the blink animation, which is defined above
     */
    animation-name: blink;
    /**
     * The animation should take 1.4 seconds
     */
    animation-duration: 1.4s;
    /**
     * It will repeat itself forever
     */
    animation-iteration-count: infinite;
    /**
     * This makes sure that the starting style (opacity: .2)
     * of the animation is applied before the animation starts.
     * Otherwise we would see a short flash or would have
     * to set the default styling of the dots to the same
     * as the animation. Same applies for the ending styles.
     */
    animation-fill-mode: both;
}

.saving span:nth-child(2) {
    /**
     * Starts the animation of the third dot
     * with a delay of .2s, otherwise all dots
     * would animate at the same time
     */
    animation-delay: .2s;
}

.saving span:nth-child(3) {
    /**
     * Starts the animation of the third dot
     * with a delay of .4s, otherwise all dots
     * would animate at the same time
     */
    animation-delay: .4s;
}
svg{
display:block;
display: block;
margin:auto;
}
div{
  height: 100px;
  width: 100px;
  background: white;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
}
</style>
</head>

<body>
<div class="top-left">
	<p class="saving">Loading<span>.</span><span>.</span><span>.</span></p>
</div>
<svg  xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" class="lds-dna" width="385px" height="385px" viewBox="0 -50 150 150" preserveAspectRatio="xMidYMid" style="background: rgba(255,255,255,0.9)">
<circle cx="6.451612903225806" cy="67.8942" r="2.94447">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-0.5s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="0s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#941946;#fbacc9;#941946" dur="2s" repeatCount="indefinite" begin="-0.5s"/>
</circle>
<circle cx="6.451612903225806" cy="32.1058" r="3.05553">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-1.5s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-1s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#a2f0fb;#164ba3;#a2f0fb" dur="2s" repeatCount="indefinite" begin="-0.5s"/>
</circle>
<circle cx="16.129032258064512" cy="64.3816" r="2.70447">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-0.7s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-0.2s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#941946;#fbacc9;#941946" dur="2s" repeatCount="indefinite" begin="-0.7s"/>
</circle>
<circle cx="16.129032258064512" cy="35.6184" r="3.29553">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-1.7s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-1.2s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#a2f0fb;#164ba3;#a2f0fb" dur="2s" repeatCount="indefinite" begin="-0.7s"/>
</circle>
<circle cx="25.806451612903224" cy="53.8199" r="2.46447">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-0.9s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-0.4s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#941946;#fbacc9;#941946" dur="2s" repeatCount="indefinite" begin="-0.9s"/>
</circle>
<circle cx="25.806451612903224" cy="46.1801" r="3.53553">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-1.9s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-1.4s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#a2f0fb;#164ba3;#a2f0fb" dur="2s" repeatCount="indefinite" begin="-0.9s"/>
</circle>
<circle cx="35.48387096774193" cy="40.3566" r="2.57553">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-1.1s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-0.6s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#941946;#fbacc9;#941946" dur="2s" repeatCount="indefinite" begin="-1.1s"/>
</circle>
<circle cx="35.48387096774193" cy="59.6434" r="3.42447">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-2.1s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-1.6s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#a2f0fb;#164ba3;#a2f0fb" dur="2s" repeatCount="indefinite" begin="-1.1s"/>
</circle>
<circle cx="45.16129032258064" cy="33.2779" r="2.81553">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-1.3s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-0.8s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#941946;#fbacc9;#941946" dur="2s" repeatCount="indefinite" begin="-1.3s"/>
</circle>
<circle cx="45.16129032258064" cy="66.7221" r="3.18447">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-2.3s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-1.8s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#a2f0fb;#164ba3;#a2f0fb" dur="2s" repeatCount="indefinite" begin="-1.3s"/>
</circle>
<circle cx="54.838709677419345" cy="32.1058" r="3.05553">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-1.5s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-1s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#941946;#fbacc9;#941946" dur="2s" repeatCount="indefinite" begin="-1.5s"/>
</circle>
<circle cx="54.838709677419345" cy="67.8942" r="2.94447">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-2.5s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-2s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#a2f0fb;#164ba3;#a2f0fb" dur="2s" repeatCount="indefinite" begin="-1.5s"/>
</circle>
<circle cx="64.51612903225805" cy="35.6184" r="3.29553">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-1.7s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-1.2s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#941946;#fbacc9;#941946" dur="2s" repeatCount="indefinite" begin="-1.7s"/>
</circle>
<circle cx="64.51612903225805" cy="64.3816" r="2.70447">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-2.7s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-2.2s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#a2f0fb;#164ba3;#a2f0fb" dur="2s" repeatCount="indefinite" begin="-1.7s"/>
</circle>
<circle cx="74.19354838709677" cy="46.1801" r="3.53553">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-1.9s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-1.4s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#941946;#fbacc9;#941946" dur="2s" repeatCount="indefinite" begin="-1.9s"/>
</circle>
<circle cx="74.19354838709677" cy="53.8199" r="2.46447">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-2.9s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-2.4s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#a2f0fb;#164ba3;#a2f0fb" dur="2s" repeatCount="indefinite" begin="-1.9s"/>
</circle>
<circle cx="83.87096774193547" cy="59.6434" r="3.42447">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-2.1s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-1.6s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#941946;#fbacc9;#941946" dur="2s" repeatCount="indefinite" begin="-2.1s"/>
</circle>
<circle cx="83.87096774193547" cy="40.3566" r="2.57553">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-3.1s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-2.6s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#a2f0fb;#164ba3;#a2f0fb" dur="2s" repeatCount="indefinite" begin="-2.1s"/>
</circle>
<circle cx="93.54838709677418" cy="66.7221" r="3.18447">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-2.3s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-1.8s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#941946;#fbacc9;#941946" dur="2s" repeatCount="indefinite" begin="-2.3s"/>
</circle>
<circle cx="93.54838709677418" cy="33.2779" r="2.81553">
  <animate attributeName="r" times="0;0.5;1" values="2.4000000000000004;3.5999999999999996;2.4000000000000004" dur="2s" repeatCount="indefinite" begin="-3.3s"/>
  <animate attributeName="cy" keyTimes="0;0.5;1" values="32;68;32" dur="2s" repeatCount="indefinite" begin="-2.8s" keySplines="0.5 0 0.5 1;0.5 0 0.5 1" calcMode="spline"/>
  <animate attributeName="fill" keyTimes="0;0.5;1" values="#a2f0fb;#164ba3;#a2f0fb" dur="2s" repeatCount="indefinite" begin="-2.3s"/>
</circle>
</svg>
</body>
</html>
