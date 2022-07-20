<?php

set_time_limit(0);

$sql1 = 'CREATE TABLE IF NOT EXISTS affiliations (
            id INTEGER PRIMARY KEY,
            page_num INTEGER,
            nama TEXT,
            scopus_h_indeks INTEGER,
            gs_h_indeks INTEGER,
            sinta_three_yr_score INTEGER,
            sinta_score INTEGER,
            affil_three_yr_score INTEGER,
            affil_score INTEGER,
            author_link INTEGER,
            auth_ok INTEGER,
            docs_ok INTEGER
        )';

$sql2 = 'CREATE TABLE IF NOT EXISTS author (
            id INTEGER PRIMARY KEY,
            departemen TEXT,
            sinta_id TEXT,  
            books INTEGER,
            ipr INTEGER,

            -- rank_in_national INTEGER,
            -- three_yr_national_rank INTEGER,
            -- rank_in_affiliation INTEGER,
            -- three_yr_affiliation_rank INTEGER,
            scopus_ro_articles INTEGER,
            scopus_ro_conference INTEGER,
            scopus_ro_other INTEGER,
            scopus_ro_total INTEGER,
            
            scopus_q1 INTEGER,
            scopus_q2 INTEGER,
            scopus_q3 INTEGER,
            scopus_q4 INTEGER,
            scopus_undefined INTEGER,
            
            sinta_s1 INTEGER,
            sinta_s2 INTEGER,
            sinta_s3 INTEGER,
            sinta_s4 INTEGER,
            sinta_s5 INTEGER,
            sinta_s6 INTEGER,
            sinta_uncategorized INTEGER,
            
            scopus_docs INTEGER,
            scopus_citations INTEGER,
            scopus_i10_idx INTEGER,
            scopus_g_idx INTEGER,

            google_docs INTEGER,
            google_citations INTEGER,
            google_i10_idx INTEGER,
            google_g_idx INTEGER,

            wos_docs INTEGER
        )';

$sql3 = 'CREATE TABLE IF NOT EXISTS scopus (
            id INTEGER PRIMARY KEY,
            sinta_id TEXT,
            quartile TEXT,
            publication TEXT,
            details TEXT,
            citation INTEGER
        )';


$database = new SQLite3('scrape1.db');
$database->exec($sql1);
$database->exec($sql2);
$database->exec($sql3);

$database = new SQLite3('scrape2.db');
$database->exec($sql1);
$database->exec($sql2);
$database->exec($sql3);

$database = new SQLite3('scrape3.db');
$database->exec($sql1);
$database->exec($sql2);
$database->exec($sql3);


// open new tab for running the program that get data from page one as the first part
echo '<script type="text/javascript" language="Javascript">'.
    'window.open("http://localhost/sinta-upi/get_affiliations.php?page=1&part=1");'.
    '</script>'
;

// open new tab for running the program that get data from page two as the second part
echo '<script type="text/javascript" language="Javascript">'.
    'window.open("http://localhost/sinta-upi/get_affiliations.php?page=&part=2");'.
    '</script>'
;

// open new tab for running the program that get data from page three as the third part
echo '<script type="text/javascript" language="Javascript">'.
    'window.open("http://localhost/sinta-upi/get_affiliations.php?page=&part=3");'.
    '</script>'
;

// close tab
// echo '<script type="text/javascript" language="Javascript">'.
//     'close();'.
//     '</script>'
// ;

?>
