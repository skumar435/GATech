# WebServer

Link to webServer: http://predict2019t2.biosci.gatech.edu/

**1) resources:** Contains the pages

**2) routes:** Contain the redirections 

Our team's goal was to handle unassembled Salmonella enterica genome sequence data. Our pipeline proceeds through various stages: genome assembly, gene prediction, functional annotation, and comparative genomics. The objective was to create a predictive webserver that weaves in these various elements in a seamless manner for the user, who will not be required to possess extensive computing knowledge.

The webserver was built using Laravel 5.8 and PHP 7.3.1, a free, open-source PHP web framework that follows the model–view–controller architectural pattern. The webserver displays visualization of analysis results. The visualization is created using D3(Version 3), a widely used JavaScript library for producing data visualizations in web browsers. A user can choose to visualize the JSON data generated by the RGI as well. Phylotree.js is used to generate the phylogenetic trees that have been generated using the newick tree that has been calculated by the software MUMMER.
