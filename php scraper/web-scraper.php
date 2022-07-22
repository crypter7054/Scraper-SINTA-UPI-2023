<?php 
    include('simple_html_dom.php');

    // get html
    $html = file_get_html('https://sinta.kemdikbud.go.id/affiliations/authors/414');
    
    // data yang akan diambil
    /*
        nama
        dept
        sinta_id
        Scopus H-index
        GS H-index
        SINTA Score 3Yr
        SINTA Score 
        Affil Score 3Yr
        Affil Score
    */

    set_time_limit(0);

    $csv = [];

    $legend = array("Nama", "Departemen", "ID_Dosen", "Scopus_H-Index", "GS_H-Index", "SINTA_Score_3Yr", "SINTA_Score", "Affil_Score_3Yr", "Affil_Score"); 

    array_push($csv, $legend);
    
    
    foreach ($html->find('div[class="au-item mt-3 mb-3 pb-5 pt-3"] div[class="row"] div[class="col-lg"]') as $item) {
        
        $name = $item->find('div[class="profile-name"] a');
        $dept = $item->find('div[class="profile-dept"] a');
        $id = $item->find('div[class="profile-id"]');
        $scopus_h_index = $item->find('div[class="profile-hindex"] span[class="profile-id text-warning"]');
        $gs_h_index = $item->find('div[class="profile-hindex"] span[class="profile-id text-success ml-3"]');
        $three_yr_sinta_score = $item->find('div[class="col-lg"] div[class="row"]');
        
        $temp1 = [];
        
        for ($i=0; $i < sizeof($name); $i++) { 
            $text = $name[$i]->text();
            $text2 = $dept[$i]->text();
            $text3 = $id[$i]->text();
            $text4 = $scopus_h_index[$i]->text();
            $text5 = $gs_h_index[$i]->text();
            
            for ($j=0; $j < sizeof($three_yr_sinta_score) ; $j++) { 
                $text6 = $three_yr_sinta_score[$i]->text();
            }

            $text2 = str_replace(" ", "", $text2);

            array_push($temp1, $text);
            array_push($temp1, $text2);
            array_push($temp1, $text3);
            array_push($temp1, $text4);
            array_push($temp1, $text5);
        }

        

        $csv[] = $temp1;


        // foreach ($html->find('div[class="profile-name"]') as $item) {
        //     $value = $item->find("a");
    
        //     for ($i=0; $i < sizeof($value); $i++) { 
        //         $text = $value[$i]->text();
    
        //         array_push($temp1, $text);
        //     }
            
        // }
    }
    
    // foreach ($html->find('div[class="profile-name"]') as $item) {
    //     $value = $item->find("a");
    //     $temp1 = [];

    //     for ($i=0; $i < sizeof($value); $i++) { 
    //         $text = $value[$i]->text();

    //         array_push($temp1, $text);
    //     }
    //     $csv[] = $temp1;
    // }

    // foreach ($html->find('div[class="profile-dept"]') as $item) {
    //     $value = $item->find("a");
    //     $temp1 = [];

    //     for ($i=0; $i < sizeof($value); $i++) { 
    //         $text2 = $value[$i]->text();

    //         array_push($temp1, $text2);
    //     }
    //     $csv[] = $temp1;
    // }

    
    var_dump($csv);

    $file = fopen("test.csv", "w");
    foreach ($csv as $line) {
        fputcsv($file, $line);
    }
    fclose($file);
    

?>

