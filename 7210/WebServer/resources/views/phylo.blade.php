@extends('layout')


<!DOCTYPE html>
<html lang='en'>

<head>
  <meta charset="utf-8">

  <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">
  <link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap-theme.min.css">
  <link href="//veg.github.io/phylotree.js/phylotree.css" rel="stylesheet">
  <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/styles/default.min.css">

  <script src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/9.12.0/highlight.min.js"></script>
  <script src="//code.jquery.com/jquery.js"></script>
  <script src="//netdna.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>
  <script src="//d3js.org/d3.v3.min.js"></script>
  <script src="//phylotree.hyphy.org/phylotree.js"></script>
  <script src="//cdnjs.cloudflare.com/ajax/libs/underscore.js/1.8.3/underscore-min.js"></script>
  <style>
#code {
  display: inline-block;
  width: 700px;
  padding-left: 50px;
}
  </style>
</head>
</head>

<body>
  <div>
    <form>
      <label>Radial layout</label>
      <input type="checkbox" id="layout"/>
    </form>
  </div>


  <svg id="tree_display"></svg>
  <!-- <div id="code"><pre><code class="javascript">d3.text("yokoyama.nwk", function(error, newick) {
  var tree = d3.layout.phylotree()
    .svg(d3.select("#tree_display"))
    .radial(true);

  tree(d3.layout.newick_parser(newick))
    .layout();

  $("#layout").on("click", function(e) {
    tree.radial($(this).prop("checked")).placenodes().update();
  });
});</code></pre></div> -->
<script>

function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function(m,key,value) {
        vars[key] = value;
    });
    return vars;
}

function getUrlParam(parameter, defaultvalue){
    var urlparameter = defaultvalue;
    if(window.location.href.indexOf(parameter) > -1){
        urlparameter = getUrlVars()[parameter];
        urlparameter = "fastas/"+urlparameter +"/output/output_cg.nwk"
        }
    return urlparameter;
}
;
function nodeStyler(dom_element, node_object) {
  if ((node_object.children == null) && !( ["CGT2093","CGT2472","CGT2683","CGT2114","CGT2400","CGT2123","CGT2332","CGT2514","CGT2116","CGT2010","CGT2742","CGT2049","CGT2344","CGT2785","CGT2552","CGT2443","CGT2364","CGT2044","CGT2517","CGT2805","CGT2374","CGT2878","CGT2214","CGT2326","CGT2069","CGT2287","CGT2196","CGT2060","CGT2471","CGT2135","CGT2006","CGT2386","CGT2567","CGT2628","CGT2318","CGT2076","CGT2540","CGT2843","CGT2304","CGT2427","CGT2269","CGT2599","CGT2908","CGT2424","CGT2119","CGT2278","CGT2393","CGT2858","CGT2428","CGT2659"].includes(node_object.name))) {

    dom_element.style("fill", "red");
  }

        // if ("bootstrap" in node_object && node_object.bootstrap) {
        //   var label = dom_element.selectAll(".bootstrap");
        //   if (label.empty()) {
        //     dom_element.append("text").classed("bootstrap", true).text(node_object.bootstrap).attr("dx", ".3em").attr("text-anchor", "start").attr("alignment-baseline", "middle");
        //   } else {
        //     if (tree.radial()) { // do not show internal node labels in radial mode
        //       label.remove();
        //     }
        //   }
        // }

      }




var file = getUrlParam('x','iso.nwk');
console.log(file);
    d3.text(file, function(error, newick) {
      var tree = d3.layout.phylotree()
      .options({
        brush: false,
        zoom: true,
        "show-scale": true
      })
        .svg(d3.select("#tree_display"))
        .radial(false)
        .options({
          brush: false,
          zoom: true,
          "show-scale": true
        })
        .style_nodes(nodeStyler);

      tree(d3.layout.newick_parser(newick))
        .layout();

      $("#layout").on("click", function(e) {
        tree.radial($(this).prop("checked")).placenodes()
        .options({
          brush: false,
          zoom: true,
          "show-scale": $(this).prop("checked")
        })
        .update();
      });
    });

    // for syntax highlighting
    hljs.initHighlightingOnLoad();
  </script>

</body>

</html>
