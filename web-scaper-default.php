<?php 
    include('simple_html_dom.php');

    // get html
    $html = file_get_html('https://sinta.kemdikbud.go.id/affiliations/authors/414');
    
    // echo $html->find('title', 0)->plaintext;
    // echo "<br>"; 

    // value of find fundtion is sensitive case
    $list = $html->find('div[class="au-item mt-3 mb-3 pb-5 pt-3"]',0);
    
    $list_array = $list->find('div[class="row"]',);

    // print the default format (hyperlink)
    // for ($i=0; $i < sizeof($list_array); $i++) {
    //     echo $list_array[$i];
    //     echo "<br>"; 
    // }
    
    // print as plaintext get href
    // foreach ($list->find('a') as $element) {
    //     echo $element->plaintext;
    //     echo "points to ", $element->href;
    //     echo "<br>";
    // }
    
    // print as plaintext
    for ($i=0; $i < sizeof($list_array); $i++) {
        echo $list_array[$i]->plaintext;
        echo "<br>"; 
    }

?>

